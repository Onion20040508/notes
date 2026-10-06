---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 20
bdp: "3.4"
aliases: ["BDP 3.4"]
tags: [ordinary-differential-equations, math331]
---
← [[§19 Complex Roots of the Characteristic Equation]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§21 Nonhomogeneous Equations; Method of Undetermined Coefficients]] →

*Boyce–DiPrima, Section 3.4 · MATH 331 Written HW 3.*

When $b^2 - 4ac = 0$ the characteristic equation of $ay'' + by' + cy = 0$ has a single repeated root $r_1 = -b/(2a)$, and the exponential method yields only one solution, $e^{r_1t}$. D'Alembert's idea finds a second: since $cy_1$ is a solution for every constant $c$, replace $c$ by a function $v(t)$ and ask which $v$ makes $vy_1$ a solution. Here $v'' = 0$, so $v = c_1 + c_2t$ and the second solution is $te^{r_1t}$. With this, all three cases of the constant-coefficient equation are complete. The same substitution works for any linear equation $y'' + p(t)y' + q(t)y = 0$ once one solution is known: it reduces the problem to a first-order equation for $v'$, hence the name reduction of order.

## Repeated Roots

If $b^2 - 4ac = 0$, the quadratic formula gives

$$
r_1 = r_2 = -\frac{b}{2a} , \qquad (3)
$$

and both roots yield the same solution

$$
y_1(t) = e^{-bt/(2a)} \qquad (4)
$$

of $ay'' + by' + cy = 0$ (1). It is not obvious how to find a second solution.

> [!remark] Remark: Why It Works
> Since $y_1$ is a solution, so is $cy_1$ for every constant $c$ ([[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-2|Theorem §18.2]]). D'Alembert's idea (18th century) is to replace the constant $c$ by a function $v(t)$ and to determine $v$ so that the product $v(t)y_1(t)$ is also a solution. A nonconstant $v$ then gives a solution that is not a multiple of $y_1$. BDP first carries this out for $y'' + 4y' + 4y = 0$, where $y_1 = e^{-2t}$; the substitution $y = v(t)e^{-2t}$ leads to $v'' = 0$, so $v = c_1t + c_2$ and $y = c_1te^{-2t} + c_2e^{-2t}$. The proof below is the same computation for general $a$, $b$, $c$.

^rem-20-1

> [!theorem] Theorem §24.1: Repeated Roots
> If $b^2 - 4ac = 0$, so that the characteristic equation has the repeated root $r_1 = -b/(2a)$, then
>
> $$
> y_1(t) = e^{-bt/(2a)}, \qquad y_2(t) = te^{-bt/(2a)} \qquad (19)
> $$
>
> form a fundamental set of solutions of $ay'' + by' + cy = 0$, with Wronskian
>
> $$
> W[y_1, y_2](t) = e^{-bt/a} , \qquad (20)
> $$
>
> and the general solution is
>
> $$
> y = c_1e^{-bt/(2a)} + c_2te^{-bt/(2a)} . \qquad (18)
> $$
>
> In words: one exponential solution corresponds to the repeated root, and a second is obtained by multiplying it by $t$.
>
> *BDP: 3.4 (text), Equations (18)–(20)*

^thm-20-1

