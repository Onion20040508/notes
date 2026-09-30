# Figures from MATH 452 notes (matplotlib). Writes m452-N-j.svg into attachments/math452/.
#
# All 3D figures use a small orthographic "painter's algorithm" renderer (class Scene)
# drawn into a plain 2D matplotlib axes, instead of mplot3d: it gives exact control over
# occlusion, label placement (labels are anchored to projected 3D points with offsets in
# points, like TikZ nodes) and a tight bounding box.  Style follows the vault's TikZ
# figures: palette figB/figR/figG/figO, Computer Modern, ~\scriptsize-\small labels.
#
# Usage:  python3 make_figures.py            (all figures)
#         python3 make_figures.py 4-1 19-2   (only the listed ones)
import os, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection, LineCollection
from matplotlib import patheffects

OUT = os.environ.get('OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

mpl = matplotlib
np.seterr(divide='ignore', over='ignore', invalid='ignore')  # spurious Accelerate-BLAS matmul warnings
mpl.rcParams['svg.fonttype'] = 'path'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['cmr10']
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['axes.formatter.use_mathtext'] = True

def rgb(r, g, b): return np.array([r, g, b]) / 255.0
figB = rgb(31, 90, 166)
figR = rgb(176, 48, 48)
figG = rgb(46, 125, 50)
figO = rgb(214, 120, 20)
BLACK = np.zeros(3)
WHITE = np.ones(3)
def mix(c, t):
    """TikZ-style c!t: fraction t of colour c, rest white."""
    return t * np.asarray(c, float) + (1 - t) * WHITE
def grey(t):
    """TikZ black!t (t in [0,1])."""
    return (1 - t) * WHITE

FS = 8        # standard label size (between \scriptsize=7pt and \small=9pt)
FS_S = 7      # secondary labels (= \scriptsize)
INCH_PER_UNIT = 0.80

def unit(v):
    v = np.asarray(v, float); return v / np.linalg.norm(v)


class Scene:
    """Orthographic projection + depth-sorted primitives, rendered into a 2D axes."""
    def __init__(self, elev, azim, offset=(0.0, 0.0)):
        e, a = np.radians(elev), np.radians(azim)
        self.e1 = np.array([-np.sin(a), np.cos(a), 0.0])                       # screen right
        self.e2 = np.array([-np.sin(e)*np.cos(a), -np.sin(e)*np.sin(a), np.cos(e)])  # screen up
        self.d = np.array([np.cos(e)*np.cos(a), np.cos(e)*np.sin(a), np.sin(e)])      # toward viewer
        self.off = np.array(offset, float)
        self.items = []
        self.texts = []
        self.light = unit(-0.45*self.e1 + 0.75*self.e2 + 0.55*self.d)

    # --- projection -------------------------------------------------------
    def P(self, p):
        p = np.asarray(p, float)
        return np.stack([p @ self.e1, p @ self.e2], -1) + self.off
    def D(self, p):
        return np.asarray(p, float) @ self.d

    # --- primitives -------------------------------------------------------
    def fill(self, pts3, fc, ec=None, lw=0.0, alpha=1.0, bias=0.0, layer=0, depth=None):
        pts3 = np.asarray(pts3, float)
        dep = self.D(pts3).mean() if depth is None else depth
        if ec is None:
            ec, lw = (fc, 0.3) if alpha == 1.0 else ('none', 0.0)
        self.items.append(dict(kind='fill', v=self.P(pts3), d=dep + bias, layer=layer,
                               fc=fc, ec=ec, lw=lw, alpha=alpha))
    def fill2d(self, v2, fc, ec='none', lw=0.0, alpha=1.0, layer=0, depth=0.0):
        self.items.append(dict(kind='fill', v=np.asarray(v2, float) + self.off, d=depth, layer=layer,
                               fc=fc, ec=ec, lw=lw, alpha=alpha))
    def line(self, pts3, color, lw=0.8, ls='-', alpha=1.0, bias=0.0, layer=0, split=True, depth=None):
        pts3 = np.asarray(pts3, float)
        v = self.P(pts3); dd = self.D(pts3)
        if split and ls == '-':
            for i in range(len(v) - 1):
                self.items.append(dict(kind='line', v=v[i:i+2], d=(dd[i]+dd[i+1])/2 + bias, layer=layer,
                                       color=color, lw=lw, ls=ls, alpha=alpha))
        else:
            dep = dd.mean() if depth is None else depth
            self.items.append(dict(kind='line', v=v, d=dep + bias, layer=layer,
                                   color=color, lw=lw, ls=ls, alpha=alpha))
    def line2d(self, v2, color, lw=0.8, ls='-', alpha=1.0, layer=0, depth=0.0):
        self.items.append(dict(kind='line', v=np.asarray(v2, float) + self.off, d=depth, layer=layer,
                               color=color, lw=lw, ls=ls, alpha=alpha))
    def head2d(self, tip2, dir2, color, hl=0.10, hw=0.042, layer=0, depth=0.0, raw=False):
        """Stealth-like arrow head with tip at tip2 (screen coords)."""
        t = np.asarray(tip2, float) + (0 if raw else self.off)
        u = unit(dir2); n = np.array([-u[1], u[0]])
        v = np.array([t, t - hl*u + hw*n, t - 0.72*hl*u, t - hl*u - hw*n])
        self.items.append(dict(kind='fill', v=v, d=depth, layer=layer, fc=color, ec=color, lw=0.3, alpha=1.0))
    def arrow(self, p, q, color, lw=0.9, hl=0.10, hw=0.042, bias=0.0, layer=0, ls='-', nseg=12):
        p = np.asarray(p, float); q = np.asarray(q, float)
        p2, q2 = self.P(p), self.P(q)
        L2 = np.linalg.norm(q2 - p2)
        tcut = max(0.0, 1 - 0.72*hl / L2) if L2 > 1e-9 else 1.0
        s = np.linspace(0, tcut, nseg + 1)[:, None]
        self.line(p + s*(q - p), color, lw=lw, bias=bias, layer=layer, ls=ls)
        self.head2d(q2 - self.off, q2 - p2, color, hl=hl, hw=hw, layer=layer, depth=self.D(q) + bias)
    def arrow2d(self, p2, q2, color, lw=0.9, hl=0.10, hw=0.042, layer=0, depth=0.0, ls='-'):
        p2 = np.asarray(p2, float); q2 = np.asarray(q2, float)
        u = unit(q2 - p2)
        self.line2d([p2, q2 - 0.72*hl*u], color, lw=lw, layer=layer, depth=depth, ls=ls)
        self.head2d(q2, u, color, hl=hl, hw=hw, layer=layer, depth=depth)
    def dot(self, p, color, r=0.035, bias=0.02, layer=0):
        c = self.P(p); t = np.linspace(0, 2*np.pi, 20, endpoint=False)
        v = c + r*np.stack([np.cos(t), np.sin(t)], -1)
        self.items.append(dict(kind='fill', v=v, d=self.D(p) + bias, layer=layer,
                               fc=color, ec=color, lw=0.3, alpha=1.0))
    def dot2d(self, c2, color, r=0.035, layer=0, depth=0.0):
        t = np.linspace(0, 2*np.pi, 20, endpoint=False)
        v = np.asarray(c2, float) + self.off + r*np.stack([np.cos(t), np.sin(t)], -1)
        self.items.append(dict(kind='fill', v=v, d=depth, layer=layer, fc=color, ec=color, lw=0.3, alpha=1.0))

    def shade(self, n, color, lo, hi):
        n = np.asarray(n, float)
        nn = n / np.maximum(np.linalg.norm(n, axis=-1, keepdims=True), 1e-12)
        I = np.abs(nn @ self.light)
        t = lo + (hi - lo) * I
        return t[..., None] * np.asarray(color) + (1 - t[..., None]) * WHITE

    def surface(self, X, Y, Z, color, lo=0.08, hi=0.30, mesh=None, mesh_color=None, mesh_lw=0.3,
                edge_color=None, edge_lw=0.8, bias=0.0, layer=0, alpha=1.0, fc=None, silhouette=True,
                edges=(True, True, True, True)):
        """Opaque shaded parametric surface. mesh=(ku,kv): draw every ku-th/kv-th grid line."""
        Pt = np.stack([X, Y, Z], -1)
        q = np.stack([Pt[:-1, :-1], Pt[1:, :-1], Pt[1:, 1:], Pt[:-1, 1:]], -2)  # (n-1,m-1,4,3)
        nrm = np.cross(Pt[1:, 1:] - Pt[:-1, :-1], Pt[:-1, 1:] - Pt[1:, :-1])
        cols = self.shade(nrm, color, lo, hi) if fc is None else np.broadcast_to(fc, nrm.shape)
        for i in range(q.shape[0]):
            for j in range(q.shape[1]):
                self.fill(q[i, j], cols[i, j], bias=bias, layer=layer, alpha=alpha)
        mc = mix(color, 0.45) if mesh_color is None else mesh_color
        if mesh:
            ku, kv = mesh
            for i in range(0, Pt.shape[0], ku)[1:]:
                if i < Pt.shape[0] - 1: self.line(Pt[i], mc, lw=mesh_lw, bias=bias + 0.03, layer=layer)
            for j in range(0, Pt.shape[1], kv)[1:]:
                if j < Pt.shape[1] - 1: self.line(Pt[:, j], mc, lw=mesh_lw, bias=bias + 0.03, layer=layer)
        if edge_lw:
            ec = color if edge_color is None else edge_color
            for b, on in zip((Pt[0], Pt[-1], Pt[:, 0], Pt[:, -1]), edges):
                if on: self.line(b, ec, lw=edge_lw, bias=bias + 0.06, layer=layer)
            if silhouette:   # fold lines: where the surface turns from facing the viewer to facing away
                nd = nrm @ self.d
                nd[np.linalg.norm(nrm, axis=-1) < 1e-9] = np.nan
                sgn = np.sign(nd)   # NaN (degenerate quads) never compares unequal-and-true below
                sgn[np.isnan(sgn)] = 0
                for i, j in zip(*np.nonzero(sgn[:-1, :] * sgn[1:, :] < 0)):
                    self.line([Pt[i+1, j], Pt[i+1, j+1]], ec, lw=edge_lw, bias=bias + 0.06, layer=layer)
                for i, j in zip(*np.nonzero(sgn[:, :-1] * sgn[:, 1:] < 0)):
                    self.line([Pt[i, j+1], Pt[i+1, j+1]], ec, lw=edge_lw, bias=bias + 0.06, layer=layer)

    def shift(self, dx, dy):
        dv = np.array([dx, dy], float)
        for it in self.items: it['v'] = it['v'] + dv
        for t in self.texts: t['xy'] = t['xy'] + dv
        self.off = self.off + dv
    def bounds(self):
        v = np.concatenate([it['v'] for it in self.items])
        return v.min(0), v.max(0)

    # --- labels -----------------------------------------------------------
    def text(self, p, s, off=(0, 0), ha='center', va='center', color=BLACK, size=FS, halo=False, raw2d=False):
        xy = (np.asarray(p, float) + self.off) if raw2d else self.P(p)
        self.texts.append(dict(xy=xy, s=s, off=off, ha=ha, va=va, color=color, size=size, halo=halo))
    def text_dir(self, p, s, dirn, dist=3.0, **kw):
        """TikZ-like: put label beyond point p in screen direction dirn (2D), anchored on the opposite side."""
        u = unit(dirn)
        ha = 'left' if u[0] > 0.38 else ('right' if u[0] < -0.38 else 'center')
        va = 'bottom' if u[1] > 0.38 else ('top' if u[1] < -0.38 else 'center')
        self.text(p, s, off=(dist*u[0], dist*u[1]), ha=ha, va=va, **kw)
    def axes(self, L, labels=('$x$', '$y$', '$z$'), origin=(0, 0, 0), lw=0.5, color=BLACK, size=FS,
             bias=0.0, neg=(0, 0, 0)):
        o = np.asarray(origin, float)
        for k in range(3):
            if L[k] <= 0: continue
            e = np.zeros(3); e[k] = 1
            p0 = o - neg[k]*e; p1 = o + L[k]*e
            self.arrow(p0, p1, color, lw=lw, hl=0.085, hw=0.032, bias=bias)
            if labels[k]:
                self.text_dir(p1, labels[k], self.P(p1) - self.P(o), dist=2.0, size=size, color=color)


def render(scenes, fname, scale=INCH_PER_UNIT, pad=0.02, extra=None):
    items = [it for sc in scenes for it in sc.items]
    items.sort(key=lambda it: (it['layer'], it['d']))
    allv = np.concatenate([it['v'] for it in items])
    xmin, ymin = allv.min(0); xmax, ymax = allv.max(0)
    W, H = xmax - xmin, ymax - ymin
    fig = plt.figure(figsize=(W*scale, H*scale))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax); ax.set_aspect('equal'); ax.axis('off')
    # group consecutive items of the same kind into collections, preserving order
    runs = []
    for it in items:
        key = (it['kind'], it.get('ls', '-') != '-')
        if runs and runs[-1][0] == key: runs[-1][1].append(it)
        else: runs.append((key, [it]))
    for z, ((kind, dashed), group) in enumerate(runs):
        if kind == 'fill':
            fc = [(*np.asarray(mpl.colors.to_rgb(g['fc'])), g['alpha']) for g in group]
            ec = [(0, 0, 0, 0) if (isinstance(g['ec'], str) and g['ec'] == 'none')
                  else (*np.asarray(mpl.colors.to_rgb(g['ec'])), g['alpha']) for g in group]
            pc = PolyCollection([g['v'] for g in group], facecolors=fc, edgecolors=ec,
                                linewidths=[g['lw'] for g in group], zorder=z + 1, clip_on=False)
            pc.set_joinstyle('round')
            ax.add_collection(pc)
        else:
            cols = [(*np.asarray(mpl.colors.to_rgb(g['color'])), g['alpha']) for g in group]
            lc = LineCollection([g['v'] for g in group], colors=cols, linewidths=[g['lw'] for g in group],
                                linestyles=[g['ls'] for g in group], zorder=z + 1, clip_on=False,
                                capstyle='butt' if dashed else 'round', joinstyle='round')
            ax.add_collection(lc)
    for sc in scenes:
        for t in sc.texts:
            pe = [patheffects.withStroke(linewidth=2.2, foreground='white')] if t['halo'] else None
            ax.annotate(t['s'], xy=t['xy'], xytext=t['off'], textcoords='offset points',
                        ha=t['ha'], va=t['va'], color=t['color'], fontsize=t['size'],
                        annotation_clip=False, zorder=10000, path_effects=pe)
    if extra: extra(fig, ax)
    fig.savefig(os.path.join(OUT, fname), bbox_inches='tight', pad_inches=pad)
    plt.close(fig)
    print('wrote', fname)


