---
type: section
subject: "[[Complex Variables]]"
chapter: 2
section: 26
bc: "26"
aliases: ["B&C 26"]
tags: [complex-variables, math342]
---
← [[§25 Analytic Functions]] · ↑ [[· 2 Analytic Functions]] · [[§27★ Harmonic Functions]] →

*Brown–Churchill, Section 26 · MAT 342 HW 3.*

There are two ways to decide where a function is analytic. A function given by a formula in $z$ is handled by the differentiation rules, [[§20 Rules for Differentiation#^thm-20-2|Theorem §20.2]] and [[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]: it is analytic except at the zeros of denominators. A function given by its components $u$ and $v$ is handled by the Cauchy–Riemann equations together with [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]. The second half of the section uses the Cauchy–Riemann equations to prove structural facts: an analytic function whose conjugate is also analytic, or whose modulus is constant, or whose values are real, must be constant. The constant-modulus result is a key step in the maximum modulus principle ([[§59 Maximum Modulus Principle#^lem-59-2|Lemma §59.2]]).

## Deciding Where a Function Is Analytic

> [!remark] Remark: Method — Where Is a Function Analytic?
> 1. **Formula in $z$** (polynomials, quotients, compositions): by [[§25 Analytic Functions#^prop-25-1|Proposition §25.1]] and [[§25 Analytic Functions#^prop-25-2|Proposition §25.2]] the function is analytic wherever every denominator is nonzero and every inner function lands where the outer one is analytic. The excluded points are the singular points. An expression for $f'(z)$ is needed only if one is actually wanted.
> 2. **Components $u, v$ given:** compute the four partials, check that they are continuous, and check the Cauchy–Riemann equations. If they hold throughout an open set, $f$ is analytic there and $f' = u_x + iv_x$ ([[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]]). If they hold only on a curve or at isolated points, $f$ is analytic nowhere ([[§25 Analytic Functions#^ex-25-3|Example §25.3]]).
> 3. **Higher derivatives:** write $f' = U + iV$ and repeat step 2 (Example §26.2).

^rem-26-1

> [!example] Example §26.1: A Rational Function
> The quotient
>
> $$
> f(z) = \frac{z^2 + 3}{(z + 1)(z^2 + 5)}
> $$
>
> is analytic throughout the $z$ plane except where the denominator vanishes: $z + 1 = 0$ gives $z = -1$, and $z^2 + 5 = 0$ gives $z = \pm\sqrt5\,i$. So $f$ is analytic except at the **singular points** $z = -1$ and $z = \pm\sqrt5\,i$ (each is a singular point: $f$ is analytic at all nearby points). The analyticity is due to the familiar differentiation rules, [[§25 Analytic Functions#^prop-25-1|Proposition §25.1]], which need to be applied only if an expression for $f'(z)$ is actually wanted.
>
> *B&C: Sec. 26, Example 1*

^ex-26-1

> [!example] Example §26.2: sin x cosh y + i cos x sinh y
> If $f(z) = \sin x\cosh y + i\cos x\sinh y$, the component functions are
>
> $$
> u(x, y) = \sin x\cosh y \qquad\text{and}\qquad v(x, y) = \cos x\sinh y .
> $$
>
> Because
>
> $$
> u_x = \cos x\cosh y = v_y \qquad\text{and}\qquad u_y = \sin x\sinh y = -v_x
> $$
>
> everywhere, and these partials are continuous everywhere, it is clear from [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] that $f$ is entire. In fact, according to that theorem,
>
> $$
> f'(z) = u_x + iv_x = \cos x\cosh y - i\sin x\sinh y . \qquad (1)
> $$
>
> It is straightforward to show that $f'(z)$ is also entire by writing (1) as $f'(z) = U(x, y) + iV(x, y)$, where
>
> $$
> U(x, y) = \cos x\cosh y \qquad\text{and}\qquad V(x, y) = -\sin x\sinh y .
> $$
>
> For then
>
> $$
> U_x = -\sin x\cosh y = V_y \qquad\text{and}\qquad U_y = \cos x\sinh y = -V_x ,
> $$
>
> with continuous partials. Furthermore,
>
> $$
> f''(z) = U_x + iV_x = -(\sin x\cosh y + i\cos x\sinh y) = -f(z) .
> $$
>
> (This $f$ is $\sin z$, [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]], and $f'$ is $\cos z$.)
>
> *B&C: Sec. 26, Example 2*

^ex-26-2

## Analytic Functions Forced to Be Constant

> [!example] Example §26.3: f and Its Conjugate Both Analytic
> Suppose that a function $f(z) = u(x, y) + iv(x, y)$ and its conjugate $\overline{f(z)} = u(x, y) - iv(x, y)$ are *both* analytic in a domain $D$. Then $f(z)$ must be constant throughout $D$.
>
> To show this, write $\overline{f(z)} = U(x, y) + iV(x, y)$, where
>
> $$
> U(x, y) = u(x, y) \qquad\text{and}\qquad V(x, y) = -v(x, y) . \qquad (2)
> $$
>
> Because of the analyticity of $f(z)$, the Cauchy–Riemann equations
>
> $$
> u_x = v_y, \qquad u_y = -v_x \qquad (3)
> $$
>
> hold in $D$; and the analyticity of $\overline{f(z)}$ in $D$ tells us that
>
> $$
> U_x = V_y, \qquad U_y = -V_x . \qquad (4)
> $$
>
> In view of relations (2), equations (4) can also be written
>
> $$
> u_x = -v_y, \qquad u_y = v_x . \qquad (5)
> $$
>
> Adding corresponding sides of the first equations in (3) and (5) gives $2u_x = 0$, so $u_x = 0$ in $D$. Subtracting the second equation in (5) from the second in (3) gives $0 = -2v_x$, so $v_x = 0$. According to the formula of [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]], then,
>
> $$
> f'(z) = u_x + iv_x = 0 + i0 = 0 ,
> $$
>
> and it follows from [[§25 Analytic Functions#^thm-25-3|Theorem §25.3]] that $f(z)$ is constant throughout $D$.
>
> *B&C: Sec. 26, Example 3*

^ex-26-3

> [!example] Example §26.4: Analytic with Constant Modulus
> Let $f$ be analytic throughout a domain $D$, and suppose further that the modulus $|f(z)|$ is constant throughout $D$. Then $f(z)$ must be constant there too.
>
> Write
>
> $$
> |f(z)| = c \qquad\text{for all } z \text{ in } D , \qquad (6)
> $$
>
> where $c$ is a real constant. If $c = 0$, then $f(z) = 0$ everywhere in $D$. If $c \ne 0$, the property $z\bar z = |z|^2$ of complex numbers ([[§6 Complex Conjugates#^prop-6-3|Proposition §6.3]]) tells us that
>
> $$
> f(z)\overline{f(z)} = c^2 \ne 0 ,
> $$
>
> and hence that $f(z)$ is never zero in $D$. So
>
> $$
> \overline{f(z)} = \frac{c^2}{f(z)} \qquad\text{for all } z \text{ in } D ,
> $$
>
> and it follows from this that $\overline{f(z)}$ is analytic everywhere in $D$ (a quotient whose denominator does not vanish, [[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]). The main result of Example §26.3 thus ensures that $f(z)$ is constant throughout $D$.
>
> This result is needed later, for the maximum modulus principle ([[§59 Maximum Modulus Principle#^lem-59-2|Lemma §59.2]]).
>
> *B&C: Sec. 26, Example 4*

^ex-26-4

> [!example] Example §26.5: Real-Valued Analytic Functions Are Constant
> **(a)** Suppose that $f'(z)$ exists for all $z$ and that $f$ takes only real values, $f(z) \in \mathbb{R}$ for all $z$. Find $f'(z)$. **(b)** What can be said about $f$?
>
> **(a)** Write $f = u + iv$. Since $f$ is real-valued, $v(x, y) = 0$ for all $(x, y)$, so $v_x = v_y = 0$ everywhere. Since $f'(z)$ exists at every $z$, the Cauchy–Riemann equations hold everywhere ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]):
>
> $$
> u_x = v_y = 0, \qquad u_y = -v_x = 0 .
> $$
>
> Hence $f'(z) = u_x + iv_x = 0 + i0 = 0$ for all $z$.
>
> **(b)** By (a), $f' = 0$ throughout the domain $\mathbb{C}$, so by [[§25 Analytic Functions#^thm-25-3|Theorem §25.3]] $f$ is constant: $f(z) = c$ for all $z$, and $c$ is real since $f$ takes real values.
>
> The same argument works in any domain $D$ (B&C's exercise): an analytic function that is real-valued throughout a domain is constant there. Alternatively, $\overline{f} = f$ is then analytic, and Example §26.3 applies. So nonconstant real-valued functions, such as $|z|^2$ or $\operatorname{Re} z$, are analytic in no domain.
>
> *B&C: Sec. 26, Exercise 7; Source: 342 HW 3, Q3*

^ex-26-5
