---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 29
bc: "29"
aliases: ["B&C 29"]
tags: [complex-variables, math342, extension]
---
← [[§28★ Uniquely Determined Analytic Functions]] · ↑ [[· 2 Analytic Functions]] · [[§30 The Exponential Function]] →

*Brown–Churchill, Section 29.*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

Some analytic functions satisfy $\overline{f(z)} = f(\bar z)$ for all $z$ in a domain, others do not: $z + 1$ and $z^2$ do, throughout the plane, while $z + i$ and $iz^2$ do not. The reflection principle predicts which: for a function analytic in a domain symmetric about the real axis, the identity holds exactly when $f$ is real on the real axis. The proof combines the Cauchy–Riemann equations with the uniqueness theorem of [[§28★ Uniquely Determined Analytic Functions|§28★]]. One consequence: the nonreal zeros of a function that is analytic in such a domain and real on the axis, a polynomial with real coefficients for instance, come in conjugate pairs, since $f(z) = 0$ gives $f(\bar z) = \overline{f(z)} = 0$.

## The Theorem

> [!theorem] Theorem §29.1: Reflection Principle
> Suppose that a function $f$ is analytic in some domain $D$ which contains a segment of the $x$ axis and whose lower half is the reflection of the upper half with respect to that axis. Then
>
> $$
> \overline{f(z)} = f(\bar z) \qquad (1)
> $$
>
> for each point $z$ in the domain if and only if $f(x)$ is real for each point $x$ on the segment.
>
> *B&C: Sec. 29, Theorem*

^thm-29-1

