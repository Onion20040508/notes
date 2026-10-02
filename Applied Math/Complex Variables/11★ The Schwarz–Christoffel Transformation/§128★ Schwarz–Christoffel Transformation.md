---
type: section
subject: "[[Complex Variables]]"
chapter: 11
section: 128
bc: "128"
aliases: ["B&C 128"]
tags: [complex-variables, math342, extension]
---
← [[§127★ Mapping the Real Axis onto a Polygon]] · ↑ [[· 11★ The Schwarz–Christoffel Transformation]] · [[§129★ Triangles and Rectangles]] →

*Brown–Churchill, Section 128.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section turns the derivative of [[§127★ Mapping the Real Axis onto a Polygon|§127★]] into a mapping function. With suitable branches the derivative is analytic in the closed upper half plane except at the points $x_j$, so it has an antiderivative there; that antiderivative stays continuous at the $x_j$ because the singularities $(z - x_j)^{-k_j}$ are integrable ($k_j < 1$), and it has a limit at infinity because $|f'(z)|$ decays like $|z|^{-(2 - k_n)}$. The result is the Schwarz–Christoffel transformation, and the argument principle shows that it maps the upper half plane one to one onto the inside of the polygon. B&C leaves three steps as exercises; they are proved here, since the theorem rests on them.

## Branches and the Integral

> [!definition] Definition §128.1: Branches of the Factors
> For $j = 1, 2, \ldots, n - 1$ the factor $(z - x_j)^{-k_j}$ in
>
> $$
> f'(z) = A(z - x_1)^{-k_1}(z - x_2)^{-k_2}\cdots(z - x_{n-1})^{-k_{n-1}} \qquad (1)
> $$
>
> denotes the branch of the power function with branch cut extending below the $x$ axis:
>
> $$
> (z - x_j)^{-k_j} = \exp\big[-k_j\log(z - x_j)\big] = |z - x_j|^{-k_j}\exp(-ik_j\theta_j) \qquad \Big(-\frac\pi2 < \theta_j < \frac{3\pi}{2}\Big) , \qquad (2)
> $$
>
> where $\theta_j = \arg(z - x_j)$. On the real axis, $\theta_j = 0$ for $x > x_j$ and $\theta_j = \pi$ for $x < x_j$. With these branches $f'$ is analytic everywhere in the half plane $y \ge 0$ except at the $n - 1$ branch points $x_j$; this region of analyticity is denoted $R$.
>
> *B&C: Sec. 128, equation (2)*

^def-128-1

More precisely, $f'$ is analytic in the domain $D$ obtained from the plane by removing the $n - 1$ closed rays $\{x_j - it : t \ge 0\}$, and $D \supseteq R$. The domain $D$ is simply connected (the removed rays all run off to infinity, so $D$ has no holes), so $f'$ has an antiderivative there ([[§52 Simply Connected Domains|§52]], [[§48 Antiderivatives|§48]]): if $z_0$ is a point of $R$, the function

$$
F(z) = \int_{z_0}^{z} f'(s)\,ds \qquad (3)
$$

is single valued and analytic throughout $R$, the path being any contour from $z_0$ to $z$ in $R$, and $F'(z) = f'(z)$.

> [!theorem] Lemma §128.1: Continuity at the Branch Points
> $F$ can be defined at each $x_j$ so that it is continuous there, as $z \to x_j$ from within $y \ge 0$. Thus $F$ is continuous throughout the region $y \ge 0$.
>
> *B&C: Sec. 128 (text)*

^lem-128-1

