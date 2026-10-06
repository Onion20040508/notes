---
subject: math
type: theorem
source: "[[Applied Linear Algebra]]"
aliases: ["MATH 235 54.1", "normal equations"]
tags: [applied-linear-algebra, hub]
---
![[§54 Least-Squares Problems#^thm-54-1]]

## Treated in
- [[§54 Least-Squares Problems#^thm-54-1|Theorem §54.1: Least Squares via the Normal Equations]], in [[§54 Least-Squares Problems]]

## Its proof uses
- [[§50 Orthogonal Complements and Angles#^thm-50-1|Theorem §50.1: Basic Facts About the Orthogonal Complement]]
- [[§50 Orthogonal Complements and Angles#^thm-50-2|Theorem §50.2: The Fundamental Subspaces Are Orthogonal Complements]]
- [[§52 Orthogonal Projections#^thm-52-1|Theorem §52.1: The Orthogonal Decomposition Theorem]]
- [[§52 Orthogonal Projections#^thm-52-3|Theorem §52.3: The Best Approximation Theorem]]

## Used in (Applied Linear Algebra)
- [[§54 Least-Squares Problems#^thm-54-2|Theorem §54.2: When the Least-Squares Solution Is Unique]]
- [[§54 Least-Squares Problems#^thm-54-3|Theorem §54.3: Least Squares via QR]]
- [[§55 Applications to Linear Models#^prop-55-1|Proposition §55.1: The Least-Squares Line Is a Least-Squares Solution]]
- [[§55 Applications to Linear Models#^prop-55-2|Proposition §55.2: Fitting a Line in Mean-Deviation Form]]
- [[§57 Applications of Inner Product Spaces#^prop-57-1|Proposition §57.1: Weighted Least Squares as Ordinary Least Squares]]

## Connections
- Rigorous treatment: the minimization theorem [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-61|LADR 6.61]] applied to $U = \operatorname{range} T$, and the pseudoinverse [[§22 Orthogonal Complements and Minimization Problems#^ladr-6-70|LADR 6.70]]: $T^\dagger b$ is a least-squares solution, and among all least-squares solutions the one of smallest norm (the one in $(\operatorname{null} T)^\perp$). The normal equations $T^*Tx = T^*b$ appear with the singular value decomposition, [[§27 Singular Value Decomposition|LADR 7E]].
- Fitting a regression line by least squares, as used in Calculus: [[§2 Mathematical Models꞉ A Catalog of Essential Functions#^def-2-3|Calc Def. §2.3]] (empirical models); the computation behind it is [[§55 Applications to Linear Models|§55]].
