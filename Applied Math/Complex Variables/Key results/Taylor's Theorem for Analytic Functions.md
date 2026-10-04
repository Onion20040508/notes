---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 63.1", "Taylor series (complex)"]
tags: [complex-variables, hub]
---
![[§63 Proof of Taylor's Theorem#^thm-63-1]]

## Treated in
- [[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1: Taylor's Theorem]], in [[§63 Proof of Taylor's Theorem]]

## Its proof uses
- [[§5 Triangle Inequality#^cor-5-2|Corollary §5.2: Reverse Triangle Inequality]]
- [[§18 Continuity#^thm-18-6|Theorem §18.6: Continuous Functions on Closed Bounded Regions Are Bounded]]
- [[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4: Chain Rule]]
- [[§44 Contour Integrals#^thm-44-2|Theorem §44.2: Properties of Contour Integrals]]
- [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2: The ML-Inequality]]
- [[§54 Cauchy Integral Formula#^thm-54-1|Theorem §54.1: Cauchy Integral Formula]]
- [[§56★ Verification of the Extension (An Extension of the Cauchy Integral Formula)#^thm-56-1|Theorem §56.1: Extended Cauchy Integral Formula]]
- [[§61 Convergence of Series#^ex-61-1|Example §61.1: The Geometric Series]]
- [[§61 Convergence of Series#^def-61-3|Definition §61.3: Remainder; Power Series]]
- [[§62 Taylor Series#^def-62-1|Definition §62.1: Taylor Series; Maclaurin Series]]

## Used in (Complex Variables)
- [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|Proposition §64.1: Six Maclaurin Series]]
- [[§67 Proof of Laurent's Theorem#^thm-67-1|Theorem §67.1: Laurent's Theorem]]
- [[§69★ Absolute and Uniform Convergence of Power Series#^ex-69-3|Example §69.3: The Two Extreme Cases]]
- [[§71★ Integration and Differentiation of Power Series#^cor-71-3|Corollary §71.3: The Taylor Disk Cannot Be Enlarged]]
- [[§72★ Uniqueness of Series Representations#^ex-72-2|Example §72.2: Dividing Out a Zero]]
- [[§73★ Multiplication and Division of Power Series#^thm-73-2|Theorem §73.2: Multiplication of Power Series]]
- [[§73★ Multiplication and Division of Power Series#^prop-73-3|Proposition §73.3: Division of Power Series]]
- [[§80 Residues at Poles#^ex-80-1|Example §80.1: Dividing an Analytic Function by z − z₀]]
- [[§80 Residues at Poles#^thm-80-1|Theorem §80.1: Poles and Their Residues]]
- [[§82 Zeros of Analytic Functions#^thm-82-1|Theorem §82.1: Factoring Out a Zero]]
- [[§82 Zeros of Analytic Functions#^thm-82-2|Theorem §82.2: Zeros Are Isolated]]
- [[§82 Zeros of Analytic Functions#^thm-82-3|Theorem §82.3: Vanishing on a Domain or Segment Through z₀]]
- [[§93 Argument Principle#^lem-93-3|Lemma §93.3: Finitely Many Zeros and Poles]]
- [[§112★ Preservation of Angles and Scale Factors#^thm-112-3|Theorem §112.3: Angles at a Critical Point Are Multiplied by m]]
- [[§128★ Schwarz–Christoffel Transformation#^lem-128-1|Lemma §128.1: Continuity at the Branch Points]]

## Connections
- In real analysis, convergence of a Taylor series to $f$ is proved from a remainder estimate that needs bounds on all derivatives ([[§31 Taylor's Theorem#^thm-31-2|451 Thm. §31.2]]), and it can fail for a function with derivatives of all orders ([[§31 Taylor's Theorem#^ex-31-3|451 Ex. §31.3]]). Here the Cauchy integral formula supplies the bounds automatically: Cauchy's inequality $|f^{(n)}(0)| \le n!M/r_0^n$ ([[§57 Some Consequences of the Extension#^thm-57-4|Theorem §57.4]]) gives $|a_nz^n| \le M(r/r_0)^n$, and summing the tail of this geometric bound from $n = N$ reproduces exactly the estimate $\frac{Mr_0}{r_0 - r}(r/r_0)^N$ of the proof.
- The calculus statement "a power series equals the Taylor series of its sum" ([[§78 Taylor and Maclaurin Series#^thm-78-1|Calc Thm. §78.1]]) is the converse direction; in this subject it is [[§72★ Uniqueness of Series Representations#^thm-72-1|Theorem §72.1]].
