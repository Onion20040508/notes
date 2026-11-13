---
type: section
subject: "[[Quantum Field Theory]]"
level: C
chapter: C6c
section: C6c.10
conventions: "[[Larsen PHY 513]]"
tags: [quantum-field-theory, level-c]
---
← [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase]] · ↑ [[· C6c Feynman Rules for Amplitudes]] · [[§C6c.11 From the Question to the Formula]] →

*Sources: PHY 513, Problem Set 10 ("Scattering Processes"), Problem 1(d) (statement, Larsen; the user's solution, 2026-11-13) · Peskin & Schroeder, An Introduction to Quantum Field Theory, Problem 4.3(d) · the homes cited in each box.*

In [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase|§C6c.9]] the potential of the linear sigma model with $m^2 = -\mu^2$ had a whole sphere of minima, the pion fields were massless, and the $\pi\pi \to \pi\pi$ amplitude vanished at threshold. Problem 1(d) adds to the Lagrangian a term $a\,\Phi^N$ that is not invariant under the rotations and asks what changes. Three things do: the minimum becomes a single point, fixed by a new condition on $v$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]]); the pions get a mass, $m_\pi^2 = a/v$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]); and the amplitude at threshold no longer vanishes but is proportional to $a$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-5|Theorem §C6c.10.5]]). Nothing has to be expanded again: the Lagrangian in $\pi$, $\sigma$ for general $v$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 1) and the derivation of the amplitude ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]]) are reused.

**The mathematical picture.** The added term singles out the $N$-th axis of field space. The potential is no longer a function of the length of $\Phi$ alone: on each sphere $\Phi^i\Phi^i = \rho^2$ it is lowest at the one point where $\Phi^N = \rho$. The rotations that remain symmetries are those that leave the $N$-th axis fixed, the group $O(N - 1)$ acting on $\Phi^1, \dots, \Phi^{N-1}$ (for $N = 3$ the subgroup of [[§14 Homogeneous Spaces#^ex-14-2|591 Example §14.2]]); it is the symmetry that was still visible in the Lagrangian written in $\pi$ and $\sigma$.

![[ph-qft-c6c-9-1.svg]]
*The potential for $N = 2$, as in §C6c.9. Panels (b) and (c): the term $-a\,\Phi^N$ tilts the potential; of the circle of minima (dashed in (c)) one minimum remains, on the positive $\Phi^N$ axis, at the $v$ of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]]. Added figure; drawn for $a = 0.25\,\mu^3/\sqrt\lambda$.*

**Setup and scope.** As in §C6c.9: classical statements about the potential of constant fields; particle content and Feynman rules from the Lagrangian rewritten in $\pi$, $\sigma$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]); amplitudes at tree level, order $\lambda$ with $\lambda v^2$ counted as order one, free relativistic pion states of mass $m_\pi$ for the in and out states ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^pr-c6b-1-3|Principle §C6b.1.3]]). "Small $a$" means $a/v \ll \mu^2$, i.e. $a \ll \mu^3/\sqrt\lambda$; results are expanded to first order in $a$. The abbreviations $\Delta_s \equiv \delta^{ij}\delta^{kl}$, $\Delta_t \equiv \delta^{ik}\delta^{jl}$, $\Delta_u \equiv \delta^{il}\delta^{jk}$ name the three index structures by the channel that carries them ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]], 2).

## The model

