---
subject: math
type: theorem
source: "[[Complex Variables]]"
aliases: ["MAT 342 33.1", "principal branch", "Log z"]
tags: [complex-variables, hub]
---
![[§33 Branches and Derivatives of Logarithms#^thm-33-1]]

## Treated in
- [[§33 Branches and Derivatives of Logarithms#^thm-33-1|Theorem §33.1: Each Branch of log z Is Analytic, with Derivative 1/z]], in [[§33 Branches and Derivatives of Logarithms]]

## Its proof uses
- [[§18 Continuity#^thm-18-2|Theorem §18.2: Composition of Continuous Functions]]
- [[§24★ Polar Coordinates#^thm-24-3|Theorem §24.3: Sufficient Conditions in Polar Coordinates]]
- [[§33 Branches and Derivatives of Logarithms#^def-33-1|Definition §33.1: A Branch of the Logarithm]]

## Used in (Complex Variables)
- [[§35 The Power Function#^thm-35-2|Theorem §35.2: Derivative of a Branch of z^c]]
- [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-3|Proposition §40.3: Derivatives of the Inverse Trigonometric Functions]]
- [[§48 Antiderivatives#^ex-48-2|Example §48.2: 1/z² Has an Antiderivative on the Punctured Plane, 1/z Does Not]]
- [[§49 Proof of the Theorem (Antiderivatives)#^ex-49-1|Example §49.1: Powers of z − z₀ Around Closed Contours]]
- [[§91★ Integration Along a Branch Cut#^prop-91-1|Proposition §91.1: The Residue Theorem on the Keyhole]]
- [[§93 Argument Principle#^prop-93-2|Proposition §93.2: Winding Number Zero Off a Ray]]
- [[§108★ Mappings by Branches of z^(1∕2)#^prop-108-3|Proposition §108.3: Branches of z^(1/n)]]
- [[§114★ Local Inverses#^ex-114-1|Example §114.1: Local Inverses of the Exponential Function]]

## Connections
- The derivative $1/z$ restricts on the positive real axis to $\frac{d}{dx}\ln x = \frac1x$, [[§19 Derivatives of Logarithmic and Inverse Trigonometric Functions#^cor-19-3|Calc Cor. §19.3]]. The real proof differentiates an inverse function; the same route works here, [[§33 Branches and Derivatives of Logarithms#^ex-33-3|Example §33.3]].
- Topologically, $z \mapsto e^z$ is a covering map of $\mathbb{C}$ onto $\mathbb{C} \setminus \{0\}$: in polar form it is $x \mapsto e^x$ times the covering $\mathbb{R} \to S^1$, $y \mapsto e^{iy}$ (up to the factor $2\pi$), of [[§24 Covering Spaces#^thm-24-2|590 Thm. §24.2]]. A branch of $\log z$ is a continuous inverse of this covering over the cut plane. No continuous logarithm exists on a circle around $0$: it would lift the generating loop of $\pi_1(S^1) \cong \mathbb{Z}$ to a closed loop, [[§24 Covering Spaces#^thm-24-10|590 Thm. §24.10]]. This is why a cut is unavoidable.