# ------------------------------------------------------------------------------------------
# shared graph function for 4-1 / 6-1
def fgraph(x, y):
    return 1.05 + 0.40*np.sin(1.35*x) + 0.38*np.cos(1.15*y) + 0.05*x
def fgraph_x(x, y): return 0.40*1.35*np.cos(1.35*x) + 0.05
def fgraph_y(x, y): return -0.38*1.15*np.sin(1.15*y)
# dome-shaped variant for the tangent plane (surface stays below the plane near the point)
def fdome(x, y):
    return 1.05 + 0.42*np.sin(1.35*x) + 0.40*np.cos(1.15*(y - 1.3)) + 0.05*x
def fdome_x(x, y): return 0.42*1.35*np.cos(1.35*x) + 0.05
def fdome_y(x, y): return -0.40*1.15*np.sin(1.15*(y - 1.3))

VIEW_STD = (30, 32)   # elev, azim: x toward lower left, y to the right, z up (as in the TikZ figures)


# ================ §4 Fig. 1: partial derivatives as slopes of slice curves ================
def fig_4_1():
    sc = Scene(*VIEW_STD)
    xa, xb, ya, yb = 0.25, 2.25, 0.25, 2.45
    x0, y0 = 1.2, 1.25; z0 = fgraph(x0, y0)
    # base: domain rectangle, the two cutting lines, base point
    sc.fill([(xa, ya, 0), (xb, ya, 0), (xb, yb, 0), (xa, yb, 0)], grey(0.045), ec=grey(0.35), lw=0.4, layer=-1)
    sc.line([(xa, y0, 0), (xb, y0, 0)], mix(figR, 0.7), lw=0.6, ls=(0, (3, 2)), layer=-0.5)
    sc.line([(x0, ya, 0), (x0, yb, 0)], mix(figG, 0.7), lw=0.6, ls=(0, (3, 2)), layer=-0.5)
    sc.axes((2.75, 2.95, 2.3))
    # surface
    u, v = np.meshgrid(np.linspace(xa, xb, 41), np.linspace(ya, yb, 45), indexing='ij')
    sc.surface(u, v, fgraph(u, v), figB, mesh=(5, 5), edge_lw=0.7)
    # slice curves
    xs = np.linspace(xa, xb, 80); ys = np.linspace(ya, yb, 80)
    sc.line(np.c_[xs, np.full_like(xs, y0), fgraph(xs, y0)], figR, lw=1.3, bias=0.06)
    sc.line(np.c_[np.full_like(ys, x0), ys, fgraph(x0, ys)], figG, lw=1.3, bias=0.06)
    # tangent lines (slopes f_x, f_y)
    fx, fy = fgraph_x(x0, y0), fgraph_y(x0, y0)
    P0 = np.array([x0, y0, z0])
    tx = unit([1, 0, fx]) * 0.62; ty = unit([0, 1, fy]) * 0.62
    sc.line([P0 - tx, P0 + tx], figR, lw=0.7, bias=0.06, split=False, depth=sc.D(P0) + 0.5)
    sc.line([P0 - ty, P0 + ty], figG, lw=0.7, bias=0.06, split=False, depth=sc.D(P0) + 0.5)
    # drop line (hidden-line convention: dotted, drawn on top) and points
    sc.line([P0, (x0, y0, 0)], grey(0.55), lw=0.5, ls=(0, (1, 1.5)), layer=1)
    sc.dot(P0, BLACK, r=0.038, layer=1)
    sc.dot((x0, y0, 0), BLACK, r=0.032, layer=1)
    # labels
    sc.text_dir((x0, y0, 0), '$(x_0,y_0)$', (-1, 0.25), dist=3, size=FS_S)
    sc.text_dir(P0 + tx, 'slope $f_x$', (-1, -0.2), dist=2.5, color=figR, size=FS_S, halo=True)
    sc.text_dir(P0 + ty, 'slope $f_y$', (0.35, 1), dist=2.0, color=figG, size=FS_S, halo=True)
    sc.text_dir((xb, y0, fgraph(xb, y0)), '$f(x,y_0)$', (-1, -0.2), dist=3, color=figR, size=FS_S, halo=True)
    sc.text_dir((x0, yb, fgraph(x0, yb)), '$f(x_0,y)$', (1, -0.2), dist=3, color=figG, size=FS_S, halo=True)
    sc.text_dir((xa, ya, fgraph(xa, ya)), '$z=f(x,y)$', (-0.5, 1), dist=2.5, color=figB, size=FS)
    render([sc], 'm452-4-1.svg')


