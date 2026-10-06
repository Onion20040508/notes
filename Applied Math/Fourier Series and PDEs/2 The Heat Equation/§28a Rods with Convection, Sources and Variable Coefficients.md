---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 2
section: 0
tags: [fourier-series-and-pdes, math341]
---
← [[§28★ The Error Function]] · ↑ [[· 2 The Heat Equation]] →

*Chapter 2 examples revisited, finite rods: the rods and eigenvalue problems that the chapter carries from one section to the next.*

## The Rod with a Uniform Heat Source

The rod $u_{xx} + K = u_t$ with $u(0, t) = T$ and $u_x(a, t) = 0$ is first used to read off the types of boundary condition, then reduced by its parabolic steady state $v = -\frac12Kx^2 + Kax + T$ to a transient problem without the source, and finally solved in the eigenfunctions of a rod with one fixed and one insulated end.

![[§17a Initial and Boundary Conditions; Diffusion#^ex-17-2]]

![[§18 Steady-State Temperatures#^ex-18-4]]

![[§21 Example꞉ Different Boundary Conditions#^ex-21-3]]

## The Rod with Lateral Convection

A rod that loses heat through its lateral surface gains the term $-\gamma^2(u - T)$ in its equation. Its steady state is not a straight line, and its transient is the fixed-end solution multiplied by the uniform decay $e^{-\gamma^2t}$.

![[§17a Initial and Boundary Conditions; Diffusion#^ex-17-4]]

![[§18 Steady-State Temperatures#^ex-18-5]]

![[§19 Example꞉ Fixed End Temperatures#^ex-19-4]]

*Chain: later in [[§51★ Insulated Disk, Cooled Plate and Step Function#The Cooled Plate|Chapter 5]] (a plate cooled through its faces)*

## The Convection Eigenfunctions

Convection at the end $x = a$ gives the eigenfunctions $\sin(\lambda_nx)$ with $\tan(\lambda_na) = -\kappa\lambda_n/h$. The chapter computes the coefficients for the rod that starts from zero temperature, verifies the norms and the orthogonality by direct integration, and treats the eigenfunctions as a generalized Fourier basis.

![[§22 Example꞉ Convection#^ex-22-2]]

![[§23 Sturm–Liouville Problems#^ex-23-3]]

![[§24 Expansion in Series of Eigenfunctions#^ex-24-1]]

## The Logarithmic Sine Eigenfunctions

Separating $w_t = x(xw_x)_x$ on $1 < x < b$ with fixed ends gives the eigenvalue problem $x(x\phi')' = \mu\phi$, whose eigenfunctions $\sin(n\pi\ln x/\ln b)$ are ordinary sines in the variable $\ln x$; they form a generalized Fourier basis with weight $1/x$.

![[§23 Sturm–Liouville Problems#^ex-23-4]]

![[§24 Expansion in Series of Eigenfunctions#^ex-24-2]]

*Chain: later in [[§34a Plucked, Struck, Midterm, Hanging and Nonuniform Strings#The Nonuniform Musical String|Chapter 3]] (the same eigenvalue problem for a string)*

## The Rod with Neumann and Robin Ends

Homework 7, Problem 2 runs over two sections: the eigenvalue problem $\phi'' = \mu\phi$, $\phi'(0) = 0$, $\phi'(2) + \phi(2) = 0$ is solved and $x^2$ is expanded in its eigenfunctions $\cos(\lambda_nx)$, and then the heat problem is solved with them.

![[§24 Expansion in Series of Eigenfunctions#^ex-24-3]]

![[§25 Generalities on the Heat Conduction Problem#^ex-25-1]]
