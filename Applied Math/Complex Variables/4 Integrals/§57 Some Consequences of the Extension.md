---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 57
bc: "57"
aliases: ["B&C 57"]
tags: [complex-variables, math342]
---
← [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)]] · ↑ [[· 4 Integrals]] · [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra]] →

*Brown–Churchill, Section 57.*

The extended Cauchy integral formula has three immediate consequences. An analytic function has derivatives of all orders, each analytic, so its real and imaginary parts have continuous partial derivatives of all orders; nothing like this holds for differentiable functions of a real variable. Morera's theorem is a converse of the Cauchy–Goursat theorem: a continuous function whose integrals around all closed contours vanish is analytic. Cauchy's inequality bounds the derivatives of $f$ at the center of a circle by the maximum of $|f|$ on the circle, and is the tool behind Liouville's theorem and the fundamental theorem of algebra in [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra|§58]].

## Derivatives of All Orders

> [!theorem] Theorem §57.1: Derivatives of Analytic Functions Are Analytic
> If a function $f$ is analytic at a given point, then its derivatives of all orders are analytic there too.
>
> *B&C: Sec. 57, Theorem 1*

^thm-57-1

> [!proof]+ Proof
> Assume that $f$ is analytic at a point $z_0$. There must, then, be a neighborhood $|z - z_0| < \varepsilon$ of $z_0$ throughout which $f$ is analytic ([[§25 Analytic Functions#^def-25-1|Definition §25.1]]). Consequently, there is a positively oriented circle $C_0$, centered at $z_0$ and with radius $\varepsilon/2$, such that $f$ is analytic inside and on $C_0$. From the extended Cauchy integral formula with $n = 2$ ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]),
>
> $$
> f''(z) = \frac{1}{\pi i}\int_{C_0}\frac{f(s)\,ds}{(s - z)^3}
> $$
>
> at each point $z$ interior to $C_0$. In particular $f''(z)$ exists throughout the neighborhood $|z - z_0| < \varepsilon/2$, which means that $f'$ is analytic at $z_0$. One can apply the same argument to the analytic function $f'$ to conclude that its derivative $f''$ is analytic at $z_0$, and so on: by induction, $f^{(n)}$ is analytic at $z_0$ for every $n$.

^pf-57-1

*Uses:* [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]], [[§25 Analytic Functions#^def-25-1|Def. §25.1]]

As a consequence, when a function $f(z) = u(x, y) + iv(x, y)$ is analytic at a point $z = (x, y)$, the differentiability of $f'$ ensures the continuity of $f'$ there ([[§19 Derivatives#^thm-19-1|Theorem §19.1]]). Since ([[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]])

$$
f'(z) = u_x + iv_x = v_y - iu_y ,
$$

the first-order partial derivatives of $u$ and $v$ are continuous at that point. Furthermore, since $f''$ is analytic and continuous at $z$ and

$$
f''(z) = u_{xx} + iv_{xx} = v_{yx} - iu_{yx} ,
$$

and so on, we arrive at a corollary that was anticipated in [[§27★ Harmonic Functions|§27★]], where harmonic functions were introduced ([[§27★ Harmonic Functions#^thm-27-1|Theorem §27.1]]).

> [!theorem] Corollary §57.2: Partial Derivatives of All Orders
> If a function $f(z) = u(x, y) + iv(x, y)$ is analytic at a point $z = (x, y)$, then the component functions $u$ and $v$ have continuous partial derivatives of all orders at that point.
>
> *B&C: Sec. 57, Corollary*

^cor-57-2

> [!proof]+ Proof
> B&C indicates the first two orders; here is the induction. For a function $g = U + iV$ analytic at a point, write $g_x = U_x + iV_x$ and $g_y = U_y + iV_y$. By the Cauchy–Riemann equations in the form above,
>
> $$
> g_x = g', \qquad g_y = U_y + iV_y = i\,(V_y - iU_y) = i\,g' .
> $$
>
> Since $f$ is analytic at $z$, it is analytic throughout some neighborhood $N$ of $z$, and Theorem §57.1, applied at each point of $N$, shows that $f$ and all its derivatives are analytic throughout $N$. We show by induction on $k$ that every $k$th order partial derivative of $f$, taken in any order with $a$ derivatives in $x$ and $b$ in $y$ ($a + b = k$), exists near $z$ and equals $i^b f^{(k)}$. For $k = 0$ this is $f = f$. If it holds for $k$, then $i^b f^{(k)}$ is analytic, and by the two rules its $x$-derivative is $i^b f^{(k+1)}$ and its $y$-derivative is $i^{b+1}f^{(k+1)}$, as claimed. Each $i^b f^{(k)}$ is analytic, hence continuous. Since the partial derivatives of $u$ and $v$ are the real and imaginary parts of the partial derivatives of $f$,
>
> $$
> \frac{\partial^k u}{\partial x^a\,\partial y^b} = \operatorname{Re}\big(i^b f^{(k)}\big), \qquad \frac{\partial^k v}{\partial x^a\,\partial y^b} = \operatorname{Im}\big(i^b f^{(k)}\big) ,
> $$
>
> and these are continuous at the point. (In particular $u_{xx} + u_{yy} = \operatorname{Re}\big(f'' + i^2f''\big) = 0$: $u$ and $v$ are harmonic.)

^pf-57-2

*Uses:* [[§57 Some Consequences of the Extension#^thm-57-1|§57.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]], [[§19 Derivatives#^thm-19-1|§19.1]]

> [!remark]- Connections
> - In the language of Multivariable Analysis, $u$ and $v$ are $C^\infty$ and satisfy Laplace's equation $\nabla^2u = 0$, [[§17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|452 Def. §17.2]]; so the real part of an analytic function is a potential in the sense of [[§39 Potential in a Disk|341 §39]], and the mean value and maximum principles there apply to it.

## Morera's Theorem

The proof of the next theorem, due to E. Morera (1856–1909), depends on the fact that the derivative of an analytic function is itself analytic.

> [!theorem] Theorem §57.3: Morera's Theorem
> Let $f$ be continuous on a domain $D$. If
>
> $$
> \int_C f(z)\,dz = 0 \qquad (1)
> $$
>
> for every closed contour $C$ in $D$, then $f$ is analytic throughout $D$.
>
> *B&C: Sec. 57, Theorem 2*

^thm-57-3

> [!proof]+ Proof
> When the hypothesis is satisfied, [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]] ensures that $f$ has an antiderivative in $D$; that is, there exists an analytic function $F$ such that $F'(z) = f(z)$ at each point in $D$. Since $f$ is the derivative of the analytic function $F$, it follows from Theorem §57.1 that $f$ is analytic in $D$.

^pf-57-3

*Uses:* [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|§49.1]], [[§57 Some Consequences of the Extension#^thm-57-1|§57.1]]

In particular, when $D$ is simply connected, Morera's theorem is, for the class of continuous functions on $D$, the converse of [[§52 Simply Connected Domains#^thm-52-1|Theorem §52.1]]: a continuous function on a simply connected domain is analytic if and only if its integral around every closed contour in $D$ is zero.

## Cauchy's Inequality

> [!theorem] Theorem §57.4: Cauchy's Inequality
> Suppose that a function $f$ is analytic inside and on a positively oriented circle $C_R$, centered at $z_0$ and with radius $R$. If $M_R$ denotes the maximum value of $|f(z)|$ on $C_R$, then
>
> $$
> |f^{(n)}(z_0)| \le \frac{n!\,M_R}{R^n} \qquad (n = 1, 2, \ldots) . \qquad (2)
> $$
>
> *B&C: Sec. 57, Theorem 3*

^thm-57-4

> [!proof]+ Proof
> By the extended Cauchy integral formula ([[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1]]),
>
> $$
> f^{(n)}(z_0) = \frac{n!}{2\pi i}\int_{C_R}\frac{f(z)\,dz}{(z - z_0)^{n+1}} \qquad (n = 1, 2, \ldots) .
> $$
>
> On $C_R$, $|z - z_0| = R$, so the integrand has modulus at most $M_R/R^{n+1}$, and $C_R$ has length $2\pi R$. The upper bound for moduli of contour integrals ([[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]]) gives
>
> $$
> |f^{(n)}(z_0)| \le \frac{n!}{2\pi}\cdot\frac{M_R}{R^{n+1}}\,2\pi R = \frac{n!\,M_R}{R^n} \qquad (n = 1, 2, \ldots) ,
> $$
>
> which is inequality (2). ($M_R$ exists because $|f|$ is continuous on the closed bounded set $C_R$.)

^pf-57-4

*Uses:* [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|§56.1]], [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|§47.2]], [[§18 Continuity#^thm-18-6|§18.6]]

## Examples

> [!example] Example §57.1: No Real Analogue of Theorem §57.1
> The real function $f(x) = x|x|$ is differentiable on the whole real line, with
>
> $$
> f'(x) = 2|x| ,
> $$
>
> (for $x \ne 0$ differentiate $x^2$ or $-x^2$; at $0$, $f(h)/h = |h| \to 0$). But $f'$ is not differentiable at $0$: $f'(h)/h = 2|h|/h = \pm 2$ has no limit. So a once differentiable function of a real variable need not be twice differentiable. Theorem §57.1 says that for functions of a complex variable this cannot happen: if $f'(z)$ exists throughout a neighborhood of $z_0$, so do $f''(z)$, $f'''(z)$, and all the others. The obvious complex counterpart $g(z) = z|z|$ is no counterexample, because it is not analytic. At $z_0 = 1$, for instance, its difference quotient is
>
> $$
> \frac{g(1 + h) - g(1)}{h} = |1 + h| + \frac{|1 + h| - 1}{h} ,
> $$
>
> which tends to $1 + 1 = 2$ as $h \to 0$ along the real axis (where $|1 + h| = 1 + h$) but to $1 + 0 = 1$ along the imaginary axis (where $|1 + it| - 1 = \sqrt{1 + t^2} - 1$ is of order $t^2$); so $g'(1)$ does not exist.
>
> *B&C: Sec. 57, Theorem 1 (a real-variable contrast)*

^ex-57-1

> [!example] Example §57.2: The Hypothesis of Morera's Theorem
> **(a)** $f(z) = \bar z$ is continuous on the plane, but by [[§51 Proof of the Theorem (Cauchy–Goursat Theorem)#^ex-51-2|Example §51.2]] its integral around the positively oriented unit circle is $2i \cdot \pi = 2\pi i \ne 0$. So Morera's theorem does not apply, consistently with the fact that $\bar z$ is nowhere analytic.
>
> **(b)** $f(z) = 1/z$ is analytic in the domain $D\colon z \ne 0$, but its integral around the unit circle is $2\pi i \ne 0$ ([[§53 Multiply Connected Domains#^ex-53-1|Example §53.1]]). So the hypothesis of Morera's theorem is sufficient for analyticity but not necessary on a multiply connected domain. On a simply connected domain it is also necessary ([[§52 Simply Connected Domains#^thm-52-1|Theorem §52.1]]).
>
> **(c)** $f(z) = 1/z^2$ on the same $D$ does satisfy the hypothesis: it has the antiderivative $-1/z$ there, so $\int_C f(z)\,dz = 0$ for every closed contour $C$ in $D$ ([[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]]), and Morera's theorem confirms that it is analytic in $D$.
>
> *B&C: Sec. 57, Theorem 2 and the text after it*

^ex-57-2

> [!example] Example §57.3: Cauchy's Inequality for the Exponential Function
> Apply Cauchy's inequality to $f(z) = e^z$ at $z_0 = 0$, and choose the best radius.
>
> Here $f^{(n)}(0) = 1$ for every $n$, and on the circle $|z| = R$ the maximum of $|e^z| = e^x$ is $M_R = e^R$, attained at $z = R$. So (2) says
>
> $$
> 1 \le \frac{n!\,e^R}{R^n} \qquad\text{for every } R > 0 .
> $$
>
> The bound is best when $e^R/R^n$ is smallest; its derivative $e^R R^{-n-1}(R - n)$ vanishes at $R = n$. With $R = n$,
>
> $$
> n! \ge \frac{n^n}{e^n} .
> $$
>
> So Cauchy's inequality is not sharp here, but it is not far off: by Stirling's formula $n! \approx \sqrt{2\pi n}\,(n/e)^n$, and indeed $n!\,e^n/n^n = 2.718, 3.695, 5.699, 7.993$ for $n = 1, 2, 5, 10$, against $\sqrt{2\pi n} = 2.507, 3.545, 5.605, 7.927$. Equality in (2) does hold for $f(z) = (z - z_0)^n$, for which $f^{(n)}(z_0) = n!$ and $M_R = R^n$.
>
> *B&C: Sec. 57, Theorem 3 (illustration)*

^ex-57-3
