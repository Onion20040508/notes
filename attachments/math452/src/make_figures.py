# Figures from MATH 452 notes (matplotlib). Writes m452-N-j.svg into attachments/math452/. Original: OneDrive 452 folder, make_figures.py.
import os, matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.fonttype']='path'
OUT=os.environ.get('OUT', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB = '#1F5AA6'; figR = '#B03030'; figG = '#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def axes_triad(ax, L=(2.8,2.6,2.2), off=0.08):
    for vec,lab in zip(np.eye(3)*np.array(L)[:,None].T, ('$x$','$y$','$z$')):
        a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=12,
                    lw=1.0, arrowstyle='-|>', color='black')
        ax.add_artist(a)
        ax.text(vec[0]+off, vec[1]+off, vec[2]+off, lab, fontsize=12)

def f(x, y):
    return 1.15 + 0.45*np.sin(1.35*x) + 0.38*np.cos(1.15*y) + 0.05*x

# ================ F2: tangent plane ================
fig = plt.figure(figsize=(5.4, 4.0))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
xx, yy = np.meshgrid(np.linspace(0.35, 2.45, 60), np.linspace(0.35, 2.45, 60))
ax.plot_surface(xx, yy, f(xx,yy), color=figB, alpha=0.30, linewidth=0)
x0, y0 = 1.35, 1.25; z0 = f(x0,y0)
fx = 0.45*1.35*np.cos(1.35*x0) + 0.05
fy = -0.38*1.15*np.sin(1.15*y0)
s = 0.52
P = np.array([[x0-s,y0-s],[x0+s,y0-s],[x0+s,y0+s],[x0-s,y0+s]])
Z = z0 + fx*(P[:,0]-x0) + fy*(P[:,1]-y0)
ax.add_collection3d(Poly3DCollection([list(zip(P[:,0],P[:,1],Z))],
                    facecolor=figR, alpha=0.40, edgecolor=figR, lw=1.5))
