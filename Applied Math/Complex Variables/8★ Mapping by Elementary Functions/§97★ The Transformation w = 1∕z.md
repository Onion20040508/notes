---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: 97
bc: "97"
aliases: ["B&C 97"]
tags: [complex-variables, math342, extension]
---
← [[§96★ Linear Transformations]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§98★ Mappings by 1∕z]] →

*Brown–Churchill, Section 97.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

The reciprocal $w = 1/z$ is the one genuinely new ingredient of the linear fractional transformations. Geometrically it is an inversion in the unit circle, which exchanges inside and outside, followed by a reflection in the real axis. Defining $1/0 = \infty$ and $1/\infty = 0$ makes it a continuous one-to-one map of the extended plane onto itself, and from now on that is what "$1/z$" means whenever the point at infinity is involved.

## Inversion and Reflection

> [!definition] Definition §97.1: Inversion in the Unit Circle
> The **inversion with respect to the unit circle** $|z| = 1$ is the mapping $Z = z/|z|^2$ of the nonzero points of the plane. The image $Z$ of $z \ne 0$ is the point with
>
> $$
> |Z| = \frac{1}{|z|} \qquad\text{and}\qquad \arg Z = \arg z ,
> $$
>
> that is, the point on the ray from the origin through $z$ at distance $1/|z|$. Points exterior to the circle go onto the nonzero points interior to it and conversely, and each point of the circle is fixed.
>
> *B&C: Sec. 97 (text)*

^def-97-1

> [!theorem] Proposition §97.1: 1/z Is an Inversion Followed by a Reflection
> The equation
>
> $$
> w = \frac1z \qquad (1)
> $$
>
> is a one-to-one correspondence between the nonzero points of the $z$ and $w$ planes, and it is the composition of the inversion in the unit circle and the reflection in the real axis:
>
> $$
> Z = \frac{z}{|z|^2}, \qquad w = \bar Z . \qquad (2)
> $$
>
> *B&C: Sec. 97 (text)*

^prop-97-1

> [!proof]+ Proof
> Since $z\bar z = |z|^2$, for $z \ne 0$
>
> $$
> \frac1z = \frac{\bar z}{z\bar z} = \overline{\Big(\frac{z}{|z|^2}\Big)} ,
> $$
>
> because $|z|^2$ is real. So $1/z = \bar Z$ with $Z = z/|z|^2$, which is (2). For the inversion, $|Z| = |z|/|z|^2 = 1/|z|$, and $Z$ is a positive multiple of $z$, so $\arg Z = \arg z$ (Definition §97.1). Finally $w = 1/z$ is one-to-one from the nonzero $z$ onto the nonzero $w$, with inverse $z = 1/w$.

^pf-97-1