> [!model] Model §C6c.10.1: The Linear Sigma Model with the Term aΦᴺ
> [[§C6c.8 The Linear Sigma Model꞉ Fields with an Internal Index#^mod-c6c-8-1|Model §C6c.8.1]] with $m^2 = -\mu^2 < 0$ and the added term
>
> $$
> \Delta\mathcal L = a\,\Phi^N , \qquad a > 0 \ \text{small} ,
> $$
>
> $a$ a constant of mass dimension $3$ (so that $\Delta\mathcal L$ has dimension $4$, with $[\Phi] = 1$: [[§C1b.3 Mass Dimension, Locality and Power Counting|§C1b.3]]).
> 1. *Symmetry.* $\Delta\mathcal L$ contains the component $\Phi^N$ alone and is not invariant under $\Phi^i \to R^{ij}\Phi^j$ for a general $R \in O(N)$; it is invariant under the $R$ that leave the $N$-th axis fixed. The symmetry of the model is broken **explicitly**: by a term of the Lagrangian.
> 2. *The potential* ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]) gains $-a\,\Phi^N$:
>
> $$
> V(\Phi) = -\frac12\,\mu^2\,\Phi^i\Phi^i + \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 - a\,\Phi^N .
> $$
>
> 3. *The interaction.* $\Delta\mathcal L$ is linear in the field, so it adds no cubic or quartic term: the interaction terms are those of §C6c.9.
>
> *Model:* [[§C6a.0 Setups and Observables#^mod-c6a-0-3|Model §C6a.0.3]] with $N$ fields; *applies:* the theory itself, for $a > 0$; at $a = 0$ it is the model of §C6c.9.
>
> *Source: PHY 513, Problem Set 10, Problem 1(d) (statement, Larsen: "Break the symmetry explicitly by adding $\Delta\mathcal L = a\,\Phi^N$ to (3), with $a > 0$ small") · PS Problem 4.3(d) · items 1–3 written here*

^mod-c6c-10-1

## The minimum and the masses

> [!theorem] Theorem §C6c.10.2: The Minimum Lies on the N-th Axis, at v(λv² − μ²) = a
> For the potential of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]]:
> 1. on every sphere $\Phi^i\Phi^i = \rho^2$ the potential is lowest at $\Phi^N = \rho$; so the field at the minimum points along the $N$-th direction, $\Phi = (0, \dots, 0, v)$ with $v > 0$;
> 2. $v$ is determined by
>
> $$
> V'(v) = -\mu^2v + \lambda v^3 - a = 0 \qquad\Longleftrightarrow\qquad v\,\bigl(\lambda v^2 - \mu^2\bigr) = a ;
> $$
>
> 3. for small $a$, $v = \dfrac{\mu}{\sqrt\lambda} + O(a)$; explicitly $v = \dfrac{\mu}{\sqrt\lambda} + \dfrac{a}{2\mu^2} + O(a^2)$.
>
> The minimum is a single point, not a sphere: the direction of the field is no longer free.
>
> *Model:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]]; *applies:* the classical potential of constant fields, $a > 0$; parts 1–2 exact, part 3 to the order stated.
>
> *Source: PHY 513, Problem Set 10, Problem 1(d) (the user's solution: parts 1–2, and "$v = \frac{\mu}{\sqrt\lambda} + O(a)$") · the coefficient $\frac{a}{2\mu^2}$ of part 3 written here, checked with `qft-C/tools/hw10/verify.py`*

^thm-c6c-10-2

> [!derivation]- Derivation
> **Step 1** (the potential). The potential is minus the non-derivative part of $\mathcal L$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]]), so $\Delta\mathcal L = a\,\Phi^N$ adds $-a\,\Phi^N$ to it:
>
> $$
> V(\Phi) = -\frac12\,\mu^2\,\Phi^i\Phi^i + \frac\lambda4\bigl(\Phi^i\Phi^i\bigr)^2 - a\,\Phi^N .
> $$
>
> **Step 2** (the direction). The first two terms depend only on $\rho^2 = \Phi^i\Phi^i$. For fixed $\rho$, since $a > 0$ and $\Phi^N \le \rho$, the last term is lowest for $\Phi^N = \rho$, i.e. for the field along the $N$'th direction, $\Phi = (0, \dots, 0, v)$.
>
> **Step 3** (along the axis). Along this direction
>
> $$
> V(v) = -\frac12\,\mu^2v^2 + \frac\lambda4\,v^4 - a\,v ,
> $$
>
> and differentiating gives the new condition determining $v$:
>
> $$
> V'(v) = -\mu^2v + \lambda v^3 - a = 0 \qquad\Longleftrightarrow\qquad v\,\bigl(\lambda v^2 - \mu^2\bigr) = a .
> $$
>
> **Step 4** (part 3; written here). Put $v = v_0 + \delta$ with $v_0 = \mu/\sqrt\lambda$, $\lambda v_0^2 = \mu^2$, and keep the first order in $\delta$: $\lambda v^2 - \mu^2 = 2\lambda v_0\delta + O(\delta^2)$, so $v(\lambda v^2 - \mu^2) = 2\lambda v_0^2\,\delta + O(\delta^2) = 2\mu^2\delta + O(\delta^2)$. Setting this equal to $a$: $\delta = \frac{a}{2\mu^2} + O(a^2)$.
>
> **What the derivation shows.**
> - For $v > 0$ and $a > 0$ the condition gives $\lambda v^2 - \mu^2 = a/v > 0$: $v$ is larger than $\mu/\sqrt\lambda$, the minimum moves outward along the axis (panel (b) of the figure).
> - The combination $a/v$ is what enters the masses and the amplitude → [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]], [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-5|Theorem §C6c.10.5]].
> - At $a = 0$ the condition is $v(\lambda v^2 - \mu^2) = 0$, the stationary points $v = 0$ and $v = \mu/\sqrt\lambda$ of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]], and Step 2 gives no direction.

