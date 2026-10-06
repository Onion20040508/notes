---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 17
bdp: "3.5"
aliases: ["BDP 3.5"]
tags: [ordinary-differential-equations, math331]
---
← [[§16 Repeated Roots; Reduction of Order]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§18★ Variation of Parameters]] →

*Boyce–DiPrima, Section 3.5 · MATH 331 Written HW 4, Final (Fall 2021), Final (Fall 2022, alternate).*

The difference of two solutions of a nonhomogeneous equation $L[y] = g(t)$ solves the homogeneous equation $L[y] = 0$. So the general solution of $L[y] = g$ is the general solution $c_1y_1 + c_2y_2$ of the homogeneous equation plus any one particular solution $Y$. For constant coefficients and forcing terms built from polynomials, exponentials, sines and cosines, a particular solution can be guessed up to constants: assume that $Y$ has the same form as $g$, substitute, and solve for the undetermined coefficients. The one complication is a guess that already solves the homogeneous equation; it is then multiplied by $t$, or by $t^2$, as recorded in BDP's table of trial forms. Variation of parameters ([[§18★ Variation of Parameters#^thm-18-1|Theorem §18.1]]) handles every other forcing term.

## Structure of the Solutions

We consider the nonhomogeneous equation

$$
L[y] = y'' + p(t)y' + q(t)y = g(t) , \qquad (1)
$$

where $p$, $q$ and $g$ are continuous on an open interval $I$, together with the **corresponding homogeneous equation**

$$
L[y] = y'' + p(t)y' + q(t)y = 0 . \qquad (2)
$$

> [!theorem] Theorem §17.1: Difference of Two Solutions
> If $Y_1$ and $Y_2$ are two solutions of the nonhomogeneous linear differential equation (1), then their difference $Y_1 - Y_2$ is a solution of the corresponding homogeneous differential equation (2). If, in addition, $y_1$ and $y_2$ form a fundamental set of solutions of (2), then
>
> $$
> Y_1(t) - Y_2(t) = c_1y_1(t) + c_2y_2(t) , \qquad (3)
> $$
>
> where $c_1$ and $c_2$ are certain constants.
>
> *BDP: Theorem 3.5.1*

^thm-17-1

> [!proof]+ Proof
> $Y_1$ and $Y_2$ satisfy
>
> $$
> L[Y_1](t) = g(t), \qquad L[Y_2](t) = g(t) . \qquad (4)
> $$
>
> Subtracting the second equation from the first,
>
> $$
> L[Y_1](t) - L[Y_2](t) = g(t) - g(t) = 0 . \qquad (5)
> $$
>
> The computation in the proof of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2]] (with $c_1 = 1$, $c_2 = -1$) shows that $L[Y_1] - L[Y_2] = L[Y_1 - Y_2]$, so (5) becomes
>
> $$
> L[Y_1 - Y_2](t) = 0 . \qquad (6)
> $$
>
> So $Y_1 - Y_2$ is a solution of (2). By [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|Theorem §14.4]], all solutions of (2) are linear combinations of a fundamental set, so $Y_1 - Y_2$ can be written in the form (3).

^pf-17-1

*Uses:* [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|§14.2]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-4|§14.4]]

> [!theorem] Theorem §17.2: General Solution of the Nonhomogeneous Equation
> The general solution of the nonhomogeneous equation (1) can be written in the form
>
> $$
> y = \phi(t) = c_1y_1(t) + c_2y_2(t) + Y(t) , \qquad (7)
> $$
>
> where $y_1$ and $y_2$ form a fundamental set of solutions of the corresponding homogeneous equation (2), $c_1$ and $c_2$ are arbitrary constants, and $Y$ is any solution of the nonhomogeneous equation (1).
>
> *BDP: Theorem 3.5.2*

^thm-17-2

> [!proof]+ Proof
> Let $\phi$ be an arbitrary solution of (1). Apply [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-1|Theorem §17.1]] with $Y_1 = \phi$ and $Y_2$ the specific solution $Y$: by (3),
>
> $$
> \phi(t) - Y(t) = c_1y_1(t) + c_2y_2(t) \qquad (8)
> $$
>
> for some constants $c_1$, $c_2$, which is (7). Conversely, every function (7) solves (1), since $L[c_1y_1 + c_2y_2 + Y] = L[c_1y_1 + c_2y_2] + L[Y] = 0 + g$ by the same linearity. Since $\phi$ is an arbitrary solution of (1), the expression on the right side of (7) includes all solutions of (1), and it is natural to call it the general solution of (1).

