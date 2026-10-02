---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: 117
bc: "117"
aliases: ["B&C 117"]
tags: [complex-variables, math342, extension]
---
← [[§116★ Transformations of Harmonic Functions]] · ↑ [[· 9★ Conformal Mapping]] · [[§118★ Steady Temperatures]] →

*Brown–Churchill, Section 117 (with Exercises 4–6 and 10).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

[[§116★ Transformations of Harmonic Functions|§116]] showed that an analytic change of variables keeps Laplace's equation. For a boundary value problem the boundary conditions must be carried along too, and this section shows that the two most common ones survive a conformal map unchanged: a prescribed constant value $h = h_0$ (an isotherm, an equipotential, a conductor) and a vanishing normal derivative $dh/dn = 0$ (an insulated edge, a wall the fluid cannot cross). Other conditions do change: gradients, tangential and normal derivatives are all multiplied by the scale factor $|f'(z)|$. Together with §116 this gives the method of Chapter 10: map the physical region onto a simple one, solve there, and compose.

## Gradients Under a Conformal Map

B&C's proof of the main theorem needs an identity it leaves to Exercise 10; here it comes first. Identify a plane vector $(a, b)$ with the complex number $a + ib$. Then the dot product of two vectors is $\operatorname{Re}(\alpha\bar\beta)$, and the gradients are $\nabla H = H_x + iH_y$ and $\nabla h = h_u + ih_v$.

