'use strict';

/*
 * Extended MathJax (obsidian-latex 0.4.1), preamble loader rewritten 2026-11-09 for
 * Obsidian 1.15+ (MathJax 4). Original plugin: Xavier Denis & Ng Wei En (MIT).
 *
 * What it does: reads a preamble file of \newcommand lines (default: preamble.sty in the
 * vault root) and makes those macros available in every formula.
 *
 * How (differs from the original, which typeset the preamble once at start-up):
 *  - MathJax.tex2chtml is wrapped. Before each formula is converted, the wrapper checks
 *    that the preamble's macros are defined in the TeX input jax that is in use *now*,
 *    and (re)defines them if they are not. So it no longer matters when MathJax finishes
 *    starting up, or whether its document / input jax is created again later.
 *  - If the definitions do not stick at all, the preamble is prepended to each formula.
 *  - A small status file (preamble-status.json, next to this file) records what happened,
 *    so a rendering problem can be diagnosed without opening the developer console.
 */

var obsidian = require('obsidian');

var DEFAULT_SETTINGS = {
    preamblePath: 'preamble.sty'
};

function stripComments(text) {
    return text.split(/\r?\n/).filter(function (line) {
        return line.trim().length > 0 && line.trim().charAt(0) !== '%';
    }).join('\n');
}

function macroNames(text) {
    var names = [];
    var re = /\\(?:re)?newcommand\s*\{?\s*\\([A-Za-z]+)\s*\}?/g;
    var m;
    while ((m = re.exec(text)) !== null) {
        names.push(m[1]);
    }
    return names;
}

function PreambleLoader(plugin) {
    this.plugin = plugin;
    this.pre = '';
    this.names = [];
    this.sentinel = null;
    this.orig = null;          // the real MathJax.tex2chtml
    this.origPromise = null;   // the real MathJax.tex2chtmlPromise
    this.hooked = null;        // the MathJax object the accessors are installed on
    this.status = {
        loader: 'v2 (2026-11-09)',
        started: new Date().toISOString(),
        mathjaxVersion: null,
        tex2chtmlAtLoad: null,
        lookupApi: null,
        sentinel: null,
        macros: 0,
        mode: 'define',
        defines: 0,
        defineFailures: 0,
        renders: 0,
        rendersWithMacro: 0,
        undefinedInOutput: 0,
        rehooks: 0,
        errors: []
    };
    this.writeTimer = null;
}

PreambleLoader.prototype.note = function (err) {
    var s = String(err && err.message ? err.message : err);
    if (this.status.errors.length < 20) {
        this.status.errors.push(new Date().toISOString() + ' ' + s);
    }
    this.scheduleWrite();
};

PreambleLoader.prototype.scheduleWrite = function () {
    var self = this;
    if (this.writeTimer !== null) {
        return;
    }
    this.writeTimer = window.setTimeout(function () {
        self.writeTimer = null;
        self.writeStatus();
    }, 1500);
};

PreambleLoader.prototype.writeStatus = function () {
    try {
        this.status.updated = new Date().toISOString();
        var dir = this.plugin.manifest && this.plugin.manifest.dir;
        if (!dir) {
            return;
        }
        this.plugin.app.vault.adapter.write(dir + '/preamble-status.json', JSON.stringify(this.status, null, 2))
            .catch(function () { });
    }
    catch (e) { /* diagnostics must never break rendering */ }
};

PreambleLoader.prototype.setPreamble = function (text) {
    this.pre = stripComments(text);
    this.names = macroNames(this.pre);
    this.sentinel = this.names.length ? this.names[this.names.length - 1] : null;
    this.status.sentinel = this.sentinel;
    this.status.macros = this.names.length;
    this.status.mode = 'define';
    this.status.defineFailures = 0;
};

// true / false if MathJax's macro table can be queried, null if it cannot.
PreambleLoader.prototype.isDefined = function (name) {
    try {
        var doc = MathJax.startup.document;
        var jax = doc.inputJax[0];
        var handler = jax.parseOptions.handlers.get('macro');
        var found = handler.lookup(name);
        this.status.lookupApi = true;
        return !!found;
    }
    catch (e) {
        this.status.lookupApi = false;
        return null;
    }
};