^der-c6c-10-2

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-1|Def. §C6c.9.1]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-1|Theorem §C6c.9.1]]

> [!theorem] Theorem §C6c.10.3: With aΦᴺ the Pions Are No Longer Massless
> With $\Phi^i = \pi^i$, $\Phi^N = v + \sigma$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]) and $v$ the solution of $v(\lambda v^2 - \mu^2) = a$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]]), the Lagrangian of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]] is
>
> $$
> \begin{aligned}
> \mathcal L ={}& \Bigl[\frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i - \frac12\,\frac{a}{v}\,\pi^i\pi^i - \frac\lambda4\bigl(\pi^i\pi^i\bigr)^2\Bigr] \\
> &+ \Bigl[\frac12\,\partial_\mu\sigma\,\partial^\mu\sigma - \frac12\Bigl(2\mu^2 + \frac{3a}{v}\Bigr)\sigma^2 - \lambda v\,\sigma^3 - \frac\lambda4\,\sigma^4\Bigr] \\
> &+ \Bigl[-\lambda v\,\pi^i\pi^i\,\sigma - \frac\lambda2\,\pi^i\pi^i\,\sigma^2\Bigr] - V(v) ,
> \end{aligned}
> $$
>
> with $V(v) = -\frac12\mu^2v^2 + \frac\lambda4v^4 - a\,v$. Hence:
> 1. the masses are
>
> $$
> m_\pi^2 = \frac{a}{v} , \qquad m_\sigma^2 = 2\mu^2 + \frac{3a}{v} ;
> $$
>
> since $a > 0$ and $v > 0$, $m_\pi^2 > 0$: the pions are no longer massless;
> 2. the term linear in $\sigma$ vanishes, again because $v$ is a stationary point of the potential ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-3|Theorem §C6c.9.3]]), and the constant is $-V(v)$;
> 3. the cubic and quartic terms have the same form as for $a = 0$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 2), with $v$ now the solution of the new condition.
>
> *Model:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]] in the fields of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]; *applies:* an identity between Lagrangians, exact in $a$; the masses are those of the free fields $\hat\pi^i$, $\hat\sigma$ of the perturbation expansion (lowest order).
>
> *Source: PHY 513, Problem Set 10, Problem 1(d) (the user's solution; statement: "Find the new condition determining $v$, and the masses $m_\pi^2$ and $m_\sigma^2$. Show that the pions are no longer massless") · checked with `qft-C/tools/hw10/verify.py`*

^thm-c6c-10-3

> [!derivation]- Derivation
> **Step 1** (the new term). With $\Phi^i = \pi^i$ and $\Phi^N = v + \sigma$, the new term is $\Delta\mathcal L = a\,v + a\,\sigma$.
>
> **Step 2** (the expansion for general $v$). The expansion of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], 1, with $v$ left general did not use $\lambda v^2 = \mu^2$, so
>
> $$
> \begin{aligned}
> \mathcal L ={}& \Bigl[\frac12\,\partial_\mu\pi^i\,\partial^\mu\pi^i + \frac12\bigl(\mu^2 - \lambda v^2\bigr)\pi^i\pi^i - \frac\lambda4\bigl(\pi^i\pi^i\bigr)^2\Bigr] \\
> &+ \Bigl[\frac12\,\partial_\mu\sigma\,\partial^\mu\sigma + \Bigl(v\bigl(\mu^2 - \lambda v^2\bigr) + a\Bigr)\sigma + \frac12\bigl(\mu^2 - 3\lambda v^2\bigr)\sigma^2 - \lambda v\,\sigma^3 - \frac\lambda4\,\sigma^4\Bigr] \\
> &+ \Bigl[-\lambda v\,\pi^i\pi^i\,\sigma - \frac\lambda2\,\pi^i\pi^i\,\sigma^2\Bigr] + \frac12\,\mu^2v^2 - \frac\lambda4\,v^4 + a\,v .
> \end{aligned}
> $$
>
> **Step 3** (use the condition). By the new condition, $\lambda v^2 - \mu^2 = a/v$. Then the term linear in $\sigma$ vanishes, $v(\mu^2 - \lambda v^2) + a = -a + a = 0$, and
>
> $$
> \frac12\bigl(\mu^2 - \lambda v^2\bigr) = -\frac12\,\frac{a}{v} , \qquad \frac12\bigl(\mu^2 - 3\lambda v^2\bigr) = -\frac12\Bigl(2\mu^2 + 3\bigl(\lambda v^2 - \mu^2\bigr)\Bigr) = -\frac12\Bigl(2\mu^2 + \frac{3a}{v}\Bigr) .
> $$
>
> **Step 4** (the constant). The constant is $\frac12\mu^2v^2 - \frac\lambda4v^4 + a\,v = -V(v)$, and the Lagrangian becomes that of the statement.
>
> **Step 5** (the masses). The quadratic terms are $-\frac12\,\frac{a}{v}\,\pi^i\pi^i$ and $-\frac12\bigl(2\mu^2 + \frac{3a}{v}\bigr)\sigma^2$, so (Step 1 of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-4|Derivation §C6c.9.4]]) $m_\pi^2 = \frac{a}{v}$ and $m_\sigma^2 = 2\mu^2 + \frac{3a}{v}$. Since $a > 0$, $m_\pi^2 > 0$: the pions are no longer massless.
>
> **What the derivation shows.**
> - The pion mass term has the coefficient $\frac12(\mu^2 - \lambda v^2)$, which at $a = 0$ was removed by the condition of the minimum; now the condition leaves $-\frac12\frac{a}{v}$: the pion mass is first order in $a$.
> - Only the quadratic terms and the constant change; $\Delta\mathcal L$ is linear in the fields and cannot change a cubic or quartic term ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]], 3).