# ================ §6 Fig. 1: tangent plane ================
def fig_6_1():
    sc = Scene(*VIEW_STD)
    xa, xb, ya, yb = 0.25, 2.25, 0.25, 2.45
    x0, y0 = 1.15, 1.3; z0 = fdome(x0, y0)
    P0 = np.array([x0, y0, z0])
    sc.fill([(xa, ya, 0), (xb, ya, 0), (xb, yb, 0), (xa, yb, 0)], grey(0.045), ec=grey(0.35), lw=0.4, layer=-1)
    sc.axes((2.75, 2.95, 2.45))
    u, v = np.meshgrid(np.linspace(xa, xb, 41), np.linspace(ya, yb, 45), indexing='ij')
    sc.surface(u, v, fdome(u, v), figB, mesh=(5, 5), edge_lw=0.7)
    # tangent plane patch centred at P0: z = f(x0,y0) + f_x h + f_y k.  The surface lies below it
    # near P0, so the (translucent) plane is drawn on top as a single polygon.
    fx, fy = fdome_x(x0, y0), fdome_y(x0, y0)
    s = 0.62
    corners = [(x0 + h, y0 + k, z0 + fx*h + fy*k) for h, k in [(-s, -s), (s, -s), (s, s), (-s, s)]]
    sc.fill(corners, mix(figR, 0.35), ec=figR, lw=0.8, alpha=0.55, layer=1)
    for p, q in zip(corners, corners[1:] + corners[:1]):
        sc.line([p, q], figR, lw=0.8, layer=1, split=False)
    sc.line([P0, (x0, y0, 0)], grey(0.55), lw=0.5, ls=(0, (1, 1.5)), layer=1)
    sc.dot(P0, BLACK, r=0.038, layer=2)
    sc.dot((x0, y0, 0), BLACK, r=0.032, layer=1)
    # labels
    sc.text_dir((x0, y0, 0), '$(x_0,y_0)$', (0.25, -1), dist=2.5, size=FS_S)
    sc.text_dir(corners[3], '$z=f(x_0,y_0)+L(h,k)$', (1, 0.2), dist=3, color=figR, size=FS_S)
    tip = sc.P(P0) - sc.off
    lab = tip + np.array([-0.55, 0.42])
    sc.line2d([tip + unit(lab - tip)*0.06, lab], BLACK, lw=0.4, layer=3)
    sc.text(lab, '$(x_0,y_0,f(x_0,y_0))$', off=(-1, 1), ha='right', va='bottom', size=FS_S, raw2d=True)
    sc.text_dir((xb, ya, fdome(xb, ya)), '$z=f(x,y)$', (-1, 0.3), dist=3, color=figB, size=FS)
    render([sc], 'm452-6-1.svg')


