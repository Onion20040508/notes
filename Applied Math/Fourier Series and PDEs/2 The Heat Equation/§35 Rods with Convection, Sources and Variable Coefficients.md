---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 35
tags: [fourier-series-and-pdes, math341]
---
← [[§34★ The Error Function]] · ↑ [[· 2 The Heat Equation]] · [[§36 Heated Section, Half Sine Wave, One-Sided Exponential and Gaussian]] →

*Chapter 2 examples revisited, finite rods: the rods and eigenvalue problems that the chapter carries from one section to the next.*

## The Rod with a Uniform Heat Source

The rod $u_{xx} + K = u_t$ with $u(0, t) = T$ and $u_x(a, t) = 0$ is first used to read off the types of boundary condition, then reduced by its parabolic steady state $v = -\frac12Kx^2 + Kax + T$ to a transient problem without the source, and finally solved in the eigenfunctions of a rod with one fixed and one insulated end.

![[§23 Initial and Boundary Conditions; Diffusion#^ex-23-1]]

![[§24 Steady-State Temperatures#^ex-24-4]]

![[§27 Example꞉ Different Boundary Conditions#^ex-27-3]]

## The Rod with Lateral Convection

A rod that loses heat through its lateral surface gains the term $-\gamma^2(u - T)$ in its equation. Its steady state is not a straight line, and its transient is the fixed-end solution multiplied by the uniform decay $e^{-\gamma^2t}$.

![[§23 Initial and Boundary Conditions; Diffusion#^ex-23-3]]

![[§24 Steady-State Temperatures#^ex-24-5]]

![[§25 Example꞉ Fixed End Temperatures#^ex-25-4]]

*Chain: later in [[§63★ Insulated Disk, Cooled Plate and Step Function#The Cooled Plate|Chapter 5]] (a plate cooled through its faces)*

## The Convection Eigenfunctions

Convection at the end $x = a$ gives the eigenfunctions $\sin(\lambda_nx)$ with $\tan(\lambda_na) = -\kappa\lambda_n/h$. The chapter computes the coefficients for the rod that starts from zero temperature, verifies the norms and the orthogonality by direct integration, and treats the eigenfunctions as a generalized Fourier basis.

![[§28 Example꞉ Convection#^ex-28-2]]

![[§29 Sturm–Liouville Problems#^ex-29-3]]

![[§30 Expansion in Series of Eigenfunctions#^ex-30-1]]

## The Logarithmic Sine Eigenfunctions

Separating $w_t = x(xw_x)_x$ on $1 < x < b$ with fixed ends gives the eigenvalue problem $x(x\phi')' = \mu\phi$, whose eigenfunctions $\sin(n\pi\ln x/\ln b)$ are ordinary sines in the variable $\ln x$; they form a generalized Fourier basis with weight $1/x$.

![[§29 Sturm–Liouville Problems#^ex-29-4]]

![[§30 Expansion in Series of Eigenfunctions#^ex-30-2]]

*Chain: later in [[§43 Plucked, Struck, Midterm, Hanging and Nonuniform Strings#The Nonuniform Musical String|Chapter 3]] (the same eigenvalue problem for a string)*

## The Rod with Neumann and Robin Ends

Homework 7, Problem 2 runs over two sections: the eigenvalue problem $\phi'' = \mu\phi$, $\phi'(0) = 0$, $\phi'(2) + \phi(2) = 0$ is solved and $x^2$ is expanded in its eigenfunctions $\cos(\lambda_nx)$, and then the heat problem is solved with them.

![[§30 Expansion in Series of Eigenfunctions#^ex-30-3]]

![[§31 Generalities on the Heat Conduction Problem#^ex-31-1]]
