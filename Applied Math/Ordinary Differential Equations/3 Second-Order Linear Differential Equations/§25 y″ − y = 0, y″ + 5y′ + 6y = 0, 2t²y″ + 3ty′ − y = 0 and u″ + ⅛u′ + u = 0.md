---
type: section
subject: "[[Ordinary Differential Equations]]"
chapter: 3
section: 25
tags: [ordinary-differential-equations, math331]
---
← [[§24 Forced Periodic Vibrations]] · ↑ [[· 3 Second-Order Linear Differential Equations]] · [[§26 Definition of the Laplace Transform]] →

*The equations of Chapter 3 that are solved in one section and taken up again with later theory, gathered in course order. The items themselves stay in their sections.*

## The Equation $y'' - y = 0$

The first constant-coefficient equation, solved by the exponentials $e^t$ and $e^{-t}$:

![[§17 Homogeneous Differential Equations with Constant Coefficients#^ex-17-1]]

The fundamental set that [[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^thm-18-5|Theorem §18.5]] specifies at $t_0 = 0$ is $\cosh t$, $\sinh t$:

![[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-4]]

## The Equation $y'' + 5y' + 6y = 0$

Two decaying exponentials from the characteristic equation:

![[§17 Homogeneous Differential Equations with Constant Coefficients#^ex-17-2]]

Their Wronskian is never zero, so they form a fundamental set:

![[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-2]]

## The Equation $2t^2y'' + 3ty' - y = 0$, $t > 0$

The solutions $t^{1/2}$ and $t^{-1}$ form a fundamental set, and their Wronskian agrees with Abel's formula:

![[§18 Solutions of Linear Homogeneous Equations; the Wronskian#^ex-18-5]]

Starting from $y_1 = t^{-1}$ alone, reduction of order recovers a second solution:

![[§20 Repeated Roots; Reduction of Order#^ex-20-4]]

## The Spring $u'' + \frac18 u' + u = 0$

A spring–mass system with small damping, free:

![[§23 Mechanical and Electrical Vibrations#^ex-23-4]]

The same system driven by the periodic force $3\cos(\omega t)$:

![[§24 Forced Periodic Vibrations#^ex-24-2]]

*Chain: later in [[§33 Introduction to Systems of First-Order Linear Equations#^ex-33-2|Chapter 7]] (the same equation as a first-order system).*