# ================ §14 Fig. 1: min / max / saddle ================
def fig_14_1():
    ca, sa = np.cos(np.radians(35)), np.sin(np.radians(35))
    def saddle(x, y):   # rising toward the screen's left and right, falling toward front and back
        u, w = -sa*x + ca*y, ca*x + sa*y
        return 0.4*(u**2 - w**2)
    specs = [(lambda x, y: 0.55*(x**2 + y**2), 'local min', r'$f_{xx}>0,\ \det H>0$'),
             (lambda x, y: -0.55*(x**2 + y**2), 'local max', r'$f_{xx}<0,\ \det H>0$'),
             (saddle, 'saddle', r'$\det H<0$')]
    scenes = []
    for k, (fun, t1, t2) in enumerate(specs):
        sc = Scene(32, 35)
        r, th = np.meshgrid(np.linspace(0, 1, 25), np.linspace(0, 2*np.pi, 73), indexing='ij')
        X, Y = r*np.cos(th), r*np.sin(th)
        sc.surface(X, Y, fun(X, Y), figB, mesh=(6, 6), edge_lw=0.8, lo=0.10, hi=0.40,
                   edges=(False, True, False, False))
        sc.dot((0, 0, fun(0, 0)), figR, r=0.065, bias=0.1)
        lo, hi = sc.bounds()
        sc.shift(2.45*k - (lo[0] + hi[0])/2, -(lo[1] + hi[1])/2)   # centre the panels on one row
        scenes.append(sc)
    low = min(sc.bounds()[0][1] for sc in scenes)
    for k, (sc, (_, t1, t2)) in enumerate(zip(scenes, specs)):
        sc.text(np.array([2.45*k, low - 0.12]) - sc.off, t1 + '\n' + t2, ha='center', va='top', size=FS, raw2d=True)
    render(scenes, 'm452-14-1.svg', scale=0.6)


# ================ §15 Fig. 1: lower / upper Darboux sums ================
def darboux_f(x, y):
    return 0.95 + 0.50*np.sin(1.35*x) + 0.40*np.cos(1.25*y) + 0.10*x

def _box(sc, xa, xb, ya, yb, h, fcol, ecol, lo, hi, n=6, glass=False):
    """Axis-parallel box [xa,xb]x[ya,yb]x[0,h]. Opaque: subdivided faces (painter-safe).
    glass: only viewer-facing faces, translucent, on top."""
    faces = [  # (corner, du, dv, outward normal)
        ((xa, ya, h), (xb-xa, 0, 0), (0, yb-ya, 0), (0, 0, 1)),
        ((xa, ya, 0), (xb-xa, 0, 0), (0, yb-ya, 0), (0, 0, -1)),
        ((xa, ya, 0), (xb-xa, 0, 0), (0, 0, h), (0, -1, 0)),
        ((xa, yb, 0), (xb-xa, 0, 0), (0, 0, h), (0, 1, 0)),
        ((xa, ya, 0), (0, yb-ya, 0), (0, 0, h), (-1, 0, 0)),
        ((xb, ya, 0), (0, yb-ya, 0), (0, 0, h), (1, 0, 0)),
    ]
    for c, du, dv, nrm in faces:
        c, du, dv, nrm = map(np.asarray, (c, du, dv, nrm))
        front = nrm @ sc.d > 0
        col = sc.shade(nrm.astype(float), fcol, lo, hi)
        if glass:
            if not front: continue
            sc.fill([c, c + du, c + du + dv, c + dv], col, ec='none', alpha=0.30, layer=1)
            for a, b in [(c, c + du), (c + du, c + du + dv), (c + du + dv, c + dv), (c + dv, c)]:
                sc.line([a, b], ecol, lw=0.5, layer=2, split=False)
            continue
        if not front: continue
        m = max(2, int(np.ceil(max(np.linalg.norm(du), np.linalg.norm(dv)) / 0.09)))
        for i in range(m):
            for j in range(m):
                p = c + du*i/m + dv*j/m
                sc.fill([p, p + du/m, p + du/m + dv/m, p + dv/m], col)
        for a, b in [(c, c + du), (c + du, c + du + dv), (c + du + dv, c + dv), (c + dv, c)]:
            sc.line(np.linspace(a, b, m + 1), ecol, lw=0.55, bias=0.004)

def fig_15_1():
    xa, xb, ya, yb = 0.35, 2.75, 0.35, 2.55
    nx, ny = 3, 3
    xs, ys = np.linspace(xa, xb, nx + 1), np.linspace(ya, yb, ny + 1)
    gx, gy = np.meshgrid(np.linspace(xa, xb, 49), np.linspace(ya, yb, 45), indexing='ij')
    gz = darboux_f(gx, gy)
    scenes = []
    for k, mode in enumerate(('lower', 'upper')):
        sc = Scene(24, 32, offset=(4.05*k, 0))
        sc.fill([(xa, ya, 0), (xb, ya, 0), (xb, yb, 0), (xa, yb, 0)], grey(0.045), ec=grey(0.35), lw=0.4, layer=-1)
        for x in xs[1:-1]: sc.line([(x, ya, 0), (x, yb, 0)], grey(0.35), lw=0.4, layer=-1, split=False)
        for y in ys[1:-1]: sc.line([(xa, y, 0), (xb, y, 0)], grey(0.35), lw=0.4, layer=-1, split=False)
        sc.axes((3.05, 3.0, 2.2), size=FS_S)
        for i in range(nx):
            for j in range(ny):
                cx, cy = np.meshgrid(np.linspace(xs[i], xs[i+1], 30), np.linspace(ys[j], ys[j+1], 30))
                vals = darboux_f(cx, cy)
                if mode == 'lower':
                    _box(sc, xs[i], xs[i+1], ys[j], ys[j+1], vals.min(), figG, figG, 0.14, 0.40)
                else:
                    _box(sc, xs[i], xs[i+1], ys[j], ys[j+1], vals.max(), figR, figR, 0.10, 0.30, glass=True)
        if mode == 'lower':
            # surface above inscribed boxes: wireframe only, so the boxes stay visible
            for i in range(0, gx.shape[0], 4):
                sc.line(np.c_[gx[i], gy[i], gz[i]], figB, lw=0.45, bias=0.01)
            for j in range(0, gx.shape[1], 4):
                sc.line(np.c_[gx[:, j], gy[:, j], gz[:, j]], figB, lw=0.45, bias=0.01)
            for b in (0, -1):
                sc.line(np.c_[gx[b], gy[b], gz[b]], figB, lw=0.9, bias=0.012)
                sc.line(np.c_[gx[:, b], gy[:, b], gz[:, b]], figB, lw=0.9, bias=0.012)
            sc.text_dir((xb, ya, darboux_f(xb, ya)), '$z=f(x,y)$', (-1, 0.4), dist=2.5, color=figB, size=FS_S)
            lab = r'$L(f,\mathcal{T})=\sum m_i\,|D_i|$'
        else:
            sc.surface(gx, gy, gz, figB, mesh=(4, 4), edge_lw=0.8, lo=0.14, hi=0.45)
            lab = r'$U(f,\mathcal{T})=\sum M_i\,|D_i|$'
        allp = np.stack([gx, gy, np.zeros_like(gx)], -1).reshape(-1, 3)
        p2 = sc.P(allp) - sc.off
        sc.text(np.array([p2[:, 0].mean(), p2[:, 1].min() - 0.12]), lab, ha='center', va='top', size=FS, raw2d=True)
        scenes.append(sc)
    render(scenes, 'm452-15-1.svg', scale=0.6)


