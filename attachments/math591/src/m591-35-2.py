# Vault-only figure for MATH 591 §35 (not in the course tex), 2026-10-04.
# Thm. §35.8 / Prop. §35.5: (a) for q = cos t + sin t·u, C_q(v) = q v q̄ is the rotation by 2t about u;
# (b) the great circle γ(t) = cos t + sin t·u in S^3 goes twice around the loop of rotations about u; q and −q give the same rotation.
# Run: python3 m591-35-2.py  -> ../m591-35-2.svg and ../m591-35-2.png
import os, warnings, numpy as np, matplotlib
warnings.filterwarnings('ignore', category=RuntimeWarning)
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
plt.rcParams.update({'font.family': 'serif', 'mathtext.fontset': 'cm', 'font.size': 12})
rgb = lambda r, g, b: (r / 255, g / 255, b / 255)
figB, figR, figG, figO = rgb(31, 90, 166), rgb(176, 48, 48), rgb(46, 125, 50), rgb(214, 120, 20)
grey = (0.45, 0.45, 0.45)
t = np.radians(60)          # q = cos t + sin t u ; rotation angle 2t = 120°
elev, azim = 30, -70


class Arrow3D(FancyArrowPatch):
    def __init__(self, a, b, **kw):
        super().__init__((0, 0), (0, 0), **kw); self._a, self._b = a, b
    def do_3d_projection(self, renderer=None):
        xs, ys, zs = proj3d.proj_transform(*zip(self._a, self._b), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1])); return np.min(zs)


def arrow3(ax, a, b, color, lw=1.8, ms=14):
    ax.add_artist(Arrow3D(a, b, arrowstyle='-|>', mutation_scale=ms, color=color, lw=lw, shrinkA=0, shrinkB=0))


fig = plt.figure(figsize=(12.6, 4.6))

# ---------------- (a) the rotation in H_0 = R^3 ----------------
ax = fig.add_axes([0.0, 0.0, 0.36, 0.94], projection='3d', computed_zorder=False)
u = np.array([0.0, 0.0, 1.0])
e1, e2 = np.array([1.0, 0, 0]), np.array([0, 1.0, 0])
h, rho = 0.55, 1.0                                   # v = h u + rho e1 (not perpendicular to u)
a0 = np.radians(-130)                                # v and C_q(v) symmetric about the viewing direction
rot = lambda a: h * u + rho * (np.cos(a + a0) * e1 + np.sin(a + a0) * e2)
v, w = rot(0.0), rot(2 * t)
# faint disc bounded by the orbit of the tip of v (it lies in a plane perpendicular to u)
rr, aa = np.meshgrid(np.linspace(0, rho, 2), np.linspace(np.pi / 2, 2.5 * np.pi, 80))   # seam hidden behind the axis
ax.plot_surface(rr * np.cos(aa), rr * np.sin(aa), h + 0 * rr, color=(0.9, 0.9, 0.94), alpha=0.18, linewidth=0, rasterized=True)
# axis u
ax.plot([0, 0], [0, 0], [-0.75, 0], color=figB, lw=1.4, alpha=0.5)
arrow3(ax, (0, 0, 0), (0, 0, 1.45), figB, lw=1.8)
ax.text(0.06, 0.0, 1.52, r'$u$', color=figB, fontsize=14)
# orbit of the tip of v (dashed) and its centre on the axis
a = np.linspace(0, 2 * np.pi, 200); C = np.array([rot(x) for x in a]).T
ax.plot(*C, color=grey, lw=0.9, ls=(0, (3, 3)), alpha=0.8)
ax.plot([0, 0], [0, 0], [h, h], 'o', color=grey, ms=2.5)
for p in (v, w):
    ax.plot([0, p[0]], [0, p[1]], [h, p[2]], color=grey, lw=0.8, alpha=0.8)
# v and its image
arrow3(ax, (0, 0, 0), tuple(v), 'black', lw=1.8)
arrow3(ax, (0, 0, 0), tuple(w), figR, lw=1.8)
ax.text(*(v + np.array([-0.05, 0.0, 0.1])), r'$v$', fontsize=14, ha='right')
ax.text(*(w + np.array([0.05, 0.0, 0.1])), r'$C_q(v) = q\,v\,\bar q$', color=figR, fontsize=13)
# the arc 2t
b = np.linspace(0, 2 * t, 60); A = np.array([h * u + 0.5 * (np.cos(x + a0) * e1 + np.sin(x + a0) * e2) for x in b]).T
ax.plot(*A[:, :-3], color=figR, lw=1.6)
arrow3(ax, tuple(A[:, -4]), tuple(A[:, -1]), figR, lw=1.6, ms=11)
m = h * u + 0.28 * (np.cos(t + a0) * e1 + np.sin(t + a0) * e2)
ax.text(*(m + np.array([0.1 * np.cos(0.35), 0.1 * np.sin(0.35), -0.02])), r'$2t$', color=figR, fontsize=14)
ax.set_box_aspect((1, 1, 0.95), zoom=1.25); ax.view_init(elev=elev, azim=azim)
ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_zlim(-0.6, 1.5)
ax.set_axis_off()
fig.text(0.02, 0.93, r'(a)  $q = \cos t + \sin t\, u$ acting on $\mathbb{H}_0 \cong \mathbb{R}^3$', fontsize=12.5)

