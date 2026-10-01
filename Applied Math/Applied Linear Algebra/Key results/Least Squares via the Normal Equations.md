---
subject: math
type: theorem
source: "[[Applied Linear Algebra]]"
aliases: ["MATH 235 44.1", "normal equations"]
tags: [applied-linear-algebra, hub]
---
![[§44 Least-Squares Problems#^thm-44-1]]

## Treated in
- [[§44 Least-Squares Problems#^thm-44-1|Theorem §44.1: Least Squares via the Normal Equations]], in [[§44 Least-Squares Problems]]

## Its proof uses
- [[§40 Inner Product, Length, and Orthogonality#^thm-40-5|Theorem §40.5: Basic Facts About the Orthogonal Complement]]
- [[§40 Inner Product, Length, and Orthogonality#^thm-40-6|Theorem §40.6: The Fundamental Subspaces Are Orthogonal Complements]]
- [[§42 Orthogonal Projections#^thm-42-1|Theorem §42.1: The Orthogonal Decomposition Theorem]]
- [[§42 Orthogonal Projections#^thm-42-3|Theorem §42.3: The Best Approximation Theorem]]

## Used in (Applied Linear Algebra)
- [[§44 Least-Squares Problems#^thm-44-2|Theorem §44.2: When the Least-Squares Solution Is Unique]]
- [[§44 Least-Squares Problems#^thm-44-3|Theorem §44.3: Least Squares via QR]]
- [[§45 Applications to Linear Models#^prop-45-1|Proposition §45.1: The Least-Squares Line Is a Least-Squares Solution]]
- [[§45 Applications to Linear Models#^prop-45-2|Proposition §45.2: Fitting a Line in Mean-Deviation Form]]
- [[§47 Applications of Inner Product Spaces#^prop-47-1|Proposition §47.1: Weighted Least Squares as Ordinary Least Squares]]

## Connections
- Rigorous treatment: the minimization theorem [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]] applied to $U = \operatorname{range} T$, and the pseudoinverse [[§21 Orthogonal Complements and Minimization Problems#^ladr-6-70|LADR 6.70]]: $T^\dagger b$ is a least-squares solution, and among all least-squares solutions the one of smallest norm (the one in $(\operatorname{null} T)^\perp$). The normal equations $T^*Tx = T^*b$ appear with the singular value decomposition, [[§26 Singular Value Decomposition|LADR 7E]].
- Fitting a regression line by least squares, as used in Calculus: [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-3|Calc Def. §2.3]] (empirical models); the computation behind it is [[§45 Applications to Linear Models|§45]].
