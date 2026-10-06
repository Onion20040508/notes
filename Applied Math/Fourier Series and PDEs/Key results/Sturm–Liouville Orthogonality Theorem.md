---
subject: math
type: theorem
source: "[[Fourier Series and PDEs]]"
aliases: ["MAT 341 29.2", "Sturm–Liouville theorem"]
tags: [fourier-series-and-pdes, hub]
---
![[§29 Sturm–Liouville Problems#^thm-29-2]]

## Treated in
- [[§29 Sturm–Liouville Problems#^thm-29-2|Theorem §29.2: Orthogonality of Eigenfunctions (Sturm–Liouville Theorem)]], in [[§29 Sturm–Liouville Problems]]

## Its proof uses
- [[§29 Sturm–Liouville Problems#^def-29-1|Definition §29.1: Regular Sturm–Liouville Problem]]
- [[§29 Sturm–Liouville Problems#^prop-29-1|Proposition §29.1: Orthogonality for φ″ + λ²φ = 0]]
- [[§29 Sturm–Liouville Problems#^def-29-2|Definition §29.2: Eigenvalue and Eigenfunction]]

## Used in (Fourier Series and PDEs)
- [[§29 Sturm–Liouville Problems#^prop-29-3|Proposition §29.3: The Eigenvalues Are Real]]
- [[§30 Expansion in Series of Eigenfunctions#^prop-30-1|Proposition §30.1: The Coefficients of an Eigenfunction Expansion]]
- [[§31 Generalities on the Heat Conduction Problem#^thm-31-3|Theorem §31.3: Solution of the General Heat Conduction Problem]]
- [[§40 One-Dimensional Wave Equation꞉ Generalities#^thm-40-2|Theorem §40.2: Solution of the Generalized Wave Problem]]
- [[§57★ Temperature in a Cylinder#^prop-57-2|Proposition §57.2: Orthogonality of the Functions J₀(λₙr)]]
- [[§58★ Vibrations of a Circular Membrane#^prop-58-3|Proposition §58.3: Orthogonality of the Eigenfunctions of the Disk]]
- [[§60★ Spherical Coordinates; Legendre Polynomials#^prop-60-5|Proposition §60.5: Orthogonality of the Legendre Polynomials]]

## Connections
- Finite-dimensional version: eigenvectors of a symmetric matrix for distinct eigenvalues are orthogonal, [[§58★ Diagonalization of Symmetric Matrices#^thm-58-1|235 Thm. §58.1]], by the same one-line computation; for self-adjoint operators on an inner product space ([[§23 Self-Adjoint and Normal Operators#^ladr-7-10|LADR 7.10]]), and more generally normal ones, it is [[§23 Self-Adjoint and Normal Operators#^ladr-7-22|LADR 7.22]]. See [[§29 Sturm–Liouville Problems#^rem-29-3|Remark: Self-Adjointness]] for the dictionary.
- $\langle f, g\rangle_p = \int_l^r f(x)g(x)p(x)\,dx$ is an inner product (a weighted version of [[§22 Definition and Examples#^ex-22-3|556 Ex. §22.3]] and [[§56 Inner Product Spaces#^ex-56-4|235 Ex. §56.4]]), and the theorem says that the eigenfunctions form an orthogonal set for it in the sense of [[§27 Orthonormal Sets and Bases#^def-27-1|556 Def. §27.1]].
- The first sentence of the statement (infinitely many eigenvalues) is part (a) of [[§29 Sturm–Liouville Problems#^thm-29-5|Theorem §29.5]], which Powers does not prove; the proof in §29 establishes the orthogonality, and its *Uses:* line accordingly lists only [[§29 Sturm–Liouville Problems#^def-29-1|Definition §29.1]], [[§29 Sturm–Liouville Problems#^def-29-2|Definition §29.2]] and [[§29 Sturm–Liouville Problems#^prop-29-1|Proposition §29.1]].
- In several variables the integration by parts of the proof becomes Green's second identity, [[§28 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-28-3|452 Thm. §28.3]], which makes the Laplacian symmetric in the same way under Dirichlet or Neumann boundary conditions.
