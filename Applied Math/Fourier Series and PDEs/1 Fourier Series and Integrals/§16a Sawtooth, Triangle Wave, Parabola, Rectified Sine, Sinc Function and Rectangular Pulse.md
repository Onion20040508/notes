---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 0
tags: [fourier-series-and-pdes, math341]
---
← [[§16★ Applications of Fourier Series and Integrals]] · ↑ [[· 1 Fourier Series and Integrals]] →

*Chapter 1 examples revisited: six functions that the chapter expands again and again, each followed from section to section.*

## The Sawtooth

The sawtooth, $f(x) = x$ on $-\pi < x < \pi$ extended with period $2\pi$, is the first Fourier series of the course, $\sum 2(-1)^{n+1}\sin(nx)/n$. It returns rescaled to period $2$ and as the odd extension of $x$ on $0 < x < 1$, as the standard function with a jump where the series converges to the average (it is also a test case in [[§8 Convergence of Fourier Series#^ex-8-2|Example §8.2]](c) and [[§9 Uniform Convergence#^ex-9-3|Example §9.3]](a): sectionally smooth, but its series does not converge uniformly), and then it is integrated term by term to sum $\sum 1/n^2$ and $\sum 1/n^4$ and checked against Parseval's equality.

![[§6 Periodic Functions and Fourier Series#^ex-6-1]]

![[§6 Periodic Functions and Fourier Series#^ex-6-2]]

![[§7a Even and Odd Functions; Half-Range Expansions#^ex-7-3]]

![[§8 Convergence of Fourier Series#^ex-8-3]]

![[§10 Operations on Fourier Series#^ex-10-1]]

![[§11★ Mean Error and Convergence in Mean#^ex-11-1]]

*Chain: later in [[§34a Plucked, Struck, Midterm, Hanging and Nonuniform Strings#The Midterm String|Chapter 3]] (the sine series of the initial displacement)*

## The Triangle Wave

The triangle wave, $|x|$ on $-\pi < x < \pi$ extended with period $2\pi$, is continuous with corners, so its cosine series converges uniformly. Differentiating that series term by term gives the series of the square wave, and in the proof of convergence the triangle wave is the model of a corner.

![[§9 Uniform Convergence#^ex-9-2]]

![[§10 Operations on Fourier Series#^ex-10-2]]

![[§12★ Proof of Convergence#^ex-12-1]]

*Chain: later in [[§50★ Legendre Series and Zonal Harmonics#^ex-49-3|Chapter 5]] (its Legendre series)*

## The Parabola

Given on a half interval, $x^2$ has an odd extension that jumps and an even extension that is continuous with corners. The chapter computes both series on $0 < x < 1$ and on $0 < x < \pi$, tests term-by-term differentiation on each, sums $\sum 1/n^4 = \pi^4/90$ from the even series by Parseval's equality, and uses the exact coefficients to judge four numerical samples; [[§9 Uniform Convergence#^ex-9-5|Example §9.5]] recovers a quadratic from its cosine series.

![[§7a Even and Odd Functions; Half-Range Expansions#^ex-7-4]]

![[§10 Operations on Fourier Series#^ex-10-3]]

![[§11★ Mean Error and Convergence in Mean#^ex-11-2]]

![[§13★ Numerical Determination of Fourier Coefficients#^ex-13-1]]

## The Rectified Sine

The rectified sine $|\sin x|$ is even and continuous with corners at the multiples of $\pi$. The chapter expands $|\sin(\pi x)|$ with period $1$, uses $|\sin x|$ as a function whose series converges uniformly ([[§9 Uniform Convergence#^ex-9-3|Example §9.3]](b)), and expands $|\sin x|$ with period $\pi$, checking pointwise and uniform convergence.

![[§7 Arbitrary Period and Half-Range Expansions#^ex-7-1]]

![[§9 Uniform Convergence#^ex-9-4]]

## The Sinc Function

The function $\sin(x)/x$ on $-\pi < x < \pi$, with the value $1$ at $0$ and extended with period $2\pi$, is continuous with a continuous derivative inside the period, so its Fourier series converges at every point and, the extension being continuous, uniformly ([[§9 Uniform Convergence#^ex-9-3|Example §9.3]](c)). Its cosine coefficients are then approximated from samples.

![[§8 Convergence of Fourier Series#^ex-8-5]]

![[§13★ Numerical Determination of Fourier Coefficients#^ex-13-2]]

## The Rectangular Pulse

The pulse equal to $1$ on an interval about the origin and $0$ outside is the basic Fourier integral; the complex form gives the same representation.

![[§14 Fourier Integral#^ex-14-2]]

![[§15★ Complex Methods#^ex-15-2]]

*Chain: later in [[§28b Heated Section, Half Sine Wave, One-Sided Exponential and Gaussian#The Heated Section|Chapter 2]] (as an initial temperature)*