^der-c6c-10-3

*Uses:* [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-2|Theorem §C6c.9.2]], [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-3|Theorem §C6c.9.3]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-4|Derivation §C6c.9.4]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]

## The amplitude

> [!theorem] Theorem §C6c.10.4: Feynman Rules and the ππ → ππ Amplitude with aΦᴺ
> In [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]], with $v$, $m_\pi^2$, $m_\sigma^2$ of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]] and [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]:
> 1. the vertex factors are those of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]], unchanged in form, with $v$ now the solution of the new condition;
> 2. the propagators carry the new masses: a pion line is $\dfrac{i\,\delta^{ij}}{p^2 - m_\pi^2 + i\varepsilon}$, a sigma line $\dfrac{i}{p^2 - m_\sigma^2 + i\varepsilon}$;
> 3. the amplitude of $\pi^i(p_1)\,\pi^j(p_2) \to \pi^k(p_3)\,\pi^l(p_4)$ at order $\lambda$ is that of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]] with the sigma mass $2\mu^2$ replaced by $m_\sigma^2$:
>
> $$
> i\mathcal M = -2i\lambda\,\bigl(\Delta_s + \Delta_t + \Delta_u\bigr) + (-2i\lambda v)^2\biggl[\Delta_s\,\frac{i}{s - m_\sigma^2} + \Delta_t\,\frac{i}{t - m_\sigma^2} + \Delta_u\,\frac{i}{u - m_\sigma^2}\biggr] ,
> $$
>
> where $\Delta_s \equiv \delta^{ij}\delta^{kl}$, $\Delta_t \equiv \delta^{ik}\delta^{jl}$, $\Delta_u \equiv \delta^{il}\delta^{jk}$, $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$, and the external pions are on shell with $p_n^2 = m_\pi^2$.
>
> *Model:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]] in the fields of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^def-c6c-9-2|Def. §C6c.9.2]]; *applies:* tree level, order $\lambda$ with $\lambda v^2$ counted as order one; exact in $a$ at this order; $i\varepsilon$ dropped, $s \ne m_\sigma^2$.
>
> *Source: PHY 513, Problem Set 10, Problem 1(d) (the user's solution: "The cubic and quartic terms of $\mathcal L$ have the same form as in (b), so the vertex factors are those of (b), with $v$ now the solution of the new condition. The derivation of (c) carries over with the sigma mass $2\mu^2$ replaced by $m_\sigma^2$ in the sigma propagator") · the pion propagator of part 2 written here (it does not enter the amplitude at this order)*

^thm-c6c-10-4

> [!derivation]- Derivation
> **Step 1** (vertices). The cubic and quartic terms of $\mathcal L$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]], 3) have the same form as in §C6c.9, so $\hat{\mathcal H}_I$ is that of Step 1 of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-5|Derivation §C6c.9.5]] and the contraction counts of its Steps 3–7 are unchanged: the vertex factors are those of Theorem §C6c.9.5, with $v$ now the solution of the new condition.
>
> **Step 2** (propagators). The quadratic part of $\mathcal L$ is again a sum of independent real Klein–Gordon Lagrangians, now with masses $m_\pi^2 = a/v$ for the $N - 1$ fields $\hat\pi^i$ and $m_\sigma^2 = 2\mu^2 + 3a/v$ for $\hat\sigma$; Step 8 of Derivation §C6c.9.5 gives part 2 ([[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]], 1).
>
> **Step 3** (the amplitude). The derivation of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]] carries over with the sigma mass $2\mu^2$ replaced by $m_\sigma^2$ in the sigma propagator (its Step 4): the contact term, the count $\frac{(-i)^2}{2!}(\lambda v)^2\cdot8 = (-2i\lambda v)^2$, the $\delta$'s of the three splits and the integrals over $z_1$, $z_2$, $q$ do not involve the masses, except through $\frac{i}{q^2 - m_\sigma^2}$ at $q^2 = s, t, u$. The external pions enter only through their plane waves; they are on shell with $p_n^2 = m_\pi^2$.

