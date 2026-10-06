---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 80.1"]
tags: [complex-variables, hub]
---
![[§80 Residues at Poles#^thm-80-1]]

## Treated in
- [[§80 Residues at Poles#^thm-80-1|Theorem §80.1: Poles and Their Residues]], in [[§80 Residues at Poles]]

## Its proof uses
- [[§63 Proof of Taylor's Theorem#^thm-63-1|Theorem §63.1: Taylor's Theorem]]
- [[§71★ Integration and Differentiation of Power Series#^cor-71-2|Corollary §71.2: The Sum of a Power Series Is Analytic]]
- [[§72★ Uniqueness of Series Representations#^thm-72-4|Theorem §72.4: Uniqueness of Laurent Series]]
- [[§75 Residues#^def-75-1|Definition §75.1: Residue]]
- [[§78 The Three Types of Isolated Singular Points#^def-78-4|Definition §78.4: Pole of Order m]]

## Used in (Complex Variables)
- [[§83 Zeros and Poles#^thm-83-1|Theorem §83.1: A Zero of Order m in the Denominator Is a Pole of Order m]]
- [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2: Residue of p/q at a Simple Zero of q]]
- [[§83 Zeros and Poles#^prop-83-3|Proposition §83.3: A Pole of Order m Comes From a Zero of Order m]]
- [[§84 Behavior of Functions Near Isolated Singular Points#^thm-84-4|Theorem §84.4: A Function Tends to Infinity at a Pole]]
- [[§93 Argument Principle#^thm-93-4|Theorem §93.4: Argument Principle]]

## Connections
- In Fourier Series and PDEs, the coefficients of $\frac{A}{s - r} + \frac{B}{(s - r)^2}$ at a double root are $B = \lim_{s\to r}(s - r)^2U(s)$ and $A = \lim_{s\to r}(s - r)\big[U(s) - \frac{B}{(s - r)^2}\big]$, [[§54★ More Difficult Examples#^prop-54-2|341 Prop. §54.2]]. In the notation of [[§80 Residues at Poles#^thm-80-1|Theorem §80.1]] with $m = 2$ and $\phi(s) = (s - r)^2U(s)$, these are $B = \phi(r)$ and $A = \phi'(r)$, the residue. At a simple root the formula $\operatorname{Res} = \phi(z_0)$ is Heaviside's $q(r)/p'(r)$, [[§52★ Partial Fractions and Convolutions#^thm-52-2|341 Thm. §52.2]] (see [[§83 Zeros and Poles#^thm-83-2|Theorem §83.2]]).
