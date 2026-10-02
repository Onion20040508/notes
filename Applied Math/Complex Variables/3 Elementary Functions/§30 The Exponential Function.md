---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 30
bc: "30"
aliases: ["B&C 30"]
tags: [complex-variables, math342]
---
← [[§29★ Reflection Principle]] · ↑ [[· 3 Elementary Functions]] · [[§31 The Logarithmic Function]] →

*Brown–Churchill, Section 30.*

Chapter 3 defines analytic functions of $z$ that reduce to the elementary functions of calculus when $z = x + i0$, and every one of them is built from the exponential. This section defines $e^z = e^xe^{iy}$ by Euler's formula and checks which properties of $e^x$ survive: the law of exponents, $e^z \ne 0$, and $\frac{d}{dz}e^z = e^z$, so $e^z$ is entire. Two properties are new and drive the rest of the chapter: $e^z$ is periodic with period $2\pi i$, and it takes every nonzero complex value, infinitely often. Solving $e^w = z$ is what defines the logarithm, [[§31 The Logarithmic Function#^def-31-1|Definition §31.1]].

## Definition and First Properties

> [!definition] Definition §30.1: The Exponential Function
> For $z = x + iy$, the **exponential function** is
>
> $$
> e^z = e^xe^{iy} \qquad (z = x + iy), \qquad (1)
> $$
>
> where $e^{iy}$ is given by Euler's formula ([[§7 Exponential Form#^def-7-2|Definition §7.2]])
>
> $$
> e^{iy} = \cos y + i\sin y , \qquad (2)
> $$
>
> with $y$ in radians. We also write $\exp z$ for $e^z$. When $y = 0$, $e^z$ is the usual exponential function $e^x$ of calculus.
>
> *B&C: Sec. 30 (text)*

^def-30-1