# ---------------- (b) two-to-one ----------------
bx = fig.add_axes([0.38, 0.0, 0.62, 0.94]); bx.set_aspect('equal'); bx.axis('off')
bx.set_xlim(-1.75, 6.55); bx.set_ylim(-1.75, 1.85)
fig.text(0.40, 0.93, r'(b)  why it is two-to-one', fontsize=12.5)
L, Rc = np.array([0.0, 0.0]), np.array([4.6, 0.0])
pt = lambda c, r, ang: c + r * np.array([np.cos(ang), np.sin(ang)])
# left: the great circle gamma in S^3 ; first half blue, second half orange
for (a0, a1, col) in ((0, np.pi, figB), (np.pi, 2 * np.pi, figO)):
    x = np.linspace(a0, a1, 200); bx.plot(L[0] + np.cos(x), L[1] + np.sin(x), color=col, lw=2.2)
for ang, col in ((np.pi / 2, figB), (3 * np.pi / 2, figO)):     # direction of travel
    p0, p1 = pt(L, 1, ang - 0.05), pt(L, 1, ang + 0.05)
    bx.annotate('', xy=p1, xytext=p0, arrowprops=dict(arrowstyle='-|>', color=col, lw=1.6, mutation_scale=16))
bx.text(L[0], L[1] - 1.55, r'$\gamma(t) = \cos t + \sin t\, u$  in  $S^3$', ha='center', fontsize=12.5)
for ang, lab, off in ((0, r'$1$', (0.12, -0.04)), (np.pi, r'$-1$', (-0.38, -0.04))):
    p = pt(L, 1, ang); bx.plot(*p, 'o', color='black', ms=4.5); bx.text(p[0] + off[0], p[1] + off[1], lab, fontsize=13, va='center')
for ang, lab, off in ((t, r'$q = \gamma(t)$', (0.1, 0.1)), (t + np.pi, r'$-q = \gamma(t+\pi)$', (-1.05, -0.3))):
    p = pt(L, 1, ang); bx.plot(*p, 'o', color=figR, ms=6.5, zorder=5); bx.text(p[0] + off[0], p[1] + off[1], lab, color=figR, fontsize=13)
bx.plot([pt(L, 1, t)[0], pt(L, 1, t + np.pi)[0]], [pt(L, 1, t)[1], pt(L, 1, t + np.pi)[1]], color=figR, lw=0.8, ls=(0, (2, 2)), alpha=0.7)
bx.plot(*L, 'o', color=grey, ms=2.5)
# map C
bx.annotate('', xy=(3.15, 0.0), xytext=(1.55, 0.0), arrowprops=dict(arrowstyle='-|>', color='black', lw=1.3, mutation_scale=16))
bx.text(2.35, 0.12, r'$C$', ha='center', fontsize=14)
# right: the loop of rotations about u, traversed twice: inner strand = image of blue half, outer = image of orange half
x = np.linspace(0, 2 * np.pi, 300)
for r, col in ((0.94, figB), (1.06, figO)):
    bx.plot(Rc[0] + r * np.cos(x), Rc[1] + r * np.sin(x), color=col, lw=2.0)
    for ang in (np.pi / 4, 5 * np.pi / 4):
        bx.annotate('', xy=pt(Rc, r, ang + 0.05), xytext=pt(Rc, r, ang - 0.05),
                    arrowprops=dict(arrowstyle='-|>', color=col, lw=1.4, mutation_scale=13))
bx.text(Rc[0], Rc[1] - 1.55, r'rotations about $u$  in  $\mathrm{SO}(3)$', ha='center', fontsize=12.5)
p = pt(Rc, 1, 0); bx.plot(*p, 'o', color='black', ms=4.5)
bx.text(p[0] + 0.14, p[1] - 0.04, r'$I = C_1 = C_{-1}$', fontsize=13, va='center')
p = pt(Rc, 1, 2 * t); bx.plot(*p, 'o', color=figR, ms=6.5, zorder=5)
bx.text(p[0] - 0.12, p[1] + 0.2, r'$C_q = C_{-q}$', ha='right', color=figR, fontsize=13)
bx.plot(*Rc, 'o', color=grey, ms=2.5)
bx.plot([Rc[0], pt(Rc, 0.9, 0)[0]], [0, 0], color=grey, lw=0.7)
bx.plot([Rc[0], pt(Rc, 0.9, 2 * t)[0]], [0, pt(Rc, 0.9, 2 * t)[1]], color=grey, lw=0.7)
xa = np.linspace(0, 2 * t, 40); bx.plot(Rc[0] + 0.3 * np.cos(xa), Rc[1] + 0.3 * np.sin(xa), color=figR, lw=1.1)
bx.text(*(pt(Rc, 0.42, t) + np.array([-0.02, -0.02])), r'$2t$', color=figR, fontsize=12, ha='center', va='center')

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'm591-35-2')
fig.savefig(out + '.svg', bbox_inches='tight', pad_inches=0.03, dpi=200)
fig.savefig(out + '.png', bbox_inches='tight', pad_inches=0.03, dpi=110)
print('ok', os.path.getsize(out + '.svg'))