> [!proof]+ Proof
> Write $E = e^{-bt/(2a)}$, so $E' = -\frac{b}{2a}E$, and try
>
> $$
> y = v(t)y_1(t) = v(t)E . \qquad (13)
> $$
>
> Then
>
> $$
> y' = v'E - \frac{b}{2a}vE, \qquad (14) \qquad\qquad y'' = v''E - \frac{b}{a}v'E + \frac{b^2}{4a^2}vE . \qquad (15)
> $$
>
> Substituting in (1),
>
> $$
> \Big[a\Big(v'' - \frac{b}{a}v' + \frac{b^2}{4a^2}v\Big) + b\Big(v' - \frac{b}{2a}v\Big) + cv\Big]E = 0 . \qquad (16)
> $$
>
> Cancel the nonzero factor $E$ and collect terms:
>
> $$
> av'' + (-b + b)v' + \Big(\frac{b^2}{4a} - \frac{b^2}{2a} + c\Big)v = 0 . \qquad (17)
> $$
>
> The coefficient of $v'$ is $0$, and the coefficient of $v$ is $c - \frac{b^2}{4a} = \frac{4ac - b^2}{4a} = 0$ because $b^2 - 4ac = 0$. So (17) reduces to $v'' = 0$, whose solutions are $v(t) = c_1 + c_2t$. From (13),
>
> $$
> y = c_1E + c_2tE ,
> $$
>
> so $y$ is a linear combination of the two solutions (19). Their Wronskian is
>
> $$
> W[y_1, y_2](t) = \begin{vmatrix} E & tE \\ -\frac{b}{2a}E & \big(1 - \frac{bt}{2a}\big)E \end{vmatrix} = E^2\Big(1 - \frac{bt}{2a} + \frac{bt}{2a}\Big) = E^2 = e^{-bt/a} ,
> $$
>
> which is never zero. So $y_1$, $y_2$ form a fundamental set and (18) is the general solution by [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|Theorem §18.4]].

^pf-20-1

*Uses:* [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^def-18-2|Def. §18.2]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|§18.4]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^def-18-3|Def. §18.3]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^def-18-4|Def. §18.4]]