PreambleLoader.prototype.define = function () {
    if (!this.pre || !this.orig) {
        return;
    }
    try {
        this.orig.call(MathJax, this.pre, { display: true });
        this.status.defines++;
    }
    catch (e) {
        this.note('define: ' + (e && e.message ? e.message : e));
        // MathJax 4 may need to load something asynchronously first.
        var self = this;
        if (this.origPromise) {
            try {
                this.origPromise.call(MathJax, this.pre, { display: true }).then(function () {
                    self.status.defines++;
                    self.scheduleWrite();
                }).catch(function (err) { self.note('definePromise: ' + err); });
            }
            catch (e2) {
                this.note('definePromise: ' + e2);
            }
        }
    }
    this.scheduleWrite();
};

PreambleLoader.prototype.ensure = function () {
    if (!this.sentinel) {
        return;
    }
    var defined = this.isDefined(this.sentinel);
    if (defined === true) {
        return;
    }
    if (defined === false) {
        this.define();
        if (this.isDefined(this.sentinel) === false) {
            this.status.defineFailures++;
            if (this.status.defineFailures >= 2 && this.status.mode !== 'prepend') {
                this.status.mode = 'prepend';
                this.scheduleWrite();
            }
        }
        return;
    }
    // Macro table not reachable: define once per MathJax document object.
    try {
        var doc = MathJax.startup && MathJax.startup.document;
        if (doc && doc.__extendedMathJaxPreamble !== this.pre) {
            this.define();
            doc.__extendedMathJaxPreamble = this.pre;
        }
    }
    catch (e) {
        this.note('ensure: ' + e);
    }
};

PreambleLoader.prototype.source = function (src) {
    this.ensure();
    if (this.status.mode === 'prepend' && typeof src === 'string') {
        return this.pre + '\n' + src;
    }
    return src;
};

PreambleLoader.prototype.inspect = function (src, node) {
    // Self-check on the first formulas that use a preamble macro: did the macro name
    // survive into the output (i.e. was it undefined)?
    try {
        this.status.renders++;
        if (this.status.rendersWithMacro >= 200 || typeof src !== 'string' || !this.sentinel) {
            return;
        }
        var token = '\\' + this.sentinel;
        if (src.indexOf(token) < 0) {
            return;
        }
        this.status.rendersWithMacro++;
        var text = node && node.textContent ? node.textContent : '';
        if (text.indexOf(token) >= 0) {
            this.status.undefinedInOutput++;
            if (this.status.mode !== 'prepend') {
                this.status.mode = 'prepend';
            }
        }
        if (this.status.rendersWithMacro <= 3 || this.status.undefinedInOutput > 0) {
            this.scheduleWrite();
        }
    }
    catch (e) { /* ignore */ }
};

// Install accessors on the MathJax object, so that the wrapper also survives
// MathJax re-creating its conversion methods.
PreambleLoader.prototype.hook = function () {
    var self = this;
    if (typeof MathJax === 'undefined' || !MathJax) {
        return false;
    }
    if (this.hooked === MathJax) {
        return true;
    }
    var mj = MathJax;
    var current = mj.tex2chtml;
    var currentPromise = mj.tex2chtmlPromise;
    if (typeof current !== 'function') {
        return false;
    }
    if (current.__extendedMathJaxWrapper) {
        // hooked by an earlier load of this plugin: take over its original functions
        current = current.__orig || current;
        currentPromise = (currentPromise && currentPromise.__orig) || currentPromise;
    }
    this.orig = current;
    this.origPromise = typeof currentPromise === 'function' ? currentPromise : null;

    var wrapped = function (src, opts) {
        var node = self.orig.call(mj, self.source(src), opts);
        self.inspect(src, node);
        return node;
    };
    wrapped.__extendedMathJaxWrapper = true;
    Object.defineProperty(wrapped, '__orig', { get: function () { return self.orig; } });

    var wrappedPromise = function (src, opts) {
        return self.origPromise.call(mj, self.source(src), opts).then(function (node) {
            self.inspect(src, node);
            return node;
        });
    };
    wrappedPromise.__extendedMathJaxWrapper = true;
    Object.defineProperty(wrappedPromise, '__orig', { get: function () { return self.origPromise; } });

    try {
        Object.defineProperty(mj, 'tex2chtml', {
            configurable: true,
            enumerable: true,
            get: function () { return self.active ? wrapped : self.orig; },
            set: function (fn) { if (typeof fn === 'function' && !fn.__extendedMathJaxWrapper) { self.orig = fn; } }
        });
        if (this.origPromise) {
            Object.defineProperty(mj, 'tex2chtmlPromise', {
                configurable: true,
                enumerable: true,
                get: function () { return self.active ? wrappedPromise : self.origPromise; },
                set: function (fn) { if (typeof fn === 'function' && !fn.__extendedMathJaxWrapper) { self.origPromise = fn; } }
            });
        }
    }
    catch (e) {
        this.note('hook: ' + e);
        return false;
    }
    if (this.hooked !== null) {
        this.status.rehooks++;
    }
    this.hooked = mj;
    this.status.mathjaxVersion = mj.version || null;
    this.scheduleWrite();
    return true;
};

