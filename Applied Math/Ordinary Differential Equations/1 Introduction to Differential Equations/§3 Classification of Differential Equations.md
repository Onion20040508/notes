---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 1
section: 3
bdp: "1.3"
aliases: ["BDP 1.3"]
tags: [ordinary-differential-equations, math331]
---
← [[§2 Solutions of Some Differential Equations]] · ↑ [[· 1 Introduction to Differential Equations]] · [[§4 Linear Differential Equations; Method of Integrating Factors]] →

*Boyce–DiPrima, Section 1.3 · MATH 331 Chapter 1 review sheet (derivation of the pendulum equation).*

Which method applies to a differential equation depends on what kind of equation it is, so this section sets up the vocabulary: ordinary versus partial, single equations versus systems, the order, and above all linear versus nonlinear. Linear equations have a highly developed theory, and much of the course is about them; nonlinear ones are harder, and are often studied through a linear approximation. The pendulum is the standard example of both: its equation is nonlinear, and for small swings it linearizes to the equation of simple harmonic motion. The section closes by defining what a solution is and naming the three basic questions about any equation: existence, uniqueness, and how to find the solution.

## Ordinary and Partial Differential Equations

> [!definition] Definition §3.1: Ordinary and Partial Differential Equations
> A differential equation is an **ordinary differential equation** if the unknown function depends on a single independent variable, so that only ordinary derivatives appear. It is a **partial differential equation** if the unknown function depends on several independent variables, so that the derivatives are partial derivatives.
>
> For example, the charge $Q(t)$ on a capacitor in a circuit with inductance $L$, resistance $R$ and capacitance $C$, driven by an impressed voltage $E(t)$, satisfies the ordinary differential equation
>
> $$
> L\,\frac{d^2Q(t)}{dt^2} + R\,\frac{dQ(t)}{dt} + \frac{1}{C}\,Q(t) = E(t) \qquad (1)
> $$
>
> (derived in [[§19 Mechanical and Electrical Vibrations#^prop-19-5|Proposition §19.5]]), while the **heat conduction equation** and the **wave equation**
>
> $$
> \alpha^2\,\frac{\partial^2 u(x, t)}{\partial x^2} = \frac{\partial u(x, t)}{\partial t} , \qquad (2)
> \qquad\qquad
> a^2\,\frac{\partial^2 u(x, t)}{\partial x^2} = \frac{\partial^2 u(x, t)}{\partial t^2} \qquad (3)
> $$
>
> are partial differential equations; $\alpha^2$ and $a^2$ are physical constants, and $u$ depends on $x$ and $t$. The first describes heat conduction in a solid body, the second wave motion in solids or fluids.
>
> *BDP: 1.3 (text)*

^def-3-1

> [!definition] Definition §3.2: System of Differential Equations
> If two or more unknown functions are to be determined, a **system of differential equations** is required. For example, the **Lotka–Volterra** (predator–prey) equations
>
> $$
> \frac{dx}{dt} = ax - \alpha xy , \qquad \frac{dy}{dt} = -cy + \gamma xy \qquad (4)
> $$
>
> govern the populations $x(t)$ of a prey species and $y(t)$ of a predator species; the positive constants $a, \alpha, c, \gamma$ come from observation of the particular species. Linear systems are the subject of Chapter 7 ([[§27 Introduction to Systems of First-Order Linear Equations|§27]]).
>
> *BDP: 1.3 (text)*

^def-3-2

## Order and Linearity

> [!definition] Definition §3.3: Order
> The **order** of a differential equation is the order of the highest derivative that appears in it. An ordinary differential equation of order $n$ is an equation
>
> $$
> F\big(t, u(t), u'(t), \ldots, u^{(n)}(t)\big) = 0 , \qquad (5)
> $$
>
> a relation between $t$, the unknown function $u$ and its first $n$ derivatives. Writing $y$ for $u(t)$, it becomes
>
> $$
> F\big(t, y, y', \ldots, y^{(n)}\big) = 0 . \qquad (6)
> $$
>
> BDP assumes throughout that such an equation can be solved for the highest derivative:
>
> $$
> y^{(n)} = f\big(t, y, y', y'', \ldots, y^{(n-1)}\big) . \qquad (8)
> $$
>
> *BDP: 1.3 (text)*

^def-3-3

> [!definition] Definition §3.4: Linear and Nonlinear Equations
> The ordinary differential equation $F(t, y, y', \ldots, y^{(n)}) = 0$ is **linear** if $F$ is a linear function of the variables $y, y', \ldots, y^{(n)}$ (it may depend on $t$ in any way). Thus the general linear ordinary differential equation of order $n$ is
>
> $$
> a_0(t)\,y^{(n)} + a_1(t)\,y^{(n-1)} + \cdots + a_n(t)\,y = g(t) . \qquad (11)
> $$
>
> An equation that is not of this form is **nonlinear**. A similar definition applies to partial differential equations.
>
> *BDP: 1.3 (text)*

^def-3-4

> [!remark]- Connections
> - The left side of (11) defines a map $y \mapsto a_0 y^{(n)} + \cdots + a_n y$ that is linear in the sense of linear algebra: it respects sums and scalar multiples ([[§8 Introduction to Linear Transformations#^def-8-3|235 Def. §8.3]]; [[§7 Vector Space of Linear Maps#^ladr-3-1|LADR 3.1]]). This is why the solutions of a linear homogeneous equation form a vector space (the Principle of Superposition, [[§14 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-14-2|Theorem §14.2]]).

> [!example] Example §3.1: Classifying Equations
> Classify the equations met so far.
>
> | equation | ODE/PDE | order | linear? |
> |---|---|---|---|
> | $m\,dv/dt = mg - \gamma v$ (falling object) | ODE | 1 | linear |
> | $dp/dt = rp - k$ (mice and owls) | ODE | 1 | linear |
> | $LQ'' + RQ' + Q/C = E(t)$, equation (1) | ODE | 2 | linear |
> | heat equation (2), wave equation (3) | PDE | 2 | linear |
> | $y''' + 2e^t y'' + yy' = t^4$ | ODE | 3 | nonlinear |
> | Lotka–Volterra system (4) | system of ODEs | 1 | nonlinear |
> | $\theta'' + (g/L)\sin\theta = 0$ (pendulum, equation (12)) | ODE | 2 | nonlinear |
>
> - In $y''' + 2e^t y'' + yy' = t^4$ the highest derivative is $y'''$, so the order is $3$. The coefficient $2e^t$ of $y''$ is harmless (coefficients may depend on $t$), and so is $t^4$; the product $yy'$ of the unknown function and its derivative is not linear in $(y, y')$, so the equation is nonlinear.
> - Each equation of (4) contains the product $xy$ of the two unknown functions, so the system is nonlinear.
> - In the pendulum equation, $\sin\theta$ is not a linear function of $\theta$.
>
> *BDP: 1.3 (text)*

^ex-3-1

> [!example] Example §3.2: One Equation, Two Normal Forms
> Write $(y')^2 + ty' + 4y = 0$ in the form (8).
>
> The equation is quadratic in $y'$. By the quadratic formula,
>
> $$
> y' = \frac{-t + \sqrt{t^2 - 16y}}{2} \qquad\text{or}\qquad y' = \frac{-t - \sqrt{t^2 - 16y}}{2} . \qquad (10)
> $$
>
> So one equation of the form (6) corresponds to *two* equations of the form (8), and a solution of the original equation may follow either branch (where $t^2 - 16y \ge 0$). Assuming (8) from the start avoids this ambiguity, which is the reason for BDP's convention.
>
> *BDP: 1.3 (text)*

^ex-3-2

## The Pendulum and Linearization

> [!theorem] Proposition §3.1: The Pendulum Equation
> A point mass $m$ hangs from a rigid weightless rod of length $L$ that swings in a vertical plane about a fixed support, with no friction or drag. If $\theta(t)$ is the angle of the rod from the downward vertical (counterclockwise positive), then
>
> $$
> \frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0 . \qquad (12)
> $$
>
> *BDP: 1.3, Equation (12); derivation in Problems 1.3.22–1.3.24*

^prop-3-1

> [!proof]+ Proof
> **By Newton's law in the tangential direction** (Problem 22). The mass moves on a circle of radius $L$ about the support. Two forces act on it: the tension in the rod, which points along the rod toward the support, and gravity, $mg$ straight down. Apply Newton's second law in the direction tangent to the circle, in the direction of increasing $\theta$; the tension is perpendicular to this direction and drops out.
> - *Acceleration.* The arc length from the rest position is $s = L\theta$, so the tangential (linear) acceleration is $s'' = L\,\theta''$.
> - *Gravity.* The unit tangent in the direction of increasing $\theta$ makes the angle $\theta$ with the horizontal, and its vertical component is $\sin\theta$ upward. So the tangential component of the downward force $mg$ is $-mg\sin\theta$: it pulls back toward $\theta = 0$ from either side.
>
> Newton's law gives $mL\,\theta'' = -mg\sin\theta$. Dividing by $mL$ gives (12).
>
> **By conservation of energy** (Problem 23). The speed of the mass is $|s'| = L|\theta'|$, so its kinetic energy is $T = \frac12 mL^2(\theta')^2$. Relative to the rest position the mass is raised by $L - L\cos\theta$, so its potential energy is $V = mgL(1 - \cos\theta)$. With no friction the total energy $E = T + V$ is constant, so
>
> $$
> 0 = \frac{dE}{dt} = mL^2\,\theta'\theta'' + mgL\sin\theta\,\theta' = mL^2\,\theta'\Big(\theta'' + \frac{g}{L}\sin\theta\Big) .
> $$
>
> Wherever $\theta' \ne 0$ this gives (12). (At isolated instants with $\theta' = 0$ it follows by continuity of $\theta''$ and $\sin\theta$; if $\theta' = 0$ on a whole interval the pendulum is at rest there, which this argument cannot detect. That is why the force derivation is the primary one.)
>
> **By angular momentum** (Problem 24). The rate of change of the angular momentum about the support equals the net external moment about it (positive counterclockwise). Place the support at the origin, so the mass is at $(L\sin\theta, -L\cos\theta)$ and has velocity $L\theta'(\cos\theta, \sin\theta)$. Its angular momentum about the support is
>
> $$
> M = m\big[(L\sin\theta)(L\theta'\sin\theta) - (-L\cos\theta)(L\theta'\cos\theta)\big] = mL^2\,\frac{d\theta}{dt} .
> $$
>
> The tension acts along the rod, through the support, so its moment is $0$. The moment of gravity $(0, -mg)$ is $(L\sin\theta)(-mg) - (-L\cos\theta)\cdot 0 = -mgL\sin\theta$. So $\dfrac{dM}{dt} = mL^2\,\theta'' = -mgL\sin\theta$, and dividing by $mL^2$ gives (12).

^pf-3-1

> [!definition] Definition §3.5: Linearization
> Approximating a nonlinear equation by a linear one is called **linearization**. For the pendulum, if $\theta$ is small then $\sin\theta \approx \theta$, and (12) is approximated by the linear equation
>
> $$
> \frac{d^2\theta}{dt^2} + \frac{g}{L}\,\theta = 0 . \qquad (13)
> $$
>
> *BDP: 1.3 (text)*

^def-3-5

![[m331-3-1.svg]]
*The pendulum released from rest at $\theta = \pi/3$: the nonlinear equation (12) (blue, numerical solution) and its linearization (13) (green, $\theta = \frac{\pi}{3}\cos\sqrt{g/L}\,t$). The linearization predicts the period $2\pi\sqrt{L/g}$; the true period at this amplitude is about $7\%$ longer ($6.74$ instead of $6.28$ in units of $\sqrt{L/g}$, gray marks), so the two drift out of phase.*

> [!remark] Remark: Why Linear Equations Come First
> The theory and methods for linear equations are highly developed, while for nonlinear equations the theory is more complicated and the methods less satisfactory. Fortunately many important problems lead to linear equations or can be approximated by them, as (13) approximates (12). Still, many phenomena cannot be represented adequately by linear equations. Most of this course is about linear equations; nonlinear ones appear in parts of Chapter 2 ([[§5 Separable Differential Equations|§5]], [[§8 Autonomous Differential Equations and Population Dynamics|§8]], [[§9 Exact Differential Equations and Integrating Factors|§9]]).

^rem-3-1

## Solutions

> [!definition] Definition §3.6: Solution on an Interval
> A **solution** of the $n$th order equation $y^{(n)} = f(t, y, y', \ldots, y^{(n-1)})$ (8) on the interval $\alpha < t < \beta$ is a function $\phi$ such that $\phi', \phi'', \ldots, \phi^{(n)}$ exist and
>
> $$
> \phi^{(n)}(t) = f\big(t, \phi(t), \phi'(t), \ldots, \phi^{(n-1)}(t)\big) \qquad (14)
> $$
>
> for every $t$ in $\alpha < t < \beta$. Unless stated otherwise, $f$ is real-valued and we look for real-valued solutions $y = \phi(t)$.
>
> *BDP: 1.3 (text)*

^def-3-6

> [!remark]- Connections
> - See also: [[§57 Modeling with Differential Equations#^def-57-6|Calc Def. §57.6]] (Stewart's definition of a solution) and [[§57 Modeling with Differential Equations#^rem-57-3|Calc Remark: Method — Checking a Proposed Solution]], the substitution check of [[§3 Classification of Differential Equations#^ex-3-3|Example §3.3]].

> [!example] Example §3.3: Verifying a Solution
> Show that $y_1(t) = \cos t$ and $y_2(t) = \sin t$ are solutions of $y'' + y = 0$ for all $t$.
>
> $y_1' = -\sin t$ and $y_1'' = -\cos t$, so $y_1'' + y_1 = -\cos t + \cos t = 0$. Likewise $y_2' = \cos t$, $y_2'' = -\sin t$, and $y_2'' + y_2 = 0$. Both hold on $-\infty < t < \infty$.
>
> In the same way $p(t) = 900 + ce^{t/2}$ solves $dp/dt = p/2 - 450$ ([[§2 Solutions of Some Differential Equations#^ex-2-1|Example §2.1]]): $p' = \frac{c}{2}e^{t/2}$ and $\frac{p}{2} - 450 = 450 + \frac{c}{2}e^{t/2} - 450$. Substitution cannot *find* solutions (there are far too many candidate functions), but it always *checks* a proposed one, and that check is worth making a habit. Note that $y'' + y = 0$ is the linearized pendulum (13) with $g/L = 1$.
>
> *BDP: 1.3 (text)*

^ex-3-3

> [!remark] Remark: Three Fundamental Questions
> 1. **Existence.** Does an equation (8) always have a solution? No: merely writing an equation down does not guarantee a solution. Existence theorems give conditions on $f$ under which solutions exist. This matters in practice: a problem with no solution should be recognized before effort is spent on it, and a sensible physical problem should lead to an equation that has a solution, which gives a check on the model.
> 2. **Uniqueness.** If solutions exist, how many are there, and what extra conditions single one out? A solution with an arbitrary constant, such as $p = 900 + ce^{t/2}$, is pinned down by an initial condition, but that alone does not rule out *other* solutions with the same initial value. If the problem is known to have a unique solution, then finding one solves it completely.
> 3. **Determination.** Can a solution actually be found, and how? Finding one also settles existence. But most solutions cannot be expressed in elementary functions, so both exact methods for simple equations and approximation methods for harder ones are needed; without existence theory, a computer might "approximate" a solution that does not exist.
>
> The answers for first-order equations are the existence and uniqueness theorems: for linear equations [[§7 Differences Between Linear and Nonlinear Differential Equations#^thm-7-1|Theorem §7.1]] (Theorem 2.4.1), and for nonlinear ones Theorem 2.4.2, stated in [[§7 Differences Between Linear and Nonlinear Differential Equations|§7]] and proved as [[§11 The Existence and Uniqueness Theorem#^thm-11-8|Theorem §11.8]].

^rem-3-2

> [!remark]- Remark: Technology
> Numerical algorithms ([[§10 Numerical Approximations꞉ Euler's Method|§10]]) approximate solutions of a wide range of equations to high accuracy within seconds, and graphical displays are often far more illuminating than tables of numbers or complicated formulas. Packages such as Maple, Mathematica and MATLAB perform numerical, graphical and symbolic computations, often solving an equation with a single command. BDP's advice: understand how the methods work by working examples in detail, then use computational tools for routine work, and combine numerical, graphical and analytical methods to understand both the solution and the process it models.

^rem-3-3