^der-c6c-10-4

*Uses:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-5|Theorem §C6c.9.5]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^der-c6c-9-5|Derivation §C6c.9.5]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-6|Theorem §C6c.9.6]], [[§C6a.14 Feynman Rules for Polynomial Interactions#^lem-c6a-14-1|Lemma §C6a.14.1]]

> [!theorem] Theorem §C6c.10.5: The Threshold Amplitude Is Proportional to a
> For the amplitude of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-4|Theorem §C6c.10.4]] at threshold, $s = 4m_\pi^2$, $t = u = 0$ (all four pions at rest in the centre-of-mass frame, [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]]):
> 1. exactly in $a$,
>
> $$
> i\mathcal M\Big|_{\text{threshold}} = -2i\lambda\,\bigl(\Delta_s + \Delta_t + \Delta_u\bigr) + 4i\lambda^2v^2\Biggl[\frac{\Delta_s}{2\mu^2 - \frac{a}{v}} + \frac{\Delta_t + \Delta_u}{2\mu^2 + \frac{3a}{v}}\Biggr] ;
> $$
>
> 2. to first order in $a$,
>
> $$
> i\mathcal M\Big|_{\text{threshold}} = \frac{i\lambda\,a}{v\mu^2}\,\bigl(3\Delta_s - \Delta_t - \Delta_u\bigr) + O(a^2) ;
> $$
>
> 3. to leading order in $a$, with the coefficient evaluated at $v = \mu/\sqrt\lambda$,
>
> $$
> i\mathcal M\Big|_{\text{threshold}} \simeq \frac{i\lambda^{3/2}}{\mu^3}\,a\,\bigl(3\,\delta^{ij}\delta^{kl} - \delta^{ik}\delta^{jl} - \delta^{il}\delta^{jk}\bigr) ,
> $$
>
> which is proportional to $a$ and vanishes for $a \to 0$, the result of [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]]. For one pion ($N = 2$, all $\Delta = 1$) it is $i\lambda^{3/2}a/\mu^3$.
>
> *Model:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^mod-c6c-10-1|Model §C6c.10.1]]; *applies:* tree level, order $\lambda$ with $\lambda v^2$ counted as order one; part 1 exact in $a$, parts 2–3 for $a/v \ll \mu^2$; the amplitude is dimensionless ([[§C6b.1 The S-Matrix and the Invariant Amplitude#^thm-c6b-1-5|Theorem §C6b.1.5]]; $[a] = 3$, $[\mu] = 1$, $[\lambda] = 0$).
>
> *Source: PHY 513, Problem Set 10, Problem 1(d) (the user's solution; statement: "Compute the $\pi^i\pi^j \to \pi^k\pi^l$ amplitude at threshold, $s = 4m_\pi^2$, $t = u = 0$. Show that, to leading order in $a$, it is proportional to $a$") · checked with `qft-C/tools/hw10/verify.py` (series in $a$, and numerically with the exact $v$)*

^thm-c6c-10-5

> [!derivation]- Derivation
> **Step 1** (the denominators at threshold). At threshold $s = 4m_\pi^2 = \frac{4a}{v}$ and $t = u = 0$. With $m_\sigma^2 = 2\mu^2 + \frac{3a}{v}$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]]),
>
> $$
> s - m_\sigma^2 = \frac{4a}{v} - 2\mu^2 - \frac{3a}{v} = -\Bigl(2\mu^2 - \frac{a}{v}\Bigr) , \qquad t - m_\sigma^2 = u - m_\sigma^2 = -\Bigl(2\mu^2 + \frac{3a}{v}\Bigr) .
> $$
>
> **Step 2** (part 1). With $(-2i\lambda v)^2\cdot i = -4i\lambda^2v^2$, the amplitude of [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-4|Theorem §C6c.10.4]] becomes
>
> $$
> i\mathcal M\Big|_{\text{threshold}} = -2i\lambda\,\bigl(\Delta_s + \Delta_t + \Delta_u\bigr) + 4i\lambda^2v^2\Biggl[\frac{\Delta_s}{2\mu^2 - \frac{a}{v}} + \frac{\Delta_t + \Delta_u}{2\mu^2 + \frac{3a}{v}}\Biggr] .
> $$
>
> **Step 3** (expansion in $a$). By the condition for $v$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]]), $\lambda v^2 = \mu^2 + \frac{a}{v}$, so $4i\lambda^2v^2 = 4i\lambda\bigl(\mu^2 + \frac{a}{v}\bigr)$. To first order in $\frac{a}{v\mu^2}$ (geometric series, [[§14 Series#^ex-14-4|451 Example §14.4]]),
>
> $$
> \begin{aligned}
> \frac{4i\lambda\bigl(\mu^2 + \frac{a}{v}\bigr)}{2\mu^2 - \frac{a}{v}} &= 2i\lambda\,\frac{1 + \frac{a}{v\mu^2}}{1 - \frac{a}{2v\mu^2}} = 2i\lambda\Bigl(1 + \frac{a}{v\mu^2}\Bigr)\Bigl(1 + \frac{a}{2v\mu^2}\Bigr) + O(a^2) = 2i\lambda + \frac{3i\lambda\,a}{v\mu^2} + O(a^2) , \\
> \frac{4i\lambda\bigl(\mu^2 + \frac{a}{v}\bigr)}{2\mu^2 + \frac{3a}{v}} &= 2i\lambda\,\frac{1 + \frac{a}{v\mu^2}}{1 + \frac{3a}{2v\mu^2}} = 2i\lambda\Bigl(1 + \frac{a}{v\mu^2}\Bigr)\Bigl(1 - \frac{3a}{2v\mu^2}\Bigr) + O(a^2) = 2i\lambda - \frac{i\lambda\,a}{v\mu^2} + O(a^2) .
> \end{aligned}
> $$
>
> **Step 4** (part 2). The terms $2i\lambda$ cancel the contact term, and
>
> $$
> i\mathcal M\Big|_{\text{threshold}} = \frac{i\lambda\,a}{v\mu^2}\,\bigl(3\Delta_s - \Delta_t - \Delta_u\bigr) + O(a^2) .
> $$
>
> **Step 5** (part 3). Since $v = \frac{\mu}{\sqrt\lambda} + O(a)$ ([[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]], 3), to leading order in $a$ the coefficient is evaluated at $v = \mu/\sqrt\lambda$: $\frac{\lambda a}{v\mu^2} \to \frac{\lambda\sqrt\lambda\,a}{\mu\cdot\mu^2} = \frac{\lambda^{3/2}a}{\mu^3}$, which gives the statement, proportional to $a$.
>
> **What the derivation shows.**
> - Three places carry the first order in $a$: the pion mass in $s = 4m_\pi^2$, the sigma mass in the denominators, and $\lambda v^2 = \mu^2 + a/v$ in the two cubic vertices. In units of $\frac{a}{v\mu^2}$: the vertices give $+1$ in every channel; the $s$-channel denominator $2\mu^2 - \frac{a}{v}$ (pion mass $\frac{4a}{v}$ against the shift $\frac{3a}{v}$ of the sigma mass) gives $+\frac12$, the $t$- and $u$-channel denominators $2\mu^2 + \frac{3a}{v}$ give $-\frac32$. Times $2i\lambda$: $2i\lambda(1 + \frac12) = 3i\lambda$ and $2i\lambda(1 - \frac32) = -i\lambda$, the coefficients $3$ and $-1$.
> - The zeroth order cancels exactly as at $a = 0$ ([[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-7|Theorem §C6c.9.7]]); what is left is the remainder of that cancellation.
> - In terms of the pion mass (written here): $\frac{a}{v} = m_\pi^2$ and $\frac{\lambda}{\mu^2} = \frac{1}{v^2} + O(a)$, so the leading term is $i\,\frac{m_\pi^2}{v^2}\,(3\Delta_s - \Delta_t - \Delta_u)$.

^der-c6c-10-5

*Uses:* [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-4|Theorem §C6c.10.4]], [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-3|Theorem §C6c.10.3]], [[§C6c.10 The Linear Sigma Model꞉ Explicit Symmetry Breaking#^thm-c6c-10-2|Theorem §C6c.10.2]], [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]], [[§14 Series#^ex-14-4|451 Example §14.4]]

> [!abstract]- Mathematical background
> Proved in the Math vault; each line says what the physics above relies on.
>
> - [[§11 Topological Groups and Classical Matrix Groups#^def-11-7|591 Def. §11.7]] — $O(N)$; the term $a\,\Phi^N$ is one component of the field vector and is not preserved by a general rotation.
> - [[§14 Homogeneous Spaces#^ex-14-2|591 Example §14.2]] — the rotations that fix one axis (written there for $N = 3$): the symmetry left by $a\,\Phi^N$.
> - [[§14 Series#^ex-14-4|451 Example §14.4]] — the geometric series, used for the expansion of the threshold amplitude to first order in $a$.

> [!remark]- Connections
> - The condition $V'(v) = 0$ does two jobs in both sections: it removes the term linear in $\sigma$, and through $\frac12(\mu^2 - \lambda v^2)$ it fixes the pion mass, $0$ for $a = 0$ and $a/v$ for $a > 0$ — [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-3|Theorem §C6c.9.3]], [[§C6c.9 The Linear Sigma Model꞉ the Broken Phase#^thm-c6c-9-4|Theorem §C6c.9.4]].
> - The threshold of $\pi\pi \to \pi\pi$ moved from $E_{\rm cm} = 0$ to $E_{\rm cm} = 2m_\pi$; at threshold the pions are at rest, which is where $t = u = 0$ comes from — [[§C6b.3 The Cross Section#^thm-c6b-3-12|Theorem §C6b.3.12]].
> - A term that breaks a symmetry by giving different masses, for the phase symmetry of the complex field — [[§C1b.6 Conserved Charges and Internal Symmetries#^ex-c1b-6-3|Example §C1b.6.3]]; here the breaking term is linear in the field and changes the minimum itself.
> - The worked translations of questions into formulas, with the procedures used in §C6c.8–§C6c.10 — [[§C6c.11 From the Question to the Formula|§C6c.11]], [[P6 Tree Amplitude from a Lagrangian|P6]].