*Uses:* [[§97★ The Transformation w = 1∕z#^def-97-1|Def. §97.1]], [[§6 Complex Conjugates|§6]] ($z\bar z = |z|^2$)

![[m342-97-1.svg]]
*The two steps of $w = 1/z$ for a point $z$ outside the unit circle: the inversion puts $Z$ on the same ray at distance $1/|z|$, inside the circle; the reflection in the real axis then gives $w = \bar Z$, with $|w| = 1/|z|$ and $\arg w = -\arg z$.*

## The Extended Plane

The reciprocal is undefined at $0$ and gives no finite value at $\infty$, but the limits ([[§17 Limits Involving the Point at Infinity|§17]]) fix the natural values.

> [!definition] Definition §97.2: 1/z on the Extended Plane
> On the extended $z$ plane define
>
> $$
> T(0) = \infty, \qquad T(\infty) = 0, \qquad\text{and}\qquad T(z) = \frac1z \quad (z \ne 0, \infty) . \qquad (6)
> $$
>
> Whenever the function $1/z$ is referred to and the point at infinity is involved, this $T$ is intended.
>
> *B&C: Sec. 97, Equation (6)*

^def-97-2

> [!theorem] Theorem §97.2: 1/z Is Continuous on the Extended Plane
> For each point $z_0$ of the extended $z$ plane, including $z_0 = 0$ and $z_0 = \infty$,
>
> $$
> \lim_{z\to z_0} T(z) = T(z_0) . \qquad (7)
> $$
>
> So $T$ is continuous on the extended plane. Moreover $T$ is a one-to-one map of the extended plane onto itself, and $T(T(z)) = z$.
>
> *B&C: Sec. 97 (text)*

^thm-97-2

> [!proof]+ Proof
> Recall from [[§17 Limits Involving the Point at Infinity|§17]] (Theorem) that $\lim_{z\to z_0} f(z) = \infty$ if and only if $\lim_{z\to z_0} 1/f(z) = 0$, and that $\lim_{z\to\infty} f(z) = w_0$ if and only if $\lim_{z\to0} f(1/z) = w_0$.
>
> *At $z_0 = 0$:*
>
> $$
> \lim_{z\to0} T(z) = \infty \qquad\text{since}\qquad \lim_{z\to0}\frac{1}{T(z)} = \lim_{z\to0} z = 0 , \qquad (4)
> $$
>
> and $\infty = T(0)$.
>
> *At $z_0 = \infty$:*
>
> $$
> \lim_{z\to\infty} T(z) = 0 \qquad\text{since}\qquad \lim_{z\to0} T\Big(\frac1z\Big) = \lim_{z\to0} z = 0 , \qquad (5)
> $$
>
> and $0 = T(\infty)$.
>
> *At a finite $z_0 \ne 0$:* $T(z) = 1/z$ is a quotient of continuous functions with nonzero denominator near $z_0$, so $\lim_{z\to z_0} T(z) = 1/z_0 = T(z_0)$ ([[§18 Continuity|§18]]).
>
> This is (7) at every point, which is continuity on the extended plane. Finally $T(T(z)) = z$: for finite $z \ne 0$ because $1/(1/z) = z$, and $T(T(0)) = T(\infty) = 0$, $T(T(\infty)) = T(0) = \infty$. A map that is its own inverse is one-to-one and onto.

^pf-97-2

*Uses:* [[§97★ The Transformation w = 1∕z#^def-97-2|Def. §97.2]], [[§17 Limits Involving the Point at Infinity|§17]] (Theorem), [[§18 Continuity|§18]]

> [!remark]- Connections
> - The extended plane is the one-point compactification of $\mathbb{C} = \mathbb{R}^2$, homeomorphic to the sphere $S^2$ by stereographic projection: [[§17 Local Compactness#^ex-17-7|590 Ex. §17.7]], [[§17 Local Compactness#^def-17-3|590 Def. §17.3]]. B&C's neighborhoods $|z| > 1/\varepsilon$ of $\infty$ are exactly the complements of closed disks, as in that topology, and Theorem §97.2 says that $T$ is a homeomorphism of the sphere onto itself (on $S^2$ it is the rotation through $\pi$ about the real axis).

## Examples

The exercises on Sections 97 and 98 are printed together after Section 98.

> [!example] Example §97.1: Orientation of the Image of the Unit Circle
> Give the circle $|z| = 1$ the positive (counterclockwise) orientation. Since $|z| = 1$ is fixed pointwise by the inversion, (2) shows that $w = 1/z$ acts on it as the reflection $w = \bar z$. Parametrically, $z = e^{i\theta}$ $(0 \le \theta \le 2\pi)$ goes to
>
> $$
> w = e^{-i\theta} \qquad (0 \le \theta \le 2\pi) ,
> $$
>
> so the image is the same circle traversed once **clockwise**: $1 \mapsto 1$, $i \mapsto -i$, $-1 \mapsto -1$, $-i \mapsto i$.
>
> *B&C: Sec. 98, Exercise 11*

^ex-97-1

> [!example] Example §97.2: A Hyperbola Goes onto a Lemniscate
> Show that $w = 1/z$ transforms the hyperbola $x^2 - y^2 = 1$ into the lemniscate $\rho^2 = \cos 2\phi$, where $w = \rho\exp(i\phi)$.
>
> In polar form $z = re^{i\theta}$, $x^2 - y^2 = r^2(\cos^2\theta - \sin^2\theta) = r^2\cos 2\theta$, so the hyperbola is $r^2\cos 2\theta = 1$. By Proposition §97.1, $w = 1/z$ has $\rho = 1/r$ and $\phi = -\theta$. Substituting $r = 1/\rho$ and $\theta = -\phi$,
>
> $$
> \frac{\cos(-2\phi)}{\rho^2} = 1 \qquad\Longleftrightarrow\qquad \rho^2 = \cos 2\phi .
> $$
>
> Each step reverses, so a point $w \ne 0$ lies on the lemniscate exactly when $1/w$ lies on the hyperbola. The origin of the lemniscate is the image of $\infty$, approached along all four ends of the two branches.
>
> *B&C: Sec. 98, Exercise 10*

^ex-97-2

> [!example] Example §97.3: Describing 1/(z − 1) and i/z Geometrically
> **(a)** $w = 1/(z - 1)$ is the translation $Z = z - 1$ (one unit to the left), followed by $w = 1/Z$: inversion in the unit circle centered at the origin of the $Z$ plane, then reflection in the real axis. Equivalently: invert in the circle $|z - 1| = 1$ (which sends $z$ to $1 + (z - 1)/|z - 1|^2$), shift one unit to the left, and reflect in the real axis. The point $z = 1$ goes to $\infty$ and $z = \infty$ to $0$.
>
> **(b)** $w = i/z$ is $W = 1/z$ followed by $w = iW$: inversion in the unit circle, reflection in the real axis, and then the rotation through $\pi/2$ ([[§96★ Linear Transformations#^prop-96-1|Proposition §96.1]]). It transforms circles and lines into circles and lines, because $1/z$ does ([[§98★ Mappings by 1∕z#^thm-98-3|Theorem §98.3]]) and a rotation obviously does.
>
> *B&C: Sec. 98, Exercises 7 and 8*

^ex-97-3
