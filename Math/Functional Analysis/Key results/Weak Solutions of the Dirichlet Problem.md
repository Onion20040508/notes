---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 34.2", "Dirichlet problem (weak solutions)", "Existence and Uniqueness of Weak Solutions"]
tags: [functional-analysis, hub]
---
![[§34 Weak Solutions of the Dirichlet Problem#^thm-34-2]]

## Treated in
- [[§34 Weak Solutions of the Dirichlet Problem#^thm-34-2|Theorem §34.2: Existence and Uniqueness of Weak Solutions]], in [[§34 Weak Solutions of the Dirichlet Problem]]

## Its proof uses
- [[§16 Means and Young's Inequality#^prop-16-1|Proposition §16.1: Cauchy–Schwarz in ℝⁿ]]
- [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Theorem §23.1: Cauchy–Schwarz]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^def-26-1|Definition §26.1: Bounded Linear Functional]]
- [[§31 Dual Spaces#^def-31-1|Definition §31.1: Dual Space]]
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^def-32-1|Definition §32.1: Sesquilinear Form; Bounded Form]]
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|Theorem §32.2: Lax–Milgram]]
- [[§33 Sobolev Spaces and Weak Derivatives#^prop-33-5|Proposition §33.5: H¹_0(Omega) is a Hilbert Space]]
- [[§33 Sobolev Spaces and Weak Derivatives#^cor-33-7|Corollary §33.7: Poincaré on H¹_0]]
- [[§34 Weak Solutions of the Dirichlet Problem#^def-34-2|Definition §34.2: Weak Solution]]

## Used in (Functional Analysis)
- [[§34 Weak Solutions of the Dirichlet Problem#^thm-34-4|Theorem §34.4: General Elliptic Equations]]

## Connections
- **What it says.** For a bounded domain $\Omega$ and $f \in L^2(\Omega)$, the problem $-\Delta u = f$ in $\Omega$, $u = 0$ on $\partial\Omega$, has exactly one weak solution in $H^1_0(\Omega)$ ([[§34 Weak Solutions of the Dirichlet Problem#^def-34-2|Def. §34.2]]); a classical solution is a weak one ([[§34 Weak Solutions of the Dirichlet Problem#^prop-34-1|§34.1]]).
- **Plan of the proof.** [[Functional Analysis Problem-Solving Techniques#^rem-t20|Technique 20]]: the form $B(u,v) = \int \nabla u \cdot \nabla v$ is bounded, and coercive because the [[Poincaré Inequality|Poincaré inequality]] controls the missing $L^2$ part; $v \mapsto \int f v$ is bounded; then the [[Lax–Milgram Theorem|Lax–Milgram theorem]] (here $B$ is symmetric, so the [[Riesz Representation Theorem (Hilbert spaces)|Riesz theorem]] suffices). The same argument with a uniformly positive definite matrix gives general elliptic equations ([[§34 Weak Solutions of the Dirichlet Problem#^thm-34-4|§34.4]]).
- **Elsewhere.** Uniqueness of classical solutions by Green's identity: [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^ex-28-1|452 Ex. §28.1]]; electrostatics: [[§B3.1 Laplace's Equation and the Uniqueness Theorems#^thm-b3-1-3|EM Theorem §B3.1.3]] and the existence of the Dirichlet Green function, [[§C7.3 Green Functions for Poisson’s Equation#^rem-c7-3-1|EM ★ Remark]]; steady heat flow: [[§B5.3★ The Thermal Diffusion Equation#^thm-b5-3-5|TH Theorem §B5.3.5]].