> [!proof]+ Proof
> Take $j = 1$; the other points are treated in the same way. The factor $(z - x_1)^{-k_1}$ is the only factor in (1) that is not analytic at $x_1$. Let $\phi(z)$ denote the product of the remaining factors. Then $\phi$ is analytic at $x_1$ and is represented throughout an open disk $|z - x_1| < R_1$ by its Taylor series about $x_1$ ([[§62 Taylor Series|§62]], Taylor's theorem), so
>
> $$
> f'(z) = (z - x_1)^{-k_1}\phi(z) = (z - x_1)^{-k_1}\Big[\phi(x_1) + \frac{\phi'(x_1)}{1!}(z - x_1) + \frac{\phi''(x_1)}{2!}(z - x_1)^2 + \cdots\Big] ,
> $$
>
> or
>
> $$
> f'(z) = \phi(x_1)(z - x_1)^{-k_1} + (z - x_1)^{1 - k_1}\psi(z) , \qquad (4)
> $$
>
> where $\psi(z) = \big(\phi(z) - \phi(x_1)\big)/(z - x_1)$ is analytic, and therefore continuous, throughout the open disk. Let $H$ be the closed upper half disk $|z - x_1| \le R_1/2$, $\operatorname{Im} z \ge 0$, and fix $Z_1$ in $H$, $Z_1 \ne x_1$.
>
> **The first term.** On $H \setminus \{x_1\}$ the function $\frac{1}{1 - k_1}(z - x_1)^{1 - k_1}$ (same branch) has derivative $(z - x_1)^{-k_1}$, so
>
> $$
> \int_{Z_1}^{z}(s - x_1)^{-k_1}\,ds = \frac{1}{1 - k_1}\Big[(z - x_1)^{1 - k_1} - (Z_1 - x_1)^{1 - k_1}\Big] .
> $$
>
> Since $1 - k_1 > 0$, $|(z - x_1)^{1 - k_1}| = |z - x_1|^{1 - k_1} \to 0$ as $z \to x_1$. So this integral has a limit as $z \to x_1$ in $H$, and it is continuous at $x_1$ if its value there is defined as that limit.
>
> **The second term.** Since $1 - k_1 > 0$, the function $g(z) = (z - x_1)^{1 - k_1}\psi(z)$ is continuous on $H$ if it is given the value $0$ at $x_1$; let $K$ bound $|g|$ on $H$. Let $G(z) = \int_{Z_1}^z g(s)\,ds$ for $z \in H \setminus \{x_1\}$ (path independent, since $g$ is analytic in the disk $|z - x_1| < R_1$ cut along the downward ray from $x_1$, a simply connected domain containing $H \setminus \{x_1\}$). (B&C asserts that $G$ is continuous at $x_1$; here is why.) For $z$, $z'$ in $H \setminus \{x_1\}$ and small $\eta > 0$, integrate along the two segments from $z'$ to $p = x_1 + i\eta$ and from $p$ to $z$; they lie in $H$ and miss $x_1$. By the ML-inequality, $|G(z) - G(z')| \le K\big(|z - x_1| + |z' - x_1| + 2\eta\big)$, and $\eta$ is arbitrary. So $G$ satisfies the Cauchy criterion as $z \to x_1$ and has a limit there.
>
> The integral of (4) from $Z_1$ to $z$ is therefore continuous at $z = x_1$; and so is (3), since it equals the integral along a contour in $R$ from $z_0$ to $Z_1$ plus the integral from $Z_1$ to $z$.

^pf-128-1

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^def-128-1|Def. §128.1]], [[§62 Taylor Series|§62]] (Taylor's theorem), [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (ML-inequality), [[§48 Antiderivatives|§48]]

> [!theorem] Lemma §128.2: Order Property at Infinity
> Let the $k_j$ satisfy conditions (5) of [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-3|Proposition §127.3]]. For a sufficiently large positive number $R$ there is a positive constant $M$ such that, if $\operatorname{Im} z \ge 0$,
>
> $$
> |f'(z)| < \frac{M}{|z|^{2 - k_n}} \qquad\text{whenever}\qquad |z| > R . \qquad (5)
> $$
>
> *B&C: Sec. 128, equation (5) and Exercise 1*

^lem-128-2

