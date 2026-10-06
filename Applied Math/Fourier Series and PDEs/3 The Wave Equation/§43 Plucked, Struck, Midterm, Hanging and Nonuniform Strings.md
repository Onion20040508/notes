---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 3
section: 43
tags: [fourier-series-and-pdes, math341]
---
← [[§42★ Wave Equation in Unbounded Regions]] · ↑ [[· 3 The Wave Equation]] · [[§44 Potential Equation]] →

*Chapter 3 examples revisited: five strings that the chapter sets up in one section and solves, or solves again by another method, in the next.*

## The Plucked String

The string lifted at its midpoint to height $h$ and released has a tent-shaped initial displacement; its sine coefficients $8h\sin(n\pi/2)/(n^2\pi^2)$ decay like $1/n^2$.

![[§37 The Vibrating String#^ex-37-3]]

![[§38 Solution of the Vibrating String Problem#^ex-38-1]]

*Chain: later in [[§45 Potential in a Rectangle#^ex-45-1|Chapter 4]] (as boundary data) · [[§73★ The Tent Function|Chapter 7]] (numerically)*

## The Struck Piano String

A hammer gives the string at rest the same tent-shaped initial velocity ([[§37 The Vibrating String#^ex-37-3|Example §37.3]](b)); the problem is solved by separation of variables and again by d'Alembert's method, and the two solutions agree.

![[§38 Solution of the Vibrating String Problem#^ex-38-3]]

![[§39 d'Alembert's Solution#^ex-39-2]]

## The Midterm String

The problem $u_{tt} = 4u_{xx}$ on $0 < x < \pi$ with fixed ends, $u(x, 0) = x$ and $u_t(x, 0) = \sin 2x$ (Midterm 2, Question 1) is solved by separation of variables and then by d'Alembert's method; the odd extension of the initial displacement is the sawtooth. [[§40 One-Dimensional Wave Equation꞉ Generalities#^ex-40-1|Example §40.1]] reuses its basic solutions.

![[§38 Solution of the Vibrating String Problem#^ex-38-2]]

![[§39 d'Alembert's Solution#^ex-39-1]]

*Chain: earlier in [[§21 Sawtooth, Triangle Wave, Parabola, Rectified Sine, Sinc Function and Rectangular Pulse#The Sawtooth|Chapter 1]] (the sawtooth)*

## The Hanging String

A string under gravity, or any constant force $F$, has the parabolic equilibrium shape $v = \frac F2(x^2 - ax)$; subtracting it reduces the full problem to a free string.

![[§37 The Vibrating String#^ex-37-2]]

![[§40 One-Dimensional Wave Equation꞉ Generalities#^ex-40-2]]

## The Nonuniform Musical String

The string $(xu_x)_x = u_{tt}/(c^2x)$ on $1 < x < 2$ has frequencies that are integer multiples of the fundamental, because $\xi = \ln x$ turns it into a uniform string; Rayleigh's estimate of its first eigenvalue is then tested against the known value.

![[§40 One-Dimensional Wave Equation꞉ Generalities#^ex-40-4]]

![[§41★ Estimation of Eigenvalues#^ex-41-2]]

*Chain: earlier in [[§35 Rods with Convection, Sources and Variable Coefficients#The Logarithmic Sine Eigenfunctions|Chapter 2]] (the same eigenvalue problem for a rod)*
