---
type: procedure
subject: "[[Quantum Field Theory]]"
level: C
tags: [quantum-field-theory, procedure]
---
# P4 Restoring ħ and c

Turns a natural-units formula ($\hbar = c = 1$) into one valid in any units, by fixing for each quantity the unique powers $\hbar^ac^b$ that its physical type requires. Why the answer is unique, and why the type is the one piece of information needed, is [[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-1|Theorem §C1.2.1]] and [[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-2|Theorem §C1.2.2]]; mass dimension is [[§C1.2 Natural Units and Dimensional Analysis#^def-c1-2-1|Def. §C1.2.1]], the counting rules [[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-3|Theorem §C1.2.3]]. The user's notes give three recipes (the exponent rule, the deficit method, anchor and match); they are steps 4 and 5 below.

## Steps

1. **State the type of the target.** Write the ordinary dimension $M^\alpha L^\beta T^\gamma$ of what the formula computes: a wavelength is $L$, an energy $ML^2T^{-2}$, a kernel that reduces to $\delta^3(\mathbf x)$ is $L^{-3}$, an action divided by $\hbar$ is a pure number. Without this the restoration is undetermined ([[§C1.2 Natural Units and Dimensional Analysis#^cau-c1-2-1|Caution: One number, several readings]]). For an equation or a sum, every term has this type ([[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-3|Theorem §C1.2.3]], 1). ^p4-1

2. **Restore inside every transcendental function first.** Each argument of $\exp$, $\sin$, $\log$, $K_\nu$, … is a separate target of type "pure number" ([[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-3|Theorem §C1.2.3]], 2): $mt \to mc^2t/\hbar$, $mr \to mcr/\hbar$, $Et \to Et/\hbar$, $\mathbf p\cdot\mathbf x \to \mathbf p\cdot\mathbf x/\hbar$; in four-vectors $x^0 = ct$, so $x^2 = c^2t^2 - \mathbf x^2$. The same holds for ratios that must be dimensionless, such as $v \to v/c$. ^p4-2

3. **Read every symbol with its own physical type.** Compute the ordinary dimension of the expression as written: $m$ a mass, $t$ a time, $r$, $\rho$ lengths, $E$ an energy, $\mathbf p$ a momentum, $\mathbf k$ an inverse length, $\omega$ an inverse time. Powers multiply the counters, fractional ones included ([[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-3|Theorem §C1.2.3]], 3); derivatives divide by, integrals multiply by, the dimension of their variable (rule 4). ^p4-3

4. **Fix the deficit with ħ and c.** The ratio of target to expression must be $M^aL^{2a + b}T^{-a - b}$; solve $a$ from the $M$ counter, $b$ from the $L$ counter, and check the $T$ counter, which must then hold (three equations, two unknowns; a failure means the natural-units formula was already wrong). Multiply by $\hbar^ac^b$. For a monomial in masses this is the exponent rule, $Q = Q_{\text{nat}}\hbar^{\beta + \gamma}c^{-\beta - 2\gamma}$ ([[§C1.2 Natural Units and Dimensional Analysis#^thm-c1-2-1|Theorem §C1.2.1]]). ^p4-4

5. **For sums and Lagrangians, anchor and match.** Pick one term whose units are certain (a gradient term $(\nabla\phi)^2$; "everything is an energy" in a dispersion relation) and give every other term the powers of $\hbar$ and $c$ that make it match; the dimension of the field itself is then never needed, and comes out of the anchor. Each term of a sum is restored separately, since $\hbar = c = 1$ may have merged terms that carried different powers. ^p4-5

6. **Check.** Recover a known limit (nonrelativistic: $c \to \infty$ with $E - mc^2$ fixed; classical: $\hbar \to 0$), the counter of step 4 that was not used, and a number with $\hbar c \simeq 197.3$ MeV fm, $\hbar \simeq 6.582\times10^{-22}$ MeV s ([[§C1.2 Natural Units and Dimensional Analysis#^def-c1-2-1|Def. §C1.2.1]]). ^p4-6

## Instances

| Instance | Step 1 (type) | Steps 2–5 | Result |
| --- | --- | --- | --- |
| Rest energy, Compton length and time from a mass | energy; length; time | [[§C1.2 Natural Units and Dimensional Analysis#^der-c1-2-1\|Derivation §C1.2.1]], Step 5 | $mc^2$; $\hbar/mc$; $\hbar/mc^2$ |
| Table of common quantities | each row | [[§C1.2 Natural Units and Dimensional Analysis#^rem-c1-2-2\|Remark: Mass dimensions of common quantities]] | — |
| Centre-of-mass energy and annihilation photons (Problem Set 1, Problem 4) | energy; length | [[§C1.2 Natural Units and Dimensional Analysis#^ex-c1-2-3\|Example §C1.2.3]], Steps 1 and 3 | $E_{\text{CM}} = \sqrt{2m_ec^2(E + m_ec^2)}$; $\hbar c/E_\gamma \simeq 55$ fm |
| The action is a multiple of $\hbar$ | action | [[§C1.2 Natural Units and Dimensional Analysis#^der-c1-2-4\|Derivation §C1.2.4]], Step 1 | $[S] = 0$ |
| Scalar action and dispersion relation (Lecture 2) | $S/\hbar$ pure number; energy | [[§C1.2 Natural Units and Dimensional Analysis#^ex-c1-2-2\|Example §C1.2.2]] (anchor and match, step 5) | $\frac{1}{2c^2}(\partial_t\phi)^2$, $(mc/\hbar)^2\phi^2$; $\hbar\omega = \sqrt{(\hbar ck)^2 + (mc^2)^2}$ |
| Single-particle amplitude, relativistic and nonrelativistic | $L^{-3}$ | [[§C1.3 Causal Structure and the Causality of a Single Particle#^ex-c1-3-1\|Example §C1.3.1]] | $\frac{im^2c^3t}{2\pi^2\hbar^2\rho^2}K_2(mc\rho/\hbar)$; $(m/2\pi i\hbar t)^{3/2}$ |
| Decay length of the Wightman function | length | [[§C2.9 Explicit Forms of the Wightman Function#^thm-c2-9-3\|Theorem §C2.9.3]] (by-product of Step 5) | $\hbar/mc$ ([[§B4.1 The Klein–Gordon Equation#^def-b4-1-2\|REL Def. §B4.1.2]]) |
| Sakurai's natural-units relativistic quantum mechanics | energies; inverse lengths; coupling | [[§C13.1★ Relativistic Wave Equations and the Klein–Gordon Field#^cau-c13-1-1\|QM Caution: Units, metric and symbols in Chapter C13★]] | $m \to mc^2$, $m \to mc/\hbar$, $e^2 \to e^2/\hbar c$ |
| Charges in Heaviside–Lorentz units | pure number $\alpha$ | [[§C1.7 Relativistic Electrodynamics in Index Form#^def-c1-7-1\|Def. §C1.7.1]] | $\alpha = e^2/4\pi\hbar c$ |
| Dirac and vector fields, loop integrals | | QFT C4, C5, C7 (planned) | |

## Pitfalls

- **The type is not in the formula.** $1/m$ is a length or a time; $1\ \text{GeV}^{-1}$ is $0.197$ fm or $6.6\times10^{-25}$ s. Decide step 1 from the physics before touching the algebra.
- **Arguments before prefactors.** Restoring the prefactor first and the argument of $K_\nu$ or $\exp$ afterwards double-counts; step 2 comes first.
- **$t$ versus $x^0$.** In restored four-vector expressions $x^0 = ct$: $\rho = \sqrt{r^2 - c^2t^2}$, not $\sqrt{r^2 - t^2}$.
- **Terms merged by ħ = c = 1.** $E_{\text{CM}} = \sqrt{2m(E + m)}$ has two terms under the root that need different powers of $c$; restore them one by one (step 5).
- **The physical dimension of a field is a convention.** $[\phi] = L^{-1}$ or $(MLT^{-2})^{1/2}$ depending on where the constants are put; only the mass dimension is fixed ([[§C1.2 Natural Units and Dimensional Analysis#^cau-c1-2-2|§C1.2, Caution: The physical dimension of a field is a normalization convention]]).
- **Factors of 2π are not dimensions.** $h$ versus $\hbar$, wavelength versus reduced wavelength: no dimensional argument decides them ([[§C1.2 Natural Units and Dimensional Analysis#^ex-c1-2-3|Example §C1.2.3]], Step 3).
- **Unit systems for charge.** Gaussian, SI and Heaviside–Lorentz differ by $4\pi$ and $\varepsilon_0$ as well as by $\hbar c$; restore $\alpha$ first ([[§C1.7 Relativistic Electrodynamics in Index Form#^def-c1-7-1|Def. §C1.7.1]], [[§C6.2 The Coulomb Problem#^cau-c6-2-1|QM Caution: Gaussian and SI units for the Coulomb problem]]).
