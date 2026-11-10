---
subject: math
type: theorem
source: "[[Functional Analysis]]"
aliases: ["MATH 556 41.4", "closed graph", "Lax §15.5, Thm 12"]
tags: [functional-analysis, hub]
---
![[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4]]

## Treated in
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-4|Theorem §41.4: Closed Graph Theorem]], in [[§41 The Open Mapping Theorem and Its Consequences]]

## Its proof uses
- [[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|Theorem §41.3: Equivalent Norm Theorem]]

## Used in (Functional Analysis)
- [[§41 The Open Mapping Theorem and Its Consequences#^prop-41-5|Proposition §41.5: Closed Range Criterion]]
- [[§42 Uniform Boundedness and Approximation#^thm-42-5|Theorem §42.5: Equivalent Norm Theorem, Second Version]]

## Connections
- **How.** Put the graph norm $\|x\|_G = \|x\| + \|Mx\|$ on $X$. It is complete because $M$ is closed ([[§39 Solving Mx = y#^prop-39-4|§39.4]]), and it dominates $\|\cdot\|$. Two comparable complete norms are equivalent ([[§41 The Open Mapping Theorem and Its Consequences#^thm-41-3|§41.3]]), so $\|Mx\| \le \|x\|_G \le C\|x\|$ ([[Functional Analysis Problem-Solving Techniques#^rem-t27|Technique 27]]).
- **What it saves.** To prove $M$ bounded one must show $x_n \to x \Rightarrow Mx_n \to Mx$. For a closed map it is enough to show: if $x_n \to x$ and $Mx_n \to y$, then $y = Mx$; the convergence of $Mx_n$ may be assumed. Continuous maps are closed ([[§39 Solving Mx = y#^ex-39-1|Ex. §39.1]]).
- **Why the whole space.** Differentiation with domain $C^1[0,1] \subset C[0,1]$ is closed but not bounded in the maximum norm ([[§39 Solving Mx = y#^ex-39-3|Ex. §39.3]]); its domain is not all of $C[0,1]$ and is not complete in that norm. “Closed” means closed graph, not “closed sets go to closed sets” ([[§39 Solving Mx = y#^rem-39-3|Remark: Why Not “Closed Sets to Closed Sets”]]).
- **Used for.** The closed range criterion ([[§41 The Open Mapping Theorem and Its Consequences#^prop-41-5|§41.5]], HW9) and the second equivalent norm theorem, where the identity map between two compatible complete norms is closed ([[§42 Uniform Boundedness and Approximation#^thm-42-5|§42.5]]). In the lecture the [[Uniform Boundedness Principle]] is proved by the same graph-norm device.
- **Finite dimensions.** Nothing to prove: every linear map is bounded ([[§30 Boundedness and Continuity#^prop-30-7|§30.7]]).
