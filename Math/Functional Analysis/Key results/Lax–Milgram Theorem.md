---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 32.2", "Lax-Milgram", "Lax §6.3, Thm 6"]
tags: [functional-analysis, hub]
---
![[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2]]

## Treated in
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-2|Theorem §32.2: Lax–Milgram]], in [[§32 Sesquilinear Forms and the Lax–Milgram Theorem]]

## Its proof uses
- [[§25 Projection and Orthogonal Decomposition#^thm-25-4|Theorem §25.4: Orthogonal Decomposition]]
- [[§26 Bounded Linear Functionals and the Riesz Representation Theorem#^thm-26-4|Theorem §26.4: Riesz Representation Theorem]]
- [[§30 Boundedness and Continuity#^prop-30-2|Proposition §30.2: Continuous if and only if Bounded]]
- [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^thm-32-1|Theorem §32.1: Bounded Sesquilinear Forms are Bounded Operators]]

## Used in (Functional Analysis)
- (not cited later in the course)

## Connections
- **What is new.** The conclusion looks like the [[Riesz Representation Theorem (Hilbert spaces)|Riesz representation theorem]], with B in place of the inner product. The difference is that B need not be symmetric. When B is symmetric, it is ± an inner product with an equivalent norm, and the theorem reduces to Riesz ([[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^lem-32-3|§32.3]], [[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^prop-32-4|§32.4]]).
- **Plan of the proof.** Write B(x, y) = (x, Ay) ([[Bounded Sesquilinear Forms Are Bounded Operators|§28.1]]) and ℓ(x) = (x, a). The theorem then says that A is one-to-one and onto, and coercivity is what will prove it ([[§32 Sesquilinear Forms and the Lax–Milgram Theorem#^rem-32-2|Remark: The Plan of the Proof]]). The proof was announced in Lecture 10 for the next lecture and is not yet in the notes.
- **Uses.** Wu called it “very useful in solving elliptic PDE”; Lax applies it to the Dirichlet problem for non-self-adjoint equations (Lax §7.2; the Dirichlet problem for Laplace's equation: [[§44 Potential Equation#^def-44-4|341 Def. §44.4]]) and to show that a bounded symmetric operator has real spectrum (Lax §31.1, Thm 2).
