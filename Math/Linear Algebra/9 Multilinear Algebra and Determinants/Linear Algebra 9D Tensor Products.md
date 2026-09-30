---
type: section
subject: "[[Linear Algebra]]"
chapter: 9
section: "9D"
tags: [linear-algebra]
---
← [[Linear Algebra 9C Determinants]] · ↑ [[Linear Algebra — 9 Multilinear Algebra and Determinants]]

> [!definition] 9.68 Bilinear functional on V× W, the vector space B(V, W)
> A *bilinear functional* on $V\times W$ is $\beta:V\times W\to\F$, linear in each slot. $\mathcal{B}(V,W)$ is the vector space of them; $\mathcal{B}(V,V)=V^{(2)}$.

^ladr-9-68

> [!example] 9.69 Bilinear functionals (p. 371)
> - $\beta(v,w)=\varphi(v)\tau(w)$ on $V\times W$, for $\varphi\in V'$, $\tau\in W'$.
> - $\beta(\varphi,\tau)=\varphi(v)\tau(w)$ on $V'\times W'$: this is $v\otimes w$ ([[Linear Algebra 9D Tensor Products#^ladr-9-71|9.71]]).
> - $\beta(v,\varphi)=\varphi(v)$ on $V\times V'$: the evaluation pairing.
> - $\beta(v,T)=\varphi(Tv)$ on $V\times\Lin(V)$.
> - $\beta(A,B)=\operatorname{tr}(AB)$ on $\F^{m,n}\times\F^{n,m}$.

^ladr-9-69

> [!theorem] 9.70 Dimension of the vector space of bilinear functionals
> $\dim\mathcal{B}(V,W)=(\dim V)(\dim W)$.

^ladr-9-70

> [!proof]+
> With bases $e$ of $V$ and $f$ of $W$, $\beta\mapsto\big(\beta(e_j,f_k)\big)_{j,k}\in\F^{m,n}$ is linear with inverse $C\mapsto\beta_C$, $\beta_C(\sum a_je_j,\sum b_kf_k)=\sum_{j,k}C_{j,k}a_jb_k$ (as in [[Linear Algebra 9A Bilinear Forms and Quadratic Forms#^ladr-9-5|9.5]]).

*Uses:* [[Linear Algebra 9A Bilinear Forms and Quadratic Forms#^ladr-9-5|9.5]]

> [!definition] 9.71 Tensor product, V⊗ W, v ⊗ w
> The *tensor product* $V\otimes W=\mathcal{B}(V',W')$. For $v\in V$, $w\in W$, $v\otimes w\in V\otimes W$ is
> $$
> (v\otimes w)(\varphi,\tau)=\varphi(v)\tau(w)\qquad(\varphi\in V',\ \tau\in W').
> $$

^ladr-9-71

> [!remark] Why this definition
> $\Lin(V,W)$ or $\F^{m,n}$ have the right dimension too, but give no basis-free meaning to $v\otimes w$. What matters is the behavior: bilinearity ([[Linear Algebra 9D Tensor Products#^ladr-9-73|9.73]]), bases ([[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]]), and the universal property ([[Linear Algebra 9D Tensor Products#^ladr-9-79|9.79]]).

> [!remark]- Connections
> - Physics: the state space of a composite system is $\mathcal{H}_A\otimes\mathcal{H}_B$; product states are $v\otimes w$, entangled states are the rest. Compare the direct sum (dimensions add, [[Linear Algebra 3E Products and Quotients of Vector Spaces#^ladr-3-92|3.92]]) with the tensor product (dimensions multiply, [[Linear Algebra 9D Tensor Products#^ladr-9-72|9.72]]).

> [!theorem] 9.72 Dimension of the tensor product of two vector spaces
> $\dim(V\otimes W)=(\dim V)(\dim W)$.

^ladr-9-72

> [!proof]+
> $\dim V'=\dim V$, $\dim W'=\dim W$ ([[Linear Algebra 3F Duality#^ladr-3-111|3.111]]); apply [[Linear Algebra 9D Tensor Products#^ladr-9-70|9.70]].

*Uses:* [[Linear Algebra 3F Duality#^ladr-3-111|3.111]], [[Linear Algebra 9D Tensor Products#^ladr-9-70|9.70]]

> [!theorem] 9.73 Bilinearity of tensor product
> $(v_1+v_2)\otimes w=v_1\otimes w+v_2\otimes w$, $\ v\otimes(w_1+w_2)=v\otimes w_1+v\otimes w_2$, $\ \lambda(v\otimes w)=(\lambda v)\otimes w=v\otimes(\lambda w)$.

^ladr-9-73

> [!remark] Warning
> $v\otimes w$ is *not* linear in the pair $(v,w)$: $(2v)\otimes(2w)=4(v\otimes w)$.

> [!proof]+
> Evaluate at $(\varphi,\tau)$: $\varphi(v_1+v_2)\tau(w)=\varphi(v_1)\tau(w)+\varphi(v_2)\tau(w)$, and similarly for the others.

> [!theorem] 9.74 Basis of V⊗ W
> (a) If $e_1,\dots,e_m$ in $V$ and $f_1,\dots,f_n$ in $W$ are independent, then $\{e_j\otimes f_k\}$ is independent in $V\otimes W$. (b) If they are bases, $\{e_j\otimes f_k\}$ is a basis of $V\otimes W$.

^ladr-9-74

> [!remark] Not every tensor is a product
> Every element is a *sum* of $v\otimes w$'s; e.g. $e_1\otimes f_1+e_2\otimes f_2$ is not a single $v\otimes w$ (its coefficient matrix has rank $2$; compare [[Linear Algebra 9D Tensor Products#^ladr-9-76|9.76]]).

> [!proof]+
> (a) Choose $\varphi_j\in V'$, $\tau_k\in W'$ with $\varphi_j(e_i)=\delta_{ji}$, $\tau_k(f_l)=\delta_{kl}$ ([[Linear map lemma|3.4]], after extending to bases). If $\sum a_{j,k}e_j\otimes f_k=0$, evaluate at $(\varphi_M,\tau_N)$: $a_{M,N}=0$. (b) (a) gives $mn=\dim(V\otimes W)$ independent vectors ([[Linear Algebra 9D Tensor Products#^ladr-9-72|9.72]], [[Linear Algebra 2C Dimension#^ladr-2-38|2.38]]).

*Uses:* [[Linear map lemma|3.4]], [[Linear Algebra 9D Tensor Products#^ladr-9-72|9.72]], [[Linear Algebra 2C Dimension#^ladr-2-38|2.38]]

> [!example] 9.76 Tensor product of element of F (p. 374)
> In $\F^m\otimes\F^n$ with the basis $\{e_j\otimes f_k\}$:
> $$
> v\otimes w=\sum_{j,k}v_jw_k\,e_j\otimes f_k,
> $$
> so identifying coefficients with an $m$-by-$n$ matrix, $v\otimes w\leftrightarrow vw^t=\begin{pmatrix}v_1w_1&\cdots&v_1w_n\\\vdots&&\vdots\\v_mw_1&\cdots&v_mw_n\end{pmatrix}$, a rank-$1$ matrix. General tensors are arbitrary matrices; the rank of the matrix is the minimal number of product terms needed (the Schmidt rank, via SVD [[Singular value decomposition|7.70]]).

^ladr-9-76

> [!definition] 9.77 Bilinear map
> A *bilinear map* $V\times W\to U$ is a function $\Gamma$ that is linear in each slot when the other is fixed.

^ladr-9-77

> [!example] 9.78 Bilinear maps (p. 374)
> - Every bilinear functional is a bilinear map to $\F$.
> - $(v,w)\mapsto v\otimes w$ from $V\times W$ to $V\otimes W$ ([[Linear Algebra 9D Tensor Products#^ladr-9-73|9.73]]).
> - $(S,T)\mapsto ST$ on $\Lin(V)\times\Lin(V)$ (composition).
> - $(v,T)\mapsto Tv$ from $V\times\Lin(V,W)$ to $W$ (evaluation). By [[Linear Algebra 9D Tensor Products#^ladr-9-79|9.79]] it becomes a linear map $V\otimes\Lin(V,W)\to W$: a 'contraction'.

^ladr-9-78

> [!theorem] 9.79 Converting bilinear maps to linear maps
> (a) For every bilinear $\Gamma:V\times W\to U$ there is a unique linear $\hat\Gamma:V\otimes W\to U$ with $\hat\Gamma(v\otimes w)=\Gamma(v,w)$. (b) Conversely, every linear $T:V\otimes W\to U$ gives a unique bilinear $T^\#(v,w)=T(v\otimes w)$.

^ladr-9-79

> [!remark] Universal property
> $\{\text{bilinear }V\times W\to U\}\cong\Lin(V\otimes W,U)$: the tensor product turns bilinear problems into linear ones. This characterizes $V\otimes W$ up to isomorphism.

> [!proof]+
> (a) Define $\hat\Gamma$ on the basis by $\hat\Gamma(e_j\otimes f_k)=\Gamma(e_j,f_k)$ ([[Linear map lemma|3.4]], [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]](b)). For $v=\sum a_je_j$, $w=\sum b_kf_k$: $\hat\Gamma(v\otimes w)=\sum a_jb_k\hat\Gamma(e_j\otimes f_k)=\sum a_jb_k\Gamma(e_j,f_k)=\Gamma(v,w)$. Uniqueness: a linear map is determined on the basis $\{e_j\otimes f_k\}$. (b) $T^\#$ is bilinear by [[Linear Algebra 9D Tensor Products#^ladr-9-73|9.73]] and linearity of $T$; uniqueness is clear.

*Uses:* [[Linear map lemma|3.4]], [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]], [[Linear Algebra 9D Tensor Products#^ladr-9-73|9.73]]

> [!theorem] 9.80 Inner product on tensor product of two inner product spaces
> If $V,W$ are inner product spaces, there is a unique inner product on $V\otimes W$ with
> $$
> \langle v\otimes w,u\otimes x\rangle=\langle v,u\rangle\langle w,x\rangle .
> $$

^ladr-9-80

> [!proof]+
> With orthonormal bases $e$ of $V$, $f$ of $W$, define $\big\langle\sum b_{j,k}e_j\otimes f_k,\sum c_{j,k}e_j\otimes f_k\big\rangle=\sum b_{j,k}\overline{c_{j,k}}$: the Euclidean inner product on coefficients (an inner product by [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]](b)). Expanding $v,u,w,x$ in the bases, $v\otimes w=\sum v_jw_ke_j\otimes f_k$, so
> $$
> \langle v\otimes w,u\otimes x\rangle=\sum_{j,k}v_jw_k\overline{u_jx_k}=\Big(\sum_jv_j\bar u_j\Big)\Big(\sum_kw_k\bar x_k\Big)=\langle v,u\rangle\langle w,x\rangle .
> $$
> Uniqueness: product tensors span $V\otimes W$.

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]]

> [!remark]- Connections
> - Physics: $\langle\psi_A\otimes\psi_B|\phi_A\otimes\phi_B\rangle=\langle\psi_A|\phi_A\rangle\langle\psi_B|\phi_B\rangle$.

> [!definition] 9.82 Inner product on tensor product of two inner product spaces
> *The* inner product on $V\otimes W$ is the one of [[Linear Algebra 9D Tensor Products#^ladr-9-80|9.80]]. In particular $\|v\otimes w\|=\|v\|\|w\|$.

^ladr-9-82

> [!theorem] 9.83 Orthonormal basis of V⊗ W
> If $e_1,\dots,e_m$ and $f_1,\dots,f_n$ are orthonormal bases of $V$ and $W$, then $\{e_j\otimes f_k\}$ is an orthonormal basis of $V\otimes W$.

^ladr-9-83

> [!remark] Point
> Any orthonormal bases work, not just the ones used to define the inner product.

> [!proof]+
> A basis by [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]](b); $\langle e_j\otimes f_k,e_M\otimes f_N\rangle=\langle e_j,e_M\rangle\langle f_k,f_N\rangle=\delta_{jM}\delta_{kN}$.

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]]

> [!remark] 9.84 Notation: V1, ..., Vm (p. 378)

^ladr-9-84

> [!definition] 9.85 M-linear functional, the vector space B(V1, ..., Vm)
> An *$m$-linear functional* on $V_1\times\dots\times V_m$ is linear in each slot; $\mathcal{B}(V_1,\dots,V_m)$ is the space of them.

^ladr-9-85

> [!example] 9.86 M-linear functional (p. 378)
> For $\varphi_k\in V_k'$: $\beta(v_1,\dots,v_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)$ is $m$-linear; sums of these give all of $\mathcal{B}(V_1,\dots,V_m)$.

^ladr-9-86

> [!theorem] 9.87 Dimension of the vector space of m-linear functionals
> $\dim\mathcal{B}(V_1,\dots,V_m)=(\dim V_1)\cdots(\dim V_m)$.

^ladr-9-87

> [!proof]+
> As in [[Linear Algebra 9D Tensor Products#^ladr-9-70|9.70]]: an $m$-linear functional is determined by its values on tuples of basis vectors, which may be arbitrary.

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-70|9.70]]

> [!definition] 9.88 Tensor product, V1 ⊗ ⋯ ⊗ Vm, v1 ⊗ ⋯ ⊗ vm
> $V_1\otimes\dots\otimes V_m=\mathcal{B}(V_1',\dots,V_m')$, and $(v_1\otimes\dots\otimes v_m)(\varphi_1,\dots,\varphi_m)=\varphi_1(v_1)\cdots\varphi_m(v_m)$.

^ladr-9-88

> [!remark]- Connections
> - Tensors of type $(r,s)$ in physics and in [[Differentiable Manifolds]]: $V^{\otimes r}\otimes(V')^{\otimes s}$.

> [!theorem] 9.89 Dimension of the tensor product
> $\dim(V_1\otimes\dots\otimes V_m)=(\dim V_1)\cdots(\dim V_m)$.

^ladr-9-89

> [!remark] Physics
> $N$ spin-$\tfrac12$ particles live in $(\C^2)^{\otimes N}$, of dimension $2^N$: the exponential growth behind the difficulty of simulating quantum many-body systems.

> [!proof]+
> [[Linear Algebra 9D Tensor Products#^ladr-9-87|9.87]] and $\dim V_k'=\dim V_k$.

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-87|9.87]]

> [!theorem] 9.90 Basis of V1 ⊗ ⋯ ⊗ Vm
> If $e^k_1,\dots,e^k_{n_k}$ is a basis of $V_k$, then $\{e^1_{j_1}\otimes\dots\otimes e^m_{j_m}\}$ is a basis of $V_1\otimes\dots\otimes V_m$. So elements are arrays with $m$ indices.

^ladr-9-90

> [!proof]+
> As in [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]]: evaluate at tuples of dual basis vectors to get independence, then count dimensions ([[Linear Algebra 9D Tensor Products#^ladr-9-89|9.89]]).

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-74|9.74]], [[Linear Algebra 9D Tensor Products#^ladr-9-89|9.89]]

> [!definition] 9.91 M-linear map
> An *$m$-linear map* $V_1\times\dots\times V_m\to U$ is linear in each slot when the others are fixed.

^ladr-9-91

> [!theorem] 9.92 Converting m-linear maps to linear maps
> (a) Every $m$-linear $\Gamma:V_1\times\dots\times V_m\to U$ induces a unique linear $\hat\Gamma:V_1\otimes\dots\otimes V_m\to U$ with $\hat\Gamma(v_1\otimes\dots\otimes v_m)=\Gamma(v_1,\dots,v_m)$. (b) Conversely, every linear $T$ on the tensor product gives the $m$-linear $T^\#(v_1,\dots,v_m)=T(v_1\otimes\dots\otimes v_m)$.

^ladr-9-92

> [!proof]+
> As in [[Linear Algebra 9D Tensor Products#^ladr-9-79|9.79]], using the basis of [[Linear Algebra 9D Tensor Products#^ladr-9-90|9.90]].

*Uses:* [[Linear Algebra 9D Tensor Products#^ladr-9-79|9.79]], [[Linear Algebra 9D Tensor Products#^ladr-9-90|9.90]]