> [!proof]+ Proof
> Let $R$ be larger than $2|x_j|$ for every $j$. If $|z| > R$, then $|z - x_j| \ge |z| - |x_j| > |z|/2$ and $|z - x_j| \le |z| + |x_j| < 2|z|$, so
>
> $$
> \frac{|z|}{2} < |z - x_j| < 2|z| \qquad (j = 1, \ldots, n - 1) .
> $$
>
> If $k_j \ge 0$, then $|z - x_j|^{-k_j} < (|z|/2)^{-k_j} = 2^{k_j}|z|^{-k_j}$; if $k_j < 0$, then $|z - x_j|^{-k_j} = |z - x_j|^{|k_j|} < (2|z|)^{|k_j|} = 2^{|k_j|}|z|^{-k_j}$. In either case $|z - x_j|^{-k_j} < 2^{|k_j|}|z|^{-k_j}$. Multiplying, by (1),
>
> $$
> |f'(z)| = |A|\prod_{j=1}^{n-1}|z - x_j|^{-k_j} < |A|\,2^{|k_1| + \cdots + |k_{n-1}|}\,|z|^{-(k_1 + \cdots + k_{n-1})} = \frac{M}{|z|^{2 - k_n}} ,
> $$
>
> with $M = |A|\,2^{|k_1| + \cdots + |k_{n-1}|}$, because $k_1 + \cdots + k_{n-1} = 2 - k_n$ by (5) of §127.

^pf-128-2

*Uses:* [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-3|§127.3]]

> [!theorem] Lemma §128.3: The Limit at Infinity
> There is a number $W_n$ such that
>
> $$
> \lim_{z\to\infty}F(z) = W_n \qquad (\operatorname{Im} z \ge 0) . \qquad (6)
> $$
>
> *B&C: Sec. 128, equation (6) and Exercise 2*

^lem-128-3

> [!proof]+ Proof
> Write $p = 2 - k_n$; since $k_n < 1$, $p > 1$. Let $R$, $M$ be as in Lemma §128.2, and let $\rho > R$.
>
> **Along the real axis.** For $x > \rho$, $F(x) = F(\rho) + \int_\rho^x f'(t)\,dt$. Since $|f'(t)| < M t^{-p}$ and $\int_\rho^\infty t^{-p}\,dt < \infty$ ($p > 1$), the real and imaginary parts of $f'$ are absolutely integrable on $[\rho, \infty)$, so $F(x)$ has a limit $W^+$ as $x \to +\infty$ (sufficient condition for the existence of an improper integral, as B&C suggests). In the same way $F(x) \to W^-$ as $x \to -\infty$.
>
> **Along arcs.** For $0 \le \theta \le \pi$, the integral of $f'$ over the arc of the circle $|z| = \rho$ from $\rho$ to $\rho e^{i\theta}$ has modulus at most
>
> $$
> \frac{M}{\rho^p}\cdot\pi\rho = \frac{\pi M}{\rho^{p - 1}} \longrightarrow 0 \qquad (\rho \to \infty) ,
> $$
>
> by the ML-inequality, uniformly in $\theta$. With $\theta = \pi$ this gives $|F(-\rho) - F(\rho)| \le \pi M\rho^{1 - p} \to 0$, so $W^- = W^+$; call it $W_n$.
>
> **Conclusion.** For $z = \rho e^{i\theta}$ with $0 \le \theta \le \pi$,
>
> $$
> |F(z) - W_n| \le |F(z) - F(\rho)| + |F(\rho) - W_n| \le \frac{\pi M}{\rho^{p - 1}} + |F(\rho) - W_n| ,
> $$
>
> and both terms tend to $0$ as $\rho = |z| \to \infty$, independently of $\theta$. This is (6).