# ================ §15 Fig. 2: Fubini slicing ================
def fubini_f(x, y):
    return 1.30 + 0.30*np.sin(1.1*x) + 0.25*np.cos(1.0*y) + 0.06*x

def fig_15_2():
    sc = Scene(24, -122)         # x to the right, y going back-left: the slices x = const face the viewer
    a, b, c, d = 0.45, 2.85, 0.4, 2.2
    x0, dx = 1.45, 0.16
    f = fubini_f
    # ground rectangle and dotted guides to the axes
    sc.fill([(a, c, 0), (b, c, 0), (b, d, 0), (a, d, 0)], grey(0.05), ec=grey(0.4), lw=0.4, layer=-1)
    for p, q in [((a, 0, 0), (a, c, 0)), ((b, 0, 0), (b, c, 0)), ((0, c, 0), (a, c, 0)), ((0, d, 0), (a, d, 0)),
                 ((x0, 0, 0), (x0, c, 0))]:
        sc.line([p, q], grey(0.45), lw=0.4, ls=(0, (1, 1.5)), layer=-0.5)
    sc.axes((3.35, 2.75, 2.6))
    for p, lab in [((a, 0, 0), '$a$'), ((b, 0, 0), '$b$'), ((x0, 0, 0), '$x$')]:
        sc.line([np.add(p, (0, 0, -0.04)), np.add(p, (0, 0, 0.04))], BLACK, lw=0.5, split=False)
        sc.text_dir(p, lab, (0, -1), dist=2.5, size=FS_S, color=figR if lab == '$x$' else BLACK)
    sc.line([(x0 + dx, 0, 0), (x0 + dx, c, 0)], grey(0.45), lw=0.4, ls=(0, (1, 1.5)), layer=-0.5)
    for p, lab in [((0, c, 0), '$c$'), ((0, d, 0), '$d$')]:
        sc.line([np.add(p, (0, 0, -0.04)), np.add(p, (0, 0, 0.04))], BLACK, lw=0.5, split=False)
        sc.text_dir(p, lab, (-1, -0.3), dist=2.5, size=FS_S)

    def solid(x1, x2, col, lo, hi, nx, mesh):
        X, Y = np.meshgrid(np.linspace(x1, x2, nx), np.linspace(c, d, 37), indexing='ij')
        sc.surface(X, Y, f(X, Y), col, lo=lo, hi=hi, mesh=mesh, edge_lw=0.7)
        ts = np.linspace(0, 1, 9)
        for yv in (c, d):   # walls y = const
            Xw, T = np.meshgrid(np.linspace(x1, x2, nx), ts, indexing='ij')
            sc.surface(Xw, np.full_like(Xw, yv), T*f(Xw, yv), col, lo=lo, hi=hi, edge_lw=0.7)
        for xv in (x1, x2):  # walls x = const
            Yw, T = np.meshgrid(np.linspace(c, d, 37), ts, indexing='ij')
            sc.surface(np.full_like(Yw, xv), Yw, T*f(xv, Yw), col, lo=lo, hi=hi, edge_lw=0.7)
    solid(x0 + dx, b, figB, 0.08, 0.30, 23, (4, 6))
    solid(x0, x0 + dx, figR, 0.20, 0.42, 3, None)
    # the rest of the solid, x in [a, x0]: light outline only
    ghost = mix(figB, 0.55); gls = (0, (2.5, 1.5))
    Ys = np.linspace(c, d, 60); Xs = np.linspace(a, x0, 60)
    for curve in (np.c_[Xs, np.full_like(Xs, c), f(Xs, c)], np.c_[Xs, np.full_like(Xs, d), f(Xs, d)],
                  np.c_[np.full_like(Ys, a), Ys, f(a, Ys)]):
        sc.line(curve, ghost, lw=0.55, ls=gls, split=False)
    for yv in (c, d):
        sc.line([(a, yv, 0), (a, yv, f(a, yv))], ghost, lw=0.55, ls=gls, split=False)
    # labels
    face = np.array([x0, (c + d)/2, 0.5*f(x0, (c + d)/2)])
    sc.text(face, '$A(x)$', color=figR, size=FS, halo=True)
    sc.text_dir((b, d, f(b, d)), '$z=f(x,y)$', (0.3, 1), dist=2.5, color=figB, size=FS_S)
    render([sc], 'm452-15-2.svg')