> [!example] Example §24.1: A Repeated Root
> Solve $y'' - 8y' + 16y = 0$, $y(0) = -3$, $y'(0) = 2$.
>
> $r^2 - 8r + 16 = (r - 4)^2 = 0$ has the repeated root $r = 4$, so by [[§20 Repeated Roots; Reduction of Order#^thm-20-1|Theorem §20.1]]
>
> $$
> y = c_1e^{4t} + c_2te^{4t}, \qquad y' = 4c_1e^{4t} + c_2e^{4t} + 4c_2te^{4t} .
> $$
>
> $y(0) = c_1 = -3$ and $y'(0) = 4c_1 + c_2 = -12 + c_2 = 2$, so $c_2 = 14$ and
>
> $$
> y = -3e^{4t} + 14te^{4t} = (14t - 3)e^{4t} .
> $$
>
> *Source: 331 Written HW 3, Problem 3*

^ex-20-1

> [!example] Example §24.2: A Critical Initial Slope
> Solve $y'' - y' + \frac{y}{4} = 0$, $y(0) = 2$, $y'(0) = \frac13$. (21)
>
> The characteristic equation $r^2 - r + \frac14 = (r - \frac12)^2 = 0$ has the repeated root $r_1 = r_2 = \frac12$, so the general solution is
>
> $$
> y = c_1e^{t/2} + c_2te^{t/2} . \qquad (22)
> $$
>
> The first initial condition gives $y(0) = c_1 = 2$. Differentiating (22) and setting $t = 0$, $y'(0) = \frac12c_1 + c_2 = \frac13$, so $c_2 = -\frac23$ and
>
> $$
> y = 2e^{t/2} - \tfrac23te^{t/2} . \qquad (23)
> $$
>
> This solution rises slightly, then crosses the axis at $t = 3$ (where $2 - \frac23t = 0$) and tends to $-\infty$. With the initial slope changed to $y'(0) = 2$, instead $c_2 = 1$ and $y = 2e^{t/2} + te^{t/2}$, which increases without bound.
>
> **The critical slope.** BDP's figure suggests a critical initial slope between $\frac13$ and $2$ that separates the two behaviors (BDP leaves it as Problem 3.4.12). With $y'(0) = b$, $c_2 = b - 1$ and
>
> $$
> y = \big(2 + (b - 1)t\big)e^{t/2} .
> $$
>
> For $b \ge 1$ the factor $2 + (b - 1)t$ stays positive for $t > 0$ (and $y' = e^{t/2}\big(b + \frac12(b - 1)t\big) > 0$), so $y$ increases to $+\infty$. For $b < 1$ the factor vanishes at $t = 2/(1 - b)$ and $y$ eventually becomes negative and tends to $-\infty$. The critical slope is $b = 1$, where $y = 2e^{t/2}$.
>
> *BDP: Example 3.4.2*

^ex-20-2

![[m331-16-1.svg]]
*[[§20 Repeated Roots; Reduction of Order#^ex-20-2|Example §20.2]]: solutions of $y'' - y' + \frac{y}{4} = 0$ with $y(0) = 2$ and $y'(0) = b$, namely $y = (2 + (b - 1)t)e^{t/2}$. The linear factor decides the sign and the exponential decides the size. For $b = \frac13$ the factor vanishes at $t = 3$; for $b = 0.8$ it would vanish at $t = 10$, beyond the picture, after which that solution too heads to $-\infty$. The critical slope $b = 1$ gives the pure exponential $2e^{t/2}$, the boundary between the two behaviors.*

> [!remark] Remark: Behavior as t → ∞
> The asymptotic behavior with a repeated root is like that for distinct real roots ([[§17 Homogeneous Differential Equations with Constant Coefficients#^rem-17-1|§17, Remark: Behavior as t → ∞]]). If the repeated root is negative, every solution decays to $0$; if it is positive, every nonzero solution grows in magnitude without bound. The linear factor $t$ has little influence: the exponential decides growth or decay. If the repeated root is zero, the equation is $y'' = 0$ and the general solution is a linear function of $t$.

^rem-20-2

## Summary

> [!theorem] Theorem §24.2: General Solution of ay″ + by′ + cy = 0
> Let $r_1$ and $r_2$ be the roots of the characteristic equation
>
> $$
> ar^2 + br + c = 0 \qquad (25)
> $$
>
> of the equation with constant coefficients
>
> $$
> ay'' + by' + cy = 0 . \qquad (24)
> $$
>
> - If $r_1$ and $r_2$ are real but not equal, the general solution of (24) is
>
> $$
> y = c_1e^{r_1t} + c_2e^{r_2t} . \qquad (26)
> $$
>
> - If $r_1$ and $r_2$ are complex conjugates $\lambda \pm i\mu$, the general solution is
>
> $$
> y = c_1e^{\lambda t}\cos(\mu t) + c_2e^{\lambda t}\sin(\mu t) . \qquad (27)
> $$
>
> - If $r_1 = r_2$, the general solution is
>
> $$
> y = c_1e^{r_1t} + c_2te^{r_1t} . \qquad (28)
> $$
>
> *BDP: 3.4 (Summary), Equations (26)–(28)*

^thm-20-2

> [!proof]+ Proof
> The three cases are [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|Theorem §17.2]] (with [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-2|Example §18.2]] for the Wronskian), [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|Theorem §19.2]] and [[§20 Repeated Roots; Reduction of Order#^thm-20-1|Theorem §20.1]]. In each case the two functions form a fundamental set, so by [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|Theorem §18.4]] the combination contains every solution.

^pf-20-2

*Uses:* [[§17 Homogeneous Differential Equations with Constant Coefficients#^thm-17-2|§17.2]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-2|Ex. §18.2]], [[§19 Complex Roots of the Characteristic Equation#^thm-19-2|§19.2]], [[§20 Repeated Roots; Reduction of Order#^thm-20-1|§20.1]], [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-4|§18.4]]

> [!remark]- Connections
> - See also: [[§1★ Homogeneous Linear Equations#^thm-1-4|341 Thm. §1.4]] (the same three cases in Powers' review); in boundary value problems the three cases of $\phi'' - p\phi = 0$ ($p > 0$, $p = 0$, $p < 0$) decide which eigenvalues exist, [[§25 Example꞉ Fixed End Temperatures#^thm-25-2|341 Thm. §25.2]].

> [!remark] Remark: Method — Constant-Coefficient Homogeneous Equations
> To solve $ay'' + by' + cy = 0$, possibly with $y(t_0) = y_0$, $y'(t_0) = y_0'$:
> 1. Write down the characteristic equation $ar^2 + br + c = 0$ and find its roots (factor, complete the square, or use the quadratic formula). The sign of $b^2 - 4ac$ tells which case occurs.
> 2. Write the general solution from [[§20 Repeated Roots; Reduction of Order#^thm-20-2|Theorem §20.2]]: $c_1e^{r_1t} + c_2e^{r_2t}$ for distinct real roots, $e^{\lambda t}(c_1\cos\mu t + c_2\sin\mu t)$ for roots $\lambda \pm i\mu$, $(c_1 + c_2t)e^{r_1t}$ for a repeated root.
> 3. For an initial value problem, differentiate the general solution, set $t = t_0$ in $y$ and $y'$, and solve the two linear equations for $c_1$, $c_2$. They always have exactly one solution, because the Wronskian of the fundamental set is nonzero ([[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-3|Theorem §18.3]]).
> 4. Read off the behavior as $t \to \infty$ from the real parts of the roots: all negative means decay to $0$; a positive one means growth (unless its coefficient is $0$); complex roots mean oscillation.

^rem-20-3

> [!example] Example §24.3: Which Case Occurs?
> For which values of $\alpha$ does the characteristic equation of $y'' - 6y' + \alpha y = 0$ have two distinct real roots, two complex roots, one repeated real root?
>
> The characteristic equation $r^2 - 6r + \alpha = 0$ has discriminant $36 - 4\alpha$ and roots
>
> $$
> r = \frac{6 \pm \sqrt{36 - 4\alpha}}{2} = 3 \pm \sqrt{9 - \alpha} .
> $$
>
> - $\alpha < 9$: two distinct real roots $3 \pm \sqrt{9 - \alpha}$, and $y = c_1e^{(3 + \sqrt{9 - \alpha})t} + c_2e^{(3 - \sqrt{9 - \alpha})t}$.
> - $\alpha = 9$: the repeated root $r = 3$, and $y = c_1e^{3t} + c_2te^{3t}$.
> - $\alpha > 9$: complex roots $3 \pm i\sqrt{\alpha - 9}$, and $y = e^{3t}\big(c_1\cos(\sqrt{\alpha - 9}\,t) + c_2\sin(\sqrt{\alpha - 9}\,t)\big)$.
>
> The repeated root is the transition between the other two cases, as $\alpha$ passes through $9$.
>
> *Source: 331 Written HW 3, Problem 1*

^ex-20-3

## Reduction of Order

The procedure used for repeated roots works more generally. Suppose that one solution $y_1(t)$, not everywhere zero, of

$$
y'' + p(t)y' + q(t)y = 0 \qquad (29)
$$

is known.

> [!theorem] Proposition §24.3: Reduction of Order
> Let $y_1$ be a solution of (29), not everywhere zero. Then $y = v(t)y_1(t)$ (30) is a solution of (29) if and only if $v$ satisfies
>
> $$
> y_1v'' + (2y_1' + py_1)v' = 0 . \qquad (32)
> $$
>
> This is a first-order differential equation for the function $v'$.
>
> *BDP: 3.4 (text), Equation (32)*

^prop-20-3

> [!proof]+ Proof
> With $y = vy_1$,
>
> $$
> y' = v'y_1 + vy_1', \qquad y'' = v''y_1 + 2v'y_1' + vy_1'' .
> $$
>
> Substituting for $y$, $y'$ and $y''$ in (29) and collecting terms,
>
> $$
> y'' + py' + qy = y_1v'' + (2y_1' + py_1)v' + (y_1'' + py_1' + qy_1)v . \qquad (31)
> $$
>
> Since $y_1$ is a solution of (29), the coefficient of $v$ is zero, so $y$ solves (29) exactly when (32) holds.

^pf-20-3

*Uses:* [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^def-18-1|Def. §18.1]]

> [!remark]- Connections
> - Equation (32) is first-order linear and separable in $w = v'$, so it is solved by Stewart's integrating factor, [[§70 Linear Equations#^thm-70-1|Calc Thm. §70.1]], or by separation of variables, [[§68 Separable Equations#^thm-68-1|Calc Thm. §68.1]]. This subject's treatments: [[§5 Linear Differential Equations; Method of Integrating Factors#^thm-5-2|Theorem §5.2]] and [[§6 Separable Differential Equations#^thm-6-1|Theorem §6.1]].
> - See also: [[§2★ Variable Coefficients and Higher-Order Equations#^thm-2-2|341 Thm. §2.2]] (the same reduction in Powers' review), applied to a Legendre equation in [[§2★ Variable Coefficients and Higher-Order Equations#^ex-2-2|341 Ex. §2.2]] and to the second solution of Bessel's equation in [[§55★ Bessel's Equation#^thm-55-3|341 Thm. §55.3]].

> [!remark] Remark: Method — Reduction of Order
> To find a second solution of $y'' + p(t)y' + q(t)y = 0$ from a known solution $y_1$:
> 1. Put the equation in standard form, with coefficient $1$ for $y''$ (divide by the leading coefficient).
> 2. Substitute $y = v(t)y_1(t)$, $y' = v'y_1 + vy_1'$, $y'' = v''y_1 + 2v'y_1' + vy_1''$ and collect terms. The coefficient of $v$ must come out $0$; this is a useful check on the algebra.
> 3. Set $w = v'$ and solve the first-order equation $y_1w' + (2y_1' + py_1)w = 0$, as a linear or as a separable equation. (Separating variables gives $w = C\,e^{-\int p\,dt}/y_1^2$, a formula BDP does not write out.)
> 4. Integrate $w$ to get $v$, then $y = vy_1$. The constant of the last integration contributes a multiple of $y_1$ and can be dropped; the rest is a new solution $y_2$.
> 5. Check that $W[y_1, y_2] \ne 0$, so that $y_1$, $y_2$ form a fundamental set.
>
> The crucial step is solving a first-order equation for $v'$ instead of the original second-order equation for $y$, which is why the method is called **reduction of order**.

^rem-20-4

> [!example] Example §24.4: Reduction of Order with Variable Coefficients
> Given that $y_1(t) = t^{-1}$ is a solution of
>
> $$
> 2t^2y'' + 3ty' - y = 0, \qquad t > 0 , \qquad (33)
> $$
>
> find a fundamental set of solutions.
>
> Set $y = v(t)t^{-1}$; then
>
> $$
> y' = v't^{-1} - vt^{-2}, \qquad y'' = v''t^{-1} - 2v't^{-2} + 2vt^{-3} .
> $$
>
> Substituting in (33) and collecting terms,
>
> $$
> \begin{aligned}
> 2t^2\big(v''t^{-1} - 2v't^{-2} + 2vt^{-3}\big) + 3t\big(v't^{-1} - vt^{-2}\big) - vt^{-1}
> &= 2tv'' + (-4 + 3)v' + \big(4t^{-1} - 3t^{-1} - t^{-1}\big)v \\
> &= 2tv'' - v' = 0 . 
> \end{aligned} \qquad (34)
> $$
>
> The coefficient of $v$ is zero, as it should be. With $w = v'$ this is the separable equation $2tw' - w = 0$: $\frac{w'}{w} = \frac{1}{2t}$, so $\ln|w| = \frac12\ln t + \text{const}$ and
>
> $$
> w(t) = v'(t) = ct^{1/2}, \qquad v(t) = \tfrac23ct^{3/2} + k .
> $$
>
> Therefore
>
> $$
> y = v(t)t^{-1} = \tfrac23ct^{1/2} + kt^{-1} , \qquad (35)
> $$
>
> with arbitrary constants $c$ and $k$. The second term is a multiple of $y_1$; the first gives the new solution $y_2(t) = t^{1/2}$. Their Wronskian is
>
> $$
> W[y_1, y_2](t) = t^{-1} \cdot \tfrac12t^{-1/2} - \big(-t^{-2}\big)t^{1/2} = \tfrac32t^{-3/2} \ne 0 \quad\text{for } t > 0 , \qquad (36)
> $$
>
> so $y_1$ and $y_2$ form a fundamental set for $t > 0$. (These are the solutions of [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-5|Example §18.5]], found there by inspection. The formula in step 3 of the method agrees: $p = \frac{3}{2t}$, $e^{-\int p\,dt} = t^{-3/2}$ and $w = Ct^{-3/2}/t^{-2} = Ct^{1/2}$.)
>
> *BDP: Example 3.4.3*

^ex-20-4