^pf-17-2

*Uses:* [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-1|§17.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|§14.2]]

> [!remark]- Connections
> - The solution set of $L[y] = g$ is the translate $Y + S$ of the two-dimensional solution space $S$ of $L[y] = 0$ ([[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^rem-14-2|§14, Remark: The Solution Space Is a Two-Dimensional Vector Space]]): [[§11 Products and Quotients of Vector Spaces#^ladr-3-97|LADR 3.97]]. The same structure for linear systems, "the solutions of $A\mathbf{x} = \mathbf{b}$ are $\mathbf{p}$ plus the solutions of $A\mathbf{x} = \mathbf{0}$": [[§5 Solution Sets of Linear Systems#^thm-5-3|235 Thm. §5.3]].
> - The same structure for linear difference equations, "one particular solution plus the general solution of the homogeneous equation": [[§30 Applications to Difference Equations#^thm-30-7|235 Thm. §30.7]].
> - See also: [[§2★ Nonhomogeneous Linear Equations#^thm-2-2|341 Thm. §2.2]] (the same statement in Powers' review of ODEs).

> [!definition] Definition §17.1: Complementary Solution; Particular Solution
> The general solution $c_1y_1(t) + c_2y_2(t)$ of the homogeneous equation (2) corresponding to (1) is called the **complementary solution** and is denoted $y_c(t)$. Any solution $Y(t)$ of the nonhomogeneous equation (1) is called a **particular solution**. By [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-2|Theorem §17.2]], solving (1) takes three steps:
> 1. find the complementary solution $y_c(t) = c_1y_1(t) + c_2y_2(t)$;
> 2. find any particular solution $Y(t)$;
> 3. form the sum $y = y_c(t) + Y(t)$.
>
> *BDP: 3.5 (text)*

^def-17-1

Step 1 is solved for constant coefficients by [[§16 Repeated Roots; Reduction of Order#^thm-16-2|Theorem §16.2]]. For step 2 there are two methods: undetermined coefficients (this section) and variation of parameters ([[§18★ Variation of Parameters#^thm-18-1|Theorem §18.1]]).

## The Method of Undetermined Coefficients

The method of undetermined coefficients makes an initial assumption about the form of the particular solution $Y(t)$, with the coefficients left unspecified. Substituting it into (1) gives equations for the coefficients. If they can be solved, we have a particular solution; if not, there is no solution of the assumed form, and the assumption must be modified. The method is straightforward once the form of $Y$ is known, but it is useful mainly when that form can be written down in advance: for **constant coefficients** and forcing terms $g(t)$ built from **polynomials, exponential functions, sines and cosines**. Within that class the principle is:
- if $g(t) = e^{\alpha t}$, assume $Y(t)$ is a multiple of $e^{\alpha t}$;
- if $g(t)$ is $\sin\beta t$ or $\cos\beta t$, assume a combination $A\sin\beta t + B\cos\beta t$ (a sine alone is not enough, since differentiation produces cosines);
- if $g(t)$ is a polynomial of degree $n$, assume a polynomial of degree $n$ (for $y'' - 3y' - 4y = 4t^2 - 1$, assume $Y = At^2 + Bt + C$);
- for a product of two or three of these, assume the product of the corresponding forms.

A forcing term that is a sum is split into its terms:

> [!theorem] Proposition §17.3: Superposition of Forcing Terms
> Suppose that $g(t) = g_1(t) + g_2(t)$, and that $Y_1$ and $Y_2$ are solutions of
>
> $$
> ay'' + by' + cy = g_1(t) \qquad (16) \qquad\qquad\text{and}\qquad\qquad ay'' + by' + cy = g_2(t) , \qquad (17)
> $$
>
> respectively. Then $Y_1 + Y_2$ is a solution of
>
> $$
> ay'' + by' + cy = g(t) . \qquad (18)
> $$
>
> The same holds for a sum of any finite number of terms. So for a forcing term that is a sum one may solve several simpler equations and add the results.
>
> *BDP: 3.5 (text)*

^prop-17-3

> [!proof]+ Proof
> Substitute $Y_1 + Y_2$ for $y$ in (18). By the sum rule for derivatives and (16), (17),
>
> $$
> a(Y_1 + Y_2)'' + b(Y_1 + Y_2)' + c(Y_1 + Y_2) = \big(aY_1'' + bY_1' + cY_1\big) + \big(aY_2'' + bY_2' + cY_2\big) = g_1(t) + g_2(t) = g(t) .
> $$
>
> For $n$ terms, repeat (or induct). The computation is valid for complex-valued $g_i$ and $Y_i$ as well (used in the proof of Theorem §17.4).

^pf-17-3

> [!example] Example §17.1: Exponential, Trigonometric and Product Forcing
> Find a particular solution of
>
> $$
> y'' - 3y' - 4y = 3e^{2t} + 2\sin t - 8e^t\cos 2t . \qquad (19)
> $$
>
> By [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-17-3|Proposition §17.3]] we solve the equation with each of the three terms on the right side and add.
>
> **(a)** $y'' - 3y' - 4y = 3e^{2t}$ (9). The exponential reproduces itself under differentiation, so assume $Y(t) = Ae^{2t}$. Then $Y' = 2Ae^{2t}$, $Y'' = 4Ae^{2t}$, and
>
> $$
> Y'' - 3Y' - 4Y = (4A - 6A - 4A)e^{2t} = -6Ae^{2t} = 3e^{2t} ,
> $$
>
> so $-6A = 3$, $A = -\frac12$, and $Y(t) = -\frac12e^{2t}$ (10).
>
> **(b)** $y'' - 3y' - 4y = 2\sin t$ (11). By analogy, try $Y(t) = A\sin t$:
>
> $$
> Y'' - 3Y' - 4Y = -A\sin t - 3A\cos t - 4A\sin t = 2\sin t, \quad\text{that is,}\quad (2 + 5A)\sin t + 3A\cos t = 0 . \qquad (12)
> $$
>
> This must hold for all $t$; at $t = 0$ it says $3A = 0$ and at $t = \frac{\pi}{2}$ it says $2 + 5A = 0$. These requirements contradict each other, so the assumption is inadequate. The cosine term in (12) suggests $Y(t) = A\sin t + B\cos t$. Then $Y' = A\cos t - B\sin t$, $Y'' = -A\sin t - B\cos t$, and
>
> $$
> Y'' - 3Y' - 4Y = (-A + 3B - 4A)\sin t + (-B - 3A - 4B)\cos t = 2\sin t . \qquad (13)
> $$
>
> Matching the coefficients of $\sin t$ and $\cos t$ (equivalently, evaluating at $t = 0$ and $t = \frac{\pi}{2}$):
>
> $$
> -5A + 3B - 2 = 0, \qquad -3A - 5B = 0 .
> $$
>
> The second gives $B = -\frac35A$; then $-5A - \frac95A = -\frac{34}{5}A = 2$, so $A = -\frac{5}{17}$ and $B = \frac{3}{17}$: $Y(t) = -\frac{5}{17}\sin t + \frac{3}{17}\cos t$.
>
> **(c)** $y'' - 3y' - 4y = -8e^t\cos 2t$ (15). Assume the product of $e^t$ and a combination of $\cos 2t$ and $\sin 2t$:
>
> $$
> Y(t) = Ae^t\cos 2t + Be^t\sin 2t .
> $$
>
> By the product rule,
>
> $$
> Y'(t) = (A + 2B)e^t\cos 2t + (-2A + B)e^t\sin 2t, \qquad Y''(t) = (-3A + 4B)e^t\cos 2t + (-4A - 3B)e^t\sin 2t .
> $$
>
> In $Y'' - 3Y' - 4Y$, the coefficient of $e^t\cos 2t$ is $(-3A + 4B) - 3(A + 2B) - 4A = -10A - 2B$ and that of $e^t\sin 2t$ is $(-4A - 3B) - 3(-2A + B) - 4B = 2A - 10B$. Matching with $-8e^t\cos 2t$:
>
> $$
> 10A + 2B = 8, \qquad 2A - 10B = 0 .
> $$
>
> So $A = 5B$, $52B = 8$, $B = \frac{2}{13}$, $A = \frac{10}{13}$, and $Y(t) = \frac{10}{13}e^t\cos 2t + \frac{2}{13}e^t\sin 2t$.
>
> **(d)** Adding the three particular solutions, a particular solution of (19) is
>
> $$
> Y(t) = -\tfrac12e^{2t} + \tfrac{3}{17}\cos t - \tfrac{5}{17}\sin t + \tfrac{10}{13}e^t\cos 2t + \tfrac{2}{13}e^t\sin 2t .
> $$
>
> *BDP: Examples 3.5.1–3.5.4*

^ex-17-1

## The Table of Trial Forms

The procedure of [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^ex-17-1|Example §17.1]] can fail in one way: the assumed form may itself solve the homogeneous equation.

> [!theorem] Theorem §17.4: Trial Forms for Undetermined Coefficients
> Consider $ay'' + by' + cy = g_i(t)$ with constants $a \ne 0$, $b$, $c$. For each $g_i$ below there is a particular solution $Y_i$ of the form shown.
>
> | $g_i(t)$ | $Y_i(t)$ |
> |---|---|
> | $P_n(t) = a_0t^n + a_1t^{n-1} + \cdots + a_n$ | $t^s(A_0t^n + A_1t^{n-1} + \cdots + A_n)$ |
> | $P_n(t)e^{\alpha t}$ | $t^s(A_0t^n + A_1t^{n-1} + \cdots + A_n)e^{\alpha t}$ |
> | $P_n(t)e^{\alpha t}\sin\beta t$ or $P_n(t)e^{\alpha t}\cos\beta t$ | $t^s\big[(A_0t^n + A_1t^{n-1} + \cdots + A_n)e^{\alpha t}\cos\beta t + (B_0t^n + B_1t^{n-1} + \cdots + B_n)e^{\alpha t}\sin\beta t\big]$ |
>
> Here $s$ is the smallest nonnegative integer ($s = 0$, $1$ or $2$) that ensures that no term in $Y_i(t)$ is a solution of the corresponding homogeneous equation. Equivalently, for the three cases, $s$ is the number of times $0$ is a root of the [[§13 Homogeneous Differential Equations with Constant Coefficients#^def-13-4|characteristic equation]], $\alpha$ is a root of the characteristic equation, and $\alpha + i\beta$ is a root of the characteristic equation, respectively.
>
> *BDP: Table 3.5.1*

^thm-17-4

> [!remark] Remark: Why It Works
> BDP motivates the factor $t^s$ by its Example 3.5.5, $y'' - 3y' - 4y = 2e^{-t}$ (20). The guess $Y = Ae^{-t}$ gives $Y'' - 3Y' - 4Y = (A + 3A - 4A)e^{-t} = 0$, and $0 = 2e^{-t}$ is impossible. The reason: the roots of $r^2 - 3r - 4 = (r + 1)(r - 4)$ are $-1$ and $4$, so $e^{-t}$ solves the homogeneous equation, and no multiple of it can produce $2e^{-t}$. The first-order analog $y' + y = 2e^{-t}$ shows the way: with the [[§4 Linear Differential Equations; Method of Integrating Factors#^def-4-2|integrating factor]] $e^t$, $(e^ty)' = 2$, so $y = 2te^{-t} + ce^{-t}$, and the particular part carries an extra factor $t$. Accordingly, try $Y = Ate^{-t}$: then $Y' = Ae^{-t} - Ate^{-t}$, $Y'' = -2Ae^{-t} + Ate^{-t}$, and
>
> $$
> Y'' - 3Y' - 4Y = (-2A - 3A)e^{-t} + (A + 3A - 4A)te^{-t} = -5Ae^{-t} = 2e^{-t} ,
> $$
>
> so $A = -\frac25$ and $Y(t) = -\frac25te^{-t}$ (26). In general: if the assumed form duplicates a solution of the homogeneous equation, multiply it by $t$; occasionally once more by $t$; for a second-order equation it is never necessary to go further.

^rem-17-1

> [!proof]- Proof
> Write $Z(r) = ar^2 + br + c$ for the characteristic polynomial; then $Z'(r) = 2ar + b$.
>
> **Case 1: $g(t) = P_n(t) = a_0t^n + a_1t^{n-1} + \cdots + a_n$.** The equation is
>
> $$
> ay'' + by' + cy = a_0t^n + a_1t^{n-1} + \cdots + a_n . \qquad (28)
> $$
>
> Assume
>
> $$
> Y(t) = A_0t^n + A_1t^{n-1} + \cdots + A_{n-2}t^2 + A_{n-1}t + A_n . \qquad (29)
> $$
>
> Substituting in (28),
>
> $$
> a\big(n(n-1)A_0t^{n-2} + \cdots + 2A_{n-2}\big) + b\big(nA_0t^{n-1} + \cdots + A_{n-1}\big) + c\big(A_0t^n + A_1t^{n-1} + \cdots + A_n\big) = a_0t^n + \cdots + a_n . \qquad (30)
> $$
>
> Equating the coefficients of like powers of $t$, beginning with $t^n$:
>
> $$
> cA_0 = a_0, \qquad cA_1 + nbA_0 = a_1, \qquad \ldots, \qquad cA_n + bA_{n-1} + 2aA_{n-2} = a_n .
> $$
>
> Provided $c \ne 0$, the first equation gives $A_0 = a_0/c$, and each later equation determines the next $A_k$, since its only new unknown appears as $cA_k$. Here $c \ne 0$ means that $0$ is not a root of $Z$, and $s = 0$.
>
> If $c = 0$ but $b \ne 0$ ($0$ is a simple root), the left side of (30) has degree only $n - 1$ and (30) cannot be satisfied. To make $aY'' + bY'$ a polynomial of degree $n$, take $Y$ of degree $n + 1$:
>
> $$
> Y(t) = t(A_0t^n + \cdots + A_n) .
> $$
>
> Substituting into (28) with $c = 0$,
>
> $$
> aY'' + bY' = bA_0(n + 1)t^n + \big(aA_0(n + 1)n + bA_1n\big)t^{n-1} + \cdots = a_0t^n + a_1t^{n-1} + \cdots + a_n .
> $$
>
> (In general the coefficient of $t^{n-k}$ is $b(n + 1 - k)A_k + a(n + 2 - k)(n + 1 - k)A_{k-1}$; BDP writes only the first two.) Since $b \ne 0$, $A_0 = a_0/(b(n + 1))$, and the coefficient $b(n + 1 - k) \ne 0$ of $A_k$ in the $t^{n-k}$ equation lets us solve for $A_1, \ldots, A_n$ in turn. There is no constant term in $Y$, and none is needed: when $c = 0$ a constant solves the homogeneous equation.
>
> If $b = c = 0$, the characteristic equation is $ar^2 = 0$, and $0$ is a repeated root: $y_1 = e^{0t} = 1$ and $y_2 = te^{0t} = t$ form a fundamental set of the homogeneous equation. Assume
>
> $$
> Y(t) = t^2(A_0t^n + \cdots + A_n) .
> $$
>
> Then $aY''$ is a polynomial of degree $n$, whose $t^{n-k}$ coefficient is $a(n + 2 - k)(n + 1 - k)A_k$, and the $A_k$ are found as before. The constant and linear terms are omitted because both solve the homogeneous equation.
>
> **Case 2: $g(t) = e^{\alpha t}P_n(t)$.** The problem
>
> $$
> ay'' + by' + cy = e^{\alpha t}P_n(t) \qquad (31)
> $$
>
> reduces to Case 1 by the substitution $Y(t) = e^{\alpha t}u(t)$. Then
>
> $$
> Y'(t) = e^{\alpha t}\big(u'(t) + \alpha u(t)\big), \qquad Y''(t) = e^{\alpha t}\big(u''(t) + 2\alpha u'(t) + \alpha^2u(t)\big) .
> $$
>
> Substituting in (31), canceling the factor $e^{\alpha t}$ and collecting terms,
>
> $$
> au''(t) + (2a\alpha + b)u'(t) + (a\alpha^2 + b\alpha + c)u(t) = P_n(t) . \qquad (32)
> $$
>
> This is equation (28) with $b$, $c$ replaced by $Z'(\alpha) = 2a\alpha + b$ and $Z(\alpha) = a\alpha^2 + b\alpha + c$. By Case 1:
> - if $Z(\alpha) \ne 0$, take $u(t) = A_0t^n + \cdots + A_n$, so a particular solution of (31) is
>
> $$
> Y(t) = e^{\alpha t}(A_0t^n + A_1t^{n-1} + \cdots + A_n) ; \qquad (33)
> $$
>
> - if $Z(\alpha) = 0$ but $Z'(\alpha) \ne 0$, take $u(t) = t(A_0t^n + \cdots + A_n)$, so $Y$ is $t$ times (33);
> - if $Z(\alpha) = Z'(\alpha) = 0$, take $u(t) = t^2(A_0t^n + \cdots + A_n)$, so $Y$ is $t^2$ times (33).
>
> $Z(\alpha) = 0$ says that $\alpha$ is a root, so that $e^{\alpha t}$ solves the homogeneous equation. $Z(\alpha) = Z'(\alpha) = 0$ says that $\alpha$ is a double root, so that both $e^{\alpha t}$ and $te^{\alpha t}$ solve it. (Writing $Z(r) = a(r - r_1)(r - r_2)$ with $\alpha = r_1$, $Z'(\alpha) = a(r_1 - r_2)$, which vanishes exactly when $r_1 = r_2$.) So $s$ is the number of times $\alpha$ is a root. The computation uses only $\frac{d}{dt}e^{\alpha t} = \alpha e^{\alpha t}$, so by [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|Proposition §15.1]] Case 2 holds for complex $\alpha$ as well, with complex coefficients $A_k$.
>
> **Case 3: $g(t) = e^{\alpha t}P_n(t)\cos\beta t$ or $e^{\alpha t}P_n(t)\sin\beta t$.** The two are similar; take the sine. By Euler's formula ([[§15 Complex Roots of the Characteristic Equation#^def-15-1|Definition §15.1]]), $\sin\beta t = (e^{i\beta t} - e^{-i\beta t})/(2i)$, so
>
> $$
> g(t) = P_n(t)\,\frac{e^{(\alpha + i\beta)t} - e^{(\alpha - i\beta)t}}{2i} ,
> $$
>
> a sum of two terms of Case 2 with the complex exponents $\alpha \pm i\beta$. By Case 2 and [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-17-3|Proposition §17.3]] we should choose
>
> $$
> Y(t) = e^{(\alpha + i\beta)t}(A_0t^n + \cdots + A_n) + e^{(\alpha - i\beta)t}(B_0t^n + \cdots + B_n) ,
> $$
>
> or, equivalently,
>
> $$
> Y(t) = e^{\alpha t}(A_0t^n + \cdots + A_n)\cos\beta t + e^{\alpha t}(B_0t^n + \cdots + B_n)\sin\beta t .
> $$
>
> (BDP asserts the equivalence; here is why. By (14) of [[§15 Complex Roots of the Characteristic Equation#^def-15-1|§15]], $e^{(\alpha \pm i\beta)t} = e^{\alpha t}(\cos\beta t \pm i\sin\beta t)$, so the first form is $e^{\alpha t}\big[(A + B)(t)\cos\beta t + i(A - B)(t)\sin\beta t\big]$ for the two polynomials $A(t)$, $B(t)$, and as $A$, $B$ run over all polynomials of degree $\le n$, so do $A + B$ and $i(A - B)$. Real coefficients suffice: $a$, $b$, $c$ and $g$ are real, so if $Y$ is a complex-valued solution, then, separating real and imaginary parts as in the proof of [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|Theorem §14.6]], $\operatorname{Re}Y$ is a real solution, and it has the second form with real polynomials.) The second form is usually preferred because it involves no complex coefficients. If $\alpha \pm i\beta$ satisfy the characteristic equation, Case 2 says to multiply each polynomial by $t$, increasing its degree by $1$. A root $\alpha + i\beta$ with $\beta \ne 0$ is never a double root (its conjugate is the other root), so here $s \le 1$.

^pf-17-4

*Uses:* [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-17-3|§17.3]], [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|§15.1]], [[§15 Complex Roots of the Characteristic Equation#^def-15-1|Def. §15.1]], [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-6|§14.6]]

> [!remark]- Connections
> - See also: [[§2★ Nonhomogeneous Linear Equations#^thm-2-4|341 Thm. §2.4]] (the same table of trial solutions in Powers' review of ODEs, with the Revision Rule for the factor $t^s$).

> [!remark] Remark: Method — Undetermined Coefficients
> To solve an initial value problem for $ay'' + by' + cy = g(t)$ (27) with constant $a$, $b$, $c$:
> 1. Find the general solution of the corresponding homogeneous equation ([[§16 Repeated Roots; Reduction of Order#^thm-16-2|Theorem §16.2]]).
> 2. Make sure that $g(t)$ belongs to the class of this section: it involves nothing more than exponential functions, sines, cosines, polynomials, or sums or products of such functions. If not, use variation of parameters ([[§18★ Variation of Parameters#^rem-18-1|§18★, Remark: Method — Variation of Parameters]]).
> 3. If $g(t) = g_1(t) + \cdots + g_n(t)$ is a sum of $n$ terms, form $n$ subproblems $ay'' + by' + cy = g_i(t)$, $i = 1, \ldots, n$, each containing only one of the terms.
> 4. For the $i$th subproblem assume a particular solution $Y_i(t)$ consisting of the appropriate exponential function, sine, cosine, polynomial, or combination thereof. If there is any duplication in the assumed form of $Y_i(t)$ with the solutions of the homogeneous equation (found in step 1), multiply $Y_i(t)$ by $t$, or (if necessary) by $t^2$, so as to remove the duplication ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^thm-17-4|Theorem §17.4]]).
> 5. Find a particular solution $Y_i(t)$ for each subproblem. Then $Y_1(t) + \cdots + Y_n(t)$ is a particular solution of the full equation (27).
> 6. Form the sum of the general solution of the homogeneous equation (step 1) and the particular solution (step 5). This is the general solution of the nonhomogeneous equation.
> 7. When initial conditions are provided, use them to determine the values of the arbitrary constants remaining in the general solution. (Do this only now: the initial conditions apply to the whole solution $y_c + Y$, not to $y_c$.)

^rem-17-2

> [!remark] Remark: The Method Is Self-Correcting
> If you assume too little for $Y(t)$, a contradiction is soon reached, as with $A\sin t$ in [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^ex-17-1|Example §17.1(b)]] or $Ae^{-t}$ in [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^rem-17-1|Remark: Why It Works]], and it usually points to the needed modification. If you assume too many terms, some unnecessary work is done and some coefficients turn out to be zero, but the correct answer is obtained. When $g$ involves both $\cos\beta t$ and $\sin\beta t$, treat the two terms together, since each alone leads to the same form. For example, for $g(t) = t\sin t + 2\cos t$ the form is $Y(t) = (A_0t + A_1)\sin t + (B_0t + B_1)\cos t$, provided that $\sin t$ and $\cos t$ are not solutions of the homogeneous equation. The algebra can be lengthy, and a computer algebra system helps once the method is understood.

^rem-17-3

## Course Examples

> [!example] Example §17.2: One Operator, Three Forcing Terms
> Find the general solution of **(a)** $y'' - 5y' - 14y = e^{4t}$ and **(b)** $y'' - 5y' - 14y = e^{-2t} - t^2$.
>
> **Complementary solution.** $r^2 - 5r - 14 = (r - 7)(r + 2) = 0$ has roots $7$ and $-2$, so $y_c = c_1e^{7t} + c_2e^{-2t}$.
>
> **(a)** $4$ is not a root, so $s = 0$: $Y = Ae^{4t}$. Then $Y'' - 5Y' - 14Y = (16 - 20 - 14)Ae^{4t} = -18Ae^{4t} = e^{4t}$, so $A = -\frac{1}{18}$ and
>
> $$
> y = c_1e^{7t} + c_2e^{-2t} - \tfrac{1}{18}e^{4t} .
> $$
>
> **(b)** Split $g$ into $g_1 = e^{-2t}$ and $g_2 = -t^2$ ([[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^prop-17-3|Proposition §17.3]]).
>
> *For $g_1 = e^{-2t}$:* $-2$ is a simple root, so $Ae^{-2t}$ would solve the homogeneous equation; $s = 1$ and $Y_1 = Ate^{-2t}$. Then $Y_1' = A(1 - 2t)e^{-2t}$, $Y_1'' = A(-4 + 4t)e^{-2t}$, and
>
> $$
> Y_1'' - 5Y_1' - 14Y_1 = Ae^{-2t}\big[(-4 + 4t) - 5(1 - 2t) - 14t\big] = -9Ae^{-2t} = e^{-2t} ,
> $$
>
> so $A = -\frac19$. (The $t$ terms cancel, as they must. In terms of (32), $Z(-2) = 0$ and $Z'(-2) = 2(-2) - 5 = -9$.)
>
> *For $g_2 = -t^2$:* $c = -14 \ne 0$, so $0$ is not a root and $s = 0$: $Y_2 = Dt^2 + Et + F$. Then
>
> $$
> Y_2'' - 5Y_2' - 14Y_2 = 2D - 5(2Dt + E) - 14(Dt^2 + Et + F) = -14Dt^2 + (-10D - 14E)t + (2D - 5E - 14F) = -t^2 .
> $$
>
> Matching coefficients: $-14D = -1$, so $D = \frac{1}{14}$; $-10D - 14E = 0$, so $E = -\frac{10}{196} = -\frac{5}{98}$; $2D - 5E - 14F = 0$, so $14F = \frac17 + \frac{25}{98} = \frac{39}{98}$ and $F = \frac{39}{1372}$.
>
> **General solution of (b):**
>
> $$
> y = c_1e^{7t} + c_2e^{-2t} - \tfrac19te^{-2t} + \tfrac{1}{14}t^2 - \tfrac{5}{98}t + \tfrac{39}{1372} .
> $$
>
> *Source: 331 Written HW 4, Problems 3 and 4*

^ex-17-2

> [!example] Example §17.3: Trigonometric Forcing with a Repeated Root
> Find the general solution of $y'' + 6y' + 9y = 50\cos t$.
>
> **Complementary solution.** $r^2 + 6r + 9 = (r + 3)^2$ has the repeated root $-3$, so $y_c = c_1e^{-3t} + c_2te^{-3t}$.
>
> **Particular solution.** $\pm i$ are not roots, so $s = 0$ and $Y = A\cos t + B\sin t$. With $Y' = -A\sin t + B\cos t$ and $Y'' = -A\cos t - B\sin t$,
>
> $$
> \underbrace{-A\cos t - B\sin t}_{Y''} + 6\underbrace{(-A\sin t + B\cos t)}_{Y'} + 9\underbrace{(A\cos t + B\sin t)}_{Y} = (8A + 6B)\cos t + (8B - 6A)\sin t = 50\cos t .
> $$
>
> Comparing coefficients: $8A + 6B = 50$ and $8B - 6A = 0$. The second gives $B = \frac34A$, and then $8A + \frac92A = \frac{25}{2}A = 50$, so $A = 4$ and $B = 3$.
>
> **General solution:**
>
> $$
> y = c_1e^{-3t} + c_2te^{-3t} + 4\cos t + 3\sin t .
> $$
>
> The repeated root affects only $y_c$; the trial form for $\cos t$ depends only on whether $\pm i$ are roots.
>
> *Source: 331 Final (Fall 2021), Q1*

^ex-17-3

> [!example] Example §17.4: An Exponential with a Parameter
> Find the general solution of $y'' + 2y' + 17y = e^{\alpha t}$, where $\alpha$ is a real constant.
>
> **Complementary solution.** $r^2 + 2r + 17 = (r + 1)^2 + 16 = 0$ gives $r = -1 \pm 4i$, so $y_c = e^{-t}(c_1\cos 4t + c_2\sin 4t)$.
>
> **Particular solution.** The roots are not real, so no real $\alpha$ is a root and $s = 0$ for every $\alpha$: $Y = Ae^{\alpha t}$. Then
>
> $$
> Y'' + 2Y' + 17Y = (\alpha^2 + 2\alpha + 17)Ae^{\alpha t} = e^{\alpha t}, \qquad A = \frac{1}{\alpha^2 + 2\alpha + 17} ,
> $$
>
> and the denominator $(\alpha + 1)^2 + 16 \ge 16$ never vanishes. So
>
> $$
> y = e^{-t}(c_1\cos 4t + c_2\sin 4t) + \frac{e^{\alpha t}}{\alpha^2 + 2\alpha + 17} .
> $$
>
> The answer "depends on $\alpha$" only through the coefficient. With real roots the case distinction would be real: for the operator $y'' + 6y' + 9y$ of [[§17 Nonhomogeneous Equations; Method of Undetermined Coefficients#^ex-17-3|Example §17.3]] and forcing $e^{\alpha t}$, $Y = e^{\alpha t}/(\alpha + 3)^2$ for $\alpha \ne -3$, while $\alpha = -3$ is a double root, so $s = 2$, $Y = At^2e^{-3t}$, and (32) with $Z(-3) = Z'(-3) = 0$ reduces to $u'' = 1$ for $u = At^2$, giving $A = \frac12$.
>
> *Source: 331 Final (Fall 2022, alternate), Q1*

^ex-17-4
