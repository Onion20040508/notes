---
type: chapter
subject: "[[Thermal and Statistical Physics]]"
level: C
chapter: C4a
tags: [chapter, thermal-and-statistical-physics]
---
# C4a Entropy and Ensembles
← [[· C3 Classical and Quantum Microstates]] · ↑ [[Thermal and Statistical Physics]]

**Builds on:** [[· B3 Thermodynamic Potentials|B3 Thermodynamic Potentials]] (3), [[· B4 Probability and Fluctuations|B4 Probability and Fluctuations]] (3), [[· B6 The Microcanonical Ensemble and Entropy|B6 The Microcanonical Ensemble and Entropy]] (3), [[· B7 The Canonical and Grand Canonical Ensembles|B7 The Canonical and Grand Canonical Ensembles]] (9), [[· C1 Thermodynamics after Carathéodory|C1 Thermodynamics after Carathéodory]] (8), [[· C2 The Fundamental Assumption|C2 The Fundamental Assumption]] (12), [[· C3 Classical and Quantum Microstates|C3 Classical and Quantum Microstates]] (6)
**Used by:** —

Mao's Chapter 4, first half. Shannon's entropy, Jaynes's maximum-entropy principle, the canonical and grand-canonical ensembles, their potentials as Legendre transforms of the entropy, and fluctuations.

## Sections
- [[§C4a.1 Shannon Entropy]] — Mao §4.1; Lectures 9/22, 9/24; PS4 P2
- [[§C4a.2 The Entropy of a Statistical State]] — Mao §4.2; Lecture 9/24
- [[§C4a.3 Maximum Entropy and Lagrange Multipliers]] — Mao §4.3.1–4.3.3; Lectures 9/24, 9/29
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy]] — Mao §4.3.4; Lecture 9/29
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles]] — Mao §4.3.5–4.3.6; Lectures 9/29, 10/1; PS4 P3
- [[§C4a.6 Massieu Functions and Thermodynamic Potentials]] — Mao §4.3.7; Lecture 10/1
- [[§C4a.7 Heat, Work and the Clausius Equality]] — Mao §4.3.8; Lecture 10/1
- [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy]] — Mao §4.3.9–4.3.10; Lecture 10/1
- [[§C4a.9★ Density of States, Laplace and Legendre]] — Mao §4.4.1–4.4.3 (optional reading)
- [[§C4a.10 Ensembles at a Glance and Fluctuations]] — Mao §4.4.4; PS5 P2
- [[§C4a.11 A Coin, a Polymer, an Einstein Solid and Adsorption]] — PS4 P2, PS5 P1, P3, P4, official solutions

## Principles
- [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^pr-c4a-3-1|§C4a.3.1]] Jaynes's Maximum-Entropy Principle

## Theorems
- [[§C4a.1 Shannon Entropy#^thm-c4a-1-1|§C4a.1.1]] Shannon's Entropy Is the Only Such Measure
- [[§C4a.1 Shannon Entropy#^thm-c4a-1-2|§C4a.1.2]] The Uniform Distribution Has the Most Uncertainty
- [[§C4a.1 Shannon Entropy#^thm-c4a-1-3|§C4a.1.3]] Shannon's Source-Coding Bound
- [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-2|§C4a.3.2]] The Microcanonical Ensemble Maximizes Entropy in a Shell
- [[§C4a.3 Maximum Entropy and Lagrange Multipliers#^thm-c4a-3-3|§C4a.3.3]] Maximum Entropy with Mean Constraints Is Exponential
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-2|§C4a.4.2]] Assignments with Given Populations
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-3|§C4a.4.3]] The Most Probable Fractions Are the MaxEnt Probabilities
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^lem-c4a-4-4|§C4a.4.4]] The Count Splits into Which List and Which Assignment
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-5|§C4a.4.5]] The Collection's Entropy Is $M$ Times the Maximum
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^thm-c4a-4-6|§C4a.4.6]] Maximum Shannon Entropy Is Thermodynamic Entropy
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-1|§C4a.5.1]] The Energy Multiplier Is $\beta$
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-2|§C4a.5.2]] The Canonical Ensemble
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-3|§C4a.5.3]] The Particle Multiplier Is $-\beta\mu$
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-4|§C4a.5.4]] The Grand-Canonical Ensemble
- [[§C4a.5 The Canonical and Grand-Canonical Ensembles#^thm-c4a-5-5|§C4a.5.5]] Canonical and Grand-Canonical Weights from a Reservoir
- [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-1|§C4a.6.1]] The Maximum Entropy in Terms of $Z$
- [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-2|§C4a.6.2]] Canonical: $\ln Z = -\beta F$
- [[§C4a.6 Massieu Functions and Thermodynamic Potentials#^thm-c4a-6-3|§C4a.6.3]] Grand Canonical: $\ln\Xi = -\beta\Phi$
- [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-1|§C4a.7.1]] Heat Moves Populations, Work Moves Levels
- [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-2|§C4a.7.2]] The Clausius Equality from Maximum Entropy
- [[§C4a.7 Heat, Work and the Clausius Equality#^thm-c4a-7-3|§C4a.7.3]] With Particle Exchange
- [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^thm-c4a-8-1|§C4a.8.1]] Classical and Quantum Forms of the MaxEnt State
- [[§C4a.8 Classical and Quantum Forms; Entanglement Entropy#^thm-c4a-8-2|§C4a.8.2]] Entanglement Entropy of a Pure Whole
- [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-1|§C4a.9.1]] The Partition Function Is a Laplace Transform
- [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-2|§C4a.9.2]] The Grand Partition Function Sums over $N$
- [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-3|§C4a.9.3]] The Scaled Logarithm of a Laplace Transform Is a Legendre Transform
- [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-4|§C4a.9.4]] $\ln Z$ as a Legendre Transform of the Shell Entropy
- [[§C4a.9★ Density of States, Laplace and Legendre#^thm-c4a-9-5|§C4a.9.5]] Grand and Gibbs Potentials as Minima
- [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-1|§C4a.10.1]] Fluctuations Are Second Derivatives of $\ln Z$
- [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-2|§C4a.10.2]] Canonical Energy Fluctuations
- [[§C4a.10 Ensembles at a Glance and Fluctuations#^thm-c4a-10-3|§C4a.10.3]] Grand-Canonical Fluctuations as Responses

## Models
- [[§C4a.4 Why the Maximum Is Thermodynamic Entropy#^mod-c4a-4-1|§C4a.4.1]] An Isolated Collection of Copies
