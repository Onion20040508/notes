# Figure for MATH 591 §34, Example "The Irrational Line on the Torus": the curve F(t) = [t, αt] drawn on a torus in R^3.
# Not from the notes' tex (added in the vault at the student's request, 2026-10-04). α = (5 − √5)/10, smaller than in m591-33-2 so the stripes run more vertically.
# Run: python3 m591-34-1.py  -> ../m591-34-1.svg (surface rasterized) and a PNG preview next to it.
import os, warnings, numpy as np, matplotlib
warnings.filterwarnings('ignore', category=RuntimeWarning)
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family': 'serif', 'mathtext.fontset': 'cm', 'font.size': 11})
rgb = lambda r, g, b: (r / 255, g / 255, b / 255)
figB, figR, figO = rgb(31, 90, 166), rgb(176, 48, 48), rgb(214, 120, 20)
R, r = 2.0, 0.8
alpha = (5 - np.sqrt(5)) / 10   # = 1/(3 + golden ratio) ≈ 0.276, badly approximable: strands spread evenly, ~3.6 tube turns per hole turn
elev, azim = 32, -58

def emb(theta, phi):
    return np.array([(R + r * np.cos(phi)) * np.cos(theta), (R + r * np.cos(phi)) * np.sin(theta), r * np.sin(phi)])

def view_dir():
    e, a = np.radians(elev), np.radians(azim)
    return np.array([np.cos(e) * np.cos(a), np.cos(e) * np.sin(a), np.sin(e)])

def front(theta, phi):  # outward normal of the torus faces the viewer
    n = np.array([np.cos(phi) * np.cos(theta), np.cos(phi) * np.sin(theta), np.sin(phi)])
    return n.T @ view_dir() > 0

def panel(ax, T, n, lw, title, mark_start=False):
    th, ph = np.meshgrid(np.linspace(0, 2 * np.pi, 120), np.linspace(0, 2 * np.pi, 60))
    X, Y, Z = emb(th, ph)
    ax.plot_surface(X, Y, Z, color=(0.93, 0.93, 0.95), alpha=0.55, linewidth=0, shade=True, rasterized=True, antialiased=True)
    t = np.linspace(0, T, n)
    theta, phi = 2 * np.pi * alpha * t, 2 * np.pi * t   # horizontal coordinate t winds around the tube, αt around the hole
    P = emb(theta, phi); f = front(theta, phi)
    for vis in (False, True):
        Q = P.copy(); Q[:, f != vis] = np.nan
        ax.plot(*Q, color=figB, lw=lw if vis else lw * 0.8, alpha=1.0 if vis else 0.22, solid_capstyle='round')
    if mark_start:
        p0 = emb(0.0, 0.0); ax.scatter(*p0, color=figR, s=18, depthshade=False, zorder=10)
        ax.text(*(p0 + np.array([0.25, -0.1, 0.45])), r'$F(0)$', color=figR, fontsize=10, zorder=11)
    ax.set_box_aspect((1, 1, 0.42), zoom=1.3); ax.view_init(elev=elev, azim=azim)
    lim = R + r; ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-r * 1.6, r * 1.6)
    ax.set_axis_off(); ax.set_title(title, fontsize=11, pad=-10)

fig = plt.figure(figsize=(9.4, 3.4))
ax1 = fig.add_subplot(1, 2, 1, projection='3d', computed_zorder=False)
panel(ax1, 9, 6000, 1.2, r'$t \in [0, 9]$', mark_start=True)
ax2 = fig.add_subplot(1, 2, 2, projection='3d', computed_zorder=False)
panel(ax2, 40, 30000, 0.7, r'$t \in [0, 40]$')
plt.subplots_adjust(left=0, right=1, top=0.93, bottom=0, wspace=-0.05)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'm591-34-1')
fig.savefig(out + '.svg', bbox_inches='tight', pad_inches=0.02, dpi=200)
fig.savefig(out + '.png', bbox_inches='tight', pad_inches=0.02, dpi=110)
print('ok', os.path.getsize(out + '.svg'))
