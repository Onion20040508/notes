---
subject: math
type: definition
source: "[[Linear Algebra]] 3.80"
ladr: "3.80"
page: 91
aliases: ["LADR 3.80"]
tags: [linear-algebra, ladr/3D]
---
> [!definition] 3.80 Invertible, inverse, A⁻¹
> A square matrix $A$ is *invertible* if there is a square matrix $B$ of the same size with $AB=BA=I$; then $B$ is unique and written $A^{-1}$.

> [!remark] Rules
> Uniqueness: same proof as [[Inverse is unique]]. $(A^{-1})^{-1}=A$, and $(AC)^{-1}=C^{-1}A^{-1}$ since $(AC)(C^{-1}A^{-1})=AIA^{-1}=I$ and similarly on the other side. By [[ST = I ⟺ TS = I (on vector spaces of the same dimension)]], one of $AB=I$, $BA=I$ already implies the other.

## Connections
- Matrix of an inverse map: [[Matrix of inverse equals inverse of matrix]]. Determinant test: [[Invertible ⟺ nonzero determinant]].
