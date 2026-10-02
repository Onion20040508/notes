---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: 132
bc: "132"
aliases: ["B&C 132"]
tags: [complex-variables, math342, extension]
---
← [[§131★ Fluid Flow in a Channel through a Slit]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§133★ Electrostatic Potential about an Edge of a Conducting Plate]] →

*Brown–Churchill, Section 132.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

A channel whose breadth changes abruptly from $\pi$ to $h\pi$ is a degenerate quadrilateral, and the Schwarz–Christoffel transformation maps the upper half plane onto it. Instead of finding the map first, B&C goes straight to the complex potential: the source at the left end of the channel corresponds to a source at $z = 0$, so the potential in the $z$ plane is $V_0\operatorname{Log}z$, and the chain rule gives the velocity in the channel in terms of $z$. The two unknown constants of the map are fixed by the speeds far upstream and downstream. The result shows a stagnation point at the inner corner and infinite speed at the outer corner. The section closes with the integration of the map itself, and a related flow over a step in a stream bed (from the exercises) is worked in the same way.

> [!example] Example §132.1: Setting Up the Map and the Potential
> Take the unit of length so that the breadth of the wide part of the channel is $\pi$; the narrow part has breadth $h\pi$, $0 < h < 1$. Let the real constant $V_0$ be the velocity far from the offset in the wide part, $\lim_{u\to-\infty}V = V_0$. The rate of flow per unit depth through the channel, the strength of the source on the left and of the sink on the right, is then
>
> $$
> Q = \pi V_0 . \qquad (1)
> $$
>
> **The map.** The cross section is the limit of the quadrilateral with vertices $w_1$ (far left on the top wall), $w_2 = 0$ (the foot of the step), $w_3$ (the top of the step) and $w_4$ (far right), as $w_1$ and $w_4$ move infinitely far to the left and right. The limiting exterior angles are
>
> $$
> k_1\pi = \pi, \qquad k_2\pi = \frac\pi2, \qquad k_3\pi = -\frac\pi2, \qquad k_4\pi = \pi .
> $$
>
> Proceeding formally ([[§130★ Degenerate Polygons#^rem-130-1|Remark: The Formal Method]]), choose $x_1 = 0$, $x_3 = 1$, $x_4 = \infty$, and leave $x_2$ to be determined, $0 < x_2 < 1$. Then
>
> $$
> \frac{dw}{dz} = Az^{-1}(z - x_2)^{-1/2}(z - 1)^{1/2} . \qquad (2)
> $$
>
> **The potential.** The source infinitely far to the left corresponds to an equal source at $z = 0$ ([[§131★ Fluid Flow in a Channel through a Slit#^prop-131-1|Proposition §131.1]]), and the whole boundary of the channel is the image of the $x$ axis. In view of (1), the function
>
> $$
> F = V_0\operatorname{Log}z = V_0\ln r + iV_0\theta \qquad (3)
> $$
>
> is the potential for the flow in the upper half of the $z$ plane, with the required source at the origin: its stream function $\psi = V_0\theta$ is constant on the axis and increases from $0$ to $V_0\pi = Q$ over each semicircle $z = Re^{i\theta}$, $0 \le \theta \le \pi$ (compare (5) of [[§125★ The Stream Function|§125★]]).
>
> **The velocity.** The conjugate of the velocity in the $w$ plane is, by the chain rule,
>
> $$
> \overline{V(w)} = \frac{dF}{dw} = \frac{dF}{dz}\frac{dz}{dw} = \frac{V_0}{z}\cdot\frac{z(z - x_2)^{1/2}}{A(z - 1)^{1/2}} = \frac{V_0}{A}\Big(\frac{z - x_2}{z - 1}\Big)^{1/2} . \qquad (4)
> $$
>
> *B&C: Sec. 132, equations (1)–(4)*

^ex-132-1

> [!example] Example §132.2: The Constants and the Velocity
> Determine $A$ and $x_2$ in (2), and describe the velocity on the walls.
>
> **Upstream.** At the limiting position of $w_1$, which corresponds to $z = 0$, the velocity is the real constant $V_0$. Letting $z \to 0$ in (4), $\big((0 - x_2)/(0 - 1)\big)^{1/2} = \sqrt{x_2}$, so
>
> $$
> V_0 = \frac{V_0}{A}\sqrt{x_2} .
> $$
>
> **Downstream.** At the limiting position of $w_4$, which corresponds to $z = \infty$, let $V_4$ be the (real) velocity. It is plausible that as a vertical segment spanning the narrow part is moved infinitely far to the right, $V$ tends to $V_4$ at each point of it; B&C assumes this, to shorten the discussion (it could be checked from the map (8) below). Since the flow is steady, the same $Q$ passes through both parts: $\pi hV_4 = \pi V_0 = Q$, so $V_4 = V_0/h$. Letting $z \to \infty$ in (4), where $(z - x_2)/(z - 1) \to 1$,
>
> $$
> \frac{V_0}{h} = \frac{V_0}{A} .
> $$
>
> Thus
>
> $$
> A = h, \qquad x_2 = h^2 , \qquad (5)
> $$
>
> and
>
> $$
> \overline{V(w)} = \frac{V_0}{h}\Big(\frac{z - h^2}{z - 1}\Big)^{1/2} . \qquad (6)
> $$
>
> **On the walls.** The magnitude $|V|$ becomes infinite at the corner $w_3$ of the offset, the image of $z = 1$; and the corner $w_2$, the image of $z = h^2$, is a stagnation point, $V = 0$. By Bernoulli's principle, along the boundary the fluid pressure is greatest at $w_2$ and least at $w_3$. Along the boundary $z = x$ the speed is $|V| = \frac{V_0}{h}\sqrt{|x - h^2|/|x - 1|}$; for $h = \frac12$, at $x = -1$ (on the top wall) it is $V_0\cdot2\sqrt{1.25/2} = 1.581\,V_0$, larger than $V_0$ because the stream is turning toward the narrow part.
>
> *B&C: Sec. 132, equations (5)–(6)*

^ex-132-2

> [!example] Example §132.3: The Mapping Function
> Integrate (2) with the constants (5), and check where the corners go.
>
> With (5), (2) reads
>
> $$
> \frac{dw}{dz} = \frac hz\Big(\frac{z - 1}{z - h^2}\Big)^{1/2} . \qquad (7)
> $$
>
> **Substitution.** Let $s$ be the new variable with $\dfrac{z - h^2}{z - 1} = s^2$. Solving, $z = \dfrac{s^2 - h^2}{s^2 - 1}$, and
>
> $$
> \frac{dz}{ds} = \frac{2s(s^2 - 1) - 2s(s^2 - h^2)}{(s^2 - 1)^2} = \frac{2s(h^2 - 1)}{(s^2 - 1)^2} .
> $$
>
> Since $\big((z - 1)/(z - h^2)\big)^{1/2} = 1/s$,
>
> $$
> \frac{dw}{ds} = \frac hz\cdot\frac1s\cdot\frac{dz}{ds} = h\,\frac{s^2 - 1}{s^2 - h^2}\cdot\frac1s\cdot\frac{2s(h^2 - 1)}{(s^2 - 1)^2} = \frac{2h(h^2 - 1)}{(s^2 - h^2)(s^2 - 1)} = 2h\Big(\frac{1}{1 - s^2} - \frac{1}{h^2 - s^2}\Big) ,
> $$
>
> the last step by partial fractions: $\frac{1}{1 - s^2} - \frac{1}{h^2 - s^2} = \frac{h^2 - 1}{(1 - s^2)(h^2 - s^2)}$.
>
> **Integration.** Since $\int\frac{2\,ds}{1 - s^2} = \operatorname{Log}\frac{1 + s}{1 - s}$ and $\int\frac{2h\,ds}{h^2 - s^2} = \operatorname{Log}\frac{h + s}{h - s}$,
>
> $$
> w = h\operatorname{Log}\frac{1 + s}{1 - s} - \operatorname{Log}\frac{h + s}{h - s} . \qquad (8)
> $$
>
> The constant of integration is zero because when $z = h^2$, $s = 0$ and so $w = 0$: the foot of the step $w_2$ is at the origin.
>
> **The corners.** (B&C does not check these; here they are.) For $z$ in the upper half plane, $s^2 = 1 + (1 - h^2)/(z - 1)$ lies in the lower half plane; take $s$ in the fourth quadrant. Then $(1 + s)/(1 - s)$ and $(h + s)/(h - s)$ lie in the lower half plane and the principal logarithms in (8) are continuous. As $z \to x > 1$ from above, $s$ tends to a real number greater than $1$ from below, both quotients tend to negative numbers from below, and both $\operatorname{Arg}$s tend to $-\pi$; so $\operatorname{Im} w \to -h\pi + \pi = (1 - h)\pi$. Thus $x > 1$ goes to the top of the step, $v = (1 - h)\pi$, and the narrow part is $(1 - h)\pi < v < \pi$, of breadth $h\pi$. For $x < 0$, $h < s < 1$, the first quotient is positive and the second negative, so $\operatorname{Im} w = \pi$: the top wall. For $h^2 < x < 1$, $s = -i\sigma$ is imaginary and $w = i\big(2\tan^{-1}(\sigma/h) - 2h\tan^{-1}\sigma\big)$ runs up the riser from $0$ to $(1 - h)\pi i$. A numerical evaluation with $h = \frac12$ gives $w = 1.5708\,i = \frac\pi2 i$ at $z = 1$, as it should.
>
> **The potential as a function of $w$.** In terms of $s$, (3) becomes $F = V_0\operatorname{Log}\dfrac{h^2 - s^2}{1 - s^2}$, so
>
> $$
> s^2 = \frac{\exp(F/V_0) - h^2}{\exp(F/V_0) - 1} . \qquad (9)
> $$
>
> Substituting $s$ from (9) into (8) gives an implicit relation that defines $F$ as a function of $w$.
>
> *B&C: Sec. 132, equations (7)–(9)*

^ex-132-3

![[m342-132-1.svg]]
*Streamlines of the flow in the channel with an offset, $h = \frac12$: the images under (8) of the rays $\arg z = k\pi/8$, $k = 1, \ldots, 7$, along which $\psi = V_0\theta$ is constant. They crowd together around the corner $w_3$, where the speed is infinite, and spread out in the corner at $w_2$, a stagnation point. Far to the right they are equally spaced across the narrow part, where the speed is $V_0/h = 2V_0$.*

> [!example] Example §132.4: Flow over a Step in a Stream Bed
> The region of B&C's Fig. 29 (Appendix 2) is the upper half of the $w$ plane above a step: the bed is the half line $v = h$, $u \le 0$ (from $A'$ to $B' = hi$), the segment from $hi$ down to $C' = 0$, and the positive $u$ axis ($C'D'$). (a) Obtain formally the map from the upper half of the $z$ plane, with $B'$, $C'$ the images of $z = -1$, $z = 1$. (b) For the flow of a deep stream with $V \to V_0$ (real) as $|w| \to \infty$, find the velocity and the speed along the bed.
>
> **(a) The map.** At $z = -1$ the direction turns from east to south, $k = \frac12$; at $z = 1$ from south to east, $k = -\frac12$. So
>
> $$
> \frac{dw}{dz} = A\Big(\frac{z + 1}{z - 1}\Big)^{1/2} .
> $$
>
> With $0 \le \arg(z \pm 1) \le \pi$, an antiderivative is $(z + 1)^{1/2}(z - 1)^{1/2} + \operatorname{Log}\big[z + (z + 1)^{1/2}(z - 1)^{1/2}\big]$: writing $q = (z + 1)^{1/2}(z - 1)^{1/2}$, $q' = z/q$, and the derivative is
>
> $$
> \frac zq + \frac{1 + z/q}{z + q} = \frac zq + \frac1q = \frac{z + 1}{q} = \Big(\frac{z + 1}{z - 1}\Big)^{1/2} .
> $$
>
> At $z = 1$, $q = 0$ and $\operatorname{Log}1 = 0$; at $z = -1$, $q = 0$ and $\operatorname{Log}(-1) = \pi i$. The requirements $w(1) = 0$ and $w(-1) = hi$ give $A = h/\pi$ and no additive constant:
>
> $$
> w = \frac h\pi\Big\{(z + 1)^{1/2}(z - 1)^{1/2} + \operatorname{Log}\big[z + (z + 1)^{1/2}(z - 1)^{1/2}\big]\Big\} .
> $$
>
> *Boundary check.* For $x > 1$ everything is real and positive, increasing: the positive $u$ axis. For $-1 < x < 1$, $q = i\sqrt{1 - x^2}$, $z + q = e^{i\cos^{-1}x}$, and $w = \frac{hi}\pi\big(\sqrt{1 - x^2} + \cos^{-1}x\big)$, which decreases from $hi$ to $0$ (its derivative in $x$ is $-\frac{h}{\pi}\sqrt{(1 + x)/(1 - x)}\,i$). For $x < -1$, $q = -\sqrt{x^2 - 1}$ and $z + q < 0$, so $\operatorname{Im} w = \frac h\pi\cdot\pi = h$: the upper bed.
>
> **(b) The velocity.** Far away the bed is the real axis and $w \approx \frac h\pi z$, so a uniform stream of speed $V_0$ in the $w$ plane is the uniform stream $F = \frac{hV_0}{\pi}z$ in the $z$ plane. By the chain rule
>
> $$
> \overline{V(w)} = \frac{dF}{dw} = \frac{dF}{dz}\frac{dz}{dw} = \frac{hV_0}{\pi}\cdot\frac\pi h\Big(\frac{z - 1}{z + 1}\Big)^{1/2} = V_0(z - 1)^{1/2}(z + 1)^{-1/2} ,
> $$
>
> and at the points $z = x$ whose images are on the bed,
>
> $$
> |V| = |V_0|\sqrt{\Big|\frac{x - 1}{x + 1}\Big|} .
> $$
>
> So the speed increases from $|V_0|$ along $A'B'$ ($x < -1$) to $\infty$ at the corner $B'$, diminishes to $0$ at $C'$ ($x = 1$, a stagnation point in the inner corner), and increases toward $|V_0|$ from $C'$ to $D'$. On the riser it equals $|V_0|$ where $|x - 1| = |x + 1|$, that is, at $x = 0$, whose image is
>
> $$
> w = \frac{hi}{\pi}\Big(1 + \frac\pi2\Big) = i\Big(\frac12 + \frac1\pi\Big)h .
> $$
>
> *B&C: Sec. 133, Exercises 3 and 5*

^ex-132-4