# ================ §18 Fig. 1: cell -> curved patch ~ tangent parallelogram ================
def fig_18_1():
    sc = Scene(36, -62)
    # ---- left: parameter domain (plain 2D, drawn at scale k to the left of the 3D scene) ----
    k = 0.8
    U0, U1, V0, V1 = 0.25, 2.25, 0.25, 1.75
    nu, nv = 4, 3
    ug, vg = np.linspace(U0, U1, nu + 1), np.linspace(V0, V1, nv + 1)
    O = np.array([-2.75, -0.55])
    Q = lambda u, v: O + k*np.array([u, v])
    ah = dict(lw=0.5, hl=0.085, hw=0.032)
    sc.arrow2d(Q(-0.15, 0), Q(2.6, 0), BLACK, **ah)
    sc.arrow2d(Q(0, -0.15), Q(0, 2.05), BLACK, **ah)
    sc.text(Q(2.6, 0), '$u$', off=(2, 0), ha='left', va='center', raw2d=True)
    sc.text(Q(0, 2.05), '$v$', off=(0, 2), ha='center', va='bottom', raw2d=True)
    sc.fill2d([Q(U0, V0), Q(U1, V0), Q(U1, V1), Q(U0, V1)], mix(figB, 0.10), ec=figB, lw=0.8, depth=-9)
    for u in ug[1:-1]: sc.line2d([Q(u, V0), Q(u, V1)], mix(figB, 0.5), lw=0.4, depth=-8)
    for v in vg[1:-1]: sc.line2d([Q(U0, v), Q(U1, v)], mix(figB, 0.5), lw=0.4, depth=-8)
    ci, cj = 2, 1
    ca, cb, da, db = ug[ci], ug[ci+1], vg[cj], vg[cj+1]
    sc.fill2d([Q(ca, da), Q(cb, da), Q(cb, db), Q(ca, db)], mix(figR, 0.30), ec=figR, lw=0.9, depth=-7)
    sc.text(Q((ca + cb)/2, da), r'$\Delta u$', off=(0, -1.5), ha='center', va='top', color=figR, size=FS_S, raw2d=True)
    sc.text(Q(cb, (da + db)/2), r'$\Delta v$', off=(1.5, 0), ha='left', va='center', color=figR, size=FS_S, raw2d=True)
    sc.text(Q(U0, V1), '$D$', off=(2, -2), ha='left', va='top', color=figB, size=FS, raw2d=True)
    # ---- right: the surface ----
    def S(u, v):
        return np.stack([1.05*u - 0.10*v,
                         1.05*v + 0.10*u,
                         0.42*np.sin(1.6*u + 0.1) + 0.32*np.cos(1.8*(v - 1.0)) + 0.55*v - 0.05*u], -1)
    uu, vv = np.meshgrid(np.linspace(U0, U1, 41), np.linspace(V0, V1, 31), indexing='ij')
    Pts = S(uu, vv)
    sc.surface(Pts[..., 0], Pts[..., 1], Pts[..., 2], figB, mesh=(10, 10), mesh_lw=0.45, edge_lw=0.8)
    # curved patch = image of the red cell
    pu, pv = np.meshgrid(np.linspace(ca, cb, 11), np.linspace(da, db, 11), indexing='ij')
    Pp = S(pu, pv)
    sc.surface(Pp[..., 0], Pp[..., 1], Pp[..., 2], figR, fc=mix(figR, 0.30), edge_color=figR, edge_lw=0.9,
               bias=0.02, silhouette=False)
    # tangent parallelogram at the corner X(ca,da): outline only, so the red patch stays visible
    eps = 1e-5
    P0 = S(ca, da); Xu = (S(ca + eps, da) - P0)/eps; Xv = (S(ca, da + eps) - P0)/eps
    A, B = Xu*(cb - ca), Xv*(db - da)
    sc.line([P0 + A, P0 + A + B, P0 + B], figG, lw=0.7, ls=(0, (2.5, 1.5)), layer=1)
    sc.arrow(P0, P0 + A, figG, lw=1.0, layer=1)
    sc.arrow(P0, P0 + B, figG, lw=1.0, layer=1)
    sc.dot(P0, BLACK, r=0.03, layer=2)
    sc.text_dir(P0 + A, r'$\mathbf{X}_u\Delta u$', (0.3, -1), dist=2, color=figG, size=FS_S, halo=True)
    sc.text_dir(P0 + B, r'$\mathbf{X}_v\Delta v$', (-1, 0.3), dist=2, color=figG, size=FS_S, halo=True)
    sc.text_dir(S(U1, V1), r'$S=\mathbf{X}(D)$', (1, -0.25), dist=3, color=figB, size=FS)
    # map arrow between the panels
    lo, hi = sc.bounds()
    xl = Q(U1, 0)[0] + 0.45; y_mid = Q(0, (V0 + V1)/2)[1] + 0.25
    xr = min(sc.P(Pts.reshape(-1, 3))[:, 0]) - 0.1
    A0, A1 = np.array([xl, y_mid]), np.array([xr, y_mid])
    sc.arrow2d(A0, A1, BLACK, lw=0.7, hl=0.09, hw=0.036)
    sc.text((A0 + A1)/2, r'$\mathbf{X}$', off=(0, 2.5), ha='center', va='bottom', size=FS, raw2d=True)
    render([sc], 'm452-18-1.svg')


# ================ §18 Fig. 2: divergence theorem ================
def fig_18_2():
    sc = Scene(20, -60)  # used only as a 2D canvas
    R = 1.25
    t = np.linspace(0, 2*np.pi, 200)
    circ = np.c_[R*np.cos(t), R*np.sin(t)]
    sc.fill2d(circ, mix(figB, 0.09), ec=figB, lw=1.0, depth=-10)
    # equator: front half solid, back half dashed
    k = np.sin(np.radians(20))
    tf = np.linspace(np.pi, 2*np.pi, 80); tb = np.linspace(0, np.pi, 80)
    sc.line2d(np.c_[R*np.cos(tf), k*R*np.sin(tf)], mix(figB, 0.6), lw=0.5, depth=-9)
    sc.line2d(np.c_[R*np.cos(tb), k*R*np.sin(tb)], mix(figB, 0.45), lw=0.5, ls=(0, (3, 2)), depth=-9)
    # green field arrows crossing the boundary outward (at silhouette points, so they
    # visibly cross \partial V along the outward normal)
    for ang in (12, 68, 128, 172, 220, 285, 332):
        n = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
        sc.arrow2d(0.86*R*n, 1.40*R*n, figG, lw=1.0, hl=0.10, hw=0.042, depth=1)
    # outward unit normal at a separate boundary point
    nn = np.array([np.cos(np.radians(98)), np.sin(np.radians(98))])
    sc.arrow2d(R*nn, 1.30*R*nn, BLACK, lw=0.8, hl=0.085, hw=0.035, depth=1)
    sc.dot2d(R*nn, BLACK, r=0.025, depth=1)
    sc.text(1.30*R*nn, r'$\hat n$', off=(0, 1.5), ha='center', va='bottom', size=FS, raw2d=True)
    n_u = np.array([np.cos(np.radians(12)), np.sin(np.radians(12))])
    sc.text(1.40*R*n_u, r'$\mathbf{u}$', off=(2, 0), ha='left', va='center', color=figG, size=FS, raw2d=True)
    # interior sources: dots with radiating arrows
    for c, s in [((-0.42, 0.30), 1.0), ((0.38, -0.12), 1.0), ((-0.18, -0.55), 0.85)]:
        c = np.array(c)
        for j in range(6):
            a = np.radians(15 + 60*j)
            e = np.array([np.cos(a), np.sin(a)])
            sc.arrow2d(c + 0.07*e, c + 0.27*s*e, figR, lw=0.65, hl=0.065, hw=0.028, depth=2)
        sc.dot2d(c, figR, r=0.04, depth=3)
    sc.text(np.array([0.38 + 0.29, -0.12 + 0.05]), r'$\nabla\!\cdot\mathbf{u}$', off=(1, 0), ha='left', va='bottom',
            color=figR, size=FS_S, raw2d=True)
    sc.text(np.array([0.05, 0.78]), '$V$', size=9, raw2d=True)
    tb2 = np.radians(250)
    sc.text(R*np.array([np.cos(tb2), np.sin(tb2)]), r'$\partial V$', off=(-3, -3), ha='right', va='top',
            color=figB, size=FS, raw2d=True)
    render([sc], 'm452-18-2.svg')