> [!remark]- Connections
> - [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]] defines $e^{(\lambda + i\mu)t} = e^{\lambda t}(\cos\mu t + i\sin\mu t)$ in exactly the same way, motivated by substituting $it$ into the series $e^t = \sum t^n/n!$ ([[§78 Taylor and Maclaurin Series#^thm-78-6|Calc Thm. §78.6]]) and splitting off the series of $\cos t$ and $\sin t$ ([[§78 Taylor and Maclaurin Series#^thm-78-7|Calc Thm. §78.7]], [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]]); the same computation from the complex-numbers side is [[§53 Complex Numbers#^rem-53-1|235 Remark: Euler's Formula]].
> - Here the series is a theorem, not a motivation: $e^z = \sum_{n=0}^{\infty} z^n/n!$ for every $z$ is the Maclaurin series of the entire function $e^z$, [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]].

Since the *positive* $n$th root $\sqrt[n]{e}$ is assigned to $e^x$ when $x = 1/n$ $(n = 2, 3, \ldots)$, definition (1) says that $e^{1/n} = \sqrt[n]{e}$. This is an exception to the convention of [[§10 Roots of Complex Numbers#^def-10-1|Definition §10.1]], which would read $e^{1/n}$ as the *set* of $n$th roots of $e$: the symbol $e^z$ always means the single number (1). (The power $c^z$ of [[§35 The Power Function#^def-35-3|Definition §35.3]] is in general multiple-valued, and $e^z$ is the value given by the principal logarithm of $e$.)

Writing (1) as $e^z = \rho e^{i\phi}$ with $\rho = e^x$ and $\phi = y$ displays the modulus and an argument of $e^z$ at once.

> [!theorem] Proposition §30.1: Modulus and Argument of e^z
> For $z = x + iy$,
>
> $$
> |e^z| = e^x \qquad\text{and}\qquad \arg(e^z) = y + 2n\pi \quad (n = 0, \pm1, \pm2, \ldots) . \qquad (3)
> $$
>
> In particular
>
> $$
> e^z \ne 0 \qquad\text{for any complex number } z . \qquad (4)
> $$
>
> *B&C: Sec. 30, Equations (3) and (4)*

^prop-30-1

> [!proof]+ Proof
> By (1), $e^z = e^x e^{iy}$ is the exponential form $\rho e^{i\phi}$ of a complex number with $\rho = e^x > 0$ and $\phi = y$. The modulus of $\rho e^{i\phi}$ is $\rho$ and its arguments are $\phi + 2n\pi$ ([[§7 Exponential Form#^def-7-2|Definition §7.2]]), which is (3). Since $e^x$ is never zero, $|e^z| = e^x > 0$, which is (4).

^pf-30-1

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§7 Exponential Form#^def-7-2|Def. §7.2]]

> [!theorem] Theorem §30.2: The Law of Exponents
> For all complex numbers $z_1$, $z_2$,
>
> $$
> e^{z_1}e^{z_2} = e^{z_1 + z_2} . \qquad (5)
> $$
>
> Consequently
>
> $$
> \frac{e^{z_1}}{e^{z_2}} = e^{z_1 - z_2} \qquad (6)
> $$
>
> and $1/e^z = e^{-z}$.
>
> *B&C: Sec. 30, Equations (5) and (6)*

^thm-30-2

> [!proof]+ Proof
> Write $z_1 = x_1 + iy_1$ and $z_2 = x_2 + iy_2$. Then, by (1),
>
> $$
> e^{z_1}e^{z_2} = (e^{x_1}e^{iy_1})(e^{x_2}e^{iy_2}) = (e^{x_1}e^{x_2})(e^{iy_1}e^{iy_2}) .
> $$
>
> Here $x_1$, $x_2$ are real, so $e^{x_1}e^{x_2} = e^{x_1 + x_2}$ by the law of exponents of calculus, and $e^{iy_1}e^{iy_2} = e^{i(y_1 + y_2)}$ by [[§8 Products and Powers in Exponential Form#^thm-8-1|Theorem §8.1]]. Hence
>
> $$
> e^{z_1}e^{z_2} = e^{x_1 + x_2}e^{i(y_1 + y_2)} ,
> $$
>
> and since $(x_1 + x_2) + i(y_1 + y_2) = z_1 + z_2$, the right-hand side is $e^{z_1 + z_2}$ by (1). This is (5).
>
> By (5), $e^{z_1 - z_2}e^{z_2} = e^{z_1}$; dividing by $e^{z_2}$, which is nonzero by (4), gives (6). With $z_1 = 0$ and $e^0 = e^0e^{i0} = 1$, (6) becomes $1/e^{z_2} = e^{-z_2}$.

^pf-30-2

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§30 The Exponential Function#^prop-30-1|§30.1]], [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]], [[§121 The Logarithm Defined as an Integral#^thm-121-6|Calc Thm. §121.6]] (laws of exponents for real $e^x$)

> [!theorem] Theorem §30.3: e^z Is Entire
> The function $e^z$ is differentiable at every point of the $z$ plane, with
>
> $$
> \frac{d}{dz}e^z = e^z . \qquad (7)
> $$
>
> So $e^z$ is entire ([[§25 Analytic Functions#^def-25-2|Definition §25.2]]).
>
> *B&C: Sec. 30, Equation (7) (proved in Sec. 23, Example 1)*

^thm-30-3

> [!proof]+ Proof
> By (1) and (2), $e^z = u + iv$ with
>
> $$
> u(x, y) = e^x\cos y, \qquad v(x, y) = e^x\sin y .
> $$
>
> Their first-order partial derivatives
>
> $$
> u_x = e^x\cos y, \quad u_y = -e^x\sin y, \qquad v_x = e^x\sin y, \quad v_y = e^x\cos y
> $$
>
> exist and are continuous everywhere, and they satisfy the Cauchy–Riemann equations $u_x = v_y$, $u_y = -v_x$ everywhere. By the sufficient conditions, [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]], $e^z$ is differentiable at every point $z$, and
>
> $$
> \frac{d}{dz}e^z = u_x + iv_x = e^x\cos y + ie^x\sin y = e^z .
> $$
>
> A function differentiable everywhere is entire.

^pf-30-3

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§23 Sufficient Conditions for Differentiability#^thm-23-1|§23.1]], [[§25 Analytic Functions#^def-25-2|Def. §25.2]]

## Properties That e^x Does Not Have

> [!theorem] Proposition §30.4: Periodicity
> The exponential function is periodic, with the pure imaginary period $2\pi i$:
>
> $$
> e^{z + 2\pi i} = e^z . \qquad (8)
> $$
>
> Moreover $e^z$ takes negative values: $e^{i(2n + 1)\pi} = -1$ $(n = 0, \pm1, \pm2, \ldots)$.
>
> *B&C: Sec. 30, Equation (8) and text*

^prop-30-4

> [!proof]+ Proof
> By (1), $e^{2\pi i} = e^0(\cos 2\pi + i\sin 2\pi) = 1$, so (5) gives $e^{z + 2\pi i} = e^ze^{2\pi i} = e^z$. Likewise $e^{i\pi} = \cos\pi + i\sin\pi = -1$ and $e^{i2n\pi} = 1$, so $e^{i(2n + 1)\pi} = e^{i2n\pi}e^{i\pi} = (1)(-1) = -1$.

^pf-30-4

*Uses:* [[§30 The Exponential Function#^def-30-1|Def. §30.1]], [[§30 The Exponential Function#^thm-30-2|§30.2]]

Periodicity means that $e^z$ is completely described by its values on one horizontal strip of height $2\pi$, such as $-\pi < y \le \pi$. On that strip the picture is simple: by (3), a vertical segment $x = c$ is carried onto the circle $|w| = e^c$, and a horizontal line $y = c$ onto the ray from the origin at angle $c$.

![[m342-30-1.svg]]
*The map $w = e^z$ on the strip $-\pi < y \le \pi$. Vertical segments $x = -1, -\frac12, 0, \frac12, 1$ (blue) go to circles of radius $e^x$; horizontal lines $y = k\pi/4$ (red) go to rays at angle $y$ (the lines $y = \pm\frac\pi2$ go to the imaginary axis, $y = 0$ to the positive real axis, and $y = \pi$ to the negative real axis). The strip is carried one to one onto the punctured plane $w \ne 0$, and each further strip of height $2\pi$ covers it again.*

The figure already shows that $e^z$ takes every nonzero value $w$: once in each strip. This is proved in [[§31 The Logarithmic Function#^thm-31-1|Theorem §31.1]]. In practice an equation $e^z = w_0$ is solved by comparing exponential forms, using [[§10 Roots of Complex Numbers#^prop-10-1|Proposition §10.1]]: *two nonzero complex numbers $r_1e^{i\theta_1}$ and $r_2e^{i\theta_2}$ are equal if and only if $r_1 = r_2$ and $\theta_1 = \theta_2 + 2k\pi$ for some integer $k$.*

> [!remark] Remark: Method — Solving e^g(z) = w₀
> To find all $z$ with $e^{g(z)} = w_0$, where $w_0 \ne 0$ (for $w_0 = 0$ there are none, by (4)):
> 1. Write $w_0 = \rho e^{i\phi}$ in exponential form ($\rho = |w_0| > 0$, $\phi$ any one argument).
> 2. Write $g(z) = X + iY$, so $e^{g(z)} = e^Xe^{iY}$ by (1).
> 3. Equate moduli and arguments: $e^X = \rho$ and $Y = \phi + 2n\pi$, that is, $X = \ln\rho$ and $Y = \phi + 2n\pi$ $(n = 0, \pm1, \pm2, \ldots)$.
> 4. Solve $g(z) = \ln\rho + i(\phi + 2n\pi)$ for $z$. There are infinitely many solutions, one for each $n$; when $g(z) = z$ they are spaced $2\pi$ apart on a vertical line.
>
> In the language of [[§31 The Logarithmic Function#^def-31-1|Definition §31.1]]: step 3 says $g(z) = \log w_0$.

^rem-30-1

## Examples

> [!example] Example §30.1: Solving e^z = 1 + √3 i
> Find all numbers $z = x + iy$ such that
>
> $$
> e^z = 1 + \sqrt3\,i . \qquad (9)
> $$
>
> Since $|1 + \sqrt3\,i| = 2$ and $\pi/3$ is an argument of $1 + \sqrt3\,i$, equation (9) reads
>
> $$
> e^xe^{iy} = 2e^{i\pi/3} .
> $$
>
> By [[§10 Roots of Complex Numbers#^prop-10-1|Proposition §10.1]] on equal exponential forms,
>
> $$
> e^x = 2 \qquad\text{and}\qquad y = \frac\pi3 + 2n\pi \quad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> Because $\ln(e^x) = x$, it follows that $x = \ln 2$, and so
>
> $$
> z = \ln 2 + \Big(2n + \frac13\Big)\pi i \qquad (n = 0, \pm1, \pm2, \ldots) . \qquad (10)
> $$
>
> Check, for $n = 0$: $e^{\ln 2 + i\pi/3} = 2\big(\cos\frac\pi3 + i\sin\frac\pi3\big) = 2\big(\frac12 + \frac{\sqrt3}{2}i\big) = 1 + \sqrt3\,i$.
>
> *B&C: Sec. 30, Example*

^ex-30-1

> [!example] Example §30.2: A Composite Exponent; When Is e^z Real?
> **(a)** Solve $\exp(2z - 1) = 1$. With $g(z) = 2z - 1$ and $1 = 1 \cdot e^{i0}$, the Method gives $2z - 1 = \ln 1 + i(0 + 2n\pi) = 2n\pi i$, so
>
> $$
> z = \frac12 + n\pi i \qquad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> The period of $\exp(2z - 1)$ is $\pi i$, half that of $e^z$, which is why consecutive solutions are only $\pi$ apart.
>
> **(b)** If $e^z$ is real, then $\operatorname{Im} z = n\pi$. Indeed, $e^z = e^x(\cos y + i\sin y)$ has imaginary part $e^x\sin y$, and $e^x > 0$, so $e^z$ is real exactly when $\sin y = 0$, that is, $y = n\pi$ $(n = 0, \pm1, \pm2, \ldots)$. Then $e^z = e^x\cos n\pi = (-1)^ne^x$: positive for even $n$, negative for odd $n$.
>
> **(c)** Similarly, $e^z$ is pure imaginary exactly when its real part $e^x\cos y$ vanishes, that is, when $\operatorname{Im} z = \frac\pi2 + n\pi$.
>
> *B&C: Sec. 30, Exercises 8(c) and 10*

^ex-30-2

> [!example] Example §30.3: Estimates from |e^z| = e^x
> **(a)** $|\exp(z^2)| \le \exp(|z|^2)$ for all $z$. With $z = x + iy$, $z^2 = (x^2 - y^2) + i2xy$, so by (3)
>
> $$
> |\exp(z^2)| = e^{x^2 - y^2} \le e^{x^2 + y^2} = \exp(|z|^2) ,
> $$
>
> because $e^t$ is increasing on the real line and $x^2 - y^2 \le x^2 + y^2$.
>
> **(b)** $|\exp(-2z)| < 1$ if and only if $\operatorname{Re} z > 0$. Indeed $-2z = -2x - 2iy$, so $|\exp(-2z)| = e^{-2x}$, and $e^{-2x} < 1 = e^0$ if and only if $-2x < 0$, that is, $x > 0$.
>
> *B&C: Sec. 30, Exercises 6 and 7*

^ex-30-3

> [!example] Example §30.4: exp z̄ Is Nowhere Analytic, exp(z²) Is Entire
> **(a)** Let $f(z) = \exp\bar z = e^{x - iy} = e^x\cos y - ie^x\sin y$. Its Cauchy–Riemann equations require $2e^x\cos y = 0$ and $2e^x\sin y = 0$, which never hold together; the computation is [[§22 Examples (Cauchy–Riemann Equations)#^ex-22-4|Example §22.4]](a). By [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]], $f'(z)$ exists at no point, so $f$ is analytic nowhere.
>
> **(b)** $f(z) = \exp(z^2)$ is entire, for two reasons. *Composition:* $z^2$ and $e^z$ are entire (Theorem §30.3), so their composition is entire by the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]]), with $f'(z) = e^{z^2}\cdot 2z = 2z\exp(z^2)$. *Cauchy–Riemann:* $z^2 = (x^2 - y^2) + i2xy$, so $u = e^{x^2 - y^2}\cos 2xy$, $v = e^{x^2 - y^2}\sin 2xy$, and
>
> $$
> u_x = e^{x^2 - y^2}(2x\cos 2xy - 2y\sin 2xy) = v_y, \qquad u_y = e^{x^2 - y^2}(-2y\cos 2xy - 2x\sin 2xy) = -v_x ,
> $$
>
> with all four partial derivatives continuous everywhere; by [[§23 Sufficient Conditions for Differentiability#^thm-23-1|Theorem §23.1]] $f$ is differentiable everywhere, and $f'(z) = u_x + iv_x = e^{x^2 - y^2}\big[(2x\cos 2xy - 2y\sin 2xy) + i(2y\cos 2xy + 2x\sin 2xy)\big] = 2z\exp(z^2)$.
>
> *B&C: Sec. 30, Exercises 3 and 4*

^ex-30-4