> [!proof]+ Proof
> **($\Leftarrow$)** Assume that $f(x)$ is real at each point $x$ on the segment. Since $D$ is symmetric about the real axis, $\bar z$ lies in $D$ whenever $z$ does, so the function
>
> $$
> F(z) = \overline{f(\bar z)} \qquad (2)
> $$
>
> is defined throughout $D$. Once we show that $F$ is analytic in $D$, we shall use it to obtain (1).
>
> *$F$ is analytic.* Write
>
> $$
> f(z) = u(x, y) + iv(x, y), \qquad F(z) = U(x, y) + iV(x, y) .
> $$
>
> Since $\bar z = x - iy$,
>
> $$
> \overline{f(\bar z)} = u(x, -y) - iv(x, -y) , \qquad (3)
> $$
>
> so the components of $F$ and $f$ are related by
>
> $$
> U(x, y) = u(x, t) \qquad\text{and}\qquad V(x, y) = -v(x, t), \qquad\text{where } t = -y . \qquad (4)
> $$
>
> Now, because $f(x + it)$ is an analytic function of $x + it$, the first-order partial derivatives of $u(x, t)$ and $v(x, t)$ are continuous throughout $D$ ([[§57 Some Consequences of the Extension|§57]], Corollary) and satisfy the Cauchy–Riemann equations
>
> $$
> u_x = v_t, \qquad u_t = -v_x . \qquad (5)
> $$
>
> Furthermore, in view of (4) and the chain rule ($dt/dy = -1$),
>
> $$
> U_x = u_x, \qquad V_y = -v_t\frac{dt}{dy} = v_t ,
> $$
>
> and it follows from these and the first of equations (5) that $U_x = V_y$. Similarly,
>
> $$
> U_y = u_t\frac{dt}{dy} = -u_t, \qquad V_x = -v_x ,
> $$
>
> and the second of equations (5) tells us that $U_y = -u_t = v_x = -V_x$. Inasmuch as the first-order partial derivatives of $U(x, y)$ and $V(x, y)$ satisfy the Cauchy–Riemann equations and are continuous, the function $F(z)$ is analytic in $D$ ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]).
>
> (The same conclusion follows directly from the definition of the derivative, without partial derivatives: for $\Delta z \ne 0$,
>
> $$
> \frac{F(z + \Delta z) - F(z)}{\Delta z} = \overline{\Big(\frac{f(\bar z + \overline{\Delta z}) - f(\bar z)}{\overline{\Delta z}}\Big)} \;\longrightarrow\; \overline{f'(\bar z)}
> $$
>
> as $\Delta z \to 0$, since $\overline{\Delta z} \to 0$ and conjugation is continuous.)
>
> *$F = f$.* Since $f(x)$ is real on the segment of the real axis lying in $D$, $v(x, 0) = 0$ on the segment; and, in view of (4),
>
> $$
> F(x) = U(x, 0) + iV(x, 0) = u(x, 0) - iv(x, 0) = u(x, 0) .
> $$
>
> That is,
>
> $$
> F(z) = f(z) \qquad (6)
> $$
>
> at each point on the segment. According to [[§28★ Uniquely Determined Analytic Functions#^thm-28-2|Theorem §28.2]], which tells us that an analytic function defined on a domain $D$ is uniquely determined by its values along any line segment lying in $D$, equation (6) actually holds throughout $D$. Because of definition (2) of $F$, then,
>
> $$
> \overline{f(\bar z)} = f(z) ; \qquad (7)
> $$
>
> and, conjugating both sides, this is the same as equation (1).
>
> **($\Rightarrow$)** Assume that equation (1) holds. In view of expression (3), the form (7) of equation (1) can be written
>
> $$
> u(x, -y) - iv(x, -y) = u(x, y) + iv(x, y) .
> $$
>
> In particular, if $(x, 0)$ is a point on the segment of the real axis that lies in $D$,
>
> $$
> u(x, 0) - iv(x, 0) = u(x, 0) + iv(x, 0) ;
> $$
>
> and, by equating imaginary parts here, we see that $v(x, 0) = 0$. Hence $f(x)$ is real on the segment of the real axis lying in $D$.

^pf-29-1

*Uses:* [[§57 Some Consequences of the Extension|§57]] (Corollary), [[§21 Cauchy–Riemann Equations|§21]] (Theorem), [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§28★ Uniquely Determined Analytic Functions#^thm-28-2|§28.2]]

![[m342-29-1.svg]]
*The setting of the reflection principle: a domain $D$ symmetric about the $x$ axis, containing a segment of it (red) on which $f$ is real. The function $F(z) = \overline{f(\bar z)}$ evaluates $f$ at the mirror point $\bar z$ and conjugates the value; it is analytic, agrees with $f$ on the segment, and so equals $f$ throughout $D$.*

## Examples

> [!example] Example §29.1: z + 1 and z² Versus z + i and iz²
> Just prior to the statement of the theorem, we noted that
>
> $$
> \overline{z + 1} = \bar z + 1 \qquad\text{and}\qquad \overline{z^2} = \bar z^{\,2}
> $$
>
> for all $z$ in the finite plane. The theorem tells us that this is true, since $x + 1$ and $x^2$ are real when $x$ is real. We also noted that $z + i$ and $iz^2$ do not have the reflection property throughout the plane: $\overline{z + i} = \bar z - i \ne \bar z + i$ and $\overline{iz^2} = -i\bar z^{\,2} \ne i\bar z^{\,2}$ (except at isolated points). We now know that this is because $x + i$ and $ix^2$ are *not* real when $x$ is real.
>
> *B&C: Sec. 29, Examples*

^ex-29-1

> [!example] Example §29.2: The Exponential Function
> The function $f(z) = e^x\cos y + ie^x\sin y$ has a derivative everywhere in the finite plane ([[§23 Sufficient Conditions for Differentiability#^ex-23-1|Example §23.1]]). Show from the reflection principle that $\overline{f(z)} = f(\bar z)$ for each $z$, and then verify this directly.
>
> **From the principle.** $f$ is entire, the plane is symmetric about the real axis and contains all of it, and on the real axis $f(x) = e^x\cos 0 + ie^x\sin 0 = e^x$ is real. By Theorem §29.1, $\overline{f(z)} = f(\bar z)$ for every $z$.
>
> **Directly.** With $\bar z = x - iy$,
>
> $$
> f(\bar z) = e^x\cos(-y) + ie^x\sin(-y) = e^x\cos y - ie^x\sin y = \overline{f(z)} ,
> $$
>
> since cosine is even and sine is odd.
>
> *B&C: Sec. 29, Exercise 4*

^ex-29-2

> [!example] Example §29.3: Pure Imaginary on the Axis
> Show that if the condition that $f(x)$ is real in the reflection principle is replaced by the condition that $f(x)$ is pure imaginary, then equation (1) is changed to
>
> $$
> \overline{f(z)} = -f(\bar z) .
> $$
>
> Let $f$ be analytic in $D$ as in Theorem §29.1, and put $g(z) = if(z)$, analytic in $D$. Then $f(x)$ is pure imaginary on the segment, $f(x) = ib(x)$ with $b(x)$ real, if and only if $g(x) = -b(x)$ is real there. By Theorem §29.1 this holds if and only if $\overline{g(z)} = g(\bar z)$ throughout $D$, that is,
>
> $$
> -i\,\overline{f(z)} = if(\bar z) \iff \overline{f(z)} = -f(\bar z) .
> $$
>
> For example, $f(z) = iz$ is pure imaginary on the real axis, and $\overline{iz} = -i\bar z = -f(\bar z)$.
>
> *B&C: Sec. 29, Exercise 5*

^ex-29-3
