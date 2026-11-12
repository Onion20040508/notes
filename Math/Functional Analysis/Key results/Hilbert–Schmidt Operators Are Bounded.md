---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 46.2", "Hilbert-Schmidt operator"]
tags: [functional-analysis, hub]
---
![[§46 The Transpose#^prop-46-2]]

## Treated in
- [[§46 The Transpose#^prop-46-2|Proposition §46.2: Hilbert–Schmidt Operators are Bounded]], in [[§46 The Transpose]]

## Its proof uses
- [[§23 Cauchy–Schwarz and the Induced Norm#^thm-23-1|Theorem §23.1: Cauchy–Schwarz]]
- [[§30 Boundedness and Continuity#^prop-30-1|Proposition §30.1: The Operator Norm]]
- [[§30 Boundedness and Continuity#^def-30-2|Definition §30.2: Bounded Linear Map]]

## Its proof uses (other subjects)
- [[Fubini's Theorem (Lebesgue)]] (Measure Theory)
- [[Tonelli's Theorem]] (Measure Theory)

## Used in (Functional Analysis)
- [[§46 The Transpose#^prop-46-3|Proposition §46.3: The Transpose of a Hilbert–Schmidt Operator]]

## Connections
- **What it says.** An integral operator $Tf(x) = \int K(x, y) f(y)\, d\mu(y)$ with a square-integrable kernel maps $L^2$ to $L^2$ with $\|T\| \le \|K\|_{L^2(\mu \times \mu)}$.
- **How.** Cauchy–Schwarz in $y$ for each fixed $x$, then integrate in $x$ ([[Tonelli's Theorem]]).
- **The kernel as a matrix.** The kernel plays the role of the matrix entries, $K(x, y) \leftrightarrow a_{ij}$; the transpose exchanges the variables ([[§46 The Transpose#^prop-46-3|§46.3]]) and the adjoint also conjugates ([[§46 The Transpose#^ex-46-1|Ex. §46.1]]). For a matrix the bound is $\|A\| \le (\sum_{i,j} |a_{ij}|^2)^{1/2}$, the Frobenius norm.
- **In Lax.** Not in Lax's Chapter 15.
