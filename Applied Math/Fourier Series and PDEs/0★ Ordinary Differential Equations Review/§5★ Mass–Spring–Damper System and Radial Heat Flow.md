---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: 0
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§5★ Green's Functions]] · ↑ [[· 0★ Ordinary Differential Equations Review]] →

*Chapter 0 examples revisited: the mass–spring–damper system and radial heat flow in a rod, followed through the chapter.*
★ *Beyond MAT 341: the course did not cover these examples; they are gathered from the sections above.*

## The Mass–Spring–Damper System

The equation $u'' + bu' + \omega^2u = 0$ of a mass on a spring with a damper is the model constant-coefficient equation: its characteristic roots sort the free motion into the undamped, underdamped, critically damped and overdamped cases. Driven by a sinusoidal force it shows beats and resonance, and without damping, variation of parameters writes the response to any force $f$ as the integral of $f$ against $\frac1\gamma\sin\gamma(t - z)$.

![[§1★ Homogeneous Linear Equations#^ex-1-2]]

![[§2★ Nonhomogeneous Linear Equations#^ex-2-3]]

![[§2★ Variation of Parameters#^ex-2-5]]

*Chain: later in [[§16★ Applications of Fourier Series and Integrals#^ex-16-1|Chapter 1]] (driven by a square wave) · [[§52★ Partial Fractions and Convolutions#^ex-52-3|Chapter 6]] (by Heaviside's formula)*

## Radial Heat Flow

Heat flowing radially in a long cylindrical bar that carries a current obeys $\frac1r(ru')' = -H$, whose coefficient $1/r$ is singular on the axis; boundedness at $r = 0$ takes the place of a boundary condition. The Green's function of the same operator on $0 < x < 1$, with $u$ bounded at $0$ and $u(1) = 0$, reproduces that solution.

![[§4★ Singular Boundary Value Problems#^ex-4-2]]

![[§5★ Green's Functions#^ex-5-4]]