^pf-128-3

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^lem-128-2|§128.2]], [[§47 Upper Bounds for Moduli of Contour Integrals|§47]] (ML-inequality), [[§36 Improper Integrals#^thm-36-1|451 Thm. §36.1]] (convergence of improper integrals of nonnegative functions)

## The Transformation

Our mapping function, whose derivative is (1), can be written $f(z) = F(z) + B$, where $B$ is a complex constant.

> [!theorem] Theorem §128.4: Schwarz–Christoffel Transformation
> Let $k_1, \ldots, k_n$ satisfy (5) of [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-3|Proposition §127.3]], let $x_1 < x_2 < \cdots < x_{n-1}$, let $A \ne 0$ and $B$ be complex constants, and let $z_0$ be a point of $R$. The **Schwarz–Christoffel transformation**
>
> $$
> w = A\int_{z_0}^{z}(s - x_1)^{-k_1}(s - x_2)^{-k_2}\cdots(s - x_{n-1})^{-k_{n-1}}\,ds + B , \qquad (7)
> $$
>
> with the branches of Definition §128.1, has these properties.
>
> **(a)** It is continuous throughout the half plane $y \ge 0$, and conformal there except at the points $x_j$. The image of $z = \infty$ exists: $w_n = W_n + B$.
>
> **(b)** As $z$ describes the $x$ axis in the positive direction, $w$ describes a closed polygon $P$ with vertices $w_j = f(x_j)$ and $w_n$ and exterior angles $k_j\pi$, each side traced once.
>
> **(c)** If the constants $x_j$ and $k_j$ are such that the sides of $P$ do not cross, so that $P$ is a simple closed contour, then $P$ is positively oriented, the axis (with $\infty$) corresponds one to one to the points of $P$, and the open half plane $y > 0$ is mapped one to one onto the interior of $P$.
>
> *B&C: Sec. 128, equation (7) and text; Exercise 3*

^thm-128-4

> [!proof]- Proof
> **(a)** By Lemmas §128.1 and §128.3, $f = F + B$ is continuous on $y \ge 0$ and has the limit $W_n + B$ at infinity. Away from the $x_j$, $f$ is analytic and $f'(z) \ne 0$, since each factor of (1) is a nonzero exponential; so $f$ is conformal there ([[§112★ Preservation of Angles and Scale Factors|§112★]]).
>
> **(b)** By [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-2|Proposition §127.2]], $\arg f'(x)$ is constant on each interval between consecutive points of $x_1, \ldots, x_{n-1}$ (and on $x < x_1$, $x > x_{n-1}$). By [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-1|Proposition §127.1]] each finite interval is mapped onto a segment, traced once in a fixed direction; for the two infinite intervals apply it on $[x_{n-1}, X]$ and $[-X, x_1]$ and let $X \to \infty$, using the continuity of $f$ at $\infty$. At $w_j$ the direction turns by $k_j\pi$, and since the turns add up to $2\pi$ by (5) of §127 the path closes up at $w_n$ with the turn $k_n\pi$. So $P$ is a closed polygon with these exterior angles.
>
> **(c)** *Orientation and the boundary.* The total turning of the direction along $P$ is $+2\pi$, so a simple $P$ is described counterclockwise. Each side is traced once and the sides of a simple polygon meet only at consecutive vertices, so distinct points of the axis (or $\infty$) have distinct images on $P$.
>
> *The interior: counting solutions.* (B&C argues that the images of interior points lie to the left of the sides, since the angle at $x_0$ between the axis and a segment into the half plane is between $0$ and $\pi$ and is preserved; the one-to-one property is its Exercise 3, carried out here.) Let $w_0$ be a point not on $P$ and $d > 0$ its distance from $P$. Let $C$ be the contour consisting of the upper half of the circle $|z| = R$ and the segment $-R \le x \le R$ of the axis, except that a small segment about each $x_j$ is replaced by the upper half of the circle $|z - x_j| = \rho_j$ (figure below). $C$ is a positively oriented simple closed contour in the simply connected domain $D$, where $f$ is analytic with $f' \ne 0$. For $R$ large and the $\rho_j$ small, $f(z) \ne w_0$ on $C$: on the axis $f(x) \in P$; near $x_j$, $|f(z) - w_0| \ge d/2$ by continuity, since $f(x_j) = w_j$ is at distance $\ge d$ from $w_0$; and for $|z|$ large $|f(z) - w_0| \ge d/2$ by (6), since $w_n \in P$. By the argument principle ([[§93 Argument Principle|§93]]), the number of points interior to $C$ with $f(z) = w_0$ is
>
> $$
> N_C = \frac{1}{2\pi i}\int_C\frac{f'(z)}{f(z) - w_0}\,dz .
> $$
>
> *The small semicircles.* Near $x_j$, $f'(z) = (z - x_j)^{-k_j}\phi_j(z)$ with $\phi_j$ bounded, so $|f'(z)| \le K|z - x_j|^{-k_j}$, and the integral over the semicircle of radius $\rho_j$ is at most $\frac{2K}{d}\rho_j^{-k_j}\cdot\pi\rho_j = \frac{2\pi K}{d}\rho_j^{1 - k_j} \to 0$ as $\rho_j \to 0$, because $k_j < 1$.
>
> *The large semicircle.* By (5), its integral is at most $\frac{2}{d}\cdot\frac{M}{R^{2 - k_n}}\cdot\pi R = \frac{2\pi M}{d}R^{k_n - 1} \to 0$ as $R \to \infty$, because $k_n < 1$.
>
> *The axis.* What remains is the integral over the segments of the axis, which tends to the improper integral of $f'(x)/(f(x) - w_0)$ over the whole axis (it converges, by the two estimates just made). Along each side of $P$ the substitution $w = f(x)$, $dw = f'(x)\,dx$, is allowed, and the sides are traced once in order, so
>
> $$
> \lim\frac{1}{2\pi i}\int_{-R}^{R}\frac{f'(x)}{f(x) - w_0}\,dx = \frac{1}{2\pi i}\int_P\frac{dw}{w - w_0} .
> $$
>
> If $w_0$ is exterior to $P$, $1/(w - w_0)$ is analytic on and inside $P$ and the integral is $0$ by the Cauchy–Goursat theorem ([[§50 Cauchy–Goursat Theorem|§50]]). If $w_0$ is interior, the integral equals the integral over a small positively oriented circle about $w_0$ ([[§53 Multiply Connected Domains|§53]]), which is $2\pi i$. So the limit is $N = 1$ or $N = 0$.
>
> The count $N_C$ is a nonnegative integer that can only increase as $R$ grows and the $\rho_j$ shrink, and every point of the open half plane lies inside $C$ once $R$ is large and the $\rho_j$ are small. Hence the number of points $z$ with $\operatorname{Im} z > 0$ and $f(z) = w_0$ is exactly $1$ if $w_0$ is interior to $P$ and $0$ if it is exterior.
>
> *No interior point goes to $P$.* (B&C does not treat this.) If $f(z_1) = w_1 \in P$ with $\operatorname{Im} z_1 > 0$, then, since $f'(z_1) \ne 0$, $f$ maps a neighborhood of $z_1$ in the half plane onto a neighborhood of $w_1$ ([[§114★ Local Inverses|§114★]]). Every neighborhood of a point of $P$ contains points exterior to $P$, and these would have preimages in $y > 0$, contradicting $N = 0$. So $f$ maps $y > 0$ one to one onto the interior of $P$.

^pf-128-4

*Uses:* [[§128★ Schwarz–Christoffel Transformation#^lem-128-1|§128.1]], [[§128★ Schwarz–Christoffel Transformation#^lem-128-2|§128.2]], [[§128★ Schwarz–Christoffel Transformation#^lem-128-3|§128.3]], [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-1|§127.1]], [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-2|§127.2]], [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-3|§127.3]], [[§93 Argument Principle|§93]] (argument principle), [[§50 Cauchy–Goursat Theorem|§50]] (Cauchy–Goursat), [[§53 Multiply Connected Domains|§53]] (deformation of paths), [[§114★ Local Inverses|§114★]], [[§112★ Preservation of Angles and Scale Factors|§112★]]

![[m342-128-1.svg]]
*The contour $C$ of the proof: the segment $-R \le x \le R$ (blue), indented by small semicircles of radius $\rho_j$ over the prevertices $x_j$ (red), and closed by the semicircle $|z| = R$ (green). The red and green pieces contribute nothing in the limit, because $k_j < 1$ and $k_n < 1$; what is left is the integral of $dw/(w - w_0)$ once around the polygon.*

Given a specific polygon $P$, how many constants in (7) must be determined? Write $z_0 = 0$, $A = 1$, $B = 0$ and require only that the $x$ axis be mapped onto some polygon $P'$ similar to $P$; the size and position of $P'$ are then adjusted by choosing $A$ and $B$.

> [!remark] Remark: Counting the Constants
> The numbers $k_j$ are all determined by the exterior angles of $P$. The $n - 1$ constants $x_j$ remain. The image of the axis is some polygon $P'$ with the same angles as $P$; for $P'$ to be similar to $P$, $n - 2$ connected sides must have a common ratio to the corresponding sides of $P$, which is $n - 3$ equations in the $n - 1$ real unknowns $x_j$. So **two** of the numbers $x_j$, or two relations between them, can be chosen arbitrarily, provided the $n - 3$ equations in the remaining $n - 3$ unknowns have real solutions.

^rem-128-1

> [!theorem] Corollary §128.5: All Prevertices Finite
> When a finite point $z = x_n$ of the $x$ axis, instead of the point at infinity, is to have the vertex $w_n$ as its image, the Schwarz–Christoffel transformation takes the form
>
> $$
> w = A\int_{z_0}^{z}(s - x_1)^{-k_1}(s - x_2)^{-k_2}\cdots(s - x_n)^{-k_n}\,ds + B , \qquad (8)
> $$
>
> where $k_1 + k_2 + \cdots + k_n = 2$, the exponents being determined by the exterior angles. Now there are $n$ real constants $x_j$ subject to the same $n - 3$ equations, so **three** of the numbers $x_j$, or three conditions on them, can be chosen arbitrarily.
>
> *B&C: Sec. 128, equation (8)*

^cor-128-5

> [!proof]+ Proof
> B&C says this "follows from Sec. 127"; here are the details. Apply Proposition §127.2 to the $n$ factors of (8): the argument of the integrand jumps by $k_j\pi$ at $x_j$ for $j = 1, \ldots, n$. For $x > x_n$ it is $\arg A$ and for $x < x_1$ it is $\arg A - (k_1 + \cdots + k_n)\pi = \arg A - 2\pi$, the same direction; so the image of $z = \infty$ is not a vertex ($k_{n+1} = 0$ in (6) of §127). Lemmas §128.1–§128.3 apply with $n + 1$ in place of $n$ and $k_{n+1} = 0$; in particular the integrand is $O(|z|^{-2})$ at infinity, so $F$ has a limit there. The proof of Theorem §128.4 then goes through unchanged, the point at infinity now being an ordinary point of the side through $w_n$ and $w_1$.

^pf-128-5

*Uses:* [[§127★ Mapping the Real Axis onto a Polygon#^prop-127-2|§127.2]], [[§128★ Schwarz–Christoffel Transformation#^lem-128-1|§128.1]], [[§128★ Schwarz–Christoffel Transformation#^lem-128-2|§128.2]], [[§128★ Schwarz–Christoffel Transformation#^lem-128-3|§128.3]], [[§128★ Schwarz–Christoffel Transformation#^thm-128-4|§128.4]]

> [!remark] Remark: Method — Schwarz–Christoffel
> To map the upper half plane onto the inside of a given polygon:
> 1. **Angles.** Read off the exterior angles $k_j\pi$, $k_j = 1 - \theta_j/\pi$, and check $\sum k_j = 2$ ([[§127★ Mapping the Real Axis onto a Polygon#^ex-127-1|Example §127.1]]).
> 2. **Prevertices.** Choose up to three prevertices freely with form (8), or two if a vertex is sent to $\infty$ with form (7). Use symmetry of the polygon (symmetric prevertices for a symmetric polygon) and put $\infty$ where it simplifies the integral.
> 3. **Derivative.** Write $f'(z) = A\prod(z - x_j)^{-k_j}$ with the branches of Definition §128.1; on the axis, $(x - x_j)^{-k_j}$ is $|x - x_j|^{-k_j}$ for $x > x_j$ and $|x - x_j|^{-k_j}e^{-ik_j\pi}$ for $x < x_j$.
> 4. **Integrate.** The integral is elementary only for degenerate polygons ([[§130★ Degenerate Polygons|§130★]]); otherwise it is an elliptic or beta-type integral ([[§129★ Triangles and Rectangles|§129★]]).
> 5. **Constants.** Evaluate $w$ at the prevertices, integrating along the axis interval by interval, and fix $A$, $B$ and any undetermined $x_j$ so that the images are the given vertices.
> 6. **Degenerate polygons.** For vertices at infinity, use the limiting angles formally (a vertex at infinity in a strip has $k = 1$; a reentrant cut has $k = -1$) and verify the resulting map directly.

^rem-128-2

## Examples

> [!example] Example §128.1: Schwarz–Christoffel for the Disk
> The inverse of the linear fractional transformation $Z = \dfrac{i - z}{i + z}$ maps the unit disk $|Z| \le 1$ conformally, except at $Z = -1$, onto the half plane $\operatorname{Im} z \ge 0$. Let $Z_j$ be the points of $|Z| = 1$ whose images are the points $x_j$ ($j = 1, \ldots, n$) of form (8). Show formally that
>
> $$
> \frac{dw}{dZ} = A'(Z - Z_1)^{-k_1}(Z - Z_2)^{-k_2}\cdots(Z - Z_n)^{-k_n} ,
> $$
>
> so that $w = A'\int_0^Z(S - Z_1)^{-k_1}\cdots(S - Z_n)^{-k_n}\,dS + B$ maps the interior of the circle onto the interior of a polygon whose vertices are the images of the $Z_j$.
>
> Solving for $z$: $z = i\dfrac{1 - Z}{1 + Z}$, so $\dfrac{dz}{dZ} = \dfrac{-2i}{(1 + Z)^2}$, and for each $j$
>
> $$
> z - x_j = i\frac{1 - Z}{1 + Z} - i\frac{1 - Z_j}{1 + Z_j} = i\,\frac{(1 - Z)(1 + Z_j) - (1 - Z_j)(1 + Z)}{(1 + Z)(1 + Z_j)} = \frac{2i(Z_j - Z)}{(1 + Z)(1 + Z_j)} .
> $$
>
> Hence, ignoring branches (constants of modulus one are absorbed into the constant), $(z - x_j)^{-k_j} = c_j(Z - Z_j)^{-k_j}(1 + Z)^{k_j}$ with constants $c_j$, and since $\sum k_j = 2$,
>
> $$
> \frac{dw}{dZ} = \frac{dw}{dz}\frac{dz}{dZ} = A\prod_j c_j(Z - Z_j)^{-k_j}\cdot(1 + Z)^{2}\cdot\frac{-2i}{(1 + Z)^2} = A'\prod_j(Z - Z_j)^{-k_j} .
> $$
>
> The factor $(1 + Z)^2$ cancels exactly because the exponents add up to $2$. Integrating from $0$ gives the stated transformation.
>
> *B&C: Sec. 130, Exercise 8*

^ex-128-1

> [!example] Example §128.2: A Regular Polygon
> In Example §128.1 let the $Z_j$ be the $n$th roots of unity, $\omega = \exp(2\pi i/n)$, $Z_1 = 1, Z_2 = \omega, \ldots, Z_n = \omega^{n-1}$, and let every $k_j = 2/n$. Show that
>
> $$
> w = \int_0^Z\frac{dS}{(S^n - 1)^{2/n}}
> $$
>
> maps the unit disk onto a regular polygon of $n$ sides centered at $w = 0$.
>
> **The integrand.** $\prod_j(S - \omega^{j-1}) = S^n - 1$, so the integrand of Example §128.1 is $(S^n - 1)^{-2/n}$ (up to a constant), with exterior angle $2\pi/n$ at each vertex. Following B&C, take the principal $n$th root of $(S^n - 1)^2 = (1 - S^n)^2$. For $|S| < 1$, $1 - S^n$ has positive real part, so $\operatorname{Arg}(1 - S^n)^2 = 2\operatorname{Arg}(1 - S^n)$ lies in $(-\pi, \pi)$ and the root is $\exp\big[\frac2n\operatorname{Log}(1 - S^n)\big]$, analytic in the disk.
>
> **The first vertex.** Along the real axis from $0$ to $1$,
>
> $$
> w_1 = \int_0^1\frac{dt}{(1 - t^n)^{2/n}} = \frac1n\int_0^1 u^{1/n - 1}(1 - u)^{-2/n}\,du = \frac1n B\Big(\frac1n, 1 - \frac2n\Big) > 0 ,
> $$
>
> substituting $u = t^n$.
>
> **The other vertices.** Along the ray $S = t\omega^{k}$, $0 \le t \le 1$, we have $S^n = t^n$ and $dS = \omega^k\,dt$, so the image of $Z_{k+1} = \omega^k$ is $\omega^k w_1$. The vertices $w_1, \omega w_1, \ldots, \omega^{n-1}w_1$ are equally spaced on the circle of radius $w_1$ about $0$, and the angles are equal, so the polygon is regular and centered at $w = 0$. For $n = 5$: $w_1 = \frac15 B(0.2, 0.6) \approx 1.17445$ (a quadrature of the integral gives the same value). For $n = 4$ the image is a square with vertices $\pm w_1$, $\pm iw_1$, $w_1 = \frac14 B\big(\frac14, \frac12\big) \approx 1.31103$.
>
> *B&C: Sec. 130, Exercise 9*

^ex-128-2

> [!example] Example §128.3: The Limit at Infinity for the Square Map
> For $f(z) = i\int_0^z(s + 1)^{-1/2}s^{-1/2}(s - 1)^{-1/2}\,ds$ ([[§127★ Mapping the Real Axis onto a Polygon#^ex-127-2|Example §127.2]]), find the order property (5) and check that $f(z)$ has the same limit along the positive real and the positive imaginary axes, as Lemma §128.3 asserts.
>
> **Order property.** Here $k_4 = \frac12$, so $2 - k_4 = \frac32$, and the proof of Lemma §128.2 gives $|f'(z)| < 2^{3/2}|z|^{-3/2}$ for $|z| > 2$.
>
> **Along the real axis.** By [[§129★ Triangles and Rectangles#^ex-129-5|Example §129.5]], $f(x) \to b + ib$ as $x \to +\infty$, where $b = \frac12 B\big(\frac14, \frac12\big) \approx 2.62206$.
>
> **Along the imaginary axis.** For $s = it$, $t > 0$: $\arg(it + 1) = \tan^{-1}t$ and $\arg(it - 1) = \pi - \tan^{-1}t$, so $(it + 1)^{-1/2}(it - 1)^{-1/2} = (1 + t^2)^{-1/2}e^{-i\pi/2} = -i(1 + t^2)^{-1/2}$; and $(it)^{-1/2} = t^{-1/2}e^{-i\pi/4}$. With $ds = i\,dt$,
>
> $$
> f(iT) = \int_0^T i\cdot(-i)(1 + t^2)^{-1/2}\,t^{-1/2}e^{-i\pi/4}\cdot i\,dt = e^{i\pi/4}\int_0^T\frac{dt}{t^{1/2}(1 + t^2)^{1/2}} \longrightarrow e^{i\pi/4}\cdot\frac12 B\Big(\frac14, \frac14\Big) ,
> $$
>
> substituting $u = t^2$ in the limit. Since $B\big(\frac14, \frac14\big) = \sqrt2\,B\big(\frac14, \frac12\big)$ (numerically $7.41630 = 1.41421 \times 5.24412$), this is $e^{i\pi/4}\sqrt2\,b = b + ib$, the same limit. At $T = 10^6$ the integral is still about $0.0014(1 + i)$ short of it, in line with the tail $\int_T^\infty t^{-3/2}\,dt = 2T^{-1/2}$ allowed by the order property.
>
> *B&C: Sec. 128, equations (5)–(6); the map is that of Sec. 130, Exercise 4*

^ex-128-3