> [!theorem] Lemma §117.1: Gradients and Directional Derivatives Are Scaled by |f′(z)|
> Let $w = f(z) = u(x, y) + iv(x, y)$ be a conformal mapping of a smooth arc $C$ onto a smooth arc $\Gamma$, let $h(u, v)$ be differentiable near $\Gamma$, and put $H(x, y) = h[u(x, y), v(x, y)]$. At a point $(x, y)$ of $C$ with image $(u, v)$ on $\Gamma$:
>
> **(a)** $\nabla H = \overline{f'(z)}\,\nabla h$; in particular
>
> $$
> |\operatorname{grad} H(x, y)| = |\operatorname{grad} h(u, v)|\,|f'(z)| .
> $$
>
> **(b)** The angle from the arc $C$ to $\operatorname{grad} H$ at $(x, y)$ equals the angle from $\Gamma$ to $\operatorname{grad} h$ at $(u, v)$.
>
> **(c)** If $s$ and $\sigma$ denote arc length along $C$ and $\Gamma$, with unit tangents $\mathbf t$ and $\boldsymbol\tau$ in the direction of increasing length, then
>
> $$
> \frac{dH}{ds} = \frac{dh}{d\sigma}\,|f'(z)|, \qquad\text{where}\quad \frac{dH}{ds} = (\operatorname{grad} H)\cdot\mathbf t, \quad \frac{dh}{d\sigma} = (\operatorname{grad} h)\cdot\boldsymbol\tau .
> $$
>
> **(d)** Likewise for the normal derivatives along the normals $\mathbf N = i\mathbf t$ and $\mathbf n = i\boldsymbol\tau$ (unit tangents turned through $+\pi/2$):
>
> $$
> \frac{dH}{dN} = \frac{dh}{dn}\,|f'(z)| .
> $$
>
> *B&C: Sec. 117, Exercise 10 (part (d) is added)*

^lem-117-1

> [!proof]+ Proof
> **(a)** By the chain rule and the Cauchy–Riemann equations $u_y = -v_x$, $v_y = u_x$,
>
> $$
> H_x = h_uu_x + h_vv_x, \qquad H_y = h_uu_y + h_vv_y = -h_uv_x + h_vu_x .
> $$
>
> Hence
>
> $$
> H_x + iH_y = h_u(u_x - iv_x) + h_v(v_x + iu_x) = (h_u + ih_v)(u_x - iv_x) = \nabla h\;\overline{f'(z)} ,
> $$
>
> since $f'(z) = u_x + iv_x$ ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]). Taking moduli gives the identity for $|\operatorname{grad} H|$.
>
> **Tangents.** Let $z = z(s)$ parametrize $C$ by arc length, so $\mathbf t = z'(s)$, $|\mathbf t| = 1$. By the chain rule (§112, (1)) the image $w(s) = f[z(s)]$ has $w'(s) = f'(z)\,\mathbf t \ne 0$; so $d\sigma/ds = |w'(s)| = |f'(z)|$ and
>
> $$
> \boldsymbol\tau = \frac{f'(z)\,\mathbf t}{|f'(z)|} .
> $$
>
> **(b)** The angle from $C$ to $\nabla H$ is $\arg(\nabla H/\mathbf t)$, and the angle from $\Gamma$ to $\nabla h$ is $\arg(\nabla h/\boldsymbol\tau) = \arg\big(\nabla h/(f'(z)\mathbf t)\big)$. Since $\overline{f'} = |f'|^2/f'$,
>
> $$
> \frac{\nabla H}{\mathbf t} = \frac{\overline{f'(z)}\,\nabla h}{\mathbf t} = |f'(z)|^2\,\frac{\nabla h}{f'(z)\,\mathbf t},
> $$
>
> a positive multiple of $\nabla h/\boldsymbol\tau$; so the two arguments agree. (If $\nabla h = 0$ there is no angle to compare, and both sides of (a) vanish.)
>
> **(c)** With the dot product $\alpha\cdot\beta = \operatorname{Re}(\alpha\bar\beta)$,
>
> $$
> \frac{dH}{ds} = \operatorname{Re}\big(\overline{f'}\,\nabla h\,\bar{\mathbf t}\big), \qquad \frac{dh}{d\sigma} = \operatorname{Re}\Big(\nabla h\,\frac{\overline{f'}\,\bar{\mathbf t}}{|f'|}\Big) = \frac{1}{|f'|}\operatorname{Re}\big(\overline{f'}\,\nabla h\,\bar{\mathbf t}\big) ,
> $$
>
> so $dH/ds = |f'(z)|\,dh/d\sigma$.
>
> **(d)** The same computation with $\mathbf N = i\mathbf t$ and $\mathbf n = i\boldsymbol\tau = f'(z)\,\mathbf N/|f'(z)|$ in place of $\mathbf t$ and $\boldsymbol\tau$.

^pf-117-1

*Uses:* [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|§112.1]], [[§94 The Chain Rule#^thm-94-2|Calc Thm. §94.2]] (chain rule), [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|Calc Cor. §95.2]] (directional derivative as a dot product)

## The Theorem

> [!theorem] Theorem §117.2: Constant Values and Zero Normal Derivatives Are Preserved
> Suppose that
>
> **(a)** a transformation $w = f(z) = u(x, y) + iv(x, y)$ is conformal at each point of a smooth arc $C$, and $\Gamma$ is the image of $C$ under that transformation;
>
> **(b)** $h(u, v)$ is a function that satisfies one of the conditions
>
> $$
> h = h_0 \qquad\text{and}\qquad \frac{dh}{dn} = 0
> $$
>
> at points of $\Gamma$, where $h_0$ is a real constant and $dh/dn$ denotes directional derivatives of $h$ normal to $\Gamma$.
>
> Then the function $H(x, y) = h[u(x, y), v(x, y)]$ satisfies the corresponding condition
>
> $$
> H = h_0 \qquad\text{or}\qquad \frac{dH}{dN} = 0
> $$
>
> at points of $C$, where $dH/dN$ denotes directional derivatives of $H$ normal to $C$. In applications $C$ may be the entire boundary of a domain or only part of it.
>
> *B&C: Sec. 117, Theorem*

^thm-117-2

> [!proof]+ Proof
> **$h = h_0$ on $\Gamma$.** The value of $H$ at a point $(x, y)$ of $C$ is the value of $h$ at its image $(u, v)$. That image lies on $\Gamma$, where $h = h_0$; so $H = h_0$ along $C$.
>
> **$dh/dn = 0$ on $\Gamma$ (B&C's geometric argument).** From calculus,
>
> $$
> \frac{dh}{dn} = (\operatorname{grad} h)\cdot\mathbf n , \qquad (1)
> $$
>
> where $\mathbf n$ is a unit normal to $\Gamma$ at $(u, v)$. Suppose first that $\operatorname{grad} h \ne \mathbf 0$ at $(u, v)$. Since $dh/dn = 0$, (1) says $\operatorname{grad} h$ is orthogonal to $\mathbf n$, that is, tangent to $\Gamma$. Gradients are orthogonal to level curves, so $\Gamma$ is orthogonal to the level curve $h(u, v) = c$ through $(u, v)$ (B&C's Fig. 151). The level curve $H(x, y) = c$ through $(x, y)$ is $h[u(x, y), v(x, y)] = c$, so $w = f(z)$ transforms it into the level curve $h(u, v) = c$; and $C$ is transformed into $\Gamma$. Since the map is conformal at $(x, y)$ ([[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]]), $C$ is orthogonal to the level curve $H(x, y) = c$ at $(x, y)$. Again because gradients are orthogonal to level curves, $\operatorname{grad} H$ is tangent to $C$ at $(x, y)$, so for a unit normal $\mathbf N$ to $C$,
>
> $$
> (\operatorname{grad} H)\cdot\mathbf N = 0 . \qquad (2)
> $$
>
> Since $dH/dN = (\operatorname{grad} H)\cdot\mathbf N$, (2) gives $dH/dN = 0$ on $C$. If $\operatorname{grad} h = \mathbf 0$ at $(u, v)$, then $\operatorname{grad} H = \mathbf 0$ at $(x, y)$ by Lemma §117.1(a), and both normal derivatives are $0$.
>
> B&C notes that this argument tacitly assumes that $\operatorname{grad} h$ and $\operatorname{grad} H$ exist, and that the level curve $H(x, y) = c$ is smooth where $\operatorname{grad} h \ne \mathbf 0$ (so that Theorem §112.1 applies to it); both hold in all the applications. (Lemma §117.1(d) removes the second assumption: $dH/dN = |f'(z)|\,dh/dn = 0$ directly, the normals $\mathbf N$ and $\mathbf n$ corresponding under the map.)

^pf-117-2

*Uses:* [[§117★ Transformations of Boundary Conditions#^lem-117-1|§117.1]], [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|§112.1]], [[§95 Directional Derivatives and the Gradient Vector#^cor-95-2|Calc Cor. §95.2]], [[§95 Directional Derivatives and the Gradient Vector#^thm-95-7|Calc Thm. §95.7]] (the gradient is perpendicular to level curves)

> [!remark]- Connections
> - Normal derivatives and the Dirichlet/Neumann/Robin conditions on a boundary: [[§35 Potential Equation#^def-35-2|341 Def. §35.2]]; the normal derivative as $\nabla v\cdot\hat n$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]].
> - Used in Electromagnetism: conductors (constant potential) and lines of symmetry (zero normal field) keep their boundary conditions under an analytic map — [[§C6.4★ The Complex Potential and the Variational Principle#^thm-c6-4-2|EM Theorem §C6.4.2]].

A condition of another type can change substantially (Example §117.3). By Lemma §117.1, the ratio of a directional derivative of $H$ along $C$ to that of $h$ along $\Gamma$ at the corresponding point is $|f'(z)|$, which in general is not constant along the arc. So $dh/dn = h_0 \ne 0$ becomes $dH/dN = h_0|f'(z)|$, a variable flux; new boundary conditions for the transformed problem can still be written down in any particular case.

> [!remark] Remark: Method — Solving a Boundary Value Problem by Conformal Mapping
> To solve Laplace's equation in a domain $D_z$ with boundary conditions of the types $H = $ const and $dH/dN = 0$ on pieces of the boundary:
> 1. **Find a conformal map** $w = f(z)$ of $D_z$ onto a simple domain $D_w$ (half plane, strip, quadrant, disk), using the elementary maps of Chapter 8 and compositions of them.
> 2. **Transfer the boundary conditions** piece by piece: each piece of $\partial D_z$ goes to a piece of $\partial D_w$ with the same condition (Theorem §117.2). Points where $f$ is not conformal (corners, critical points) are allowed on the boundary, where the conditions change.
> 3. **Solve the simpler problem** for $h(u, v)$ in $D_w$, usually as the real or imaginary part of an analytic function such as $A\operatorname{Log} w + B$ or $A w + B$.
> 4. **Compose**: $H(x, y) = h[u(x, y), v(x, y)]$ is harmonic in $D_z$ (Theorem §116.1) and satisfies the original conditions. If needed, find the level curves $H = c$ (isotherms, equipotentials) and the conjugate (heat-flow lines, field lines).
>
> Chapter 10 carries this out for steady temperatures ([[§119★ Steady Temperatures in a Half Plane|§119]]–[[§121★ Temperatures in a Quadrant|§121]]), electrostatic potentials ([[§123★ Examples (Electrostatic Potential)|§123]]) and flows ([[§126★ Flows Around a Corner and Around a Cylinder|§126]]).

^rem-117-1

## Examples

> [!example] Example §117.1: A Wedge Mapped by iz²
> Let $h(u, v) = v + 2$. The transformation
>
> $$
> w = iz^2 = i(x + iy)^2 = -2xy + i(x^2 - y^2)
> $$
>
> is conformal when $z \ne 0$. It maps the half line $y = x$ $(x > 0)$ onto the negative $u$ axis, where $h = 2$, and the positive $x$ axis onto the positive $v$ axis, where the normal derivative $h_u$ is $0$. By Theorem §117.2 the function
>
> $$
> H(x, y) = h[u(x, y), v(x, y)] = x^2 - y^2 + 2
> $$
>
> must satisfy $H = 2$ along the half line $y = x$ $(x > 0)$ and $H_y = 0$ along the positive $x$ axis.
>
> **Images.** On $z = t(1 + i)$, $t > 0$: $z^2 = 2it^2$ and $iz^2 = -2t^2 < 0$. On $z = t > 0$: $iz^2 = it^2$, on the positive $v$ axis. The wedge $0 < \arg z < \pi/4$ goes to $\pi/2 < \arg w < \pi$, the second quadrant.
>
> **Direct check.** On $y = x$, $H = x^2 - x^2 + 2 = 2$. And $H_y = -2y$, which is $0$ on the $x$ axis. The normal derivative there is $H_y$ (up to sign), as the theorem predicts.
>
> *B&C: Sec. 117, Example*

^ex-117-1

![[m342-117-1.svg]]
*Example §117.1. Left: the wedge $0 < \arg z < \pi/4$ with the level curves $H = x^2 - y^2 + 2 = 2.25, 2.5, \ldots$ (blue), hyperbolas that meet the $x$ axis (where $H_y = 0$) at right angles; the edge $y = x$ (red) is the level curve $H = 2$. Right: under $w = iz^2$ the wedge becomes the second quadrant, the level curves become the horizontal lines $h = v + 2 = $ const, meeting the $v$ axis (where $h_u = 0$) at right angles, and the edge becomes the negative $u$ axis, where $h = 2$.*

> [!example] Example §117.2: The Value 2 on a Semicircle and on a Segment
> Under $w = e^z$ the segment $0 \le y \le \pi$ of the $y$ axis goes onto the semicircle $u^2 + v^2 = 1$, $v \ge 0$ ([[§103★ Mappings by the Exponential Function#^ex-103-1|Example §103.1]]): $e^{iy}$, $0 \le y \le \pi$. The function
>
> $$
> h(u, v) = \operatorname{Re}\Big(2 - w + \frac1w\Big) = 2 - u + \frac{u}{u^2 + v^2}
> $$
>
> is harmonic everywhere except at the origin, and on the semicircle $u^2 + v^2 = 1$ it equals $2 - u + u = 2$. Find $H$ and check that $H = 2$ on the segment.
>
> Since $1/w = e^{-z}$, $\operatorname{Re}(1/w) = e^{-x}\cos y$, and
>
> $$
> H(x, y) = 2 - e^x\cos y + e^{-x}\cos y = 2 - 2\sinh x\cos y .
> $$
>
> On $x = 0$, $H = 2 - 0 = 2$, as Theorem §117.2 says.
>
> *B&C: Sec. 117, Exercise 4*

^ex-117-2

> [!example] Example §117.3: Zero Normal Derivatives Survive, Nonzero Ones Do Not
> The transformation $w = z^2$ maps the positive $x$ and $y$ axes and the origin onto the $u$ axis.
>
> **(a)** The harmonic function $h(u, v) = \operatorname{Re}(e^{-w}) = e^{-u}\cos v$ has normal derivative $h_v = -e^{-u}\sin v = 0$ along the $u$ axis. With $u = x^2 - y^2$, $v = 2xy$,
>
> $$
> H(x, y) = e^{-(x^2 - y^2)}\cos 2xy, \qquad H_y = e^{-(x^2 - y^2)}\big[2y\cos 2xy - 2x\sin 2xy\big], \qquad H_x = e^{-(x^2 - y^2)}\big[-2x\cos 2xy - 2y\sin 2xy\big].
> $$
>
> On the positive $x$ axis ($y = 0$), $H_y = 0$; on the positive $y$ axis ($x = 0$), $H_x = 0$. So the normal derivative of $H$ vanishes along both positive axes, as Theorem §117.2 predicts, although $w = z^2$ is not conformal at the origin, where the two axes meet.
>
> **(b)** Replace $h$ by the harmonic function $h(u, v) = \operatorname{Re}(-2iw + e^{-w}) = 2v + e^{-u}\cos v$. Now $h_v = 2 - e^{-u}\sin v = 2$ along the $u$ axis, but $H = 4xy + e^{-(x^2 - y^2)}\cos 2xy$ has
>
> $$
> H_y = 4x \ \text{ on the positive } x \text{ axis}, \qquad H_x = 4y \ \text{ on the positive } y \text{ axis} .
> $$
>
> So a condition $dh/dn = h_0 \ne 0$ is not transformed into $dH/dN = h_0$. It becomes $h_0|f'(z)|$, as Lemma §117.1(d) predicts: $|f'(z)| = |2z| = 2x$ on the $x$ axis and $2y$ on the $y$ axis, and $2 \cdot 2x = 4x$, $2 \cdot 2y = 4y$.
>
> *B&C: Sec. 117, Exercises 5 and 6*

^ex-117-3
