---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 4
section: 24
tags: [multivariable-analysis, math452]
---
← [[§23 Fubini's Theorem]] · ↑ [[· 4 Integration on Flat Domains]] · [[§25 Change of Variables on General Domains]] →

## General Change of Variables

**The Core Idea.**

When we compute $\iint_D f(x,y) \, dx \, dy$, we are summing up $f$-values weighted by infinitesimal areas $dx \, dy$.

Under a coordinate transformation $(x, y) = \Phi(u, v)$, the domain $D$ becomes $D^{\ast}$ in the $(u, v)$-plane. But here's the key point: *the infinitesimal areas change*.

A small rectangle $du \times dv$ in the $(u,v)$-plane does **not** map to a rectangle of the same area in the $(x,y)$-plane. Instead, it maps to a (curvilinear) region with area approximately $|J| \, du \, dv$, where $J$ is the Jacobian determinant ([[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]]).

![[m452-15-5.svg]]
*A small rectangle $R$ with sides $du, dv$ at $(u_0, v_0)$ (left) is carried by $\Phi$ to a curvilinear region $\Phi(R)$ (blue). The derivative sends the sides to $\boldsymbol{\Phi}_u\,du$ and $\boldsymbol{\Phi}_v\,dv$ (red). These span a parallelogram (dashed) of area $|\det(\boldsymbol{\Phi}_u, \boldsymbol{\Phi}_v)|\,du\,dv = |J|\,du\,dv$, and it approximates $\Phi(R)$ ever better as the rectangle shrinks.*

To make the integral come out correctly, we must **compensate for this area distortion** by multiplying by $|J|$:

$$
\underbrace{\iint_D f(x, y) \, dx \, dy}_{\text{sum of } f \times \text{(true area)}} = \underbrace{\iint_{D^*} f(\Phi(u,v)) \cdot |J(u,v)| \, du \, dv}_{\text{sum of } f \times |J| \times du \, dv}
$$

The factor $|J|$ exactly cancels the area distortion, ensuring both sides compute the same weighted sum.

**Section Organization:**
1. **Preliminaries:** Jordan measurability and the 1D formula
2. **Main Theorem:** Statement for rectangular domains, with three proofs
3. **Extension:** General Jordan measurable domains
4. **Geometric Interpretation:** Determinants as volume distortion; higher dimensions
5. **Coordinate Systems and Worked Examples:** Polar, elliptical, spherical; full computations

### Preliminaries

> [!definition] Definition §24.1: Jordan Measure Zero
> A bounded set $E \subseteq \mathbb{R}^2$ has **Jordan measure zero** if for every $\varepsilon > 0$, there exist finitely many rectangles $R_1, \ldots, R_N$ such that:
>
> $$
> E \subseteq \bigcup_{k=1}^N R_k \quad \text{and} \quad \sum_{k=1}^N \text{Area}(R_k) < \varepsilon.
> $$

^def-24-1

> [!remark]- Connections
> - Lebesgue null sets allow countably many rectangles ([[§10 Lebesgue Outer Measure#^def-10-4|551 Def. §10.4]]), so every countable set is null ([[§10 Lebesgue Outer Measure#^ex-10-2|551 Ex. §10.2]]); the graph of any measurable function is null by [[§26 Applications of Tonelli's Theorem#^cor-26-4|551 Cor. §26.4]].

> [!definition] Definition §24.2: Jordan Measurable Set
> A bounded set $D \subseteq \mathbb{R}^2$ is **Jordan measurable** if its boundary $\partial D$ ([[§2 Open and Closed Sets#^def-2-5|Def. §2.5]]) has Jordan measure zero.

^def-24-2

> [!remark]- Connections
> - Agrees with the inner/outer-content definition [[§20 Multivariable Integration#^def-20-7|Def. §20.7]] for bounded sets, by the [[§20 Multivariable Integration#^rem-20-2|remark following it]].

> [!example] Example §24.1: Jordan Measurable Sets
> The following are Jordan measurable:
> - Rectangles, triangles, and polygons
> - Disks $\{(x,y): x^2 + y^2 \leq r^2\}$ and ellipses
> - [[§23 Fubini's Theorem#^def-23-1|Type I regions]]: $\{(x,y): a \leq x \leq b, \, \phi(x) \leq y \leq \psi(x)\}$ where $\phi, \psi$ are continuous
> - Type II regions: $\{(x,y): c \leq y \leq d, \, \phi(y) \leq x \leq \psi(y)\}$ where $\phi, \psi$ are continuous
> - Finite unions and intersections of the above
>
> **Non-example:** The set $\mathbb{Q}^2 \cap [0,1]^2$ (rationals in the unit square) is *not* Jordan measurable — its boundary is the entire square $[0,1]^2$.

^ex-24-1

> [!remark]- Connections
> - The non-example is the 2D analogue of the [[§32 The Definition of the Riemann Integral#^ex-32-3|Dirichlet function]] (451 Ex. §32.3): its indicator function is not Riemann integrable.

> [!theorem] Lemma §24.1: One-Dimensional Change of Variables
> Let $g: [a, b] \to [\alpha, \beta]$ be a $C^1$ bijection with $g'(t) \neq 0$ throughout. If $f$ is continuous on $[\alpha, \beta]$, then:
>
> $$
> \int_\alpha^\beta f(x) \, dx = \int_a^b f(g(t)) \cdot |g'(t)| \, dt.
> $$

^lem-24-1

> [!proof]+ Proof
> Define $F(x) = \int_\alpha^x f(s) \, ds$, so $F'(x) = f(x)$ by the [[§34 Fundamental Theorem of Calculus#^thm-34-4|Fundamental Theorem of Calculus]] (451 §34.4).
>
> Consider the composition $H(t) = F(g(t))$. By the [[§28 Basic Properties of the Derivative#^thm-28-3|chain rule]]:
>
> $$
> H'(t) = F'(g(t)) \cdot g'(t) = f(g(t)) \cdot g'(t).
> $$
>
> Integrating from $a$ to $b$ ([[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]):
>
> $$
> H(b) - H(a) = \int_a^b f(g(t)) \cdot g'(t) \, dt.
> $$
>
> But $H(b) - H(a) = F(g(b)) - F(g(a))$.
>
> If $g' > 0$: then $g(a) = \alpha$, $g(b) = \beta$, so $H(b) - H(a) = F(\beta) - F(\alpha) = \int_\alpha^\beta f(x) \, dx$.
>
> If $g' < 0$: then $g(a) = \beta$, $g(b) = \alpha$, and the formula gives a negative sign that cancels with $|g'| = -g'$.

^pf-24-1

*Uses:* [[§34 Fundamental Theorem of Calculus#^thm-34-4|451 §34.4]], [[§28 Basic Properties of the Derivative#^thm-28-3|451 §28.3]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 §34.1]]

> [!remark]- Connections
> - Both halves of the [[Fundamental Theorem of Calculus]] (451 §34) combined with the 1D chain rule; this lemma is the base case of every proof of [[§24 The Change of Variables Formula#^thm-24-2|Theorem §24.2]] below.
> - Computational version: the substitution rule for definite integrals, [[§43 The Substitution Rule#^thm-43-3|Calc Thm. §43.3]], and the inverse substitution x = g(t), [[§53 Trigonometric Substitution#^thm-53-1|Calc Thm. §53.1]] (with worked examples).

### Main Theorem (Rectangular Domain)

> [!theorem] Theorem §24.2: Change of Variables Formula — Rectangular Case
> Let $D^* = [a,b] \times [c,d]$ be a rectangle. Let $\Phi: D^* \to D$ be a $C^1$ bijection with $C^1$ inverse, where $D = \Phi(D^*)$.
>
> Write $\Phi(u, v) = (\varphi(u, v), \psi(u, v)) = (x, y)$.
>
> Assume the **Jacobian** ([[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]])
>
> $$
> J = \frac{\partial(x, y)}{\partial(u, v)} = \det \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix} = \varphi_u \psi_v - \varphi_v \psi_u
> $$
>
> satisfies $J \neq 0$ on $D^*$.
>
> If $f$ is continuous on $\overline{D}$, then:
>
> $$
> \boxed{\iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv}
> $$

^thm-24-2

We present three different proofs, each offering a distinct perspective:

| **Proof** | **Method** | **Key Idea** |
|:-:|:--|:--|
| 1 | Linear Case + Taylor | Prove for linear maps, then linearize via Taylor |
| 2 | Implicit Function Theorem | Reduce 2D to two 1D substitutions via IFT |
| 3 | Two-Step Decomposition | Factor into primitive transformations |

**Proof 1** is the most geometric: it shows why the Jacobian determinant measures area distortion. **Proof 2** is the most analytic: it tracks coordinate changes explicitly. **Proof 3** (from Courant–John) generalizes most easily to $n$ dimensions.

---

#### First proof: linear case and Taylor linearization

> [!proof]+ First Proof: Linear Case + Taylor Linearization
> We give a rigorous proof by first establishing the result for linear transformations, then extending to the general $C^1$ case with explicit error estimates.
>
> **Part I: The Linear Case.**
>
> Consider the linear transformation:
>
> $$
> \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix}, \quad \text{i.e.,} \quad x = au + bv, \quad y = cu + dv.
> $$
>
> The Jacobian is $J = ad - bc$ (the determinant of the matrix).
>
> *Claim:* A rectangle $[u_0, u_0 + h] \times [v_0, v_0 + k]$ maps to a parallelogram with area $|J| \cdot hk$.
>
> *Proof of claim:* The four corners of the rectangle map to:
>
> $$
> \begin{aligned}
> (u_0, v_0) &\mapsto (au_0 + bv_0, \, cu_0 + dv_0) =: P_0 \\
> (u_0 + h, v_0) &\mapsto (au_0 + bv_0 + ah, \, cu_0 + dv_0 + ch) =: P_1 \\
> (u_0, v_0 + k) &\mapsto (au_0 + bv_0 + bk, \, cu_0 + dv_0 + dk) =: P_2 \\
> (u_0 + h, v_0 + k) &\mapsto (au_0 + bv_0 + ah + bk, \, cu_0 + dv_0 + ch + dk) =: P_3
> \end{aligned}
> $$
>
> Observe that $\mathbf{P_0 P_1} = (ah, ch)$ and $\mathbf{P_0 P_2} = (bk, dk)$. Also, $\mathbf{P_2 P_3} = (ah, ch) = \mathbf{P_0 P_1}$ and $\mathbf{P_1 P_3} = (bk, dk) = \mathbf{P_0 P_2}$. Thus the image is indeed a parallelogram (opposite sides are equal and parallel).
>
> The two edge vectors of the parallelogram are:
>
> $$
> \boldsymbol{\alpha} = (ah, ch), \quad \boldsymbol{\beta} = (bk, dk).
> $$
>
> The area of the parallelogram is $|\det(\boldsymbol{\alpha}, \boldsymbol{\beta})|$ ([[§37 Determinants#^ladr-9-61|LADR 9.61]]):
>
> $$
> \text{Area} = \left| \det \begin{pmatrix} ah & bk \\ ch & dk \end{pmatrix} \right| = |adhk - bchk| = |ad - bc| \cdot hk = |J| \cdot hk.
> $$
>
> **Part II: General Case $\varphi, \psi \in C^1(D^{\ast})$.**
>
> Now consider the general transformation $\Phi(u, v) = (\varphi(u, v), \psi(u, v))$ where $\varphi, \psi$ are $C^1$ on a compact domain $\overline{D^*}$.
>
> Assume $J \neq 0$ on $D^*$ (WLOG, say $J > 0$; the case $J < 0$ is similar with $|J| = -J$).
>
> **Step 1: Linearization with uniform remainder.**
>
> Fix a point $(u_0, v_0) \in D^*$. For $(u, v)$ near $(u_0, v_0)$, the [[Mean Value Theorem]] (applied as in Step 3) gives:
>
> $$
> \begin{aligned}
> \varphi(u, v) &= \varphi(u_0, v_0) + \varphi_u(u_0, v_0)(u - u_0) + \varphi_v(u_0, v_0)(v - v_0) + R_\varphi(u, v) \\
> \psi(u, v) &= \psi(u_0, v_0) + \psi_u(u_0, v_0)(u - u_0) + \psi_v(u_0, v_0)(v - v_0) + R_\psi(u, v)
> \end{aligned}
> $$
>
> where the remainders satisfy:
>
> $$
> |R_\varphi(u, v)|, |R_\psi(u, v)| \leq 2\,\omega\big(\|(u - u_0, v - v_0)\|\big) \cdot \|(u - u_0, v - v_0)\|
> $$
>
> where $\omega(\delta) = \sup\{|g(p) - g(q)| : g \in \{\varphi_u, \varphi_v, \psi_u, \psi_v\},\ \|p - q\| \leq \delta\}$. Since $\Phi$ is only $C^1$, we use no second derivatives: $\omega(\delta) \to 0$ as $\delta \to 0$ by uniform continuity of the partials on the compact set $\overline{D^*}$.
>
> **Step 2: Image of a small rectangle.**
>
> Consider the rectangle $R = [u_0, u_0 + h] \times [v_0, v_0 + k]$. Define the **linearized map** at $(u_0, v_0)$ ([[§7 Differentiability#^def-7-2|Def. §7.2]]):
>
> $$
> L(u, v) = \Phi(u_0, v_0) + J_\Phi(u_0, v_0) \cdot \begin{pmatrix} u - u_0 \\ v - v_0 \end{pmatrix}
> $$
>
> where $J_\Phi = \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix}$ is the Jacobian matrix.
>
> By Part I, the linearized map $L$ takes $R$ to a parallelogram $P$ with:
>
> $$
> \text{Area}(P) = |J(u_0, v_0)| \cdot hk.
> $$
>
> **Step 3: Rigorous error estimate for curvilinear vs. parallelogram area.**
>
> The actual image $\Phi(R)$ is a curvilinear quadrilateral. We need to show the area differs from the parallelogram area by a controllable amount.
>
> *Setup:* Divide $D^{\ast}$ into small squares of side $1/2^m$. (For the unit square $D^{\ast}$ there are $2^m \cdot 2^m = 2^{2m}$ of them; for a general rectangle, see the end of the proof.)
>
> Since $\varphi, \psi \in C^1(\overline{D^*})$, the functions $\varphi, \psi, \varphi_u, \varphi_v, \psi_u, \psi_v$ are all [[§18 Compact Spaces#^rem-18-1|uniformly continuous]] on the compact domain. Also, assume these are bounded by some constant $B$:
>
> $$
> |\varphi_u|, |\varphi_v|, |\psi_u|, |\psi_v|, |\varphi|, |\psi| \leq B.
> $$
>
> *Focus on one small square:* Consider the square $[u_0, u_0 + h] \times [v_0, v_0 + k]$ where $h = k = 1/2^m$.
>
> A point $(u_0 + \theta h, v_0 + \alpha k)$ in this square (with $\theta, \alpha \in [0,1]$) maps to:
>
> $$
> \Phi(u_0 + \theta h, v_0 + \alpha k) = (\varphi(u_0 + \theta h, v_0 + \alpha k), \, \psi(u_0 + \theta h, v_0 + \alpha k)).
> $$
>
> The displacement from the corner $\Phi(u_0, v_0)$ is:
>
> $$
> \begin{aligned}
> &\Phi(u_0 + \theta h, v_0 + \alpha k) - \Phi(u_0, v_0) \\
> &= \big( \varphi(u_0 + \theta h, v_0 + \alpha k) - \varphi(u_0, v_0), \; \psi(u_0 + \theta h, v_0 + \alpha k) - \psi(u_0, v_0) \big).
> \end{aligned}
> $$
>
> *Linear approximation:* By the [[Mean Value Theorem]]:
>
> $$
> \begin{aligned}
> \varphi(u_0 + \theta h, v_0 + \alpha k) - \varphi(u_0, v_0) &= \varphi_u(u_0 + \theta' h, v_0 + \alpha' k) \cdot \theta h + \varphi_v(u_0 + \theta'' h, v_0 + \alpha'' k) \cdot \alpha k
> \end{aligned}
> $$
>
> for some intermediate points.
>
> The **linearized approximation** at $(u_0, v_0)$ would give:
>
> $$
> \varphi_u(u_0, v_0) \cdot \theta h + \varphi_v(u_0, v_0) \cdot \alpha k.
> $$
>
> *Error in first component:*
>
> $$
> \begin{aligned}
> |\text{error}_1| &= \big| \varphi_u(u_0 + \theta' h, v_0 + \alpha' k) - \varphi_u(u_0, v_0) \big| \cdot h \\
> &\quad + \big| \varphi_v(u_0 + \theta'' h, v_0 + \alpha'' k) - \varphi_v(u_0, v_0) \big| \cdot k.
> \end{aligned}
> $$
>
> *Using uniform continuity:* For any $\varepsilon > 0$, there exists $M$ such that for all $m \geq M$:
>
> $$
> \sup_{D_{ij}} \varphi_u - \inf_{D_{ij}} \varphi_u \leq \varepsilon
> $$
>
> where $D_{ij}$ is any square of side $1/2^m$. The same holds for $\varphi_v, \psi_u, \psi_v$ (four versions of $M$, one for each of $\varphi_u, \varphi_v, \psi_u, \psi_v$; take $M = \max$).
>
> Therefore, for $m \geq M$:
>
> $$
> |\text{error}_1| \leq \varepsilon \cdot \frac{1}{2^m} + \varepsilon \cdot \frac{1}{2^m} = \frac{2\varepsilon}{2^m}.
> $$
>
> Similarly, $|\text{error}_2| \leq \frac{2\varepsilon}{2^m}$.
>
> *Total position error:*
>
> $$
> |\text{error}| \leq \sqrt{(\text{error}_1)^2 + (\text{error}_2)^2} \leq \sqrt{4\varepsilon^2 \cdot \frac{1}{2^{2m}} + 4\varepsilon^2 \cdot \frac{1}{2^{2m}}} = \sqrt{2} \cdot \frac{2\varepsilon}{2^m}.
> $$
>
> *Geometric interpretation:* For each point in the parallelogram (the linearized image), draw a ball of radius $r = 2\sqrt{2} \varepsilon / 2^m$. The actual image point lies inside this ball.
>
> Take the union: $\bigcup_{p \in \text{parallelogram}} B(p; 2\sqrt{2}\varepsilon/2^m)$.
>
> *Area error estimate:* Assume the error region remains on the same side (no self-intersection, guaranteed when $\varepsilon$ is small relative to $|J|$). The error region is like a “fattened boundary” of the parallelogram. Here we use two inclusions: $\Phi(R)$ lies in $P$ fattened by $r$, which is immediate from the position estimate, and $\Phi(R)$ contains the points of $P$ at distance more than $r$ from $\partial P$, which needs a topological argument (the closed curve $\Phi(\partial R)$ stays within $r$ of $\partial P$ and so winds once around each such point) that we do not carry out here. Then $\Phi(R)$ and $P$ differ only inside the band of width $r$ on either side of $\partial P$.
> - The parallelogram has perimeter $\leq 4B \cdot (h + k) = 8B/2^m$ (since edge vectors have length $\leq B \cdot h$ and $B \cdot k$).
> - Fattening by radius $r = 2\sqrt{2}\varepsilon/2^m$ adds area $\leq \text{perimeter} \times r + \pi r^2$.
>
> Therefore:
>
> $$
> |\text{Area}(\Phi(R)) - \text{Area}(P)| \leq \frac{8B}{2^m} \cdot \frac{2\sqrt{2}\varepsilon}{2^m} + \pi \left( \frac{2\sqrt{2}\varepsilon}{2^m} \right)^2 = O\left( \frac{\varepsilon}{2^{2m}} \right).
> $$
>
> Since Area$(P) = |J| \cdot h \cdot k = |J|/2^{2m}$, the relative error is $O(\varepsilon)$, which can be made arbitrarily small.
>
> **Step 4: Riemann sum estimate.**
>
> Partition $D^*$ into $N = 2^{2m}$ small squares $R_{ij}$ of side $\Delta = 1/2^m$.
>
> Let $(u_{ij}, v_{ij})$ be a point in $R_{ij}$, and let $(x_{ij}, y_{ij}) = \Phi(u_{ij}, v_{ij})$.
>
> The Riemann sum for $\iint_D f \, dA$ is:
>
> $$
> S_N := \sum_{i,j} f(x_{ij}, y_{ij}) \cdot \text{Area}(\Phi(R_{ij})).
> $$
>
> By Step 3:
>
> $$
> \text{Area}(\Phi(R_{ij})) = |J(u_{ij}, v_{ij})| \cdot \Delta^2 + E_{ij}
> $$
>
> where $|E_{ij}| \leq C \varepsilon \cdot \Delta^2$ for $m \geq M(\varepsilon)$.
>
> Therefore:
>
> $$
> S_N = \sum_{i,j} f(x_{ij}, y_{ij}) \cdot |J(u_{ij}, v_{ij})| \cdot \Delta^2 + \sum_{i,j} f(x_{ij}, y_{ij}) \cdot E_{ij}.
> $$
>
> **Step 5: Error vanishes in the limit.**
>
> Since $f$ is continuous on the compact set $\overline{D}$, it is bounded ([[Continuous Image of a Compact Space is Compact|continuous image of compact is compact]]): $|f| \leq M_f$.
>
> The total error is:
>
> $$
> \left| \sum_{i,j} f(x_{ij}, y_{ij}) \cdot E_{ij} \right| \leq M_f \cdot \sum_{i,j} |E_{ij}| \leq M_f \cdot C\varepsilon \sum_{i,j} \Delta^2 = M_f \cdot C\varepsilon \cdot \text{Area}(D^*).
> $$
>
> Since $\varepsilon > 0$ was arbitrary, this error can be made as small as desired by choosing $m$ large enough.
>
> **Step 6: Transition from finite sum to integral (Riemann sum argument).**
>
> Cut the domain $D^*$ into $(2^m)^2$ pieces. Label all squares as $D_{ij}^{(m)}$ for $1 \leq i, j \leq 2^m$.
>
> After being mapped by $(\varphi, \psi)$, the square $D_{ij}^{(m)}$ maps to a curvilinear region $\Sigma_{ij}^{(m)}$.
>
> Denote the parallelogram approximation of $\Sigma_{ij}^{(m)}$ as $S_{ij}^{(m)}$.
>
> By Step 5, for all $\varepsilon > 0$, there exists $M$ such that for all $m \geq M$:
>
> $$
> \sum_{i=1}^{2^m} \sum_{j=1}^{2^m} \big| |\Sigma_{ij}^{(m)}| - |S_{ij}^{(m)}| \big| \leq C\varepsilon
> $$
>
> for some constant $C$ depending only on the bound $B$ for the partial derivatives.
>
> Now we relate the two sums:
>
> *Exact area sum* ([[§20 Multivariable Integration#^thm-20-1|additivity]]):
>
> $$
> \sum_{i,j} |\Sigma_{ij}^{(m)}| = |\Sigma| = \text{Area}(D) = \iint_D dx \, dy.
> $$
>
> *Parallelogram approximation sum:*
>
> $$
> \sum_{i,j} |S_{ij}^{(m)}| = \sum_{i,j} \left| \det \begin{pmatrix} \varphi_u & \varphi_v \\ \psi_u & \psi_v \end{pmatrix}_{(u_{i-1}, v_{j-1})} \right| \cdot \left( \frac{1}{2^m} \right)^2 = \sum_{i,j} |J(u_{i-1}, v_{j-1})| \cdot \left( \frac{1}{2^m} \right)^2.
> $$
>
> This is a Riemann sum for $\iint_{D^*} |J| \, du \, dv$.
>
> As $m \to \infty$, the Riemann sum converges:
>
> $$
> \sum_{i,j} |S_{ij}^{(m)}| = \sum_{i,j} |J(u_{i-1}, v_{j-1})| \cdot \left( \frac{1}{2^m} \right)^2 \xrightarrow{m \to \infty} \iint_{D^*} |J| \, du \, dv.
> $$
>
> Since $\big| \sum_{i,j} |\Sigma_{ij}^{(m)}| - \sum_{i,j} |S_{ij}^{(m)}| \big| \leq C\varepsilon$ for $m \geq M$, and $\varepsilon$ was arbitrary:
>
> $$
> \iint_D dx \, dy = |\Sigma| = \iint_{D^*} |J| \, du \, dv.
> $$
>
> **Step 7: Derive the final result with $f$.**
>
> Now consider $\iint_D f(x, y) \, dx \, dy$.
>
> The diameter ([[§21 The Definition of the Integral#^def-21-4|Def. §21.4]]) of the curvilinear region $\Sigma_{ij}^{(m)}$ is small: for $p, q$ in the square $D_{ij}^{(m)}$, the [[Mean Value Theorem]] in each coordinate direction gives $|\varphi(p) - \varphi(q)|, |\psi(p) - \psi(q)| \leq B(|p_1 - q_1| + |p_2 - q_2|) \leq \sqrt{2}B\|p - q\|$, so
>
> $$
> \text{diam}(\Sigma_{ij}^{(m)}) \leq 2B \cdot \text{diam}(D_{ij}^{(m)}) = 2B \cdot \frac{\sqrt{2}}{2^m}.
> $$
>
> As $m \to \infty$, the diameter $\to 0$, so by the definition of the Riemann integral ([[§21 The Definition of the Integral#^def-21-7|Def. §21.7]]):
>
> $$
> \iint_D f(x, y) \, dx \, dy = \lim_{m \to \infty} \sum_{i,j} f(x_{ij}^*, y_{ij}^*) \cdot |\Sigma_{ij}^{(m)}|
> $$
>
> where $(x_{ij}^*, y_{ij}^*)$ is any point in $\Sigma_{ij}^{(m)}$.
>
> Choose $(x_{ij}^*, y_{ij}^*) = (\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1}))$. Then:
>
> $$
> \begin{aligned}
> \iint_D f(x, y) \, dx \, dy &= \lim_{m \to \infty} \sum_{i,j} f(\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1})) \cdot |\Sigma_{ij}^{(m)}| \\
> &= \lim_{m \to \infty} \sum_{i,j} f(\varphi(u_{i-1}, v_{j-1}), \psi(u_{i-1}, v_{j-1})) \cdot |J(u_{i-1}, v_{j-1})| \cdot \frac{1}{(2^m)^2} \\
> &= \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv.
> \end{aligned}
> $$
>
> The second equality uses that $|\Sigma_{ij}^{(m)}| = |J| \cdot (1/2^m)^2 + O(\varepsilon/2^{2m})$ and the error vanishes in the limit (since $f$ is bounded and the total error is $O(\varepsilon)$).
>
> This completes the proof for the case where $D^*$ is the unit square. For a rectangle $D^* = [a, b] \times [c, d]$, replace the squares of side $1/2^m$ by the $2^{2m}$ congruent rectangles of sides $(b - a)/2^m$ and $(d - c)/2^m$; every estimate above holds with the same proof, up to constants depending on $b - a$ and $d - c$.

^pf-24-2

*Uses:* [[§37 Determinants#^ladr-9-61|LADR 9.61]], [[§7 Differentiability#^def-7-2|Def. §7.2]], [[§16 The Inverse Function Theorem#^def-16-1|Def. §16.1]], [[Mean Value Theorem|451 §29.3]], [[§18 Compact Spaces#^rem-18-1|590 §18 Rem. (uniform continuity on compact sets)]], [[Continuous Image of a Compact Space is Compact|590 §18.3]], [[§20 Multivariable Integration#^thm-20-1|§20.1]], [[§21 The Definition of the Integral#^def-21-4|Def. §21.4]], [[§21 The Definition of the Integral#^def-21-7|Def. §21.7]], [[§21 The Definition of the Integral#^rem-21-6|§21 Rem. (Evaluating the Integral)]]

![[m452-15-9.svg]]
*Step 3 of the first proof. The linearized map $L$ sends the small square $R$ to the parallelogram $P$ (red, dashed) of area $|J|\,hk$. Each point of $\Phi(R)$ lies within $r = 2\sqrt2\,\varepsilon/2^m$ of the corresponding point of $P$, as at the top corner (dashed circle of radius $r$). So the boundary of $\Phi(R)$ (blue) stays inside the band of width $r$ around $\partial P$ (gray). The two areas can differ only by the area of that band, at most $\text{perimeter}(P) \cdot r + \pi r^2 = O(\varepsilon/2^{2m})$. That is small even compared with $\text{Area}(P) \sim 1/2^{2m}$.*

---

#### Second proof: via the Implicit Function Theorem

> [!proof]+ Second Proof: Implicit Function Theorem Approach
> This approach uses IFT to introduce intermediate coordinates $(x, v)$, reducing the 2D change of variables to two applications of the 1D formula ([[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]).
>
> **Setup and Assumptions.**
>
> Consider the transformation $\Phi(u, v) = (\varphi(u, v), \psi(u, v))$ with Jacobian $J = \varphi_u \psi_v - \varphi_v \psi_u$.
>
> Since $J \neq 0$ and the partial derivatives are continuous, at least one of $\varphi_u$ or $\varphi_v$ is nonzero at each point. WLOG, assume $\varphi_u > 0$ throughout (if not, we can partition the domain or relabel variables).
>
> Also assume $J > 0$ (the case $J < 0$ gives $|J| = -J$).
>
> **Step 1: Apply IFT to introduce $(x, v)$ coordinates.**
>
> Define $F(u, v, x) = \varphi(u, v) - x$. Since $F_u = \varphi_u > 0$, by the [[§15 The Implicit Function Theorem#^thm-15-2|Implicit Function Theorem]], we can locally solve $F = 0$ for $u$:
>
> $$
> \exists \, u = U(x, v) \quad \text{such that} \quad \varphi(U(x, v), v) = x.
> $$
>
> The function $U$ is $C^1$ with derivatives computed by implicit differentiation. Differentiating $\varphi(U(x,v), v) = x$:
>
> $$
> \begin{aligned}
> \text{w.r.t. } x: \quad & \varphi_u \cdot U_x = 1 \quad \Longrightarrow \quad U_x = \frac{1}{\varphi_u} > 0. \\
> \text{w.r.t. } v: \quad & \varphi_u \cdot U_v + \varphi_v = 0 \quad \Longrightarrow \quad U_v = -\frac{\varphi_v}{\varphi_u}.
> \end{aligned}
> $$
>
> **Step 2: Define $\gamma(x, v)$ and compute its derivative.**
>
> Define the composed function:
>
> $$
> \gamma(x, v) := \psi(U(x, v), v).
> $$
>
> This gives $y$ as a function of $(x, v)$: when we hold $x$ fixed and vary $v$, the point $(x, y) = (x, \gamma(x, v))$ traces a curve in the $(x, y)$-plane.
>
> Compute $\gamma_v$ using the [[Multivariable Chain Rule|chain rule]]:
>
> $$
> \begin{aligned}
> \gamma_v &= \psi_u \cdot U_v + \psi_v = \psi_u \cdot \left( -\frac{\varphi_v}{\varphi_u} \right) + \psi_v \\
> &= \frac{-\psi_u \varphi_v + \psi_v \varphi_u}{\varphi_u} = \frac{\varphi_u \psi_v - \varphi_v \psi_u}{\varphi_u} = \frac{J}{\varphi_u} > 0.
> \end{aligned}
> $$
>
> The inequality $\gamma_v > 0$ shows that, for fixed $x$, the map $v \mapsto y = \gamma(x, v)$ is strictly increasing.
>
> **Step 3: Change variables $(x, y) \to (x, v)$ using the 1D formula.**
>
> Consider any region $R$ in the $(x, y)$-plane that is the image of a region $B$ in the $(x, v)$-plane under the map $(x, v) \mapsto (x, \gamma(x, v))$.
>
> For fixed $x$, the map $v \mapsto y = \gamma(x, v)$ satisfies $\frac{dy}{dv} = \gamma_v(x, v)$.
>
> By the 1D change of variables formula ([[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]) applied to the inner integral:
>
> $$
> \int_{y_1(x)}^{y_2(x)} f(x, y) \, dy = \int_{v_1}^{v_2} f(x, \gamma(x, v)) \cdot \gamma_v(x, v) \, dv.
> $$
>
> Integrating over $x$ and using [[§23 Fubini's Theorem#^thm-23-2|Fubini]]:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_B f(x, \gamma(x, v)) \cdot \gamma_v(x, v) \, dx \, dv = \iint_B f(x, y) \cdot \frac{J}{\varphi_u} \, dx \, dv.
> $$
>
> **Step 4: Change variables $(x, v) \to (u, v)$ using the 1D formula again.**
>
> Now we transform from $(x, v)$ to $(u, v)$ via $x = \varphi(u, v)$, $v = v$.
>
> For fixed $v$, the map $u \mapsto x = \varphi(u, v)$ satisfies $\frac{dx}{du} = \varphi_u(u, v) > 0$.
>
> By the 1D formula applied to the inner integral (now integrating over $x$):
>
> $$
> \int_{x_1(v)}^{x_2(v)} g(x, v) \, dx = \int_{u_1}^{u_2} g(\varphi(u, v), v) \cdot \varphi_u(u, v) \, du.
> $$
>
> Applying this to our integral with $g(x, v) = f(x, \gamma(x, v)) \cdot \frac{J}{\varphi_u}$:
>
> $$
> \iint_B f(x, y) \cdot \frac{J}{\varphi_u} \, dx \, dv = \iint_{D^*} f(\varphi, \psi) \cdot \frac{J(u,v)}{\varphi_u(u,v)} \cdot \varphi_u(u, v) \, du \, dv.
> $$
>
> The $\varphi_u$ terms cancel:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot J(u, v) \, du \, dv.
> $$
>
> Since we assumed $J > 0$, we have $J = |J|$, completing the proof.

^pf-24-2-2

*Uses:* [[§24 The Change of Variables Formula#^lem-24-1|§24.1]], [[§15 The Implicit Function Theorem#^thm-15-2|§15.2]], [[Multivariable Chain Rule|§12.2]], [[§23 Fubini's Theorem#^thm-23-2|§23.2]]

---

#### Third proof: two-step decomposition (Courant–John)

> [!proof]+ Third Proof: Two-Step Decomposition (Courant–John)
> This approach, from Courant & John's *Introduction to Calculus and Analysis*, decomposes the general transformation into two simpler “primitive” transformations, each changing only one variable at a time. This method extends naturally to higher dimensions.
>
> **Setup.** We want to prove:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{R'} f(\phi(u, v), \psi(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du \, dv
> $$
>
> where $x = \phi(u, v)$, $y = \psi(u, v)$ gives a 1-1 $C^1$ mapping of region $R'$ (in the $uv$-plane) onto region $R$ with $J \neq 0$.
>
> **Key Idea: Factor the transformation into two primitive steps.**
>
> A **primitive transformation** is one that changes only one coordinate:
> - Type I: $(x, v) \mapsto (x, y)$ where $x$ stays fixed, $y = \Phi(v, x)$
> - Type II: $(u, v) \mapsto (x, v)$ where $v$ stays fixed, $x = \Psi(u, v)$
>
> *Claim:* Any $C^1$ transformation with $J \neq 0$ can be locally decomposed as a composition of two primitive transformations.
>
> *Proof of claim:* Since $J = \phi_u \psi_v - \phi_v \psi_u \neq 0$, at least one of $\phi_u$ or $\phi_v$ is nonzero.
>
> **Case 1:** If $\phi_u \neq 0$, define:
>
> $$
> \begin{aligned}
> \text{Step 2: } & (u, v) \mapsto (x, v) \quad \text{via} \quad x = \phi(u, v), \; v = v \\
> \text{Step 1: } & (x, v) \mapsto (x, y) \quad \text{via} \quad x = x, \; y = \psi(U(x, v), v)
> \end{aligned}
> $$
>
> where $U(x, v)$ is the inverse of $u \mapsto \phi(u, v)$ for fixed $v$ (exists by [[§15 The Implicit Function Theorem#^thm-15-2|IFT]] since $\phi_u \neq 0$).
>
> **Case 2:** If $\phi_v \neq 0$, we can interchange $u$ and $v$ and proceed similarly.
>
> In either case, the region $R$ can be covered by finitely many subregions where the decomposition works, and the integral over $R$ is the sum of integrals over these subregions ([[§22 Properties of the Integral#^thm-22-3|additivity over domains]]). $\square$ (claim)
>
> **Primitive Transformation Formula.**
>
> We prove the change of variables formula for primitive transformations using the 1D result ([[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]).
>
> Consider a Type I primitive: $(x, v) \mapsto (x, y)$ with $y = \Phi(v, x)$ and $\Phi_v > 0$.
>
> For fixed $x$, the map $v \mapsto y = \Phi(v, x)$ is a 1D change of variables with derivative $\Phi_v$.
>
> By [[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]:
>
> $$
> \int_{y_1}^{y_2} f(x, y) \, dy = \int_{v_1}^{v_2} f(x, \Phi(v, x)) \cdot \Phi_v(v, x) \, dv.
> $$
>
> Integrating over $x$ and using [[§23 Fubini's Theorem#^thm-23-2|Fubini]]:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_B f(x, \Phi(v, x)) \cdot \Phi_v(v, x) \, dx \, dv.
> $$
>
> The Jacobian of the Type I primitive is:
>
> $$
> \frac{\partial(x, y)}{\partial(x, v)} = \det \begin{pmatrix} 1 & 0 \\ \Phi_x & \Phi_v \end{pmatrix} = \Phi_v.
> $$
>
> Similarly, for a Type II primitive $(u, v) \mapsto (x, v)$ with $x = \Psi(u, v)$ and $\Psi_u > 0$:
>
> $$
> \iint_B g(x, v) \, dx \, dv = \iint_{R'} g(\Psi(u, v), v) \cdot \Psi_u(u, v) \, du \, dv.
> $$
>
> The Jacobian is:
>
> $$
> \frac{\partial(x, v)}{\partial(u, v)} = \det \begin{pmatrix} \Psi_u & \Psi_v \\ 0 & 1 \end{pmatrix} = \Psi_u.
> $$
>
> **Combining the Two Steps.**
>
> Composing the two primitive transformations $(u, v) \xrightarrow{\text{II}} (x, v) \xrightarrow{\text{I}} (x, y)$:
>
> *Step 1 (Type II):*
>
> $$
> \iint_B f(x, \Phi(v, x)) \cdot \Phi_v \, dx \, dv = \iint_{R'} f(\Psi, \Phi(v, \Psi)) \cdot \Phi_v(v, \Psi) \cdot \Psi_u \, du \, dv.
> $$
>
> Note that $y = \Phi(v, \Psi(u, v)) = \psi(u, v)$ by construction.
>
> *Step 2* ([[§12 Composition of Functions and the Chain Rule#^rem-12-4|Chain Rule for Jacobians]]):
>
> $$
> \frac{\partial(x, y)}{\partial(u, v)} = \frac{\partial(x, y)}{\partial(x, v)} \cdot \frac{\partial(x, v)}{\partial(u, v)} = \Phi_v \cdot \Psi_u.
> $$
>
> **Conclusion.**
>
> Combining everything:
>
> $$
> \iint_R f(x, y) \, dx \, dy = \iint_{R'} f(\phi(u, v), \psi(u, v)) \cdot \Phi_v \cdot \Psi_u \, du \, dv = \iint_{R'} f(\phi, \psi) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| du \, dv.
> $$
>
> (The absolute value appears because if $\Phi_v < 0$ or $\Psi_u < 0$, the orientation reverses, but the area element remains positive.)

^pf-24-2-3

*Uses:* [[§24 The Change of Variables Formula#^lem-24-1|§24.1]], [[§15 The Implicit Function Theorem#^thm-15-2|§15.2]], [[§22 Properties of the Integral#^thm-22-3|§22.3]], [[§23 Fubini's Theorem#^thm-23-2|§23.2]], [[§12 Composition of Functions and the Chain Rule#^rem-12-4|§12 Rem. (Chain Rule for Jacobians)]], [[§37 Determinants#^ladr-9-49|LADR 9.49]]

![[m452-15-10.svg]]
*The decomposition behind the second and third proofs. A $C^1$ map with $J \neq 0$ factors into two primitive maps, each of which changes one coordinate only. First, Type II: $(u, v) \mapsto (x, v)$ with $x = \Psi(u, v)$, so points slide horizontally and the lines $v = \text{const}$ (green) stay horizontal. Then Type I: $(x, v) \mapsto (x, y)$ with $y = \Phi(v, x)$, so points slide vertically (red dot: hollow before, filled after each step). Each step is a family of 1D substitutions ([[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]) in one variable. Integrating over the other variable with Fubini gives factors $\Psi_u$ and $\Phi_v$, and their product is the full Jacobian.*

> [!remark]- Connections
> - The linear case (Part I of the first proof) is [[§37 Determinants#^ladr-9-61|LADR 9.61]]: $T$ changes volume by the factor $|\det T|$; the $C^1$ case is this applied to the derivative cell by cell.
> - Generalizes the 1D substitution rule ([[§24 The Change of Variables Formula#^lem-24-1|Lemma §24.1]]) and the [[§22 Properties of the Integral#^thm-22-6|polar formula]]; extended to Jordan measurable domains in [[Change of Variables Formula (multiple integrals)|Theorem §25.3]] and to $\mathbb{R}^n$ in [[§25 Change of Variables on General Domains#^thm-25-6|Theorem §25.6]].
> - In forms language the integrand $f\,|J|\,du\,dv$ is the pullback $\Phi^*(f\,dx \wedge dy)$ (up to orientation): [[§37 The Algebra of Differential Forms#^ex-37-4|Ex. §37.4]].
> - Computational version: [[§124 Change of Variables in Multiple Integrals#^thm-124-1|Calc Thm. §124.1]] (with worked examples).

> [!remark] Remark: $|J|$ vs. $J$: Orientation and Area
> The change of variables formula uses $|J|$, not $J$. This distinction matters:
> - $|J|$ measures **area distortion**: how much the transformation stretches or compresses infinitesimal areas. This is always nonnegative and is the correct factor for computing integrals.
> - $J$ (with sign) measures **oriented area distortion**: $J > 0$ means the transformation preserves orientation, $J < 0$ means it reverses orientation (like a reflection).
>
> A common exam mistake is writing $J$ instead of $|J|$ in the formula. If you know $J > 0$ on your domain (e.g., polar coordinates with $J = r > 0$ for $r > 0$), then $|J| = J$ and the distinction is harmless. But if orientation could reverse (e.g., a transformation involving a reflection), omitting the absolute value gives the wrong answer.
>
> The signed Jacobian becomes important later when we study **differential forms** ([[§36 Introduction to Differential Forms|§36]]) and **oriented integrals** ([[§38 The Exterior Derivative#^def-38-3|Def. §38.3]]), where the orientation of the domain carries geometric meaning.

^rem-24-14

> [!remark]- Connections
> - The linear-algebra picture: [[§37 Determinants#^ladr-9-61|LADR 9.61]] (volume scales by $|\det T|$) and its orientation remark; $\det$ as signed volume.

#### Remarks: beyond rectangles

> [!remark] Remark: Extension to Arbitrary Domains: Jordan Measurability
> The three proofs above assume $D^{\ast}$ is a square (or rectangle). For arbitrary domains, we need additional assumptions and a more careful treatment using **Jordan measure**.
>
> **The Problem:** If $D^{\ast}$ is not a rectangle, how do we define the Riemann sum? We can't simply partition $D^{\ast}$ into small squares — some squares will partially overlap the boundary $\partial D^{\ast}$.
>
> **Solution: Jordan Measurable Domains.**
>
> *Definition:* A bounded set $D^{\ast} \subseteq \mathbb{R}^2$ is **Jordan measurable** if its boundary $\partial D^{\ast}$ has Jordan measure zero, i.e., for any $\varepsilon > 0$, the boundary can be covered by finitely many rectangles with total area $< \varepsilon$ ([[§24 The Change of Variables Formula#^def-24-1|Def. §24.1]], [[§24 The Change of Variables Formula#^def-24-2|Def. §24.2]]).
>
> *Equivalently:* The **inner Jordan measure** (supremum of areas of finite unions of rectangles contained in $D^{\ast}$) equals the **outer Jordan measure** (infimum of areas of finite unions of rectangles containing $D^{\ast}$) ([[§20 Multivariable Integration#^def-20-5|Def. §20.5]], [[§20 Multivariable Integration#^def-20-6|Def. §20.6]], [[§20 Multivariable Integration#^def-20-7|Def. §20.7]]).
>
> **Procedure for Arbitrary Jordan Measurable $D^{\ast}$:**
>
> *Step 1:* Enclose $D^{\ast}$ in a large rectangle $R = [a, b] \times [c, d]$.
>
> *Step 2:* Partition $R$ into small squares of side $1/2^m$. Classify each square $D_{ij}^{(m)}$ as:
> - **Interior squares:** $D_{ij}^{(m)} \subseteq D^{\ast}$ (entirely inside)
> - **Exterior squares:** $D_{ij}^{(m)} \cap D^{\ast} = \emptyset$ (entirely outside)
> - **Boundary squares:** $D_{ij}^{(m)} \cap \partial D^{\ast} \neq \emptyset$ (touch the boundary)
>
> *Step 3:* For the Riemann sum, sum only over interior squares:
>
> $$
> S_m^{\text{inner}} = \sum_{\substack{i,j \\ D_{ij}^{(m)} \subseteq D^*}} f(\varphi(u_{ij}), \psi(u_{ij})) \cdot |J(u_{ij})| \cdot \frac{1}{(2^m)^2}.
> $$
>
> Similarly, define the outer sum including boundary squares.
>
> *Step 4:* Since $\partial D^{\ast}$ has Jordan measure zero:
>
> $$
> \#\{\text{boundary squares}\} \cdot \frac{1}{(2^m)^2} \to 0 \quad \text{as } m \to \infty.
> $$
>
> Therefore, inner and outer sums converge to the same limit.
>
> **Additional Assumption Needed:**
>
> For the Change of Variables formula, we need both $D^*$ and $D = \Phi(D^*)$ to be Jordan measurable.
>
> *Key Lemma* ([[§25 Change of Variables on General Domains#^prop-25-2|Proposition §25.2]]): If $D^{\ast}$ is Jordan measurable and $\Phi: D^{\ast} \to D$ is a $C^1$ diffeomorphism with $J \neq 0$, then $D = \Phi(D^{\ast})$ is also Jordan measurable.
>
> *Proof sketch:* The boundary $\partial D = \Phi(\partial D^{\ast})$. Since $\Phi$ is $C^1$ and $\partial D^{\ast}$ has measure zero, the image $\Phi(\partial D^{\ast})$ also has measure zero (Lipschitz maps preserve measure zero sets). $\square$
>
> **Refined Theorem Statement:**
>
> > Let $D^{\ast} \subseteq \mathbb{R}^2$ be a **bounded, Jordan measurable** domain. Let $\Phi: \overline{D^{\ast}} \to \overline{D}$ be a $C^1$ bijection with $C^1$ inverse and $J \neq 0$ on $D^{\ast}$. If $f$ is continuous on $\overline{D}$, then:
> >
> > $$
> > \iint_D f(x, y) \, dx \, dy = \iint_{D^*} f(\varphi(u, v), \psi(u, v)) \cdot |J(u, v)| \, du \, dv.
> > $$
>
> **Common Jordan Measurable Domains** ([[§24 The Change of Variables Formula#^ex-24-1|Ex. §24.1]]):
> - Rectangles, triangles, polygons
> - Disks, ellipses
> - Regions between the graphs of two continuous functions (Type I and Type II regions)
> - Finite unions and intersections of the above
>
> **Non-Example:** The set of points in $[0,1]^2$ with both coordinates rational is bounded but *not* Jordan measurable (its boundary is the entire square, which has positive area).

^rem-24-12

> [!remark] Remark: Alternative: Lebesgue Integration
> In Lebesgue integration theory (MATH 551), the situation is cleaner:
> - The change of variables formula holds for any **Lebesgue measurable** set $D^{\ast}$.
> - No need for Jordan measurability — Lebesgue measure handles much more general sets.
> - The assumption “$J \neq 0$ everywhere” can be relaxed to “$J \neq 0$ [[§16 Limits and Positive Parts of Measurable Functions#^def-16-2|almost everywhere]].”
>
> However, for this course (Riemann integration), Jordan measurability is the appropriate condition.

^rem-24-13

*Continued in [[§25 Change of Variables on General Domains]]: arbitrary Jordan measurable domains, determinants as volume distortion, change of variables in ℝⁿ, and worked examples.*
