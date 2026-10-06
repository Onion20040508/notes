---
subject: math
type: theorem
source: "[[Fourier Series and PDEs]]"
aliases: ["MAT 341 38.2", "standing waves"]
tags: [fourier-series-and-pdes, hub]
---
![[§38 Solution of the Vibrating String Problem#^thm-38-2]]

## Treated in
- [[§38 Solution of the Vibrating String Problem#^thm-38-2|Theorem §38.2: Series Solution of the Vibrating String Problem]], in [[§38 Solution of the Vibrating String Problem]]

## Its proof uses
- [[§11 Even and Odd Functions; Half-Range Expansions#^def-11-4|Definition §11.4: Fourier Sine Series]]
- [[§12 Convergence of Fourier Series#^thm-12-1|Theorem §12.1: Convergence of Fourier Series]]
- [[§38 Solution of the Vibrating String Problem#^prop-38-1|Proposition §38.1: Standing Waves Solve the Homogeneous Problem]]

## Used in (Fourier Series and PDEs)
- [[§38 Solution of the Vibrating String Problem#^prop-38-3|Proposition §38.3: Solution as an Average of Two Shifted Copies of f]]
- [[§38 Solution of the Vibrating String Problem#^prop-38-4|Proposition §38.4: The String Vibrates Periodically]]
- [[§39 d'Alembert's Solution#^prop-39-4|Proposition §39.4: d'Alembert's Solution Agrees with the Series Solution]]

## Connections
- The coefficients $\lambda_n = n\pi/a$, $\phi_n = \sin(\lambda_nx)$ are the eigenvalues and eigenfunctions of the regular Sturm–Liouville problem $\phi'' + \lambda^2\phi = 0$, $\phi(0) = \phi(a) = 0$ (equations (6)–(7) of [[§38 Solution of the Vibrating String Problem]]), and the sine coefficients (10), (11) are orthogonal projections onto them: [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2]], [[§30 Expansion in Series of Eigenfunctions#^thm-30-2|Theorem §30.2]]. The finite-dimensional picture is the expansion of a vector in an orthogonal basis of eigenvectors of a symmetric matrix, [[§58★ Diagonalization of Symmetric Matrices#^thm-58-3|235 Thm. §58.3]].
- Uniform convergence of (9) when $\sum(|a_n| + |b_n|) < \infty$ (as for the plucked string of [[§38 Solution of the Vibrating String Problem#^ex-38-1|Example §38.1]], where $|a_n| \le 8h/(\pi^2n^2)$) is the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]].