# ================ §19 Fig. 1: spherical coordinates (theta polar, psi azimuth) ================
def sph(r, th, ps):
    """Note's convention: theta = polar angle from the z-axis, psi = azimuth in the xy-plane."""
    return np.stack(np.broadcast_arrays(r*np.sin(th)*np.cos(ps), r*np.sin(th)*np.sin(ps), r*np.cos(th)), -1)

def fig_19_1():
    sc = Scene(18, 22)
    R = 1.8; th, ps = np.radians(50), np.radians(62)
    P = sph(R, th, ps); Pxy = np.array([P[0], P[1], 0])
    sc.axes((2.3, 2.4, 2.25))
    # faint coordinate curves through P: meridian (psi fixed) and parallel (theta fixed), and the equator
    tt = np.linspace(0, np.pi/2, 60); pp = np.linspace(0, np.pi/2, 60)
    for C in (sph(R, tt, ps), sph(R, th, pp), sph(R, np.pi/2, pp)):
        sc.line(C, grey(0.4), lw=0.45, ls=(0, (1, 1.5)), split=False)
    # r, drop line, projection onto the xy-plane
    sc.line([(0, 0, 0), P], figR, lw=1.2)
    sc.line([P, Pxy], grey(0.5), lw=0.6, ls=(0, (3, 1.5)), split=False)
    sc.line([(0, 0, 0), Pxy], figG, lw=0.9)
    # psi arc in the xy-plane (from the x-axis), theta arc from the z-axis to r
    rp, rt = 0.72, 0.78
    a1 = np.linspace(0, ps, 40)
    sc.line(np.c_[rp*np.cos(a1), rp*np.sin(a1), 0*a1], figG, lw=0.8)
    e = sc.P((rp*np.cos(ps), rp*np.sin(ps), 0))
    sc.head2d(e - sc.off, e - sc.P((rp*np.cos(ps - 0.1), rp*np.sin(ps - 0.1), 0)), figG, hl=0.08, hw=0.032, depth=5)
    a2 = np.linspace(0, th, 40)
    sc.line(sph(rt, a2, ps), figR, lw=0.8)
    e = sc.P(sph(rt, th, ps))
    sc.head2d(e - sc.off, e - sc.P(sph(rt, th - 0.1, ps)), figR, hl=0.08, hw=0.032, depth=5)
    sc.dot(P, figR, r=0.045, layer=1)
    # labels next to what they label
    O2 = sc.P((0, 0, 0))
    q = (rp*np.cos(ps/2), rp*np.sin(ps/2), 0)
    sc.text_dir(q, r'$\psi$', sc.P(q) - O2, dist=1.5, color=figG, size=FS)
    q = sph(rt, th/2, ps)
    sc.text_dir(q, r'$\theta$', sc.P(q) - O2, dist=1.0, color=figR, size=FS, halo=True)
    d2 = sc.P(P) - O2; nrm2 = np.array([d2[1], -d2[0]])
    sc.text_dir(P*0.6, '$r$', nrm2, dist=2.5, color=figR, size=FS)
    sc.text_dir(P, r'$P=(r,\theta,\psi)$', (1, 0.8), dist=3, color=figR, size=FS, halo=True)
    render([sc], 'm452-19-1.svg')


# ================ §19 Fig. 2: spherical volume element ================
def fig_19_2():
    sc = Scene(20, 30)
    r0, r1 = 1.75, 2.15
    t0, t1 = np.radians(40), np.radians(64)      # theta (polar)
    p0, p1 = np.radians(24), np.radians(52)      # psi (azimuth)
    sc.axes((2.9, 2.85, 2.65))
    # octant of the sphere r = r0 (light) with the coordinate curves bounding the cell
    TT, PP = np.meshgrid(np.linspace(0.02, np.pi/2, 36), np.linspace(0, np.pi/2, 36), indexing='ij')
    Sp = sph(r0, TT, PP)
    sc.surface(Sp[..., 0], Sp[..., 1], Sp[..., 2], figB, lo=0.05, hi=0.20, edge_color=mix(figB, 0.6), edge_lw=0.5)
    tr = np.linspace(0.0, np.pi/2, 60); pr = np.linspace(0, np.pi/2, 60)
    for p in (p0, p1): sc.line(sph(r0, tr, p), mix(figB, 0.75), lw=0.5, bias=0.01)
    for t in (t0, t1): sc.line(sph(r0, t, pr), mix(figB, 0.75), lw=0.5, bias=0.01)
    # the brick: six faces
    n = 10
    def face(F, col):
        for i in range(F.shape[0] - 1):
            for j in range(F.shape[1] - 1):
                q = [F[i, j], F[i+1, j], F[i+1, j+1], F[i, j+1]]
                nr = np.cross(F[i+1, j+1] - F[i, j], F[i, j+1] - F[i+1, j])
                sc.fill(q, sc.shade(nr, col, 0.18, 0.42))
    T, Pp = np.meshgrid(np.linspace(t0, t1, n), np.linspace(p0, p1, n), indexing='ij')
    Rr, T2 = np.meshgrid(np.linspace(r0, r1, 5), np.linspace(t0, t1, n), indexing='ij')
    Rr3, P3 = np.meshgrid(np.linspace(r0, r1, 5), np.linspace(p0, p1, n), indexing='ij')
    for F in (sph(r1, T, Pp), sph(r0, T, Pp), sph(Rr, T2, p0), sph(Rr, T2, p1), sph(Rr3, t0, P3), sph(Rr3, t1, P3)):
        face(F, figR)
    s = np.linspace(0, 1, 20)
    for (t, p) in [(t0, p0), (t0, p1), (t1, p0), (t1, p1)]:
        sc.line(sph(r0 + s*(r1 - r0), t, p), figR, lw=0.8, bias=0.01)
    for (r, p) in [(r0, p0), (r0, p1), (r1, p0), (r1, p1)]:
        sc.line(sph(r, t0 + s*(t1 - t0), p), figR, lw=0.8, bias=0.01)
    for (r, t) in [(r0, t0), (r0, t1), (r1, t0), (r1, t1)]:
        sc.line(sph(r, t, p0 + s*(p1 - p0)), figR, lw=0.8, bias=0.01)
    # radial guide from the origin (hidden-line convention)
    sc.line([(0, 0, 0), sph(r0, t0, p1)], grey(0.5), lw=0.5, ls=(0, (3, 1.5)), layer=1)
    # edge labels, each just outside the midpoint of a visible edge
    ctr = sc.P(sph((r0 + r1)/2, (t0 + t1)/2, (p0 + p1)/2))
    def elab(pm, pa, pb, s_, **kw):
        m2 = sc.P(pm); dd = sc.P(pb) - sc.P(pa); nr = np.array([-dd[1], dd[0]])
        if nr @ (m2 - ctr) < 0: nr = -nr
        sc.text_dir(pm, s_, nr, dist=2.5, color=figR, size=FS_S, halo=True, **kw)
    elab(sph((r0 + r1)/2, t1, p1), sph(r0, t1, p1), sph(r1, t1, p1), '$dr$')
    elab(sph(r1, (t0 + t1)/2, p1), sph(r1, t0, p1), sph(r1, t1, p1), r'$r\,d\theta$')
    elab(sph(r1, t1, (p0 + p1)/2), sph(r1, t1, p0), sph(r1, t1, p1), r'$r\sin\theta\,d\psi$')
    render([sc], 'm452-19-2.svg', extra=None)
    return sc