PreambleLoader.prototype.unhook = function () {
    this.active = false;
    try {
        if (this.hooked) {
            Object.defineProperty(this.hooked, 'tex2chtml', { configurable: true, enumerable: true, writable: true, value: this.orig });
            if (this.origPromise) {
                Object.defineProperty(this.hooked, 'tex2chtmlPromise', { configurable: true, enumerable: true, writable: true, value: this.origPromise });
            }
        }
    }
    catch (e) { /* ignore */ }
    this.hooked = null;
};

class JaxPlugin extends obsidian.Plugin {
    async onload() {
        this.loader = new PreambleLoader(this);
        this.loader.active = true;
        try {
            await this.loadSettings();
        }
        catch (e) {
            this.settings = Object.assign({}, DEFAULT_SETTINGS);
            this.loader.note('loadSettings: ' + e);
        }
        try {
            this.addSettingTab(new JaxPluginSettingTab(this.app, this));
        }
        catch (e) {
            this.loader.note('addSettingTab: ' + e);
        }
        // Read the preamble first, so that it is ready the moment MathJax is.
        await this.readPreamble();
        try {
            // Load MathJax so that it can be modified (it is otherwise loaded lazily).
            await obsidian.loadMathJax();
        }
        catch (e) {
            this.loader.note('loadMathJax: ' + e);
        }
        this.loader.status.tex2chtmlAtLoad = (typeof MathJax !== 'undefined' && MathJax) ? typeof MathJax.tex2chtml : 'no MathJax';
        var self = this;
        var tryHook = function () {
            try {
                if (self.loader.active && self.loader.hook()) {
                    self.loader.ensure();
                }
            }
            catch (e) {
                self.loader.note('tryHook: ' + e);
            }
        };
        tryHook();
        try {
            if (typeof MathJax !== 'undefined' && MathJax && MathJax.startup && MathJax.startup.promise) {
                MathJax.startup.promise.then(tryHook, tryHook);
            }
        }
        catch (e) {
            this.loader.note('startup.promise: ' + e);
        }
        // Watchdog: re-hook if MathJax was not ready yet or its global object was replaced.
        this.registerInterval(window.setInterval(tryHook, 2000));
        this.loader.scheduleWrite();
    }

    onunload() {
        if (this.loader) {
            this.loader.unhook();
        }
    }

    async readPreamble() {
        try {
            var text = await this.app.vault.adapter.read(this.settings.preamblePath);
            this.loader.setPreamble(text);
        }
        catch (e) {
            this.loader.note('read preamble "' + this.settings.preamblePath + '": ' + e);
        }
    }

    // kept for compatibility with the original plugin's name
    async loadPreamble() {
        await this.readPreamble();
        if (this.loader.hook()) {
            this.loader.define();
        }
    }

    async loadSettings() {
        this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    }

    async saveSettings() {
        await this.saveData(this.settings);
    }
}

class JaxPluginSettingTab extends obsidian.PluginSettingTab {
    constructor(app, plugin) {
        super(app, plugin);
        this.plugin = plugin;
    }

    display() {
        var self = this;
        var containerEl = this.containerEl;
        containerEl.empty();
        new obsidian.Setting(containerEl)
            .setName('Preamble file')
            .setDesc('Path (relative to the vault) of the file with \\newcommand definitions. Changes to the file are picked up when Obsidian is reloaded.')
            .addText(function (text) {
                text.setValue(self.plugin.settings.preamblePath)
                    .onChange(async function (value) {
                        self.plugin.settings.preamblePath = value;
                        await self.plugin.saveSettings();
                        await self.plugin.loadPreamble();
                    });
            });
    }
}

module.exports = JaxPlugin;
