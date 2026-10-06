---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: "131★"
bc: "131"
aliases: ["B&C 131"]
tags: [complex-variables, math342, extension]
---
← [[§130★ Degenerate Polygons]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§132★ Flow in a Channel with an Offset]] →

*Brown–Churchill, Section 131.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section continues the idealized steady flow of Chapter 10 ([[§124★ Two-Dimensional Fluid Flow|§124★]], [[§125★ The Stream Function|§125★]]) and shows how sources and sinks are handled. The key fact is that a conformal map carries the stream function to a stream function, so a source or sink at a point becomes an equal source or sink at the image point. Fluid entering a channel through a slit in one wall is then solved by mapping the channel onto a half plane with $z = e^w$, writing down the potential of a source and a sink on the boundary of the half plane, and mapping back. From this section on, the problems are posed in the $uv$ plane, so that the results of [[§127★ Mapping the Real Axis onto a Polygon|§127★]]–[[§130★ Degenerate Polygons|§130★]] apply without interchanging the planes.

## Sources and Sinks under Conformal Maps

Consider the two-dimensional steady flow between the parallel planes $v = 0$ and $v = \pi$, when the fluid enters through a narrow slit along the line in the first plane that is perpendicular to the $uv$ plane at the origin. Let the rate of flow into the channel through the slit be $Q$ units of volume per unit time for each unit of depth of the channel (depth measured perpendicular to the $uv$ plane). The rate of flow out at either end is then $Q/2$.