# ================ §20 Fig. 1: Stokes' theorem ================
def fig_20_1():
    sc = Scene(26, -62)
    def cap(rho, t):
        return np.stack(np.broadcast_arrays(1.35*rho*np.cos(t), 1.10*rho*np.sin(t),
                                            0.85*(1 - rho**2) + 0.10*rho*np.sin(2*t)), -1)
    rr, tt = np.meshgrid(np.linspace(0, 1, 21), np.linspace(0, 2*np.pi, 73), indexing='ij')
    C = cap(rr, tt)
    sc.surface(C[..., 0], C[..., 1], C[..., 2], figB, mesh=(5, 6), edge_lw=0)
    # rim: solid where visible (painter), dashed overlay shows the hidden back half
    t = np.linspace(0, 2*np.pi, 241)
    rim = cap(1.0, t)
    sc.line(rim, figG, lw=1.4, bias=0.02)
    sc.line(rim, mix(figG, 0.8), lw=0.6, ls=(0, (3, 2)), layer=-1, split=False)
    # orientation arrows on the front of the rim: counterclockwise seen from above (n up)
    for tp in (np.radians(250), np.radians(330), np.radians(170)):
        p1 = cap(1.0, tp); p2 = cap(1.0, tp + 0.03)
        sc.head2d(sc.P(p2) - sc.off, sc.P(p2) - sc.P(p1), figG, hl=0.12, hw=0.05, depth=sc.D(p2) + 0.05)
    # curl vectors with tiny loops in the tangent plane
    eps = 1e-4
    def frame(rho, tq):
        P = cap(rho, tq)
        Tu = (cap(rho + eps, tq) - cap(rho - eps, tq)) / (2*eps)
        Tv = (cap(rho, tq + eps) - cap(rho, tq - eps)) / (2*eps)
        N = unit(np.cross(Tu, Tv))
        if N[2] < 0: N = -N
        e1 = unit(Tu - (Tu @ N)*N); e2 = np.cross(N, e1)
        return P, N, e1, e2
    for (rho, tq, tilt) in [(0.52, np.radians(215), (0.25, 0.1)), (0.55, np.radians(305), (-0.2, 0.15)),
                            (0.5, np.radians(80), (0.1, -0.25))]:
        P, N, e1, e2 = frame(rho, tq)
        V = unit(N + tilt[0]*e1 + tilt[1]*e2) * 0.62
        s = np.linspace(0.15, 2*np.pi - 0.35, 40)
        loop = P + 0.13*(np.outer(np.cos(s), e1) + np.outer(np.sin(s), e2))
        sc.line(loop, figR, lw=0.6, bias=0.03)
        sc.head2d(sc.P(loop[-1]) - sc.off, sc.P(loop[-1]) - sc.P(loop[-3]), figR, hl=0.07, hw=0.03,
                  depth=sc.D(loop[-1]) + 0.03)
        sc.arrow(P, P + V, figR, lw=1.0, bias=0.05)
        if tq == np.radians(305):
            sc.text_dir(P + V, r'$\nabla\times\mathbf{F}$', (1, 0.3), dist=2, color=figR, size=FS_S)
    # the unit normal at the top of the cap
    P, N, _, _ = frame(0.0 + 1e-3, 0.0)
    P = cap(0.0, 0.0); N = np.array([0.0, 0.0, 1.0])
    sc.arrow(P, P + 0.55*N, figB, lw=1.0, bias=0.05)
    sc.dot(P, figB, r=0.03, bias=0.05)
    sc.text_dir(P + 0.55*N, r'$\hat n$', (0, 1), dist=1.5, color=figB, size=FS)
    # labels
    sc.text_dir(cap(1.0, np.radians(290)), r'$\partial S$', (0.3, -1), dist=2, color=figG, size=FS)
    sc.text(cap(0.72, np.radians(150)), '$S$', color=figB, size=9, halo=True)
    render([sc], 'm452-20-1.svg')


# ================ §21 Fig. 1: the three shadows of the tangent parallelogram ================
def fig_21_1():
    sc = Scene(22, 42)
    Lw = 2.35; Hz = 2.1
    # coordinate planes (walls) of the octant
    sc.fill([(0, 0, 0), (Lw, 0, 0), (Lw, Lw, 0), (0, Lw, 0)], grey(0.04), ec=grey(0.3), lw=0.4, layer=-3)
    sc.fill([(0, 0, 0), (0, Lw, 0), (0, Lw, Hz), (0, 0, Hz)], grey(0.04), ec=grey(0.3), lw=0.4, layer=-3)
    sc.fill([(0, 0, 0), (Lw, 0, 0), (Lw, 0, Hz), (0, 0, Hz)], grey(0.04), ec=grey(0.3), lw=0.4, layer=-3)
    P = np.array([1.05, 0.95, 1.05])
    A = np.array([0.78, 0.20, 0.30])    # X_u (du)
    B = np.array([-0.05, 0.72, 0.52])   # X_v (dv)
    quad = np.array([P, P + A, P + A + B, P + B])
    shadows = [(np.array([1, 1, 0]), figR, r'$dx\wedge dy$'),
               (np.array([0, 1, 1]), figG, r'$dy\wedge dz$'),
               (np.array([1, 0, 1]), figO, r'$dz\wedge dx$')]
    for mask, col, lab in shadows:
        sq = quad*mask
        sc.fill(sq, mix(col, 0.28), ec=col, lw=0.8, layer=-2)
        sc.line([P, P*mask], grey(0.45), lw=0.45, ls=(0, (1, 1.5)), layer=-1)
        sc.dot(P*mask, col, r=0.025, layer=-1)
        sc.text(sq.mean(0), lab, color=col, size=FS_S, halo=True)
    sc.axes((3.0, 3.0, 2.65), lw=0.5)
    sc.fill(quad, mix(figB, 0.25), ec=figB, lw=0.9, layer=0)
    sc.arrow(P, P + A, figB, lw=1.1, layer=1)
    sc.arrow(P, P + B, figB, lw=1.1, layer=1)
    sc.dot(P, BLACK, r=0.03, layer=1)
    sc.text_dir(P + A, r'$\mathbf{X}_u$', sc.P(A) - sc.P(0*A), dist=2, color=figB, size=FS)
    sc.text_dir(P + B, r'$\mathbf{X}_v$', sc.P(B) - sc.P(0*B), dist=2, color=figB, size=FS)
    render([sc], 'm452-21-1.svg')


FIGS = {'4-1': fig_4_1, '6-1': fig_6_1, '14-1': fig_14_1, '15-1': fig_15_1, '15-2': fig_15_2,
        '18-1': fig_18_1, '18-2': fig_18_2, '19-1': fig_19_1, '19-2': fig_19_2, '20-1': fig_20_1,
        '21-1': fig_21_1}

if __name__ == '__main__':
    for k in (sys.argv[1:] or FIGS):
        FIGS[k]()
