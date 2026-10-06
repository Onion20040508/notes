---
type: section
subject: "[[Linear Algebra]]"
chapter: 9
section: 38
aliases: ["LADR 9D", "9D Tensor Products"]
tags: [linear-algebra]
---
← [[§37 Determinants]] · ↑ [[· 9 Multilinear Algebra and Determinants]]

> [!definition] Definition 9.68: Bilinear functional on V× W
> A *bilinear functional* on $V\times W$ is $\beta:V\times W\to\F$, linear in each slot.

^ladr-9-68

> [!remark]- Connections
> - Same notion in 591, called a bilinear pairing: [[§21 Linear Algebra Toolkit#^def-21-4|591 Def. §21.4]]; a non-degenerate one identifies each space with the dual of the other, [[§21 Linear Algebra Toolkit#^thm-21-5|591 Thm. §21.5]].

> [!definition] Definition 9.68b: The vector space B(V, W)
> $\mathcal{B}(V,W)$ is the vector space of bilinear functionals on $V\times W$; $\mathcal{B}(V,V)=V^{(2)}$.

^ladr-9-68b

> [!example] Example 9.69: Bilinear functionals (p. 371)
> - $\beta(v,w)=\varphi(v)\tau(w)$ on $V\times W$, for $\varphi\in V'$, $\tau\in W'$.
> - $\beta(\varphi,\tau)=\varphi(v)\tau(w)$ on $V'\times W'$: this is $v\otimes w$ ([[§38 Tensor Products#^ladr-9-71b|9.71b]]).
> - $\beta(v,\varphi)=\varphi(v)$ on $V\times V'$: the evaluation pairing.
> - $\beta(v,T)=\varphi(Tv)$ on $V\times\Lin(V)$.
> - $\beta(A,B)=\operatorname{tr}(AB)$ on $\F^{m,n}\times\F^{n,m}$.

^ladr-9-69

> [!theorem] Theorem 9.70: Dimension of the vector space of bilinear functionals
> $\dim\mathcal{B}(V,W)=(\dim V)(\dim W)$.

^ladr-9-70

> [!proof]+ Proof
> With bases $e$ of $V$ and $f$ of $W$, $\beta\mapsto\big(\beta(e_j,f_k)\big)_{j,k}\in\F^{m,n}$ is linear with inverse $C\mapsto\beta_C$, $\beta_C(\sum a_je_j,\sum b_kf_k)=\sum_{j,k}C_{j,k}a_jb_k$ (as in [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-5|9.5]]).

*Uses:* [[§35 Bilinear Forms and Quadratic Forms#^ladr-9-5|9.5]]

> [!definition] Definition 9.71: Tensor product, V⊗ W
> The *tensor product* $V\otimes W=\mathcal{B}(V',W')$.

^ladr-9-71

> [!definition] Definition 9.71b: v ⊗ w
> For $v\in V$, $w\in W$, $v\otimes w\in V\otimes W$ is
> $$
> (v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)\qquad(\varphi\in V',\ \tau\in W').
> $$

^ladr-9-71b

> [!remark] Remark: Why this definition
> $\Lin(V,W)$ or $\F^{m,n}$ have the right dimension too, but give no basis-free meaning to $v\otimes w$. What matters is the behavior: bilinearity ([[§38 Tensor Products#^ladr-9-73|9.73]]), bases ([[§38 Tensor Products#^ladr-9-74|9.74]]), and the universal property ([[§38 Tensor Products#^ladr-9-79|9.79]]).

> [!remark]- Connections
> - Compare the product or direct sum (dimensions add, [[§11 Products and Quotients of Vector Spaces#^ladr-3-92|3.92]]) with the tensor product (dimensions multiply, [[§38 Tensor Products#^ladr-9-72|9.72]]).
> - Used in Quantum Mechanics: the state space of a composite system is the tensor product $\mathcal{H}_A\otimes\mathcal{H}_B$ of the parts' spaces, with the product basis of [[§38 Tensor Products#^ladr-9-83|Theorem 9.83]] — [[§C1.5 Composite Systems and Tensor Products#^pr-c1-5-1|QM Principle §C1.5.1]]; operators on the parts act on it through [[§38 Tensor Products#^ladr-9-79|Theorem 9.79]] — [[§C1.5 Composite Systems and Tensor Products#^def-c1-5-1|QM Def. §C1.5.1]]; product states are the $v\otimes w$, and a state is entangled when it is not a product tensor ([[§38 Tensor Products#^ladr-9-76|Example 9.76]]) — [[§C1.5 Composite Systems and Tensor Products#^thm-c1-5-3|QM Theorem §C1.5.3]]; the product of two angular-momentum multiplets decomposed into irreducible ones, the Clebsch–Gordan series — [[§C7.1 Addition of Angular Momenta and Clebsch–Gordan Coefficients#^thm-c7-1-2|QM Theorem §C7.1.2]].

> [!theorem] Theorem 9.72: Dimension of the tensor product of two vector spaces
> $\dim(V\otimes W)=(\dim V)(\dim W)$.

^ladr-9-72

> [!proof]+ Proof
> $\dim V'=\dim V$, $\dim W'=\dim W$ ([[§12 Duality#^ladr-3-111|3.111]]); apply [[§38 Tensor Products#^ladr-9-70|9.70]].

*Uses:* [[§12 Duality#^ladr-3-111|3.111]], [[§38 Tensor Products#^ladr-9-70|9.70]]

> [!theorem] Theorem 9.73: Bilinearity of tensor product
> $(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w$, $\ v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2$, $\ \lambda(v\otimes w)=(\lambda v)\otimes w=v\otimes(\lambda w)$.

^ladr-9-73

> [!proof]+ Proof
> Evaluate at $(\varphi,\tau)$: $\varphi(v_1+v_2)\tau(w)=\varphi(v_1)\tau(w)+\varphi(v_2)\tau(w)$, and similarly for the others.

> [!remark] Remark: Warning
> $v\otimes w$ is *not* linear in the pair $(v,w)$: $(2v)\otimes(2w)=4(v\otimes w)$.

> [!theorem] Theorem 9.74: Basis of V⊗ W
> (a) If $e_1,\dots,e_m$ in $V$ and $f_1,\dots,f_n$ in $W$ are independent, then $\{e_j\otimes f_k\}$ is independent in $V\otimes W$. (b) If they are bases, $\{e_j\otimes f_k\}$ is a basis of $V\otimes W$.

^ladr-9-74

> [!proof]+ Proof
> (a) Choose $\varphi_j\in V'$, $\tau_k\in W'$ with $\varphi_j(e_i)=\delta_{ji}$, $\tau_k(f_l)=\delta_{kl}$ ([[Linear map lemma|3.4]], after extending to bases). If $\sum a_{j,k}e_j\otimes f_k=0$, evaluate at $(\varphi_M,\tau_N)$: $a_{M,N}=0$. (b) (a) gives $mn=\dim(V\otimes W)$ independent vectors ([[§38 Tensor Products#^ladr-9-72|9.72]], [[§6 Dimension#^ladr-2-38|2.38]]).

*Uses:* [[Linear map lemma|3.4]], [[§38 Tensor Products#^ladr-9-72|9.72]], [[§6 Dimension#^ladr-2-38|2.38]]

> [!remark] Remark: Not every tensor is a product
> Every element is a *sum* of $v\otimes w$'s; e.g. $e_1\otimes f_1+e_2\otimes f_2$ is not a single $v\otimes w$ (its coefficient matrix has rank $2$; compare [[§38 Tensor Products#^ladr-9-76|9.76]]).

> [!example] Example 9.76: Tensor product of element of Fᵐ with element of Fⁿ (p. 374)
> In $\F^m\otimes\F^n$ with the basis $\{e_j\otimes f_k\}$:
> $$
> v\otimes w=\sum_{j,k}v_jw_k\,e_j\otimes f_k,
> $$
> so identifying coefficients with an $m$-by-$n$ matrix, $v\otimes w\leftrightarrow vw^t=\begin{pmatrix}v_1w_1&\cdots&v_1w_n\\\vdots&&\vdots\\v_mw_1&\cdots&v_mw_n\end{pmatrix}$, a rank-$1$ matrix. General tensors are arbitrary matrices; the rank of the matrix is the minimal number of product terms needed (the Schmidt rank, via SVD [[Singular value decomposition|7.70]]).

^ladr-9-76

> [!definition] Definition 9.77: Bilinear map
> A *bilinear map* $V\times W\to U$ is a function $\Gamma$ that is linear in each slot when the other is fixed.

^ladr-9-77

> [!example] Example 9.78: Bilinear maps (p. 374)
> - Every bilinear functional is a bilinear map to $\F$.
> - $(v,w)\mapsto v\otimes w$ from $V\times W$ to $V\otimes W$ ([[§38 Tensor Products#^ladr-9-73|9.73]]).
> - $(S,T)\mapsto ST$ on $\Lin(V)\times\Lin(V)$ (composition).
> - $(v,T)\mapsto Tv$ from $V\times\Lin(V,W)$ to $W$ (evaluation). By [[§38 Tensor Products#^ladr-9-79|9.79]] it becomes a linear map $V\otimes\Lin(V,W)\to W$: a 'contraction'.

^ladr-9-78

> [!theorem] Theorem 9.79: Converting bilinear maps to linear maps
> (a) For every bilinear $\Gamma:V\times W\to U$ there is a unique linear $\hat\Gamma:V\otimes W\to U$ with $\hat\Gamma(v\otimes w)=\Gamma(v,w)$. (b) Conversely, every linear $T:V\otimes W\to U$ gives a unique bilinear $T^\#(v,w)=T(v\otimes w)$.

^ladr-9-79

> [!proof]+ Proof
> (a) Define $\hat\Gamma$ on the basis by $\hat\Gamma(e_j\otimes f_k)=\Gamma(e_j,f_k)$ ([[Linear map lemma|3.4]], [[§38 Tensor Products#^ladr-9-74|9.74]](b)). For $v=\sum a_je_j$, $w=\sum b_kf_k$: $\hat\Gamma(v\otimes w)=\sum a_jb_k\hat\Gamma(e_j\otimes f_k)=\sum a_jb_k\Gamma(e_j,f_k)=\Gamma(v,w)$. Uniqueness: a linear map is determined on the basis $\{e_j\otimes f_k\}$. (b) $T^\#$ is bilinear by [[§38 Tensor Products#^ladr-9-73|9.73]] and linearity of $T$; uniqueness is clear.

*Uses:* [[Linear map lemma|3.4]], [[§38 Tensor Products#^ladr-9-74|9.74]], [[§38 Tensor Products#^ladr-9-73|9.73]]

> [!remark] Remark: Universal property
> $\{\text{bilinear }V\times W\to U\}\cong\Lin(V\otimes W,U)$: the tensor product turns bilinear problems into linear ones. This characterizes $V\otimes W$ up to isomorphism.

%% ex:9.79-fig %%
> [!example] Example: The universal property as a diagram
> Every bilinear $\Gamma$ factors uniquely through $(v,w)\mapsto v\otimes w$: the blue map $\hat\Gamma$ is linear, and the triangle commutes, $\hat\Gamma(v\otimes w)=\Gamma(v,w)$.
>
> ![[ladr-9.79-universal.svg|260]]

> [!theorem] Theorem 9.80: Inner product on tensor product of two inner product spaces
> If $V,W$ are inner product spaces, there is a unique inner product on $V\otimes W$ with
> $$
> \langle v\otimes w,u\otimes x\rangle=\langle v,u\rangle\langle w,x\rangle .
> $$

^ladr-9-80

> [!proof]+ Proof
> With orthonormal bases $e$ of $V$, $f$ of $W$, define $\big\langle\sum b_{j,k}e_j\otimes f_k,\sum c_{j,k}e_j\otimes f_k\big\rangle=\sum b_{j,k}\overline{c_{j,k}}$: the Euclidean inner product on coefficients (an inner product by [[§38 Tensor Products#^ladr-9-74|9.74]](b)). Expanding $v,u,w,x$ in the bases, $v\otimes w=\sum v_jw_ke_j\otimes f_k$, so
> $$
> \langle v\otimes w,u\otimes x\rangle=\sum_{j,k}v_jw_k\overline{u_jx_k}=\Big(\sum_jv_j\bar u_j\Big)\Big(\sum_kw_k\bar x_k\Big)=\langle v,u\rangle\langle w,x\rangle .
> $$
> Uniqueness: product tensors span $V\otimes W$.

*Uses:* [[§38 Tensor Products#^ladr-9-74|9.74]]

> [!remark]- Connections
> - Physics: $\langle\psi_A\otimes\psi_B|\phi_A\otimes\phi_B\rangle=\langle\psi_A|\phi_A\rangle\langle\psi_B|\phi_B\rangle$.

> [!definition] Definition 9.82: Inner product on tensor product of two inner product spaces
> *The* inner product on $V\otimes W$ is the one of [[§38 Tensor Products#^ladr-9-80|9.80]]. In particular $\|v\otimes w\|=\|v\|\|w\|$.

^ladr-9-82

> [!theorem] Theorem 9.83: Orthonormal basis of V⊗ W
> If $e_1,\dots,e_m$ and $f_1,\dots,f_n$ are orthonormal bases of $V$ and $W$, then $\{e_j\otimes f_k\}$ is an orthonormal basis of $V\otimes W$.

^ladr-9-83

> [!proof]+ Proof
> A basis by [[§38 Tensor Products#^ladr-9-74|9.74]](b); $\langle e_j\otimes f_k,e_M\otimes f_N\rangle=\langle e_j,e_M\rangle\langle f_k,f_N\rangle=\delta_{jM}\delta_{kN}$.

*Uses:* [[§38 Tensor Products#^ladr-9-74|9.74]]

> [!remark] Remark: Point
> Any orthonormal bases work, not just the ones used to define the inner product.

> [!remark] Notation 9.84: $V_1,\dots,V_m$ (p. 378)
> For the rest of this subsection, $m$ is an integer greater than $1$ and $V_1,\dots,V_m$ are finite-dimensional vector spaces.

^ladr-9-84

> [!definition] Definition 9.85: m-linear functional
> An *$m$-linear functional* on $V_1\times\dots\times V_m$ is linear in each slot.

^ladr-9-85

> [!definition] Definition 9.85b: The vector space B(V1, ..., Vm)
> $\mathcal{B}(V_1,\dots,V_m)$ is the space of $m$-linear functionals on $V_1\times\dots\times V_m$.

^ladr-9-85b

> [!example] Example 9.86: m-linear functional (p. 378)
> For $\varphi_k\in V_k'$: $\beta(v_1,\dots,v_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)$ is $m$-linear; sums of these give all of $\mathcal{B}(V_1,\dots,V_m)$.

^ladr-9-86

> [!theorem] Theorem 9.87: Dimension of the vector space of m-linear functionals
> $\dim\mathcal{B}(V_1,\dots,V_m)=(\dim V_1)\cdots(\dim V_m)$.

^ladr-9-87

> [!proof]+ Proof
> As in [[§38 Tensor Products#^ladr-9-70|9.70]]: an $m$-linear functional is determined by its values on tuples of basis vectors, which may be arbitrary.

*Uses:* [[§38 Tensor Products#^ladr-9-70|9.70]]

> [!definition] Definition 9.88: Tensor product, V1 ⊗ ⋯ ⊗ Vm
> $V_1\otimes\dots\otimes V_m=\mathcal{B}(V_1',\dots,V_m')$.

^ladr-9-88

> [!remark]- Connections
> - Tensors of type $(r,s)$ in physics and in [[Differentiable Manifolds]]: $V^{\otimes r}\otimes(V')^{\otimes s}$.
> - Used in Relativity: Lorentz tensors of type (m, n) — [[§B2.2 Tensors and the Covariance Principle#^def-b2-2-1|REL Def. §B2.2.1]]; tensors as multilinear functions of covectors and vectors, without coordinates — [[§B2.2 Tensors and the Covariance Principle#^rem-b2-2-2|REL Remark: Tensors without coordinates]].

> [!definition] Definition 9.88b: v1 ⊗ ⋯ ⊗ vm
> $(v_1\otimes\dots\otimes v_m)(\varphi_1,\dots,\varphi_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)$.

^ladr-9-88b

> [!theorem] Theorem 9.89: Dimension of the tensor product
> $\dim(V_1\otimes\dots\otimes V_m)=(\dim V_1)\cdots(\dim V_m)$.

^ladr-9-89

> [!proof]+ Proof
> [[§38 Tensor Products#^ladr-9-87|9.87]] and $\dim V_k'=\dim V_k$.

*Uses:* [[§38 Tensor Products#^ladr-9-87|9.87]]

> [!remark] Remark: Physics
> $N$ spin-$\tfrac12$ particles live in $(\C^2)^{\otimes N}$, of dimension $2^N$: the exponential growth behind the difficulty of simulating quantum many-body systems.

> [!theorem] Theorem 9.90: Basis of V1 ⊗ ⋯ ⊗ Vm
> If $e^k_1,\dots,e^k_{n_k}$ is a basis of $V_k$, then $\{e^1_{j_1}\otimes\dots\otimes e^m_{j_m}\}$ is a basis of $V_1\otimes\dots\otimes V_m$. So elements are arrays with $m$ indices.

^ladr-9-90

> [!proof]+ Proof
> As in [[§38 Tensor Products#^ladr-9-74|9.74]]: evaluate at tuples of dual basis vectors to get independence, then count dimensions ([[§38 Tensor Products#^ladr-9-89|9.89]]).

*Uses:* [[§38 Tensor Products#^ladr-9-74|9.74]], [[§38 Tensor Products#^ladr-9-89|9.89]]

> [!definition] Definition 9.91: m-linear map
> An *$m$-linear map* $V_1\times\dots\times V_m\to U$ is linear in each slot when the others are fixed.

^ladr-9-91

> [!theorem] Theorem 9.92: Converting m-linear maps to linear maps
> (a) Every $m$-linear $\Gamma:V_1\times\dots\times V_m\to U$ induces a unique linear $\hat\Gamma:V_1\otimes\dots\otimes V_m\to U$ with $\hat\Gamma(v_1\otimes\dots\otimes v_m)=\Gamma(v_1,\dots,v_m)$. (b) Conversely, every linear $T$ on the tensor product gives the $m$-linear $T^\#(v_1,\dots,v_m)=T(v_1\otimes\dots\otimes v_m)$.

^ladr-9-92

> [!proof]+ Proof
> As in [[§38 Tensor Products#^ladr-9-79|9.79]], using the basis of [[§38 Tensor Products#^ladr-9-90|9.90]].

*Uses:* [[§38 Tensor Products#^ladr-9-79|9.79]], [[§38 Tensor Products#^ladr-9-90|9.90]]