The transformation $w = \operatorname{Log}z$ is a one to one mapping of the upper half $y > 0$ of the $z$ plane onto the strip $0 < v < \pi$ ([[§130★ Degenerate Polygons#^ex-130-2|Example §130.2]]). The inverse transformation

$$
z = e^w = e^ue^{iv} \qquad (1)
$$

maps the strip onto the half plane ([[§103★ Mappings by the Exponential Function#^ex-103-3|Example §103.3]]). Under (1) the $u$ axis goes onto the positive half of the $x$ axis and the line $v = \pi$ onto the negative half, so the boundary of the strip goes onto the boundary of the half plane. The image of $w = 0$ is $z = 1$; the image of $w = u_0 > 0$ is a point $z = x_0 > 1$, and the image of $w = u_1 < 0$ is a point $z = x_1$ with $0 < x_1 < 1$.

> [!theorem] Proposition §131.1: Sources and Sinks Correspond under Conformal Maps
> Under a conformal one to one transformation of one flow region onto another, the stream function $\psi$ of a flow is carried to a stream function of the flow in the image region, and the rate of flow across corresponding curves is the same. Consequently a source or sink at a point corresponds to an equal source or sink at the image of that point, including sources and sinks "at infinity" at the ends of a channel.
>
> *B&C: Sec. 131 (text)*

^prop-131-1

> [!proof]+ Proof
> This is B&C's argument. Let $F = \phi + i\psi$ be a complex potential of the flow in the $w$ plane, and let $w = g(z)$ be the conformal map. Then $F(g(z))$ is analytic, so it is a complex potential in the $z$ plane, with stream function $\psi(g(z))$ ([[§116★ Transformations of Harmonic Functions#^thm-116-1|Theorem §116.1]]); as in Chapter 10, the same symbol $\psi$ is used for the stream functions in both planes. By [[§125★ The Stream Function#^prop-125-1|Proposition §125.1]], the rate of flow across a curve joining two points is the difference of the values of $\psi$ at its ends. Corresponding curves have corresponding ends, where the two stream functions take the same values, so the rates of flow are equal.
>
> For the channel: the rate of flow across a curve joining $w = u_0$ to $w = u_1$ around the slit is $\psi(u_1, 0) - \psi(u_0, 0) = Q$ (taking $\psi(u_0, 0) = 0$). The image curve joins $z = x_0$ to $z = x_1$ in the upper half plane, around $z = 1$, and the rate of flow across it is also $Q$: there is a source at $z = 1$ equal to the source at $w = 0$. The same argument applies at any point. For the sink infinitely far to the left in the strip, use a curve joining the walls $v = 0$ and $v = \pi$ in the left part of the strip: since $z = e^w \to 0$ as $\operatorname{Re} w \to -\infty$, its image is a curve around $z = 0$ joining the two half axes, and it carries the same flow $Q/2$; so there is a sink of strength $Q/2$ at $z = 0$. In the same way the sink at the right-hand end of the strip becomes a sink at infinity in the $z$ plane.

^pf-131-1

*Uses:* [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]], [[§125★ The Stream Function#^prop-125-1|§125.1]]

## The Flow through the Slit

> [!example] Example §131.1: Complex Potential and Velocity
> Find the complex potential and the velocity of the flow in the channel.
>
> **In the $z$ plane.** By Proposition §131.1 we need a stream function $\psi$ in $y > 0$ that is constant along each of the three parts $x < 0$, $0 < x < 1$, $x > 1$ of the $x$ axis, increases by $Q$ as $z$ moves around $z = 1$ from $x_0$ to $x_1$, and decreases by $Q/2$ as $z$ moves around the origin in the same manner. The function
>
> $$
> \psi = \frac Q\pi\Big[\operatorname{Arg}(z - 1) - \frac12\operatorname{Arg}z\Big]
> $$
>
> does this: $\operatorname{Arg}(z - 1)$ goes from $0$ to $\pi$ around $z = 1$, and $\operatorname{Arg}z$ from $0$ to $\pi$ around $z = 0$. It is harmonic in $\operatorname{Im} z > 0$, being the imaginary component of
>
> $$
> F = \frac Q\pi\Big[\operatorname{Log}(z - 1) - \frac12\operatorname{Log}z\Big] = \frac Q\pi\operatorname{Log}\big(z^{1/2} - z^{-1/2}\big) .
> $$
>
> (The last equality holds with principal branches: in $y > 0$, $\operatorname{Arg}(z - 1) - \frac12\operatorname{Arg}z$ lies in $(-\pi/2, \pi)$, so no multiple of $2\pi i$ appears.) $F$ is a complex potential for the flow in the upper half plane.
>
> **In the $w$ plane.** Since $z = e^w$ and $z^{1/2} = e^{w/2}$ for $0 < v < \pi$, a complex potential for the channel is
>
> $$
> F(w) = \frac Q\pi\operatorname{Log}\big(e^{w/2} - e^{-w/2}\big) = \frac Q\pi\operatorname{Log}\Big(2\sinh\frac w2\Big) ,
> $$
>
> and dropping the additive constant $\frac Q\pi\ln2$,
>
> $$
> F(w) = \frac Q\pi\operatorname{Log}\Big(\sinh\frac w2\Big) . \qquad (2)
> $$
>
> (B&C uses the same symbol $F$ for three distinct functions, once in the $z$ plane and twice in the $w$ plane.)
>
> **Velocity.** By [[§125★ The Stream Function#^prop-125-2|Proposition §125.2]] the velocity is the conjugate of $F'$:
>
> $$
> V = \overline{F'(w)} = \frac{Q}{2\pi}\coth\frac{\overline w}{2} . \qquad (3)
> $$
>
> As $u \to +\infty$, $\coth(\overline w/2) \to 1$, and as $u \to -\infty$, $\coth(\overline w/2) \to -1$. So $V \to Q/2\pi$ far to the right and $V \to -Q/2\pi$ far to the left: the fluid leaves through both ends, at the speed $Q/2\pi$ that carries $Q/2$ through a channel of width $\pi$.
>
> *B&C writes $\lim_{|u|\to\infty}V = Q/2\pi$; this holds for $u \to +\infty$, while for $u \to -\infty$ the limit is $-Q/2\pi$. It is the speed $|V|$ that tends to $Q/2\pi$ at both ends.*
>
> **Check of the outflow.** On $v = 0$, $u > 0$: $\sinh(u/2) > 0$, so $\psi = 0$; on $v = \pi$: $\sinh\big((u + \pi i)/2\big) = i\cosh(u/2)$, so $\psi = \frac Q\pi\cdot\frac\pi2 = \frac Q2$. The flow across the right end is $\frac Q2 - 0 = \frac Q2$. On $v = 0$, $u < 0$: $\sinh(u/2) < 0$, $\psi = Q$; so across the left end the flow is $\frac Q2 - Q = -\frac Q2$, that is, $Q/2$ to the left.
>
> *B&C: Sec. 131, equations (2)–(3)*

^ex-131-1

> [!example] Example §131.2: Streamlines and the Stagnation Point
> Find the streamlines and the stagnation points of the flow (2).
>
> **Stagnation point.** $V = 0$ exactly when $\cosh(w/2) = 0$, that is, $w/2 = \pi i/2 + k\pi i$; in the channel this is $w = \pi i$, the point of the far wall opposite the slit. By Bernoulli's principle ([[§124★ Two-Dimensional Fluid Flow#^prop-124-3|Proposition §124.3]]) the pressure is greatest where the speed is least, so the fluid pressure along the wall $v = \pi$ is greatest at points opposite the slit.
>
> **Streamlines.** The stream function is the imaginary part of (2), so the streamlines $\psi(u, v) = c_2$ are the curves
>
> $$
> \frac Q\pi\operatorname{Arg}\Big(\sinh\frac w2\Big) = c_2 .
> $$
>
> (B&C states the result; here is the reduction.) With $w = u + iv$,
>
> $$
> \sinh\frac w2 = \sinh\frac u2\cos\frac v2 + i\cosh\frac u2\sin\frac v2 ,
> $$
>
> so the argument is constant exactly when the ratio of real to imaginary part, $\tanh\frac u2\cot\frac v2$, is constant. Calling that constant $1/c$,
>
> $$
> \tan\frac v2 = c\tanh\frac u2 , \qquad (4)
> $$
>
> where $c$ is any real constant. Since $0 < v < \pi$ makes $\tan(v/2) > 0$, a streamline with $c > 0$ lies in $u > 0$ and one with $c < 0$ in $u < 0$. Each starts at the slit ($u \to 0$ forces $v \to 0$) and approaches the line $v = 2\tan^{-1}|c|$ far down the channel. The limiting case $c = \pm\infty$ is the segment $u = 0$ from the slit to the stagnation point $\pi i$, which divides the flow going left from the flow going right.
>
> *B&C: Sec. 131, equation (4)*

^ex-131-2

![[m342-131-1.svg]]
*Streamlines (4) of the flow into the channel $0 < v < \pi$ through a slit at the origin, for $c = \pm0.15, \pm0.4, \pm1, \pm2.5, \pm7$ (blue), and the dividing streamline $u = 0$ (red) ending at the stagnation point $\pi i$. Half the fluid leaves at each end (orange arrows).*

> [!example] Example §131.3: The Speed along the Walls
> Find the speed of the fluid along the two walls of the channel.
>
> On the wall $v = \pi$, $\overline w/2 = u/2 - \pi i/2$, and $\coth(x - \pi i/2) = \tanh x$ (since $\cosh(x - \pi i/2) = -i\sinh x$ and $\sinh(x - \pi i/2) = -i\cosh x$). So by (3)
>
> $$
> |V| = \frac{Q}{2\pi}\Big|\tanh\frac u2\Big| \qquad (v = \pi) ,
> $$
>
> which is $0$ at the stagnation point $u = 0$ and increases to $Q/2\pi$ as $|u| \to \infty$. On the wall $v = 0$,
>
> $$
> |V| = \frac{Q}{2\pi}\Big|\coth\frac u2\Big| \qquad (v = 0,\ u \ne 0) ,
> $$
>
> which decreases from $\infty$ at the slit to $Q/2\pi$ as $|u| \to \infty$. For example, at $u = 1$ the speeds are $0.462\,Q/2\pi$ on the far wall and $2.164\,Q/2\pi$ on the near wall. Along the far wall the pressure therefore falls steadily away from the point opposite the slit.
>
> *B&C: Sec. 131, equation (3)*

^ex-131-3
