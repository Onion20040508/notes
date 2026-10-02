# Website configuration

This folder (hidden in Obsidian because its name starts with a dot) configures the public website
built from this vault by `.github/workflows/deploy-site.yml`.

| File | Purpose |
|---|---|
| `quartz.config.yaml` | Quartz settings: site title, base URL, ignored folders, LaTeX macros (copied from `preamble.sty`) |
| `custom.scss` | Callout colours and figure styling, matching `.obsidian/snippets/` |
| `prepare.py` | Copies the vault into Quartz and rewrites figure embeds so Quartz can find them |

If you add a macro to `preamble.sty`, add the same macro under `customMacros` in `quartz.config.yaml`.