ax.scatter([x0],[y0],[z0], color='black', s=20, depthshade=False)
axes_triad(ax, L=(3.0,2.9,2.3))
ax.view_init(elev=24, azim=-57)
ax.set_xlim(0,2.9); ax.set_ylim(0,2.8); ax.set_zlim(0,2.3)
ax.set_box_aspect((1,1,0.7))
ax.text2D(0.60, 0.90, '$z=f(x,y)$', transform=ax.transAxes, color=figB, fontsize=13)
ax.text2D(0.76, 0.60, 'tangent plane', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.42, 0.36, '$(x_0,y_0,f(x_0,y_0))$', transform=ax.transAxes, fontsize=10)
plt.savefig(OUT+'/m452-6-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================ F13: partial derivative slices ================
fig = plt.figure(figsize=(5.6, 4.0))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
ax.plot_surface(xx, yy, f(xx,yy), color=figB, alpha=0.22, linewidth=0)
xs = np.linspace(0.35, 2.45, 80)
ax.plot(xs, np.full_like(xs,y0), f(xs,y0), color=figR, lw=2.6)
ys = np.linspace(0.35, 2.45, 80)
ax.plot(np.full_like(ys,x0), ys, f(x0,ys), color=figG, lw=2.6)
ax.scatter([x0],[y0],[z0], color='black', s=20, depthshade=False)
axes_triad(ax, L=(3.0,2.9,2.3))
ax.view_init(elev=24, azim=-57)
ax.set_xlim(0,2.9); ax.set_ylim(0,2.8); ax.set_zlim(0,2.3)
ax.set_box_aspect((1,1,0.7))
ax.text2D(0.56, 0.92, '$z=f(x,y)$', transform=ax.transAxes, color=figB, fontsize=13)
ax.text2D(0.63, 0.50, r'$x\mapsto f(x,y_0)$: slope $=f_x$', transform=ax.transAxes, color=figR, fontsize=11)
ax.text2D(0.10, 0.76, r'$y\mapsto f(x_0,y)$: slope $=f_y$', transform=ax.transAxes, color=figG, fontsize=11)
ax.text2D(0.40, 0.42, '$(x_0,y_0)$', transform=ax.transAxes, fontsize=10)
plt.savefig(OUT+'/m452-4-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================ F7: parametrized surface ================
fig = plt.figure(figsize=(7.8, 3.4))
axL = fig.add_axes([0.02, 0.12, 0.27, 0.76])
axL.set_xlim(-0.3, 3.1); axL.set_ylim(-0.55, 2.7); axL.set_aspect('equal'); axL.axis('off')
axL.annotate('', xy=(3.0,0), xytext=(-0.2,0), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.annotate('', xy=(0,2.55), xytext=(0,-0.3), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.text(3.02,-0.06,'$u$',fontsize=12); axL.text(-0.06,2.6,'$v$',fontsize=12)
axL.add_patch(Rectangle((0.4,0.35), 2.1, 1.75, facecolor=figB, alpha=0.10, edgecolor=figB, lw=1.4))
for u in np.linspace(0.4,2.5,5)[1:-1]: axL.plot([u,u],[0.35,2.1], color=figB, alpha=0.4, lw=0.7)
for v in np.linspace(0.35,2.1,5)[1:-1]: axL.plot([0.4,2.5],[v,v], color=figB, alpha=0.4, lw=0.7)
axL.plot([1.45],[1.22],'ko',ms=3.5); axL.text(1.52,1.0,'$(u_0,v_0)$',fontsize=9)
axL.text(0.6,-0.5,'parameter domain $D$',fontsize=11)
fig.text(0.315, 0.55, r'$\mathbf{X}$', fontsize=14)
fig.patches.append(FancyArrowPatch((0.30,0.50),(0.36,0.50), transform=fig.transFigure,
                                    arrowstyle='-|>', mutation_scale=14, lw=1.3, color='black'))
axR = fig.add_axes([0.34, -0.06, 0.66, 1.12], projection='3d')
axR.set_axis_off(); axR.set_proj_type('ortho')
uu, vv = np.meshgrid(np.linspace(0,2.1,50), np.linspace(0,1.75,50))
XX = 0.3 + uu + 0.18*vv
YY = 0.2 + 0.9*vv
ZZ = 0.9 + 0.42*np.sin(1.3*uu) + 0.36*np.cos(1.35*vv) + 0.06*uu
axR.plot_surface(XX, YY, ZZ, color=figB, alpha=0.25, linewidth=0)
for uc in np.linspace(0,2.1,5):
    v1 = np.linspace(0,1.75,60)
    axR.plot(0.3+uc+0.18*v1, 0.2+0.9*v1, 0.9+0.42*np.sin(1.3*uc)+0.36*np.cos(1.35*v1)+0.06*uc,
             color=figB, alpha=0.5, lw=0.7)
for vc in np.linspace(0,1.75,5):
    u1 = np.linspace(0,2.1,60)
    axR.plot(0.3+u1+0.18*vc, 0.2+0.9*vc, 0.9+0.42*np.sin(1.3*u1)+0.36*np.cos(1.35*vc)+0.06*u1,
             color=figB, alpha=0.5, lw=0.7)
u0v, v0v = 1.05, 0.875
P0 = np.array([0.3+u0v+0.18*v0v, 0.2+0.9*v0v, 0.9+0.42*np.sin(1.3*u0v)+0.36*np.cos(1.35*v0v)+0.06*u0v])
Xu = np.array([1,0,0.42*1.3*np.cos(1.3*u0v)+0.06]); Xu = 0.75*Xu/np.linalg.norm(Xu)
Xv = np.array([0.18,0.9,-0.36*1.35*np.sin(1.35*v0v)]); Xv = 0.75*Xv/np.linalg.norm(Xv)
Nn = np.cross(Xu,Xv); Nn = 0.8*Nn/np.linalg.norm(Nn)
for vec,col in [(Xu,figG),(Xv,figG),(Nn,figR)]:
    a = Arrow3D([P0[0],P0[0]+vec[0]],[P0[1],P0[1]+vec[1]],[P0[2],P0[2]+vec[2]],
                mutation_scale=13, lw=2.0, arrowstyle='-|>', color=col)
    axR.add_artist(a)
axR.scatter(*P0, color='black', s=16, depthshade=False)
axR.view_init(elev=26, azim=-60)
axR.set_xlim(0.2,2.9); axR.set_ylim(0,1.9); axR.set_zlim(0.4,2.3)
axR.set_box_aspect((1.35,0.95,0.85))
axR.text2D(0.70, 0.94, r'$S=\mathbf{X}(D)$', transform=axR.transAxes, color=figB, fontsize=12)
axR.text2D(0.40, 0.88, r'$\mathbf{X}_u\times\mathbf{X}_v$', transform=axR.transAxes, color=figR, fontsize=11)
axR.text2D(0.63, 0.62, r'$\mathbf{X}_v$', transform=axR.transAxes, color=figG, fontsize=11)
axR.text2D(0.72, 0.40, r'$\mathbf{X}_u$', transform=axR.transAxes, color=figG, fontsize=11)
plt.savefig(OUT+'/m452-18-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================ F10: projection ================
fig = plt.figure(figsize=(5.6, 4.2))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
P  = np.array([0.9, 0.9, 1.25])
A  = np.array([1.15, 0.25, 0.32]); B = np.array([0.35, 0.95, 0.55])
quad = [P, P+A, P+A+B, P+B]
ax.add_collection3d(Poly3DCollection([[tuple(q) for q in quad]],
                    facecolor=figB, alpha=0.38, edgecolor=figB, lw=1.5))
quad0 = [q*np.array([1,1,0]) for q in quad]
ax.add_collection3d(Poly3DCollection([[tuple(q) for q in quad0]],
                    facecolor=figR, alpha=0.30, edgecolor=figR, lw=1.5))
ax.add_collection3d(Line3DCollection([(tuple(q),tuple(q0)) for q,q0 in zip(quad,quad0)],
                    colors='gray', linestyles='dashed', linewidths=0.9))
for vec,off in [(A,(0.06,-0.16,-0.04)),(B,(-0.12,0.10,0.05))]:
    a = Arrow3D([P[0],P[0]+vec[0]],[P[1],P[1]+vec[1]],[P[2],P[2]+vec[2]],
                mutation_scale=13, lw=2.0, arrowstyle='-|>', color=figG)
    ax.add_artist(a)
ax.text(P[0]+A[0]+0.10, P[1]+A[1]-0.16, P[2]+A[2]-0.05, r'$\mathbf{X}_u$', color=figG, fontsize=11)
ax.text(P[0]+B[0]-0.30, P[1]+B[1]+0.10, P[2]+B[2]+0.07, r'$\mathbf{X}_v$', color=figG, fontsize=11)
axes_triad(ax, L=(3.0,2.9,2.3))
ax.view_init(elev=20, azim=-60)
ax.set_xlim(0,3.0); ax.set_ylim(0,2.9); ax.set_zlim(0,2.3)
ax.set_box_aspect((1,1,0.72))
ax.text2D(0.55, 0.90, 'parallelogram spanned by $\\mathbf{X}_u,\\mathbf{X}_v$',
          transform=ax.transAxes, color=figB, fontsize=11)
ax.text2D(0.55, 0.16, 'projection onto $xy$-plane:\nsigned area $= dx\\wedge dy$',
          transform=ax.transAxes, color=figR, fontsize=11)
plt.savefig(OUT+'/m452-21-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================ F16: Riemann boxes ================
fig = plt.figure(figsize=(6.0, 4.3))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
def g(x,y): return 1.5 + 0.30*np.sin(1.1*x) + 0.24*np.cos(0.9*y) + 0.07*x
xx2, yy2 = np.meshgrid(np.linspace(0.3,2.7,60), np.linspace(0.3,2.4,60))
ax.plot_surface(xx2, yy2, g(xx2,yy2), color=figB, alpha=0.22, linewidth=0)
xs2 = np.linspace(0.3,2.7,5); ys2 = np.linspace(0.3,2.4,4)
for x in xs2: ax.plot([x,x],[ys2[0],ys2[-1]],[0,0], color=figG, alpha=0.55, lw=0.8)
for y in ys2: ax.plot([xs2[0],xs2[-1]],[y,y],[0,0], color=figG, alpha=0.55, lw=0.8)
xa,xb = xs2[1],xs2[2]; ya,yb = ys2[1],ys2[2]
xi = np.array([(xa+xb)/2,(ya+yb)/2]); h = g(*xi)
corners = [(xa,ya),(xb,ya),(xb,yb),(xa,yb)]
def face(pts, alpha):
    ax.add_collection3d(Poly3DCollection([pts], facecolor=figR, alpha=alpha, edgecolor=figR, lw=1.1))
face([(x,y,0) for x,y in corners], 0.30)
face([(x,y,h) for x,y in corners], 0.22)
for i in range(4):
    x1,y1 = corners[i]; x2,y2 = corners[(i+1)%4]
    face([(x1,y1,0),(x2,y2,0),(x2,y2,h),(x1,y1,h)], 0.10)
ax.scatter([xi[0]],[xi[1]],[0], color='black', s=14, depthshade=False)
axes_triad(ax, L=(3.3,2.8,2.6))
ax.view_init(elev=20, azim=-64)
ax.set_xlim(0,3.3); ax.set_ylim(0,2.8); ax.set_zlim(0,2.6)
ax.set_box_aspect((1.15,1,0.8))
ax.text2D(0.42, 0.93, '$z=f(x,y)$', transform=ax.transAxes, color=figB, fontsize=13)
ax.text2D(0.67, 0.52, 'one term of the sum:\n$f(\\boldsymbol{\\xi}_{ij})\\,\\Delta x_i\\,\\Delta y_j$',
          transform=ax.transAxes, color=figR, fontsize=11)
ax.text2D(0.455, 0.175, r'$\boldsymbol{\xi}_{ij}$', transform=ax.transAxes, fontsize=11)
ax.text2D(0.80, 0.12, '$D$', transform=ax.transAxes, color=figG, fontsize=12)
plt.savefig(OUT+'/m452-15-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("fix round done")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from mpl_toolkits.mplot3d import proj3d

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB = '#1F5AA6'; figR = '#B03030'; figG = '#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

fig = plt.figure(figsize=(7.8, 3.6))
# ---- left: parameter domain ----
axL = fig.add_axes([0.02, 0.14, 0.26, 0.72])
axL.set_xlim(-0.3, 3.1); axL.set_ylim(-0.6, 2.7); axL.set_aspect('equal'); axL.axis('off')
axL.annotate('', xy=(3.0,0), xytext=(-0.2,0), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.annotate('', xy=(0,2.55), xytext=(0,-0.3), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.text(3.02,-0.06,'$u$',fontsize=12); axL.text(-0.06,2.6,'$v$',fontsize=12)
axL.add_patch(Rectangle((0.4,0.35), 2.1, 1.75, facecolor=figB, alpha=0.10, edgecolor=figB, lw=1.4))
for u in np.linspace(0.4,2.5,5)[1:-1]: axL.plot([u,u],[0.35,2.1], color=figB, alpha=0.4, lw=0.7)
for v in np.linspace(0.35,2.1,5)[1:-1]: axL.plot([0.4,2.5],[v,v], color=figB, alpha=0.4, lw=0.7)
axL.plot([1.45],[1.22],'ko',ms=3.5); axL.text(1.52,1.0,'$(u_0,v_0)$',fontsize=9)
axL.text(0.55,-0.55,'parameter domain $D$',fontsize=11)
fig.text(0.305, 0.56, r'$\mathbf{X}$', fontsize=14)
fig.patches.append(FancyArrowPatch((0.295,0.50),(0.355,0.50), transform=fig.transFigure,
                                    arrowstyle='-|>', mutation_scale=14, lw=1.3, color='black'))
# ---- right: 3D surface, steeper and better separated ----
axR = fig.add_axes([0.33, -0.10, 0.67, 1.22], projection='3d')
axR.set_axis_off(); axR.set_proj_type('ortho')
uu, vv = np.meshgrid(np.linspace(0,2.0,50), np.linspace(0,1.8,50))
XX = 0.3 + uu - 0.15*vv
YY = 0.15 + 1.0*vv + 0.10*uu
ZZ = 0.7 + 0.55*np.sin(1.25*uu+0.3) + 0.50*np.cos(1.2*vv) - 0.05*uu
axR.plot_surface(XX, YY, ZZ, color=figB, alpha=0.22, linewidth=0)
def curve_u(uc):
    v1 = np.linspace(0,1.8,60)
    return 0.3+uc-0.15*v1, 0.15+1.0*v1+0.10*uc, 0.7+0.55*np.sin(1.25*uc+0.3)+0.50*np.cos(1.2*v1)-0.05*uc
def curve_v(vc):
    u1 = np.linspace(0,2.0,60)
    return 0.3+u1-0.15*vc, 0.15+1.0*vc+0.10*u1, 0.7+0.55*np.sin(1.25*u1+0.3)+0.50*np.cos(1.2*vc)-0.05*u1
for uc in np.linspace(0,2.0,5): axR.plot(*curve_u(uc), color=figB, alpha=0.5, lw=0.7)
for vc in np.linspace(0,1.8,5): axR.plot(*curve_v(vc), color=figB, alpha=0.5, lw=0.7)
u0, v0 = 1.0, 0.9
P0 = np.array([0.3+u0-0.15*v0, 0.15+1.0*v0+0.10*u0, 0.7+0.55*np.sin(1.25*u0+0.3)+0.50*np.cos(1.2*v0)-0.05*u0])
Xu = np.array([1, 0.10, 0.55*1.25*np.cos(1.25*u0+0.3)-0.05]); Xu = 0.78*Xu/np.linalg.norm(Xu)
Xv = np.array([-0.15, 1.0, -0.50*1.2*np.sin(1.2*v0)]);        Xv = 0.78*Xv/np.linalg.norm(Xv)
Nn = np.cross(Xu,Xv); Nn = 0.85*Nn/np.linalg.norm(Nn)
labpos = {}
for name,vec,col in [('Xu',Xu,figG),('Xv',Xv,figG),('N',Nn,figR)]:
    a = Arrow3D([P0[0],P0[0]+vec[0]],[P0[1],P0[1]+vec[1]],[P0[2],P0[2]+vec[2]],
                mutation_scale=13, lw=2.0, arrowstyle='-|>', color=col)
    axR.add_artist(a)
    labpos[name] = P0+vec
axR.scatter(*P0, color='black', s=16, depthshade=False)
axR.text(labpos['Xu'][0]+0.10, labpos['Xu'][1]-0.12, labpos['Xu'][2]-0.06, r'$\mathbf{X}_u$', color=figG, fontsize=11)
axR.text(labpos['Xv'][0]-0.05, labpos['Xv'][1]+0.10, labpos['Xv'][2]+0.03, r'$\mathbf{X}_v$', color=figG, fontsize=11)
axR.text(labpos['N'][0]-0.55, labpos['N'][1]+0.03, labpos['N'][2]+0.10, r'$\mathbf{X}_u\times\mathbf{X}_v$', color=figR, fontsize=11)
axR.view_init(elev=30, azim=-48)
axR.set_xlim(0.1,2.6); axR.set_ylim(0,2.2); axR.set_zlim(0.2,2.3)
axR.set_box_aspect((1.15,1.0,0.85))
axR.text2D(0.74, 0.90, r'$S=\mathbf{X}(D)$', transform=axR.transAxes, color=figB, fontsize=12)
plt.savefig(OUT+'/m452-18-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("F7 redone")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB = '#1F5AA6'; figR = '#B03030'; figG = '#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

def newax(figsize=(5.6,4.1)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off(); ax.set_proj_type('ortho')
    return fig, ax

def axes_triad(ax, L=(2.8,2.6,2.2), labels=('$x$','$y$','$z$'), off=0.08):
    import numpy as np
    for vec,lab in zip(np.eye(3)*np.array(L)[:,None].T, labels):
        a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=12,
                    lw=1.0, arrowstyle='-|>', color='black')
        ax.add_artist(a)
        ax.text(vec[0]+off, vec[1]+off, vec[2]+off, lab, fontsize=12)

# ---------------- F10: parallelogram projection ----------------
fig, ax = newax()
P  = np.array([0.9, 0.9, 1.25])
A  = np.array([1.15, 0.25, 0.32])   # Xu
B  = np.array([0.35, 0.95, 0.55])   # Xv
quad = [P, P+A, P+A+B, P+B]
ax.add_collection3d(Poly3DCollection([ [tuple(q) for q in quad] ],
                    facecolor=figB, alpha=0.35, edgecolor=figB, lw=1.5))
# projection to z=0
quad0 = [q*np.array([1,1,0]) for q in quad]
ax.add_collection3d(Poly3DCollection([ [tuple(q) for q in quad0] ],
                    facecolor=figR, alpha=0.28, edgecolor=figR, lw=1.5))
# dashed drop lines
segs = [ (tuple(q), tuple(q0)) for q,q0 in zip(quad, quad0) ]
lc = Line3DCollection(segs, colors='gray', linestyles='dashed', linewidths=0.9)
ax.add_collection3d(lc)
# vectors
for vec, lab, off in [(A, r'$\mathbf{X}_u$', (0.08,-0.14,-0.03)), (B, r'$\mathbf{X}_v$', (-0.1,0.12,0.06))]:
    a = Arrow3D([P[0],P[0]+vec[0]],[P[1],P[1]+vec[1]],[P[2],P[2]+vec[2]],
                mutation_scale=13, lw=2.0, arrowstyle='-|>', color=figG)
    ax.add_artist(a)
    ax.text(P[0]+vec[0]+off[0], P[1]+vec[1]+off[1], P[2]+vec[2]+off[2], lab, color=figG, fontsize=11)
ax.text(P[0]+0.4, P[1]+1.45, P[2]+1.05, 'parallelogram spanned by $\\mathbf{X}_u,\\mathbf{X}_v$', color=figB, fontsize=10)
ax.text(2.15, 1.15, -0.35, 'projection onto $xy$-plane:\nsigned area $= dx\\wedge dy$', color=figR, fontsize=10)
axes_triad(ax, L=(3.0,2.9,2.3))
ax.view_init(elev=20, azim=-60)
ax.set_xlim(0,3.0); ax.set_ylim(0,2.9); ax.set_zlim(0,2.3)
ax.set_box_aspect((1,1,0.72))
plt.savefig(OUT+'/m452-21-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ---------------- F16: Riemann boxes ----------------
fig, ax = newax(figsize=(6.2,4.4))
def g(x,y): return 1.5 + 0.30*np.sin(1.1*x) + 0.24*np.cos(0.9*y) + 0.07*x
xx, yy = np.meshgrid(np.linspace(0.3,2.7,60), np.linspace(0.3,2.4,60))
ax.plot_surface(xx, yy, g(xx,yy), color=figB, alpha=0.25, linewidth=0)
# base grid on z=0: 4 x 3 cells
xs = np.linspace(0.3, 2.7, 5); ys = np.linspace(0.3, 2.4, 4)
for x in xs: ax.plot([x,x],[ys[0],ys[-1]],[0,0], color=figG, alpha=0.5, lw=0.8)
for y in ys: ax.plot([xs[0],xs[-1]],[y,y],[0,0], color=figG, alpha=0.5, lw=0.8)
ax.text(2.78, 0.35, 0, '$D$', color=figG, fontsize=12)
# one highlighted box: cell (1,1)
xa, xb = xs[1], xs[2]; ya, yb = ys[1], ys[2]
xi = np.array([(xa+xb)/2, (ya+yb)/2])
h = g(*xi)
# box faces
def face(pts, color, alpha):
    ax.add_collection3d(Poly3DCollection([pts], facecolor=color, alpha=alpha, edgecolor=figR, lw=1.1))
corners = [(xa,ya),(xb,ya),(xb,yb),(xa,yb)]
face([(x,y,0) for x,y in corners], figR, 0.30)
face([(x,y,h) for x,y in corners], figR, 0.22)
for i in range(4):
    x1,y1 = corners[i]; x2,y2 = corners[(i+1)%4]
    face([(x1,y1,0),(x2,y2,0),(x2,y2,h),(x1,y1,h)], figR, 0.10)
ax.scatter([xi[0]],[xi[1]],[0], color='black', s=14, depthshade=False)
ax.text(xi[0]+0.03, xi[1]-0.28, 0.02, r'$\boldsymbol{\xi}_{ij}$', fontsize=11)
ax.text(1.0, 2.35, 2.45, '$z=f(x,y)$', color=figB, fontsize=12)
ax.text(3.0, 1.6, 1.35, 'one term of the sum:\n$f(\\boldsymbol{\\xi}_{ij})\\,\\Delta x_i\\,\\Delta y_j$', color=figR, fontsize=10)
axes_triad(ax, L=(3.3,2.8,2.6))
ax.view_init(elev=20, azim=-64)
ax.set_xlim(0,3.3); ax.set_ylim(0,2.8); ax.set_zlim(0,2.6)
ax.set_box_aspect((1.15,1,0.8))
plt.savefig(OUT+'/m452-15-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ---------------- F8: Stokes cap ----------------
fig, ax = newax()
th, rr = np.meshgrid(np.linspace(0, 2*np.pi, 80), np.linspace(0, 1, 30))
XX = 1.5 + 1.25*rr*np.cos(th)
YY = 1.4 + 1.05*rr*np.sin(th)
ZZ = 0.75 + 0.85*(1 - rr**2) + 0.10*rr*np.sin(2*th)
ax.plot_surface(XX, YY, ZZ, color=figB, alpha=0.30, linewidth=0)
# boundary curve with orientation arrows
t = np.linspace(0, 2*np.pi, 200)
bx = 1.5 + 1.25*np.cos(t); by = 1.4 + 1.05*np.sin(t); bz = 0.75 + 0.10*np.sin(2*t)
ax.plot(bx, by, bz, color=figG, lw=2.2)
for tp in [0.4, 2.5, 4.6]:
    p1 = np.array([1.5+1.25*np.cos(tp), 1.4+1.05*np.sin(tp), 0.75+0.10*np.sin(2*tp)])
    dp = np.array([-1.25*np.sin(tp), 1.05*np.cos(tp), 0.20*np.cos(2*tp)])
    dp = 0.02*dp
    a = Arrow3D([p1[0],p1[0]+dp[0]],[p1[1],p1[1]+dp[1]],[p1[2],p1[2]+dp[2]],
                mutation_scale=16, lw=0, arrowstyle='-|>', color=figG)
    ax.add_artist(a)
ax.text(2.8, 0.55, 0.72, r'$\partial S$', color=figG, fontsize=13)
# normal from cap top
a = Arrow3D([1.5,1.5],[1.4,1.4],[1.62,2.45], mutation_scale=14, lw=2.2, arrowstyle='-|>', color=figR)
ax.add_artist(a)
ax.text(1.55, 1.42, 2.5, r'$\hat{n}$', color=figR, fontsize=13)
ax.text(0.35, 2.3, 1.7, '$S$', color=figB, fontsize=13)
ax.view_init(elev=22, azim=-60)
ax.set_xlim(0.1,2.9); ax.set_ylim(0.2,2.6); ax.set_zlim(0,2.6)
ax.set_box_aspect((1,0.95,0.8))
plt.savefig(OUT+'/m452-20-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

print("batch 2 done")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB = '#1F5AA6'; figR = '#B03030'; figG = '#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0),(0,0),*args,**kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)

# ============ F20: min / max / saddle (3 panels) ============
fig = plt.figure(figsize=(9.0, 3.1))
data = [
    (lambda x,y: 0.55*(x**2+y**2), 'local min\n$f_{xx}>0,\\ \\det H>0$', 22),
    (lambda x,y: -0.55*(x**2+y**2)+1.6, 'local max\n$f_{xx}<0,\\ \\det H>0$', 22),
    (lambda x,y: 0.55*(x**2-y**2)+0.8, 'saddle\n$\\det H<0$', 20),
]
for k,(fun,title,el) in enumerate(data):
    ax = fig.add_subplot(1,3,k+1, projection='3d')
    ax.set_axis_off(); ax.set_proj_type('ortho')
    xx,yy = np.meshgrid(np.linspace(-1.1,1.1,50), np.linspace(-1.1,1.1,50))
    ax.plot_surface(xx,yy,fun(xx,yy), color=figB, alpha=0.35, linewidth=0)
    ax.scatter([0],[0],[fun(0,0)], color=figR, s=25, depthshade=False)
    ax.view_init(elev=el, azim=-58)
    ax.set_box_aspect((1,1,0.65))
    ax.text2D(0.5, -0.06, title, transform=ax.transAxes, ha='center', fontsize=11)
plt.subplots_adjust(wspace=0.02, left=0.01, right=0.99, top=1.05, bottom=0.10)
plt.savefig(OUT+'/m452-14-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ============ F21: Fubini slicing ============
fig = plt.figure(figsize=(6.0, 4.2))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
def g(x,y): return 1.35 + 0.30*np.sin(1.1*x) + 0.25*np.cos(1.0*y) + 0.06*x
xx,yy = np.meshgrid(np.linspace(0.3,2.7,60), np.linspace(0.3,2.3,60))
ax.plot_surface(xx,yy,g(xx,yy), color=figB, alpha=0.20, linewidth=0)
# base rectangle
for (x1,y1,x2,y2) in [(0.3,0.3,2.7,0.3),(2.7,0.3,2.7,2.3),(2.7,2.3,0.3,2.3),(0.3,2.3,0.3,0.3)]:
    ax.plot([x1,x2],[y1,y2],[0,0], color=figG, lw=1.0, alpha=0.7)
# slice at x = x0: filled cross-section
x0s = 1.5
ys = np.linspace(0.3,2.3,40)
verts = [(x0s, y, 0) for y in ys] + [(x0s, y, g(x0s,y)) for y in ys[::-1]]
ax.add_collection3d(Poly3DCollection([verts], facecolor=figR, alpha=0.45, edgecolor=figR, lw=1.2))
ax.plot([x0s,x0s],[0.3,2.3],[0,0], color=figR, lw=1.6)
# axes triad
for vec,lab in zip([(3.3,0,0),(0,2.8,0),(0,0,2.4)], ('$x$','$y$','$z$')):
    a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=12, lw=1.0, arrowstyle='-|>', color='black')
    ax.add_artist(a)
    ax.text(vec[0]+0.08, vec[1]+0.08, vec[2]+0.08, lab, fontsize=12)
ax.view_init(elev=20, azim=-64)
ax.set_xlim(0,3.3); ax.set_ylim(0,2.8); ax.set_zlim(0,2.4)
ax.set_box_aspect((1.15,1,0.75))
ax.text2D(0.42, 0.92, '$z=f(x,y)$', transform=ax.transAxes, color=figB, fontsize=13)
ax.text2D(0.60, 0.42, 'cross-section at $x$:\narea $A(x)=\\int f(x,y)\\,dy$', transform=ax.transAxes, color=figR, fontsize=11)
ax.text2D(0.30, 0.06, 'volume $=\\int A(x)\\,dx$ \\ (Fubini: slice, then stack)', transform=ax.transAxes, fontsize=11)
plt.savefig(OUT+'/m452-15-2.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ============ F23: spherical coordinates ============
fig = plt.figure(figsize=(5.4, 4.4))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
# wire sphere (light)
u,v = np.meshgrid(np.linspace(0,2*np.pi,40), np.linspace(0,np.pi,20))
R = 1.6
ax.plot_wireframe(R*np.cos(u)*np.sin(v), R*np.sin(u)*np.sin(v), R*np.cos(v),
                  color=figB, alpha=0.12, linewidth=0.5)
# point P at (theta=50deg azimuth, phi=55deg polar)
th, ph = np.radians(48), np.radians(52)
P = R*np.array([np.cos(th)*np.sin(ph), np.sin(th)*np.sin(ph), np.cos(ph)])
# radius line
ax.plot([0,P[0]],[0,P[1]],[0,P[2]], color=figR, lw=2.0)
ax.scatter(*P, color=figR, s=25, depthshade=False)
# projection to xy-plane
Pxy = np.array([P[0],P[1],0])
ax.plot([P[0],Pxy[0]],[P[1],Pxy[1]],[P[2],0], color='gray', ls='dashed', lw=1.0)
ax.plot([0,Pxy[0]],[0,Pxy[1]],[0,0], color=figG, lw=1.6)
# theta arc in xy-plane
tt = np.linspace(0, th, 30)
ax.plot(0.65*np.cos(tt), 0.65*np.sin(tt), 0*tt, color=figG, lw=1.4)
# phi arc from z-axis to radius
pp = np.linspace(0, ph, 30)
ax.plot(0.75*np.cos(th)*np.sin(pp), 0.75*np.sin(th)*np.sin(pp), 0.75*np.cos(pp), color=figR, lw=1.4)
# axes
for vec,lab in zip([(2.5,0,0),(0,2.4,0),(0,0,2.3)], ('$x$','$y$','$z$')):
    a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=12, lw=1.0, arrowstyle='-|>', color='black')
    ax.add_artist(a)
    ax.text(vec[0]+0.07, vec[1]+0.07, vec[2]+0.07, lab, fontsize=12)
ax.view_init(elev=18, azim=-55)
ax.set_xlim(-1.4,2.3); ax.set_ylim(-1.4,2.2); ax.set_zlim(-1.2,2.1)
ax.set_box_aspect((1,0.97,0.9))
ax.text2D(0.66, 0.72, '$P=(r,\\theta,\\varphi)$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.56, 0.55, '$r$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.485, 0.60, '$\\varphi$', transform=ax.transAxes, color=figR, fontsize=11)
ax.text2D(0.485, 0.285, '$\\theta$', transform=ax.transAxes, color=figG, fontsize=11)
plt.savefig(OUT+'/m452-19-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("python batch done")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB = '#1F5AA6'; figR = '#B03030'; figG = '#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0),(0,0),*args,**kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)

def f(x,y):
    return 1.00 + 0.52*np.sin(1.35*x) + 0.44*np.cos(1.25*y) + 0.10*x

x0a, x0b, y0a, y0b = 0.55, 2.85, 0.55, 2.5
xs = np.linspace(x0a, x0b, 4)   # 3 cells in x
ys = np.linspace(y0a, y0b, 4)   # 3 cells in y

def cell_inf_sup(xa,xb,ya,yb):
    gx, gy = np.meshgrid(np.linspace(xa,xb,25), np.linspace(ya,yb,25))
    vals = f(gx,gy)
    return vals.min(), vals.max()

def draw_box(ax, xa,xb,ya,yb,h, fc, ec, alpha):
    cor = [(xa,ya),(xb,ya),(xb,yb),(xa,yb)]
    faces = [ [(x,y,h) for x,y in cor] ]                      # top
    for i in range(4):
        x1,y1 = cor[i]; x2,y2 = cor[(i+1)%4]
        faces.append([(x1,y1,0),(x2,y2,0),(x2,y2,h),(x1,y1,h)])
    pc = Poly3DCollection(faces, facecolor=fc, edgecolor=ec, lw=0.8, alpha=alpha)
    pc.set_zsort('max')
    ax.add_collection3d(pc)

def panel(ax, mode):
    ax.set_axis_off(); ax.set_proj_type('ortho')
    # draw boxes back-to-front relative to camera azim=-62
    cells = []
    for i in range(3):
        for j in range(3):
            xa,xb,ya,yb = xs[i],xs[i+1],ys[j],ys[j+1]
            m, M = cell_inf_sup(xa,xb,ya,yb)
            h = m if mode=='lower' else M
            score = 0.47*(xa+xb)/2 - 0.88*(ya+yb)/2
            cells.append((score, xa,xb,ya,yb,h))
    for score,xa,xb,ya,yb,h in sorted(cells):
        if mode=='lower':
            draw_box(ax, xa,xb,ya,yb,h, '#tmp', figG, 0.55)
        else:
            draw_box(ax, xa,xb,ya,yb,h, '#tmp', figR, 0.32)
    # surface
    gx, gy = np.meshgrid(np.linspace(x0a,x0b,60), np.linspace(y0a,y0b,60))
    ax.plot_surface(gx, gy, f(gx,gy), color=figB, alpha=0.30, linewidth=0)
    # base outline
    for (x1,y1,x2,y2) in [(x0a,y0a,x0b,y0a),(x0b,y0a,x0b,y0b),(x0b,y0b,x0a,y0b),(x0a,y0b,x0a,y0a)]:
        ax.plot([x1,x2],[y1,y2],[0,0], color='gray', lw=0.7, alpha=0.7)
    # axes triad
    for vec,lab in zip([(3.2,0,0),(0,2.9,0),(0,0,2.3)], ('$x$','$y$','$z$')):
        a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=11, lw=0.9, arrowstyle='-|>', color='black')
        ax.add_artist(a)
        ax.text(vec[0]+0.07, vec[1]+0.07, vec[2]+0.07, lab, fontsize=11)
    ax.view_init(elev=22, azim=-62)
    ax.set_xlim(0,3.2); ax.set_ylim(0,2.9); ax.set_zlim(0,2.3)
    ax.set_box_aspect((1.1,1,0.72))

# color fix: matplotlib needs real colors
import matplotlib.colors as mcolors
green_face = mcolors.to_rgba(figG, 0.0)
fig = plt.figure(figsize=(9.4, 3.9))
axL = fig.add_subplot(121, projection='3d')
axR = fig.add_subplot(122, projection='3d')

def panel2(ax, mode):
    ax.set_axis_off(); ax.set_proj_type('ortho')
    cells = []
    for i in range(3):
        for j in range(3):
            xa,xb,ya,yb = xs[i],xs[i+1],ys[j],ys[j+1]
            m, M = cell_inf_sup(xa,xb,ya,yb)
            h = m if mode=='lower' else M
            score = 0.47*(xa+xb)/2 - 0.88*(ya+yb)/2
            cells.append((score, xa,xb,ya,yb,h))
    col = figG if mode=='lower' else figR
    al  = 0.50 if mode=='lower' else 0.30
    for score,xa,xb,ya,yb,h in sorted(cells):
        draw_box(ax, xa,xb,ya,yb,h, col, col, al)
    gx, gy = np.meshgrid(np.linspace(x0a,x0b,60), np.linspace(y0a,y0b,60))
    ax.plot_surface(gx, gy, f(gx,gy), color=figB, alpha=0.30, linewidth=0)
    for (x1,y1,x2,y2) in [(x0a,y0a,x0b,y0a),(x0b,y0a,x0b,y0b),(x0b,y0b,x0a,y0b),(x0a,y0b,x0a,y0a)]:
        ax.plot([x1,x2],[y1,y2],[0,0], color='gray', lw=0.7, alpha=0.7)
    for vec,lab in zip([(3.2,0,0),(0,2.9,0),(0,0,2.3)], ('$x$','$y$','$z$')):
        a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=11, lw=0.9, arrowstyle='-|>', color='black')
        ax.add_artist(a)
        ax.text(vec[0]+0.07, vec[1]+0.07, vec[2]+0.07, lab, fontsize=11)
    ax.view_init(elev=22, azim=-62)
    ax.set_xlim(0,3.2); ax.set_ylim(0,2.9); ax.set_zlim(0,2.3)
    ax.set_box_aspect((1.1,1,0.72))

panel2(axL, 'lower')
panel2(axR, 'upper')
axL.text2D(0.5, -0.04, 'lower sum: box height $m_i=\\inf_{D_i} f$\n$L(f,\\mathcal{T})=\\sum m_i\\,|D_i|$ (inscribed)',
           transform=axL.transAxes, ha='center', fontsize=11)
axR.text2D(0.5, -0.04, 'upper sum: box height $M_i=\\sup_{D_i} f$\n$U(f,\\mathcal{T})=\\sum M_i\\,|D_i|$ (circumscribing)',
           transform=axR.transAxes, ha='center', fontsize=11)
axL.text2D(0.32, 0.93, '$z=f(x,y)$', transform=axL.transAxes, color=figB, fontsize=12)
plt.subplots_adjust(left=0.0, right=1.0, top=1.08, bottom=0.10, wspace=0.0)
plt.savefig(OUT+'/m452-15-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("F16 Darboux version done")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 11
figB='#1F5AA6'; figR='#B03030'; figG='#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *a, **k):
        super().__init__((0,0),(0,0),*a,**k); self._v = xs,ys,zs
    def do_3d_projection(self, renderer=None):
        xs,ys,zs = proj3d.proj_transform(*self._v, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1])); return np.min(zs)

# ================= F7 v2: surface integral, cell -> patch =================
fig = plt.figure(figsize=(7.8, 3.6))
axL = fig.add_axes([0.02, 0.14, 0.26, 0.72])
axL.set_xlim(-0.3,3.1); axL.set_ylim(-0.6,2.7); axL.set_aspect('equal'); axL.axis('off')
axL.annotate('', xy=(3.0,0), xytext=(-0.2,0), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.annotate('', xy=(0,2.55), xytext=(0,-0.3), arrowprops=dict(arrowstyle='-|>', lw=1))
axL.text(3.02,-0.06,'$u$',fontsize=12); axL.text(-0.06,2.6,'$v$',fontsize=12)
axL.add_patch(Rectangle((0.4,0.35),2.1,1.75, facecolor=figB, alpha=0.10, edgecolor=figB, lw=1.4))
ugrid = np.linspace(0.4,2.5,5); vgrid = np.linspace(0.35,2.1,5)
for u in ugrid[1:-1]: axL.plot([u,u],[0.35,2.1], color=figB, alpha=0.4, lw=0.7)
for v in vgrid[1:-1]: axL.plot([0.4,2.5],[v,v], color=figB, alpha=0.4, lw=0.7)
# highlighted cell (2nd col, 2nd row)
ca, cb = ugrid[2], ugrid[3]; da, db = vgrid[2], vgrid[3]
axL.add_patch(Rectangle((ca,da), cb-ca, db-da, facecolor=figR, alpha=0.35, edgecolor=figR, lw=1.4))
axL.text((ca+cb)/2-0.32, da-0.34, r'$\Delta u \times \Delta v$', fontsize=9, color=figR)
axL.text(0.55,-0.55,'parameter domain $D$',fontsize=11)
fig.text(0.305,0.56, r'$\mathbf{X}$', fontsize=14)
fig.patches.append(FancyArrowPatch((0.295,0.50),(0.355,0.50), transform=fig.transFigure,
                                    arrowstyle='-|>', mutation_scale=14, lw=1.3, color='black'))
axR = fig.add_axes([0.33,-0.10,0.67,1.22], projection='3d')
axR.set_axis_off(); axR.set_proj_type('ortho')
def S(u,v):
    return (0.3+u-0.15*v, 0.15+1.0*v+0.10*u, 0.7+0.55*np.sin(1.25*u+0.3)+0.50*np.cos(1.2*v)-0.05*u)
uu,vv = np.meshgrid(np.linspace(0,2.1,50), np.linspace(0,1.75,50))
XX,YY,ZZ = S(uu,vv)
axR.plot_surface(XX,YY,ZZ, color=figB, alpha=0.20, linewidth=0)
# param -> surface scaling: u_surf = (u_dom-0.4), v_surf = (v_dom-0.35)
for uc in np.linspace(0,2.1,5):
    v1 = np.linspace(0,1.75,60); axR.plot(*S(uc,v1), color=figB, alpha=0.45, lw=0.7)
for vc in np.linspace(0,1.75,5):
    u1 = np.linspace(0,2.1,60); axR.plot(*S(u1,vc), color=figB, alpha=0.45, lw=0.7)
# highlighted patch: cell (ca..cb, da..db) mapped: u in [1.05,1.575], v in [0.875,1.3125]
pu0, pu1 = ca-0.4, cb-0.4; pv0, pv1 = da-0.35, db-0.35
pu, pv = np.meshgrid(np.linspace(pu0,pu1,12), np.linspace(pv0,pv1,12))
PX,PY,PZ = S(pu,pv)
axR.plot_surface(PX,PY,PZ, color=figR, alpha=0.55, linewidth=0)
# corner point + tangent parallelogram Xu*du, Xv*dv
u0,v0 = pu0, pv0; du = pu1-pu0; dv = pv1-pv0
P0 = np.array(S(u0,v0))
eps=1e-4
Xu = (np.array(S(u0+eps,v0))-P0)/eps
Xv = (np.array(S(u0,v0+eps))-P0)/eps
A = Xu*du; B = Xv*dv
quad = [P0, P0+A, P0+A+B, P0+B]
axR.add_collection3d(Poly3DCollection([[tuple(q) for q in quad]], facecolor=(0,0,0,0), edgecolor=figG, lw=1.8))
for vec in (A,B):
    a = Arrow3D([P0[0],P0[0]+vec[0]],[P0[1],P0[1]+vec[1]],[P0[2],P0[2]+vec[2]],
                mutation_scale=11, lw=1.8, arrowstyle='-|>', color=figG)
    axR.add_artist(a)
axR.view_init(elev=30, azim=-48)
axR.set_xlim(0.1,2.6); axR.set_ylim(0,2.2); axR.set_zlim(0.2,2.3)
axR.set_box_aspect((1.15,1.0,0.85))
axR.text2D(0.74,0.92, r'$S=\mathbf{X}(D)$', transform=axR.transAxes, color=figB, fontsize=12)
axR.text2D(0.04,0.86, 'curved patch (red)\n$\\approx$ tangent parallelogram (green)\nspanned by $\\mathbf{X}_u\\Delta u,\\ \\mathbf{X}_v\\Delta v$', transform=axR.transAxes, fontsize=10)
axR.text2D(0.30,0.06, 'patch area $\\approx |\\mathbf{X}_u\\times\\mathbf{X}_v|\\,\\Delta u\\,\\Delta v$', transform=axR.transAxes, color=figG, fontsize=11)
plt.savefig(OUT+'/m452-18-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================= F8 v2: Stokes both sides =================
fig = plt.figure(figsize=(6.4,4.3))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
th, rr = np.meshgrid(np.linspace(0,2*np.pi,80), np.linspace(0,1,30))
XX = 1.5+1.25*rr*np.cos(th); YY = 1.4+1.05*rr*np.sin(th)
ZZ = 0.75+0.85*(1-rr**2)+0.10*rr*np.sin(2*th)
ax.plot_surface(XX,YY,ZZ, color=figB, alpha=0.25, linewidth=0)
t = np.linspace(0,2*np.pi,200)
bx = 1.5+1.25*np.cos(t); by = 1.4+1.05*np.sin(t); bz = 0.75+0.10*np.sin(2*t)
ax.plot(bx,by,bz, color=figG, lw=2.4)
# circulation arrows on boundary (field F tangent along rim)
for tp in [0.35, 1.55, 2.75, 3.95, 5.15]:
    p1 = np.array([1.5+1.25*np.cos(tp), 1.4+1.05*np.sin(tp), 0.75+0.10*np.sin(2*tp)])
    dp = np.array([-1.25*np.sin(tp), 1.05*np.cos(tp), 0.20*np.cos(2*tp)]); dp = 0.30*dp/np.linalg.norm(dp)
    a = Arrow3D([p1[0],p1[0]+dp[0]],[p1[1],p1[1]+dp[1]],[p1[2],p1[2]+dp[2]],
                mutation_scale=13, lw=2.0, arrowstyle='-|>', color=figG)
    ax.add_artist(a)
# curl vectors on the surface (red, along local normals) at several interior points
def cap(u_r,u_t):
    x = 1.5+1.25*u_r*np.cos(u_t); y = 1.4+1.05*u_r*np.sin(u_t)
    z = 0.75+0.85*(1-u_r**2)+0.10*u_r*np.sin(2*u_t)
    return np.array([x,y,z])
for (ur,ut) in [(0.0,0.0),(0.55,0.8),(0.55,2.9),(0.55,4.9)]:
    P = cap(ur,ut); eps=1e-4
    Tu = (cap(ur+eps,ut)-P)/eps if ur>0 else np.array([1,0,0.0])
    Tv = (cap(max(ur,0.3),ut+eps)-cap(max(ur,0.3),ut))/eps
    if ur==0.0:
        N = np.array([0,0,1.0])
    else:
        N = np.cross(Tu,Tv); N = N/np.linalg.norm(N)
        if N[2] < 0: N = -N
    N = 0.55*N
    a = Arrow3D([P[0],P[0]+N[0]],[P[1],P[1]+N[1]],[P[2],P[2]+N[2]],
                mutation_scale=11, lw=1.7, arrowstyle='-|>', color=figR)
    ax.add_artist(a)
    # tiny circulation loop around the base of the vector, in the tangent plane
    if ur>0:
        e1 = Tu/np.linalg.norm(Tu); e2 = np.cross(N/np.linalg.norm(N), e1)
        s = np.linspace(0, 1.7*np.pi, 40)
        loop = P[:,None] + 0.14*(np.outer(e1,np.cos(s)) + np.outer(e2,np.sin(s)))
        ax.plot(loop[0],loop[1],loop[2], color=figR, lw=1.1, alpha=0.85)
ax.view_init(elev=22, azim=-60)
ax.set_xlim(0.1,2.9); ax.set_ylim(0.2,2.6); ax.set_zlim(0,2.6)
ax.set_box_aspect((1,0.95,0.8))
ax.text2D(0.72,0.20, 'rim: $\\oint_{\\partial S}\\mathbf{F}\\cdot d\\mathbf{r}$\n(circulation, green)', transform=ax.transAxes, color=figG, fontsize=11)
ax.text2D(0.02,0.86, 'surface: $\\iint_S(\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}$\n(curl flux, red)', transform=ax.transAxes, color=figR, fontsize=11)
ax.text2D(0.40,0.02, 'tiny interior loops cancel; only the rim survives', transform=ax.transAxes, fontsize=10)
plt.savefig(OUT+'/m452-20-1.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================= F28: spherical volume element =================
fig = plt.figure(figsize=(5.8,4.6))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
# light sphere wireframe (octant-ish)
u,v = np.meshgrid(np.linspace(0,np.pi/2,15), np.linspace(0.15,np.pi/2,12))
R0 = 1.75
ax.plot_wireframe(R0*np.cos(u)*np.sin(v), R0*np.sin(u)*np.sin(v), R0*np.cos(v),
                  color=figB, alpha=0.12, linewidth=0.5)
r0, r1 = 1.75, 2.15
t0, t1 = np.radians(28), np.radians(52)   # theta (azimuth)
p0, p1 = np.radians(38), np.radians(60)   # phi (polar)
def sph(r,t,p): return np.array([r*np.cos(t)*np.sin(p), r*np.sin(t)*np.sin(p), r*np.cos(p)])
# 12 edges
def edge(f, n=25):
    s = np.linspace(0,1,n); pts = np.array([f(si) for si in s]).T
    ax.plot(pts[0],pts[1],pts[2], color=figR, lw=1.5)
for (t,p) in [(t0,p0),(t0,p1),(t1,p0),(t1,p1)]:
    edge(lambda s,t=t,p=p: sph(r0+s*(r1-r0), t, p))
for (r,p) in [(r0,p0),(r0,p1),(r1,p0),(r1,p1)]:
    edge(lambda s,r=r,p=p: sph(r, t0+s*(t1-t0), p))
for (r,t) in [(r0,t0),(r0,t1),(r1,t0),(r1,t1)]:
    edge(lambda s,r=r,t=t: sph(r, t, p0+s*(p1-p0)))
# shade outer face r=r1
tt,pp = np.meshgrid(np.linspace(t0,t1,12), np.linspace(p0,p1,12))
F = sph(r1,tt,pp)
ax.plot_surface(F[0],F[1],F[2], color=figR, alpha=0.30, linewidth=0)
# axes triad
for vec,lab in zip([(2.9,0,0),(0,2.7,0),(0,0,2.5)], ('$x$','$y$','$z$')):
    a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=11, lw=0.9, arrowstyle='-|>', color='black')
    ax.add_artist(a)
    ax.text(vec[0]+0.06, vec[1]+0.06, vec[2]+0.06, lab, fontsize=11)
# radial guide line from origin to inner corner
C = sph(r0,t0,p0)
ax.plot([0,C[0]],[0,C[1]],[0,C[2]], color='gray', ls='dashed', lw=0.9)
ax.view_init(elev=20, azim=-52)
ax.set_xlim(0,2.9); ax.set_ylim(0,2.7); ax.set_zlim(0,2.5)
ax.set_box_aspect((1,0.95,0.88))
ax.text2D(0.565,0.635,'$dr$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.545,0.375,'$r\\sin\\varphi\\,d\\theta$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.215,0.565,'$r\\,d\\varphi$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.05,0.90,'$dV = r^2\\sin\\varphi\\;dr\\,d\\theta\\,d\\varphi$', transform=ax.transAxes, fontsize=13)
plt.savefig(OUT+'/m452-19-2.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()

# ================= F31: divergence theorem =================
fig = plt.figure(figsize=(5.8,4.4))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
u,v = np.meshgrid(np.linspace(0,2*np.pi,36), np.linspace(0,np.pi,18))
R=1.45; C0=np.array([1.7,1.6,1.5])
ax.plot_wireframe(C0[0]+R*np.cos(u)*np.sin(v), C0[1]+R*np.sin(u)*np.sin(v), C0[2]+R*np.cos(v),
                  color=figB, alpha=0.15, linewidth=0.5)
# field arrows crossing the surface outward (radial field), plus outward normals
pts = [(0.4,1.2),(1.6,1.2),(2.9,1.3),(0.9,2.1),(2.3,2.1),(5.5,1.1),(4.4,1.9)]
for (tt,pp) in pts:
    n = np.array([np.cos(tt)*np.sin(pp), np.sin(tt)*np.sin(pp), np.cos(pp)])
    base = C0 + (R-0.45)*n; tip = C0 + (R+0.5)*n
    a = Arrow3D([base[0],tip[0]],[base[1],tip[1]],[base[2],tip[2]],
                mutation_scale=12, lw=1.9, arrowstyle='-|>', color=figG)
    ax.add_artist(a)
# a couple of explicit normal arrows (short, red) at two of those points
for (tt,pp) in [(1.6,1.2),(4.4,1.9)]:
    n = np.array([np.cos(tt)*np.sin(pp), np.sin(tt)*np.sin(pp), np.cos(pp)])
    base = C0 + R*n; tip = C0 + (R+0.42)*n
    a = Arrow3D([base[0],tip[0]],[base[1],tip[1]],[base[2],tip[2]],
                mutation_scale=10, lw=1.6, arrowstyle='-|>', color=figR)
    ax.add_artist(a)
    ax.text(tip[0]+0.04, tip[1]+0.03, tip[2]+0.05, r'$\hat n$', color=figR, fontsize=10)
# interior sources: small dots with tiny diverging arrows
for c in [C0+np.array([-0.35,-0.2,0.0]), C0+np.array([0.45,0.3,-0.3])]:
    ax.scatter(*c, color=figR, s=12, depthshade=False)
    for d in [np.array([0.28,0.05,0.05]), np.array([-0.2,0.2,0.08]), np.array([0.0,-0.22,0.18])]:
        a = Arrow3D([c[0],c[0]+d[0]],[c[1],c[1]+d[1]],[c[2],c[2]+d[2]],
                    mutation_scale=7, lw=1.0, arrowstyle='-|>', color=figR, alpha=0.8)
        ax.add_artist(a)
ax.view_init(elev=18, azim=-58)
ax.set_xlim(0,3.6); ax.set_ylim(0,3.4); ax.set_zlim(0,3.2)
ax.set_box_aspect((1,0.95,0.88))
ax.text2D(0.66,0.86,'flux out through $\\partial V$:\n$\\iint_{\\partial V}\\mathbf{F}\\cdot\\hat n\\,dS$', transform=ax.transAxes, color=figG, fontsize=11)
ax.text2D(0.02,0.14,'sources inside $V$:\n$\\iiint_V \\nabla\\cdot\\mathbf{F}\\,dV$', transform=ax.transAxes, color=figR, fontsize=11)
plt.savefig(OUT+'/m452-18-2.svg', bbox_inches='tight', pad_inches=0.05)
plt.close()
print("python integral figs done")
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

mpl.rcParams['mathtext.fontset']='cm'; mpl.rcParams['font.family']='serif'; mpl.rcParams['font.size']=11
figB='#1F5AA6'; figR='#B03030'; figG='#22783C'

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *a, **k):
        super().__init__((0,0),(0,0),*a,**k); self._v=xs,ys,zs
    def do_3d_projection(self, renderer=None):
        xs,ys,zs = proj3d.proj_transform(*self._v, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1])); return np.min(zs)

def sph(r,t,p):
    t,p = np.broadcast_arrays(np.asarray(t,dtype=float), np.asarray(p,dtype=float))
    return np.array([r*np.cos(t)*np.sin(p), r*np.sin(t)*np.sin(p), r*np.cos(p)])

fig = plt.figure(figsize=(5.9,4.7))
ax = fig.add_subplot(111, projection='3d'); ax.set_axis_off(); ax.set_proj_type('ortho')
r0, r1 = 1.75, 2.15
t0, t1 = np.radians(24), np.radians(50)
p0, p1 = np.radians(36), np.radians(60)

# ---- sphere octant surface at r0 (semi-transparent) ----
tt, pp = np.meshgrid(np.linspace(0, np.pi/2, 40), np.linspace(0.10, np.pi/2, 32))
Ssph = sph(r0, tt, pp)
ax.plot_surface(Ssph[0], Ssph[1], Ssph[2], color=figB, alpha=0.16, linewidth=0)
# ---- extended coordinate curves delimiting the cell ----
pr = np.linspace(0.10, np.pi/2, 60)
for t in (t0, t1):
    C = sph(r0, t, pr); ax.plot(C[0],C[1],C[2], color=figB, lw=1.1, alpha=0.75)
tr = np.linspace(0, np.pi/2, 60)
for p in (p0, p1):
    C = sph(r0, tr, p); ax.plot(C[0],C[1],C[2], color=figB, lw=1.1, alpha=0.75)
# ---- inner face of the box: the grid cell itself, shaded on the sphere ----
tt2, pp2 = np.meshgrid(np.linspace(t0,t1,14), np.linspace(p0,p1,14))
Fin = sph(r0, tt2, pp2)
ax.plot_surface(Fin[0], Fin[1], Fin[2], color=figR, alpha=0.40, linewidth=0)
# ---- outer face at r1 ----
Fout = sph(r1, tt2, pp2)
ax.plot_surface(Fout[0], Fout[1], Fout[2], color=figR, alpha=0.28, linewidth=0)
# ---- 12 red edges ----
def edge(f, n=25):
    s = np.linspace(0,1,n); pts = np.array([f(si) for si in s]).T
    ax.plot(pts[0],pts[1],pts[2], color=figR, lw=1.6)
for (t,p) in [(t0,p0),(t0,p1),(t1,p0),(t1,p1)]:
    edge(lambda s,t=t,p=p: sph(r0+s*(r1-r0), t, p))
for (r,p) in [(r0,p0),(r0,p1),(r1,p0),(r1,p1)]:
    edge(lambda s,r=r,p=p: sph(r, t0+s*(t1-t0), p))
for (r,t) in [(r0,t0),(r0,t1),(r1,t0),(r1,t1)]:
    edge(lambda s,r=r,t=t: sph(r, t, p0+s*(p1-p0)))
# ---- radial dashed guide through the box (origin to outer corner) ----
Cout = sph(r1, t0, p0)
ax.plot([0,Cout[0]],[0,Cout[1]],[0,Cout[2]], color='gray', ls='dashed', lw=0.9)
# ---- axes ----
for vec,lab in zip([(2.9,0,0),(0,2.7,0),(0,0,2.5)], ('$x$','$y$','$z$')):
    a = Arrow3D([0,vec[0]],[0,vec[1]],[0,vec[2]], mutation_scale=11, lw=0.9, arrowstyle='-|>', color='black')
    ax.add_artist(a); ax.text(vec[0]+0.06, vec[1]+0.06, vec[2]+0.06, lab, fontsize=11)
ax.view_init(elev=20, azim=-52)
ax.set_xlim(0,2.9); ax.set_ylim(0,2.7); ax.set_zlim(0,2.5)
ax.set_box_aspect((1,0.95,0.88))
ax.text2D(0.05,0.90,'$dV = r^2\\sin\\varphi\\;dr\\,d\\theta\\,d\\varphi$', transform=ax.transAxes, fontsize=13)
ax.text2D(0.58,0.035,'cell of the spherical grid,\nthickened radially by $dr$', transform=ax.transAxes, fontsize=10)
# edge labels placed after a test render
ax.text2D(0.600,0.535,'$dr$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.585,0.395,'$r\\sin\\varphi\\,d\\theta$', transform=ax.transAxes, color=figR, fontsize=12)
ax.text2D(0.225,0.610,'$r\\,d\\varphi$', transform=ax.transAxes, color=figR, fontsize=12)
plt.savefig(OUT+'/m452-19-2.svg', bbox_inches='tight', pad_inches=0.05)
plt.close(); print("F28 remade")
