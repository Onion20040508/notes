---
subject: math
type: theorem
source: "[[Fourier Series and PDEs]]"
aliases: ["MAT 341 30.2", "standing waves"]
tags: [fourier-series-and-pdes, hub]
---
![[§30 Solution of the Vibrating String Problem#^thm-30-2]]

## Treated in
- [[§30 Solution of the Vibrating String Problem#^thm-30-2|Theorem §30.2: Series Solution of the Vibrating String Problem]], in [[§30 Solution of the Vibrating String Problem]]

## Its proof uses
- [[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Definition §7.4: Half-Range Expansions; Fourier Sine and Cosine Series]]
- [[§8 Convergence of Fourier Series#^thm-8-1|Theorem §8.1: Convergence of Fourier Series]]
- [[§30 Solution of the Vibrating String Problem#^prop-30-1|Proposition §30.1: Standing Waves Solve the Homogeneous Problem]]

## Used in (Fourier Series and PDEs)
- [[§30 Solution of the Vibrating String Problem#^prop-30-3|Proposition §30.3: Solution as an Average of Two Shifted Copies of f]]
- [[§30 Solution of the Vibrating String Problem#^prop-30-4|Proposition §30.4: The String Vibrates Periodically]]
- [[§31 d'Alembert's Solution#^prop-31-4|Proposition §31.4: d'Alembert's Solution Agrees with the Series Solution]]

## Connections
- The coefficients $\lambda_n = n\pi/a$, $\phi_n = \sin(\lambda_nx)$ are the eigenvalues and eigenfunctions of the regular Sturm–Liouville problem $\phi'' + \lambda^2\phi = 0$, $\phi(0) = \phi(a) = 0$ (equations (6)–(7) of [[§30 Solution of the Vibrating String Problem]]), and the sine coefficients (10), (11) are orthogonal projections onto them: [[§23 Sturm–Liouville Problems#^thm-23-2|Theorem §23.2]], [[§24 Expansion in Series of Eigenfunctions#^thm-24-2|Theorem §24.2]]. The finite-dimensional picture is the expansion of a vector in an orthogonal basis of eigenvectors of a symmetric matrix, [[§48★ Diagonalization of Symmetric Matrices#^thm-48-3|235 Thm. §48.3]].
- Uniform convergence of (9) when $\sum(|a_n| + |b_n|) < \infty$ (as for the plucked string of [[§30 Solution of the Vibrating String Problem#^ex-30-1|Example §30.1]], where $|a_n| \le 8h/(\pi^2n^2)$) is the Weierstrass M-test, [[§25 More on Uniform Convergence#^thm-25-3|451 Thm. §25.3]].
