---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 0
section: "8★"
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§7★ Green's Functions]] · ↑ [[· 0★ Ordinary Differential Equations Review]] · [[§9 Periodic Functions and Fourier Series]] →

*Chapter 0 examples revisited: the mass–spring–damper system and radial heat flow in a rod, followed through the chapter.*
★ *Beyond MAT 341: the course did not cover these examples; they are gathered from the sections above.*

## The Mass–Spring–Damper System

The equation $u'' + bu' + \omega^2u = 0$ of a mass on a spring with a damper is the model constant-coefficient equation: its characteristic roots sort the free motion into the undamped, underdamped, critically damped and overdamped cases. Driven by a sinusoidal force it shows beats and resonance, and without damping, variation of parameters writes the response to any force $f$ as the integral of $f$ against $\frac1\gamma\sin\gamma(t - z)$.

![[§1★ Homogeneous Linear Equations#^ex-1-2]]

![[§3★ Nonhomogeneous Linear Equations#^ex-3-3]]

![[§4★ Variation of Parameters#^ex-4-2]]

*Chain: later in [[§20★ Applications of Fourier Series and Integrals#^ex-20-1|Chapter 1]] (driven by a square wave) · [[§65★ Partial Fractions and Convolutions#^ex-65-3|Chapter 6]] (by Heaviside's formula)*

## Radial Heat Flow

Heat flowing radially in a long cylindrical bar that carries a current obeys $\frac1r(ru')' = -H$, whose coefficient $1/r$ is singular on the axis; boundedness at $r = 0$ takes the place of a boundary condition. The Green's function of the same operator on $0 < x < 1$, with $u$ bounded at $0$ and $u(1) = 0$, reproduces that solution.

![[§6★ Singular Boundary Value Problems#^ex-6-2]]

![[§7★ Green's Functions#^ex-7-4]]
