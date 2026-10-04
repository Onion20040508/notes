---
type: section
subject: "[[Complex Variables]]"
chapter: 12
section: 137
bc: "137"
aliases: ["B&C 137"]
tags: [complex-variables, math342, extension]
---
← [[§136★ Examples (Dirichlet Problem for a Disk)]] · ↑ [[· 12★ Integral Formulas of the Poisson Type]] · [[§138★ Schwarz Integral Formula]] →

*Brown–Churchill, Section 137.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Symmetry and inversion extend the disk formula to three more regions. If the boundary values are extended oddly across the horizontal diameter, the Poisson integral vanishes on the diameter, which solves the Dirichlet problem for a half disk; an even extension makes the normal derivative vanish there instead (an insulated or flow-free diameter). The map $z = r_0^2/Z$, followed by the reflection $\theta \mapsto -\theta$, carries the disk to the exterior of the circle and turns the Poisson integral into the solution of the exterior Dirichlet problem, whose value at infinity is the mean of the boundary values. B&C leaves the details to exercises; they are written out here, for piecewise continuous boundary functions $F$.

## Half Disks

> [!theorem] Proposition §137.1: Half Disk, Zero Values on the Diameter
> Let $F$ be piecewise continuous on $0 \le \theta \le \pi$, and extend it to $\pi < \theta < 2\pi$ by $F(2\pi - \theta) = -F(\theta)$. Then the Poisson integral transform (1) of [[§135★ Dirichlet Problem for a Disk#^def-135-1|§135★]] becomes
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^\pi\big[P(r_0, r, \phi - \theta) - P(r_0, r, \phi + \theta)\big]F(\phi)\,d\phi . \qquad (1)
> $$
>
> This function is harmonic in the semicircular region $r < r_0$, $0 < \theta < \pi$, it is zero on the diameter $AB$ ($\theta = 0$ and $\theta = \pi$), and
>
> $$
> \lim_{\substack{r\to r_0\\ r < r_0}}U(r, \theta) = F(\theta) \qquad (0 < \theta < \pi) \qquad (2)
> $$
>
> for each fixed $\theta$ at which $F$ is continuous.
>
> *B&C: Sec. 137, equations (1)–(2); Exercise 2*

^prop-137-1

> [!proof]+ Proof
> Split the integral in (1) of §135 at $\phi = \pi$, and in the part over $\pi < \phi < 2\pi$ substitute $\phi = 2\pi - \phi'$:
>
> $$
> \frac{1}{2\pi}\int_\pi^{2\pi}P(r_0, r, \phi - \theta)F(\phi)\,d\phi = \frac{1}{2\pi}\int_0^{\pi}P(r_0, r, 2\pi - \phi' - \theta)F(2\pi - \phi')\,d\phi' = -\frac{1}{2\pi}\int_0^\pi P(r_0, r, \phi' + \theta)F(\phi')\,d\phi' ,
> $$
>
> since $P$ is even and $2\pi$-periodic in its last argument ([[§134★ Poisson Integral Formula#^prop-134-2|Proposition §134.2]](d)), so $P(r_0, r, 2\pi - \phi' - \theta) = P(r_0, r, \phi' + \theta)$, and $F(2\pi - \phi') = -F(\phi')$. Adding the part over $0 < \phi < \pi$ gives (1).
>
> The extended $F$ is piecewise continuous on $[0, 2\pi]$, so by [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]] $U$ is harmonic in the whole disk, in particular in the half disk, and (2) holds at each $\theta \in (0, \pi)$ where $F$ is continuous. On the diameter: at $\theta = 0$ the bracket in (1) is $P(\phi) - P(\phi) = 0$; at $\theta = \pi$ it is $P(r_0, r, \phi - \pi) - P(r_0, r, \phi + \pi) = 0$ by periodicity. So $U = 0$ at every point of the diameter inside the circle, as one expects of a steady temperature with an odd distribution of boundary values.

^pf-137-1

*Uses:* [[§135★ Dirichlet Problem for a Disk#^def-135-1|Def. §135.1]], [[§135★ Dirichlet Problem for a Disk#^thm-135-1|§135.1]], [[§134★ Poisson Integral Formula#^prop-134-2|§134.2]]

> [!theorem] Proposition §137.2: Half Disk, Zero Normal Derivative on the Diameter
> If instead $F$ is extended by $F(2\pi - \theta) = F(\theta)$, then
>
> $$
> U(r, \theta) = \frac{1}{2\pi}\int_0^\pi\big[P(r_0, r, \phi - \theta) + P(r_0, r, \phi + \theta)\big]F(\phi)\,d\phi , \qquad (3)
> $$
>
> and $U_\theta(r, \theta) = 0$ when $\theta = 0$ or $\theta = \pi$. So (3) is harmonic in the semicircular region $r < r_0$, $0 < \theta < \pi$, satisfies condition (2), and has normal derivative zero on the diameter $AB$.
>
> *B&C: Sec. 137, equation (3); Exercise 3*

^prop-137-2

> [!proof]+ Proof
> The same substitution as in Proposition §137.1, now with $F(2\pi - \phi') = +F(\phi')$, gives (3); harmonicity and (2) again follow from [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]], which makes $U$ harmonic in the whole disk $r < r_0$, so $U_\theta$ exists there.
>
> *$U$ is even in $\theta$.* (B&C asserts $U_\theta = 0$ on the diameter; here is why.) In (1) of §135, substitute $\phi = 2\pi - \phi'$ and use the evenness and periodicity of $P$ and $F(2\pi - \phi') = F(\phi')$:
>
> $$
> U(r, -\theta) = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, \phi + \theta)F(\phi)\,d\phi = \frac{1}{2\pi}\int_0^{2\pi}P(r_0, r, 2\pi - \phi' + \theta)F(\phi')\,d\phi' = U(r, \theta) .
> $$
>
> With the $2\pi$-periodicity of $U$ in $\theta$ this also gives $U(r, \pi + t) = U(r, -\pi - t) = U(r, \pi - t)$. A differentiable function that is even about a point has derivative zero there, so $U_\theta(r, 0) = U_\theta(r, \pi) = 0$. On the diameter the normal direction is the direction of increasing $\theta$, and the normal derivative is $\frac1rU_\theta = 0$.

^pf-137-2

*Uses:* [[§135★ Dirichlet Problem for a Disk#^thm-135-1|§135.1]], [[§134★ Poisson Integral Formula#^prop-134-2|§134.2]]

## The Exterior of a Circle

> [!theorem] Lemma §137.3: Reflection Preserves Harmonicity
> If $u(r, \theta)$ is harmonic in a domain, then $u(r, -\theta)$ is harmonic in the reflected domain.
>
> *B&C: Sec. 137 (text); Exercise 4*

^lem-137-3

> [!proof]+ Proof
> Let $w(r, \theta) = u(r, -\theta)$. Then $w_r = u_r$, $w_{rr} = u_{rr}$ and $w_{\theta\theta} = u_{\theta\theta}$, all evaluated at $(r, -\theta)$, so the polar form of Laplace's equation ([[§27★ Harmonic Functions|§27★]], Exercise 1)
>
> $$
> r^2w_{rr}(r, \theta) + rw_r(r, \theta) + w_{\theta\theta}(r, \theta) = \big[r^2u_{rr} + ru_r + u_{\theta\theta}\big](r, -\theta) = 0
> $$
>
> holds. (In rectangular coordinates this is the reflection $u(x, -y)$.)

^pf-137-3

*Uses:* [[§27★ Harmonic Functions|§27★]]

> [!theorem] Theorem §137.4: Dirichlet Problem for the Exterior of a Circle
> Write $Z = Re^{i\psi}$. The function
>
> $$
> H(R, \psi) = -\frac{1}{2\pi}\int_0^{2\pi}P(r_0, R, \phi - \psi)\,F(\phi)\,d\phi \qquad (R > r_0) \qquad (4)
> $$
>
> is harmonic in the domain $R > r_0$, and for each fixed $\psi$ at which $F$ is continuous,
>
> $$
> \lim_{\substack{R\to r_0\\ R > r_0}}H(R, \psi) = F(\psi) . \qquad (5)
> $$
>
> Thus (4) solves the Dirichlet problem for the region exterior to the circle $R = r_0$. The kernel $P(r_0, R, \phi - \psi)$ is negative when $R > r_0$, and
>
> $$
> \frac{1}{2\pi}\int_0^{2\pi}P(r_0, R, \phi - \psi)\,d\phi = -1 \qquad (R > r_0) , \qquad (6)
> $$
>
> $$
> \lim_{R\to\infty}H(R, \psi) = \frac{1}{2\pi}\int_0^{2\pi}F(\phi)\,d\phi . \qquad (7)
> $$
>
> *B&C: Sec. 137, equations (4)–(7); Exercises 4–6*

^thm-137-4

> [!proof]+ Proof
> **Harmonic.** The analytic function $z = r_0^2/Z$ maps the circle $|Z| = r_0$ onto the circle $|z| = r_0$ and the exterior of the first onto the interior of the second, punctured at $0$ ([[§97★ The Transformation w = 1∕z#^prop-97-1|Proposition §97.1]]). With $z = re^{i\theta}$, $r = r_0^2/R$ and $\theta = 2\pi - \psi$. The harmonic function $U(r, \theta)$ of (1), §135, is transformed into a function harmonic in $R > r_0$ ([[§116★ Transformations of Harmonic Functions#^thm-116-1|Theorem §116.1]]):
>
> $$
> U\Big(\frac{r_0^2}{R}, 2\pi - \psi\Big) = -\frac{1}{2\pi}\int_0^{2\pi}\frac{r_0^2 - R^2}{r_0^2 - 2r_0R\cos(\phi + \psi) + R^2}F(\phi)\,d\phi .
> $$
>
> (Here is the computation. With $r = r_0^2/R$, $r_0^2 - r^2 = \frac{r_0^2}{R^2}(R^2 - r_0^2)$ and $r_0^2 - 2r_0r\cos(\phi - \theta) + r^2 = \frac{r_0^2}{R^2}\big(R^2 - 2r_0R\cos(\phi - \theta) + r_0^2\big)$; the factors $r_0^2/R^2$ cancel, and $\cos(\phi - 2\pi + \psi) = \cos(\phi + \psi)$.) By Lemma §137.3 we may replace $\psi$ by $-\psi$; by periodicity in $\theta$ this gives
>
> $$
> H(R, \psi) = U\Big(\frac{r_0^2}{R}, \psi - 2\pi\Big) = U\Big(\frac{r_0^2}{R}, \psi\Big) ,
> $$
>
> which is (4), and it is harmonic.
>
> **Boundary values (5).** As $R \to r_0$ with $R > r_0$, $r = r_0^2/R \to r_0$ with $r < r_0$, and $H(R, \psi) = U(r, \psi) \to F(\psi)$ by (2) of [[§135★ Dirichlet Problem for a Disk#^thm-135-1|Theorem §135.1]].
>
> **The kernel and (6).** By (8) of §134, $P(r_0, R, \phi - \psi) = (r_0^2 - R^2)/|s - Z|^2 < 0$ for $R > r_0$. Interchanging the roles of the radii in (7) of §134 shows $P(r_0, R, \cdot) = -P(R, r_0, \cdot)$, and since $r_0 < R$, property (f) of [[§134★ Poisson Integral Formula#^prop-134-2|Proposition §134.2]] (for the circle of radius $R$) gives $\frac{1}{2\pi}\int_0^{2\pi}P(R, r_0, \phi - \psi)\,d\phi = 1$. This is (6).
>
> **The limit (7).** For $R > r_0$,
>
> $$
> \big|P(r_0, R, \phi - \psi) + 1\big| = \frac{|2r_0^2 - 2r_0R\cos(\phi - \psi)|}{r_0^2 - 2r_0R\cos(\phi - \psi) + R^2} \le \frac{2r_0^2 + 2r_0R}{(R - r_0)^2} \longrightarrow 0 \qquad (R \to \infty) ,
> $$
>
> uniformly in $\phi$. Since $F$ is bounded, $H(R, \psi) - \frac{1}{2\pi}\int_0^{2\pi}F = -\frac{1}{2\pi}\int_0^{2\pi}\big(P + 1\big)F\,d\phi \to 0$.

^pf-137-4

*Uses:* [[§135★ Dirichlet Problem for a Disk#^thm-135-1|§135.1]], [[§134★ Poisson Integral Formula#^prop-134-2|§134.2]], [[§137★ Related Boundary Value Problems#^lem-137-3|§137.3]], [[§97★ The Transformation w = 1∕z#^prop-97-1|§97.1]], [[§116★ Transformations of Harmonic Functions#^thm-116-1|§116.1]]

## Examples

> [!example] Example §137.1: A Semicircular Plate
> Find the steady temperatures in the half disk $r < 1$, $0 < \theta < \pi$ when the semicircular edge is kept at $1$ and the diameter at $0$.
>
> By Proposition §137.1 extend $F = 1$ on $(0, \pi)$ oddly: $F = -1$ on $(\pi, 2\pi)$. Then $F = 1 - 2G$, where $G = 1$ on $(\pi, 2\pi)$ and $0$ on $(0, \pi)$ is the boundary function of [[§136★ Examples (Dirichlet Problem for a Disk)#^ex-136-1|Example §136.1]]. The Poisson transform is linear and transforms the constant $1$ into $1$ (property (f)), so
>
> $$
> U = 1 - 2V = 1 - \frac2\pi\arctan\Big(\frac{1 - r^2}{2r\sin\theta}\Big) .
> $$
>
> For $0 < \theta < \pi$ the argument of the arctangent is positive, the arctangent lies in $(0, \pi/2)$, and $\frac\pi2 - \arctan t = \arctan(1/t)$ gives
>
> $$
> U(r, \theta) = \frac2\pi\arctan\Big(\frac{2r\sin\theta}{1 - r^2}\Big) = \frac2\pi\arctan\frac{2y}{1 - x^2 - y^2} .
> $$
>
> *Check:* $U = 0$ for $y = 0$; $U \to \frac2\pi\cdot\frac\pi2 = 1$ as $r \to 1$ with $\sin\theta > 0$. At $r = 0.5$, $\theta = 1.2$, quadrature of (1) and the formula both give $0.568631$.
>
> *B&C: Sec. 137, equation (1)*

^ex-137-1

> [!example] Example §137.2: The Exterior Problem with Boundary Values cos ψ
> Find the function harmonic in $R > r_0$ with $H \to \cos\psi$ on the circle and $H$ bounded at infinity.
>
> Inside the circle the solution with these boundary values is $U = \frac{r}{r_0}\cos\theta$ ([[§136★ Examples (Dirichlet Problem for a Disk)#^ex-136-2|Example §136.2]] with $A = 1$). By the proof of Theorem §137.4, $H(R, \psi) = U(r_0^2/R, \psi)$, so
>
> $$
> H(R, \psi) = \frac{r_0}{R}\cos\psi = \frac{r_0X}{X^2 + Y^2} = r_0\operatorname{Re}\frac1Z .
> $$
>
> It is harmonic for $Z \ne 0$, equals $\cos\psi$ at $R = r_0$, and tends to $0$, the mean of $\cos\psi$, as $R \to \infty$, in agreement with (7). Quadrature of (4) with $r_0 = 1$, $R = 3$, $\psi = 0.4$ gives $0.307020 = \frac13\cos0.4$; and the mean of the kernel at these values is $-1.000000$, as (6) says.
>
> *B&C: Sec. 137, equations (4)–(7)*

^ex-137-2

> [!example] Example §137.3: The Exterior of a Half Disk
> Let $H(R, \psi)$ be harmonic in the unbounded region $R > r_0$, $0 < \psi < \pi$ (the upper half plane outside the semicircle), with $\lim_{R\to r_0^+}H(R, \psi) = F(\psi)$ on the semicircle. Show that
>
> **(a)** if $H = 0$ on the rays $BA$ and $DE$ (the real axis outside the circle),
>
> $$
> H(R, \psi) = \frac{1}{2\pi}\int_0^\pi\big[P(r_0, R, \phi + \psi) - P(r_0, R, \phi - \psi)\big]F(\phi)\,d\phi ;
> $$
>
> **(b)** if the normal derivative of $H$ is zero on those rays,
>
> $$
> H(R, \psi) = -\frac{1}{2\pi}\int_0^\pi\big[P(r_0, R, \phi + \psi) + P(r_0, R, \phi - \psi)\big]F(\phi)\,d\phi .
> $$
>
> In (4) extend $F$ oddly for (a), $F(2\pi - \phi) = -F(\phi)$, or evenly for (b), and substitute $\phi = 2\pi - \phi'$ in the part of the integral over $(\pi, 2\pi)$, exactly as in Proposition §137.1: the evenness and periodicity of $P(r_0, R, \cdot)$ turn $P(r_0, R, 2\pi - \phi' - \psi)$ into $P(r_0, R, \phi' + \psi)$. With the overall minus sign of (4), the odd extension gives (a) and the even one gives (b). In (a) the bracket vanishes at $\psi = 0$ and $\psi = \pi$; in (b) its $\psi$-derivative does, as in Proposition §137.2. Harmonicity and the boundary limit on the semicircle come from Theorem §137.4.
>
> *B&C: Sec. 137, Exercise 1*

^ex-137-3
