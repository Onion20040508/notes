---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Canonical Quantization in Modes|Worksheet]] · [[PHY 513 Practice Midterm Solutions|Practice Midterm Solutions]]

# PHY 513 Worksheet — Canonical Quantization in Modes (Solutions)

Solutions to [[PHY 513 Worksheet — Canonical Quantization in Modes]], folded so that you can try first; each problem is embedded above its solution. Every solution follows the steps of [[P1 Canonical Quantization]] in the course's conventions ([[Larsen PHY 513]]): conjugate momenta, equal-time (anti)commutators, mode expansion, extraction and algebra, $\hat H$, $\hat{\mathbf P}$, $\hat Q$ in modes with the number-changing terms shown to vanish and the reordering constant shown, then states. Every $d^3x$ integral of plane waves is the identity $\int d^3x\,e^{i\mathbf k\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf k)$ in $\mathcal S'$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-3|Theorem §CA.3.3]]); every relabelling $\mathbf p \to -\mathbf p$ has Jacobian $1$ and keeps $E_{-\mathbf p} = E_{\mathbf p}$ ([[§CA.3 Fourier Transforms and Fourier Tricks#^thm-ca-3-7|Theorem §CA.3.7]]); a smooth prefactor times $\delta^3$ is evaluated on the support of the delta ([[§CA.2 Generalized Functions#^thm-ca-2-8|Theorem §CA.2.8]]). Each solution ends with the line that says how it was checked: *Checked against* names the home box in these notes (or the submitted solution, "as written"); *Derived here; check* marks a result with no home box, derived from boxes that exist, with the special case or independent computation it was checked against. A printable copy is `~/Downloads/PHY513_worksheet_quantization_solutions.pdf`.

---

## The real scalar field

### W1. Momentum density, equal-time relations, Heisenberg equations

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-1]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-1-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-1-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-1-c]]

> [!success]- Solution
> **Answers.** (a) $\pi = \dot\phi$, $\mathcal H = \frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2$, $H = \int d^3x\,\mathcal H$; $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, $[\hat\phi, \hat\phi] = [\hat\pi, \hat\pi] = 0$; mass dimension $3$. (b) $[\hat\phi, \hat H] = i\hat\pi$, $[\hat\pi, \hat H] = -i(-\nabla^2 + m^2)\hat\phi$, so $\partial_t\hat\phi = \hat\pi$, $\partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$ and $(\partial^2 + m^2)\hat\phi = 0$. (c) Conjugation by the unitary $e^{i\hat Ht}$ carries the relations to every common time; nothing about different times.
>
> **(a) Step 1** (momentum). $\partial_\mu\phi\,\partial^\mu\phi = \dot\phi^2 - (\nabla\phi)^2$, so $\mathcal L = \frac12\dot\phi^2 - \frac12(\nabla\phi)^2 - \frac12m^2\phi^2$ and $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi$ (the $\frac12$ cancels against the square).
>
> **Step 2** (Legendre transform). $\mathcal H = \pi\dot\phi - \mathcal L = \pi^2 - \frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2 = \frac12\pi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2$, the velocity eliminated by $\dot\phi = \pi$; $H = \int d^3x\,\mathcal H \ge 0$.
>
> **Step 3** (the postulate). On a time slice, $\hat\phi(\mathbf x)$ and $\hat\pi(\mathbf x)$ are Hermitian with $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$ and $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)] = [\hat\pi(\mathbf x), \hat\pi(\mathbf y)] = 0$; $\hat H = H[\hat\phi, \hat\pi]$. The relations are identities of operator-valued distributions: smeared, $[\hat\phi(f), \hat\pi(g)] = i\int d^3x\,fg$.
>
> **Step 4** (why a delta). Cut space into cells $V_i$ with cell averages $\Phi_i$. Then $L = \sum_iV_i\mathcal L_i$, so the momentum conjugate to $\Phi_i$ is $\Pi_i = \partial L/\partial\dot\Phi_i = V_i\pi_i$, and the ordinary canonical relation $[\hat\Phi_i, \hat\Pi_j] = i\delta_{ij}$ reads $[\hat\Phi_i, \hat\pi_j] = i\delta_{ij}/V_j$. As the cells shrink, $\delta_{ij}/V_j \to \delta^3(\mathbf x - \mathbf y)$: exactly the kernel with $\sum_jV_jf_j\,\delta_{ij}/V_j = f_i \to \int d^3y\,f(\mathbf y)\delta^3(\mathbf x - \mathbf y) = f(\mathbf x)$. Fields at different points commute.
>
> **Step 5** (dimension). $[\mathcal L] = 4$ gives $[\phi] = 1$ and $[\pi] = [\dot\phi] = 2$, so the commutator has dimension $3$, that of $\delta^3(\mathbf x - \mathbf y)$ (inverse volume). A Kronecker delta would be dimensionless.
>
> **(b) Step 1** ($\hat\phi$ against $\hat H$). All fields at time $t$; primes at $\mathbf x'$. $[\hat\phi, \hat\pi'^2] = \hat\pi'[\hat\phi, \hat\pi'] + [\hat\phi, \hat\pi']\hat\pi' = 2i\delta^3(\mathbf x - \mathbf x')\hat\pi'$ (the commutator is a number). $[\hat\phi, \partial'_i\hat\phi'] = \partial'_i[\hat\phi, \hat\phi'] = 0$, because $[\hat\phi(\mathbf x), \hat\phi(\mathbf x')]$ vanishes for all $\mathbf x'$; and $[\hat\phi, \hat\phi'^2] = 0$. So
>
> $$
> i\partial_t\hat\phi = [\hat\phi, \hat H] = \int d^3x'\,\tfrac12\cdot2i\,\delta^3(\mathbf x - \mathbf x')\,\hat\pi(t, \mathbf x') = i\hat\pi(t, \mathbf x), \qquad \partial_t\hat\phi = \hat\pi .
> $$
>
> **Step 2** (rewrite the gradient term). By parts, dropping the surface term for fields that fall off (matrix elements between wave packets), $\int d^3x'\,(\nabla'\hat\phi')^2 = -\int d^3x'\,\hat\phi'\nabla'^2\hat\phi'$, so $\hat H = \int d^3x'\,\bigl[\frac12\hat\pi'^2 + \frac12\hat\phi'(-\nabla'^2 + m^2)\hat\phi'\bigr]$.
>
> **Step 3** ($\hat\pi$ against $\hat H$). $[\hat\pi, \hat\pi'^2] = 0$. With $[\hat\pi, \hat\phi'] = -i\delta^3(\mathbf x - \mathbf x')$,
>
> $$
> [\hat\pi, \hat\phi'(-\nabla'^2 + m^2)\hat\phi'] = -i\delta^3(\mathbf x - \mathbf x')(-\nabla'^2 + m^2)\hat\phi' - i\,\hat\phi'(-\nabla'^2 + m^2)\delta^3(\mathbf x - \mathbf x') .
> $$
>
> In the second term move $-\nabla'^2$ onto $\hat\phi'$ by two integrations by parts (the distributional derivative of δ); both terms then give $-i(-\nabla^2 + m^2)\hat\phi(t, \mathbf x)$ after the $\mathbf x'$ integral, and they cancel the $\frac12$:
>
> $$
> i\partial_t\hat\pi = [\hat\pi, \hat H] = -i(-\nabla^2 + m^2)\hat\phi, \qquad \partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi .
> $$
>
> **Step 4** (combine). $\partial_t^2\hat\phi = \partial_t\hat\pi = (\nabla^2 - m^2)\hat\phi$, i.e. $(\partial_t^2 - \nabla^2 + m^2)\hat\phi = (\partial_\mu\partial^\mu + m^2)\hat\phi = 0$. Only the equal-time relations were used, never the mode expansion. (Do not replace $(-\nabla^2 + m^2)\hat\phi$ by $-\partial_t^2\hat\phi$ inside the commutator: a time derivative involves other times.)
>
> **(c) Step 1** (sandwich). Insert $\mathbf 1 = e^{-i\hat Ht}e^{i\hat Ht}$ between the factors of each product:
>
> $$
> e^{i\hat Ht}[\hat\phi_S(\mathbf x), \hat\pi_S(\mathbf y)]e^{-i\hat Ht} = \hat\phi(t, \mathbf x)\hat\pi(t, \mathbf y) - \hat\pi(t, \mathbf y)\hat\phi(t, \mathbf x) = [\hat\phi(t, \mathbf x), \hat\pi(t, \mathbf y)] ,
> $$
>
> while the right side $i\delta^3(\mathbf x - \mathbf y)$ is a number and is unchanged; the same for $[\hat\phi, \hat\phi]$ and $[\hat\pi, \hat\pi]$. Only unitarity was used, so this holds for any $\hat H$.
>
> **Step 2** (different times). One unitary sandwiches the whole product, so the same $t$ enters both fields: nothing is postulated for $[\hat\phi(x), \hat\phi(y)]$ at $x^0 \ne y^0$. That commutator is computed, not assumed: for the free field it is the c-number $iD(x - y)$, nonzero inside the light cone.
>
> *Checked against:* (a) [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], [[§C2a.1 Canonical Quantization of Fields#^pr-c2a-1-2|Principle §C2a.1.2]], [[§C2a.1 Canonical Quantization of Fields#^rem-c2a-1-2|§C2a.1, Remark: Why a delta function, and not a Kronecker delta]] (cells, dimension 3), [[§C2a.1 Canonical Quantization of Fields#^thm-c2a-1-3|Theorem §C2a.1.3]]; (b) [[§C2b.1 Heisenberg Fields#^thm-c2b-1-2|Theorem §C2b.1.2]] and [[§C2b.1 Heisenberg Fields#^der-c2b-1-2|Derivation §C2b.1.2]] (the same steps), [[§C2b.1 Heisenberg Fields#^cau-c2b-1-1|§C2b.1, Caution: Equal times only]]; (c) [[§C2b.1 Heisenberg Fields#^thm-c2b-1-1|Theorem §C2b.1.1]], [[§C2b.1 Heisenberg Fields#^der-c2b-1-1|Derivation §C2b.1.1]], [[§C2b.4 Microcausality and the Commutator Function#^thm-c2b-4-10|Theorem §C2b.4.10]].

^sol-wq-1

### W2. The Klein–Gordon product

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-2]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-2-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-2-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-2-c]]

> [!success]- Solution
> **Answers.** (a) $\frac{d}{dt}(f, g) = i\oint d\mathbf S\cdot(f^{\ast}\nabla g - g\nabla f^{\ast}) = 0$. (b) $(f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$, $(f_{\mathbf p}, f^{\ast}_{\mathbf q}) = 0$, $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$. (c) No: $(f_h, f_h) = \int\frac{d^3p}{(2\pi)^3}\lvert h\rvert^2 \ge 0$ but $(f^{\ast}_h, f^{\ast}_h) = -\int\frac{d^3p}{(2\pi)^3}\lvert h\rvert^2 \le 0$; a conserved, sesquilinear, indefinite product, positive on positive frequencies.
>
> **(a) Step 1** (differentiate). The product rule gives four terms; $\dot f^{\ast}\dot g$ appears twice with opposite signs:
>
> $$
> \frac{d}{dt}(f, g) = i\int d^3x\,\bigl(\dot f^{\ast}\dot g + f^{\ast}\ddot g - \ddot f^{\ast}g - \dot f^{\ast}\dot g\bigr) = i\int d^3x\,\bigl(f^{\ast}\ddot g - \ddot f^{\ast}g\bigr) .
> $$
>
> **Step 2** (field equation). $\ddot g = (\nabla^2 - m^2)g$, and $f^{\ast}$ solves the same equation because the Klein–Gordon equation is real. The mass terms cancel: $\frac{d}{dt}(f, g) = i\int d^3x\,\bigl(f^{\ast}\nabla^2g - (\nabla^2f^{\ast})g\bigr)$.
>
> **Step 3** (a divergence). $\nabla\cdot(f^{\ast}\nabla g - g\nabla f^{\ast}) = \nabla f^{\ast}\cdot\nabla g + f^{\ast}\nabla^2g - \nabla g\cdot\nabla f^{\ast} - g\nabla^2f^{\ast}$, so the integrand is a divergence and $\frac{d}{dt}(f, g) = i\lim_{R\to\infty}\oint_{\lvert\mathbf x\rvert = R}d\mathbf S\cdot(f^{\ast}\nabla g - g\nabla f^{\ast}) = 0$ for solutions that fall off at spatial infinity (wave packets; for plane waves in the distributional sense). Equivalently, $j^\mu = i(f^{\ast}\partial^\mu g - (\partial^\mu f^{\ast})g)$ is a conserved current and $(f, g) = \int d^3x\,j^0$ its charge.
>
> **(b) Step 1** ($\partial_t$ of the modes). $f^{\ast}_{\mathbf p} = e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, $\partial_tf_{\mathbf q} = -iE_{\mathbf q}f_{\mathbf q}$, $\partial_tf^{\ast}_{\mathbf p} = iE_{\mathbf p}f^{\ast}_{\mathbf p}$.
>
> **Step 2** (positive frequencies). $(f_{\mathbf p}, f_{\mathbf q}) = i\int d^3x\,f^{\ast}_{\mathbf p}f_{\mathbf q}\bigl(-iE_{\mathbf q} - iE_{\mathbf p}\bigr) = \frac{E_{\mathbf p} + E_{\mathbf q}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p - q)\cdot x}$. With $e^{i(p - q)\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x}$ the integral is $e^{i(E_{\mathbf p} - E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$. On the support $\mathbf q = \mathbf p$ the phase is $1$ and the prefactor $2E_{\mathbf p}/2E_{\mathbf p} = 1$:
>
> $$
> (f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q) .
> $$
>
> **Step 3** (mixed). With $\partial_tf^{\ast}_{\mathbf q} = iE_{\mathbf q}f^{\ast}_{\mathbf q}$, $(f_{\mathbf p}, f^{\ast}_{\mathbf q}) = i\int d^3x\,f^{\ast}_{\mathbf p}f^{\ast}_{\mathbf q}(iE_{\mathbf q} - iE_{\mathbf p}) = -\frac{E_{\mathbf q} - E_{\mathbf p}}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\,e^{i(E_{\mathbf p} + E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p + \mathbf q)$. The delta sets $\mathbf q = -\mathbf p$, where $E_{-\mathbf p} = E_{\mathbf p}$ makes the prefactor vanish: $(f_{\mathbf p}, f^{\ast}_{\mathbf q}) = 0$. This is where $E_{-\mathbf p} = E_{\mathbf p}$ is used; the oscillating phase $e^{2iE_{\mathbf p}t}$ is harmless only because its coefficient vanishes.
>
> **Step 4** (negative frequencies). Conjugating the definition, $(f^{\ast}, g^{\ast}) = i\int(f\partial_tg^{\ast} - (\partial_tf)g^{\ast})$ while $(f, g)^{\ast} = -i\int(f\partial_tg^{\ast} - (\partial_tf)g^{\ast})$: so $(f^{\ast}, g^{\ast}) = -(f, g)^{\ast}$ and $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (the delta is real).
>
> **(c)** By linearity (antilinear in the first slot), $(f_h, f_h) = \int\frac{d^3p\,d^3q}{(2\pi)^6}\overline{h(\mathbf p)}h(\mathbf q)(f_{\mathbf p}, f_{\mathbf q}) = \int\frac{d^3p}{(2\pi)^3}\lvert h(\mathbf p)\rvert^2 \ge 0$, and by Step 4, $(f^{\ast}_h, f^{\ast}_h) = -(f_h, f_h)^{\ast} = -\int\frac{d^3p}{(2\pi)^3}\lvert h\rvert^2 \le 0$. So $(f, f)$ has no sign in general: the product is sesquilinear and conserved, positive definite on positive-frequency solutions and negative definite on negative-frequency ones, with the two orthogonal (Step 3). It is not a Hilbert-space inner product; its indefiniteness is what defeated the probability interpretation of the Klein–Gordon equation, and in the field theory it is the basis-free statement of the frequency split: positive-norm modes carry annihilators, negative-norm modes creators.
>
> *Checked against:* [[§C2a.2 Mode Expansion and the Mode Algebra#^def-c2a-2-1|Def. §C2a.2.1]]; [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-3|Theorem §C2a.2.3]] and [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-3|Derivation §C2a.2.3]] (steps 2–4 for (a) in four-current form, steps 6–10 for (b)); [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-4|Theorem §C2a.2.4]] (the wave-packet norms of (c)); [[§C2a.2 Mode Expansion and the Mode Algebra#^rem-c2a-2-4|§C2a.2, Remark: Why this inner product, and why it is indefinite]]. The submitted solution of PS3.3(a) writes out the same integration by parts.

^sol-wq-2

### W3. Mode extraction

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-3]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-3-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-3-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-3-c]]

> [!success]- Solution
> **Answers.** (a) $(f_{\mathbf p}, \hat\phi) = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}(f_{\mathbf p}, f_{\mathbf q}) + \hat a^\dagger_{\mathbf q}(f_{\mathbf p}, f^{\ast}_{\mathbf q})\bigr) = \hat a_{\mathbf p}$. (b) $\int d^3x\,e^{ip\cdot x}\hat\phi = \frac{\hat a_{\mathbf p} + e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}$, $\int d^3x\,e^{ip\cdot x}\hat\pi = -iE_{\mathbf p}\frac{\hat a_{\mathbf p} - e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}$; the $\hat a^\dagger_{-\mathbf p}$ terms and all $t$-dependence cancel in $\hat\pi - iE_{\mathbf p}\hat\phi$. (c) $-(f^{\ast}_{\mathbf p}, \hat\phi) = \hat a^\dagger_{\mathbf p}$; the minus sign is the negative norm of $f^{\ast}_{\mathbf p}$.
>
> **(a) Step 1** (write the field in modes). $\hat\phi = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^{\ast}_{\mathbf q}\bigr)$, since $e^{\mp iq\cdot x}/\sqrt{2E_{\mathbf q}} = f_{\mathbf q}$, $f^{\ast}_{\mathbf q}$.
>
> **Step 2** (pull the product through). $(f_{\mathbf p}, \cdot)$ is linear in its second slot and contains only $\int d^3x$ and $\partial_t$, which do not act on the $x$-independent operators $\hat a_{\mathbf q}$ (the exchange of $\int d^3x$ with $\int d^3q$ is made after smearing in $\mathbf p$, where it is Fubini). So $(f_{\mathbf p}, \hat\phi) = \int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}(f_{\mathbf p}, f_{\mathbf q}) + \hat a^\dagger_{\mathbf q}(f_{\mathbf p}, f^{\ast}_{\mathbf q})\bigr)$.
>
> **Step 3** (orthonormality, W2(b)). The second product vanishes and the first is $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; the $\mathbf q$ integral sets $\mathbf q = \mathbf p$ and cancels the $(2\pi)^3$: $(f_{\mathbf p}, \hat\phi) = \hat a_{\mathbf p}$. By W2(a) the product is the same on every slice, so the right side carries no $t$.
>
> **(b) Step 1** (explicit form). With $\partial_tf^{\ast}_{\mathbf p} = iE_{\mathbf p}f^{\ast}_{\mathbf p}$ and $\partial_t\hat\phi = \hat\pi$ (time derivative traded for the canonical momentum),
>
> $$
> \hat a_{\mathbf p} = i\int d^3x\,\bigl(f^{\ast}_{\mathbf p}\hat\pi - iE_{\mathbf p}f^{\ast}_{\mathbf p}\hat\phi\bigr) = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\bigl(\hat\pi(x) - iE_{\mathbf p}\hat\phi(x)\bigr) .
> $$
>
> **Step 2** (the field alone). Insert the expansion with variable $\mathbf q$: $e^{ip\cdot x}e^{-iq\cdot x} = e^{i(E_{\mathbf p} - E_{\mathbf q})t}e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x}$ and $e^{ip\cdot x}e^{iq\cdot x} = e^{i(E_{\mathbf p} + E_{\mathbf q})t}e^{-i(\mathbf p + \mathbf q)\cdot\mathbf x}$, so the $d^3x$ integral gives $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ in the $\hat a$ term and $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$ in the $\hat a^\dagger$ term. The $\mathbf q$ integrals set $\mathbf q = \pm\mathbf p$, $E_{\mathbf q} = E_{\mathbf p}$:
>
> $$
> \int d^3x\,e^{ip\cdot x}\hat\phi(x) = \frac{\hat a_{\mathbf p} + e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}} .
> $$
>
> **Step 3** (the momentum alone). $\hat\pi$ has the coefficients $-i\sqrt{E_{\mathbf q}/2} = -iE_{\mathbf q}/\sqrt{2E_{\mathbf q}}$ and $+iE_{\mathbf q}/\sqrt{2E_{\mathbf q}}$; the same deltas give $\int d^3x\,e^{ip\cdot x}\hat\pi = -iE_{\mathbf p}\bigl(\hat a_{\mathbf p} - e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr)/\sqrt{2E_{\mathbf p}}$. Each alone mixes $\hat a_{\mathbf p}$ with $\hat a^\dagger_{-\mathbf p}$ and depends on $t$: one piece of Cauchy data does not separate the two frequencies.
>
> **Step 4** (combine). $\int d^3x\,e^{ip\cdot x}(\hat\pi - iE_{\mathbf p}\hat\phi) = \frac{1}{\sqrt{2E_{\mathbf p}}}\bigl(-iE_{\mathbf p}\hat a_{\mathbf p} + iE_{\mathbf p}e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p} - iE_{\mathbf p}\hat a_{\mathbf p} - iE_{\mathbf p}e^{2iE_{\mathbf p}t}\hat a^\dagger_{-\mathbf p}\bigr) = -i\sqrt{2E_{\mathbf p}}\,\hat a_{\mathbf p}$. Multiplying by $i/\sqrt{2E_{\mathbf p}}$ gives $\hat a_{\mathbf p}$: the $\hat a^\dagger_{-\mathbf p}$ terms, and with them all $t$-dependence, cancel.
>
> **(c)** As in (a), $-(f^{\ast}_{\mathbf p}, \hat\phi) = -\int\frac{d^3q}{(2\pi)^3}\bigl(\hat a_{\mathbf q}(f^{\ast}_{\mathbf p}, f_{\mathbf q}) + \hat a^\dagger_{\mathbf q}(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q})\bigr)$. Here $(f^{\ast}_{\mathbf p}, f_{\mathbf q}) = -(f_{\mathbf p}, f^{\ast}_{\mathbf q})^{\ast} = 0$ and $(f^{\ast}_{\mathbf p}, f^{\ast}_{\mathbf q}) = -(2\pi)^3\delta^3(\mathbf p - \mathbf q)$ (W2(b)), so $-(f^{\ast}_{\mathbf p}, \hat\phi) = \hat a^\dagger_{\mathbf p}$. The minus sign compensates the negative norm of the negative-frequency mode. (Equivalently, take the adjoint of (b): $\hat a^\dagger_{\mathbf p} = \frac{-i}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{-ip\cdot x}(\hat\pi + iE_{\mathbf p}\hat\phi)$.)
>
> *Checked against:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-5|Theorem §C2a.2.5]] and [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-5|Derivation §C2a.2.5]] (steps 1–3 for (a) and (c), steps 4–6 for (b), the same two Fourier transforms); the submitted solution of PS3.3(b) evaluates at $t = 0$, justified by W2(a), the course solution keeps general $t$ as here.

^sol-wq-3

### W4. The ladder algebra in both directions

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-4]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-4-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-4-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-4-c]]

> [!success]- Solution
> **Answers.** (a) $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = \frac{E_{\mathbf k} + E_{\mathbf p}}{2\sqrt{E_{\mathbf k}E_{\mathbf p}}}e^{i(E_{\mathbf k} - E_{\mathbf p})t}(2\pi)^3\delta^3(\mathbf k - \mathbf p) = (2\pi)^3\delta^3(\mathbf k - \mathbf p)$. (b) $[\hat a_{\mathbf k}, \hat a_{\mathbf p}] \propto (E_{\mathbf k} - E_{\mathbf p})\,\delta^3(\mathbf k + \mathbf p) = 0$ by $E_{-\mathbf p} = E_{\mathbf p}$; $[\hat a^\dagger, \hat a^\dagger] = 0$ by adjoints. (c) The bracket $[\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}] = -2(2\pi)^3\delta^3(\mathbf p + \mathbf p')$ and the factor $\frac{1}{\sqrt{2E}}(-i)\sqrt{\frac E2} = -\frac i2$ give $+i\delta^3(\mathbf x - \mathbf y)$; the relative minus sign in $\hat\pi$ makes the two terms add.
>
> **(a) Step 1** (both operators). By W3(b) and its adjoint ($i \to -i$, $e^{ik\cdot x} \to e^{-ik\cdot x}$; $\hat\phi$, $\hat\pi$ Hermitian), on one slice $t$,
>
> $$
> \hat a_{\mathbf k} = \frac{i}{\sqrt{2E_{\mathbf k}}}\int d^3x\,e^{ik\cdot x}\bigl(\hat\pi(\mathbf x) - iE_{\mathbf k}\hat\phi(\mathbf x)\bigr), \qquad \hat a^\dagger_{\mathbf p} = \frac{-i}{\sqrt{2E_{\mathbf p}}}\int d^3y\,e^{-ip\cdot y}\bigl(\hat\pi(\mathbf y) + iE_{\mathbf p}\hat\phi(\mathbf y)\bigr) .
> $$
>
> **Step 2** (expand by bilinearity). $(i)(-i) = 1$, and the exponentials are numbers:
>
> $$
> [\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = \frac{1}{2\sqrt{E_{\mathbf k}E_{\mathbf p}}}\int d^3x\,d^3y\,e^{ik\cdot x - ip\cdot y}\Bigl([\hat\pi, \hat\pi'] + iE_{\mathbf p}[\hat\pi, \hat\phi'] - iE_{\mathbf k}[\hat\phi, \hat\pi'] + E_{\mathbf k}E_{\mathbf p}[\hat\phi, \hat\phi']\Bigr) .
> $$
>
> **Step 3** (equal-time relations). The first and last commutators vanish; $[\hat\pi(\mathbf x), \hat\phi(\mathbf y)] = -i\delta^3(\mathbf x - \mathbf y)$ and $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, so the bracket is $iE_{\mathbf p}(-i)\delta^3 - iE_{\mathbf k}(i)\delta^3 = (E_{\mathbf p} + E_{\mathbf k})\delta^3(\mathbf x - \mathbf y)$: the two surviving terms add.
>
> **Step 4** (integrate). The $\mathbf y$ integral sets $\mathbf y = \mathbf x$; then $\int d^3x\,e^{i(k - p)\cdot x} = e^{i(E_{\mathbf k} - E_{\mathbf p})t}(2\pi)^3\delta^3(\mathbf k - \mathbf p)$:
>
> $$
> [\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = \frac{E_{\mathbf k} + E_{\mathbf p}}{2\sqrt{E_{\mathbf k}E_{\mathbf p}}}\,e^{i(E_{\mathbf k} - E_{\mathbf p})t}\,(2\pi)^3\delta^3(\mathbf k - \mathbf p) = (2\pi)^3\delta^3(\mathbf k - \mathbf p) ,
> $$
>
> because on the support of the delta the prefactor is $2E_{\mathbf k}/2E_{\mathbf k} = 1$ and the phase is $1$. The slice $t$ drops out. In the language of W2: $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf p}] = (f_{\mathbf k}, f_{\mathbf p})$.
>
> **(b) Step 1.** $\hat a_{\mathbf p} = \frac{i}{\sqrt{2E_{\mathbf p}}}\int d^3y\,e^{ip\cdot y}(\hat\pi' - iE_{\mathbf p}\hat\phi')$, so the prefactor is $(i)(i) = -1$ and the bracket $[\hat\pi - iE_{\mathbf k}\hat\phi, \hat\pi' - iE_{\mathbf p}\hat\phi'] = -iE_{\mathbf p}[\hat\pi, \hat\phi'] - iE_{\mathbf k}[\hat\phi, \hat\pi'] = (-E_{\mathbf p} + E_{\mathbf k})\delta^3(\mathbf x - \mathbf y)$.
>
> **Step 2.** With $\int d^3x\,e^{i(k + p)\cdot x} = e^{i(E_{\mathbf k} + E_{\mathbf p})t}(2\pi)^3\delta^3(\mathbf k + \mathbf p)$,
>
> $$
> [\hat a_{\mathbf k}, \hat a_{\mathbf p}] = -\frac{E_{\mathbf k} - E_{\mathbf p}}{2\sqrt{E_{\mathbf k}E_{\mathbf p}}}\,e^{i(E_{\mathbf k} + E_{\mathbf p})t}\,(2\pi)^3\delta^3(\mathbf k + \mathbf p) = 0 ,
> $$
>
> because the delta sets $\mathbf p = -\mathbf k$ and $E_{-\mathbf k} = E_{\mathbf k}$: a smooth function vanishing on the support of δ times δ is zero. This is $-(f_{\mathbf k}, f^{\ast}_{\mathbf p})$ of W2(b).
>
> **Step 3.** $[\hat a_{\mathbf k}, \hat a_{\mathbf p}]^\dagger = \hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf k} - \hat a^\dagger_{\mathbf k}\hat a^\dagger_{\mathbf p} = [\hat a^\dagger_{\mathbf p}, \hat a^\dagger_{\mathbf k}] = 0$.
>
> **(c) Step 1** (the $t = 0$ forms). At $t = 0$, $e^{-ip\cdot x} = e^{i\mathbf p\cdot\mathbf x}$ and $e^{ip\cdot x} = e^{-i\mathbf p\cdot\mathbf x}$. In the $\hat a^\dagger$ terms of W3's expansion substitute $\mathbf p \to -\mathbf p$: both terms then carry $e^{i\mathbf p\cdot\mathbf x}$, and $\hat a^\dagger_{\mathbf p} \to \hat a^\dagger_{-\mathbf p}$. This gives $\hat\phi(\mathbf x)$ as stated; $\hat\pi = \partial_t\hat\phi$ brings down $-iE_{\mathbf p}$ on $\hat a$ and $+iE_{\mathbf p}$ on $\hat a^\dagger$, i.e. $(-i)\sqrt{E_{\mathbf p}/2}\,(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p})$ after the same relabelling.
>
> **Step 2** (four terms). Variable $\mathbf p$ in $\hat\phi(\mathbf x)$, $\mathbf p'$ in $\hat\pi(\mathbf y)$:
>
> $$
> [\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}] = [\hat a_{\mathbf p}, \hat a_{\mathbf p'}] - [\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] + [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] - [\hat a^\dagger_{-\mathbf p}, \hat a^\dagger_{-\mathbf p'}] .
> $$
>
> The first and last vanish; $[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$ and $[\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = -(2\pi)^3\delta^3(\mathbf p + \mathbf p')$. The bracket is $-2(2\pi)^3\delta^3(\mathbf p + \mathbf p')$.
>
> **Step 3** (integrate). The $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$, cancels one $(2\pi)^3$, turns $E_{\mathbf p'}$ into $E_{\mathbf p}$ and $e^{i\mathbf p\cdot\mathbf x + i\mathbf p'\cdot\mathbf y}$ into $e^{i\mathbf p\cdot(\mathbf x - \mathbf y)}$. The numbers: $\frac{1}{\sqrt{2E_{\mathbf p}}}\cdot(-i)\sqrt{\frac{E_{\mathbf p}}2} = -\frac i2$, times $-2$, is $+i$:
>
> $$
> [\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = i\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot(\mathbf x - \mathbf y)} = i\,\delta^3(\mathbf x - \mathbf y) .
> $$
>
> **Step 4** (the other two). In $[\hat\phi, \hat\phi]$ the bracket is $[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] + [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = 0$; in $[\hat\pi, \hat\pi]$ it is $-[\hat a_{\mathbf p}, \hat a^\dagger_{-\mathbf p'}] - [\hat a^\dagger_{-\mathbf p}, \hat a_{\mathbf p'}] = 0$: the two orderings cancel. In $[\hat\phi, \hat\pi]$ the relative minus sign inside $\hat\pi$ makes them add, and the factor $-i$ turns $-2\cdot\frac12$ into $+i$: the ansatz for $\hat\pi$ is fixed by the commutator.
>
> *Checked against:* [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]]; [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6|Derivation §C2a.2.6]] (step 8 is (a) in the same explicit variables, step 6 is (b)); [[§C2a.2 Mode Expansion and the Mode Algebra#^der-c2a-2-6b|Derivation §C2a.2.6, second route]] ((c), Lecture 4's direction); [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-2|Theorem §C2a.2.2]] (the $t = 0$ forms). The submitted solution of PS3.3(c) does the explicit Fourier integrals at $t = 0$; the course solution reduces the commutator to $(f_{\mathbf k}, f_{\mathbf p})$, the last sentence of (a).

^sol-wq-4

### W5. The Hamiltonian in modes and the zero-point energy

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-5]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-5-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-5-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-5-c]]

> [!success]- Solution
> **Answers.** (a) The terms $\hat a_{\mathbf p}\hat a_{-\mathbf p}$ and $\hat a^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p}$ cancel between $\frac12\hat\pi^2$ and $\frac12(\nabla\hat\phi)^2 + \frac12m^2\hat\phi^2$, because $\mathbf p^2 + m^2 = E_{\mathbf p}^2$. (b) $E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}{2}$; in the box $E_0(V, \Lambda) = \frac12\sum_{\lvert\mathbf k\rvert<\Lambda}E_{\mathbf k}$, and $E_0/V \approx \Lambda^4/16\pi^2$. (c) $[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$; $E_0$ is a c-number; $:\!\hat H\!:\hat a^\dagger_{\mathbf p_1}\cdots\hat a^\dagger_{\mathbf p_n}\lvert0\rangle = (E_{\mathbf p_1} + \dots + E_{\mathbf p_n})\hat a^\dagger_{\mathbf p_1}\cdots\lvert0\rangle$, ground state $\lvert0\rangle$ with $0$.
>
> **(a) Step 1** (substitute). Variable $\mathbf p$ in the first factor, $\mathbf p'$ in the second; $\nabla e^{i\mathbf p\cdot\mathbf x} = i\mathbf p\,e^{i\mathbf p\cdot\mathbf x}$, $(-i)^2 = -1$. Each term of $\hat H$ is $\int d^3x\int\frac{d^3p\,d^3p'}{(2\pi)^6}e^{i(\mathbf p + \mathbf p')\cdot\mathbf x}$ times
>
> $$
> \tfrac12\hat\pi^2:\ -\frac{\sqrt{E_{\mathbf p}E_{\mathbf p'}}}{4}(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p})(\hat a_{\mathbf p'} - \hat a^\dagger_{-\mathbf p'}), \qquad \tfrac12(\nabla\hat\phi)^2 + \tfrac12m^2\hat\phi^2:\ \frac{(i\mathbf p)\cdot(i\mathbf p') + m^2}{4\sqrt{E_{\mathbf p}E_{\mathbf p'}}}(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p})(\hat a_{\mathbf p'} + \hat a^\dagger_{-\mathbf p'}) .
> $$
>
> **Step 2** ($d^3x$, then $\mathbf p'$). $\int d^3x\,e^{i(\mathbf p + \mathbf p')\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p + \mathbf p')$; the $\mathbf p'$ integral sets $\mathbf p' = -\mathbf p$: $\sqrt{E_{\mathbf p}E_{\mathbf p'}} \to E_{\mathbf p}$, $(i\mathbf p)\cdot(i\mathbf p') \to (i\mathbf p)\cdot(-i\mathbf p) = \mathbf p^2$, $\hat a_{\mathbf p'} \to \hat a_{-\mathbf p}$, $\hat a^\dagger_{-\mathbf p'} \to \hat a^\dagger_{\mathbf p}$:
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\Bigl[-\frac{E_{\mathbf p}}4(\hat a_{\mathbf p} - \hat a^\dagger_{-\mathbf p})(\hat a_{-\mathbf p} - \hat a^\dagger_{\mathbf p}) + \frac{\mathbf p^2 + m^2}{4E_{\mathbf p}}(\hat a_{\mathbf p} + \hat a^\dagger_{-\mathbf p})(\hat a_{-\mathbf p} + \hat a^\dagger_{\mathbf p})\Bigr] .
> $$
>
> **Step 3** (mass shell). $\mathbf p^2 + m^2 = E_{\mathbf p}^2$: the second coefficient is $+E_{\mathbf p}/4$, equal and opposite to the first.
>
> **Step 4** (all four terms, in order). The first product is $\hat a_{\mathbf p}\hat a_{-\mathbf p} - \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p} + \hat a^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p}$, the second the same with all signs $+$. With coefficients $-E_{\mathbf p}/4$ and $+E_{\mathbf p}/4$: the $\hat a\hat a$ and $\hat a^\dagger\hat a^\dagger$ terms cancel ($-1 + 1 = 0$), the other two double. Hence $\hat H = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p})$, and $\mathbf p \to -\mathbf p$ in the last term gives the stated form. The cancelled terms would create or destroy two quanta of opposite momenta; the mass-shell relation removes them.
>
> **(b) Step 1** (reorder). $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + [\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf p}] = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$, so
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + E_0, \qquad E_0 = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2(2\pi)^3\delta^3(\mathbf 0) = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2 .
> $$
>
> $E_0 = \langle0|\hat H|0\rangle$: $\frac12E_{\mathbf p}$ per mode, the oscillator's ground-state energy.
>
> **Step 2** (no value). $\delta^3(\mathbf 0)$ is δ at its singular point: replacing δ by a nascent delta $\varepsilon^{-3}\rho(\mathbf u/\varepsilon)$, the would-be value $\varepsilon^{-3}\rho(\mathbf 0)$ diverges and depends on the shape $\rho$. A distribution has values only against test functions; as written $\hat H$ is not an operator on the Fock space.
>
> **Step 3** (the box). With periodic boundary conditions on a cube of side $L$, $\mathbf k \in (2\pi/L)\mathbb Z^3$ and $\int_Vd^3x\,e^{i(\mathbf k - \mathbf k')\cdot\mathbf x} = V\delta_{\mathbf k\mathbf k'}$, an honest integral; $\int\frac{d^3p}{(2\pi)^3} \to \frac1V\sum_{\mathbf k}$ and $[\hat a_{\mathbf k}, \hat a^\dagger_{\mathbf k'}] = V\delta_{\mathbf k\mathbf k'}$. The same reordering leaves $E_0(V, \Lambda) = \frac12\sum_{\lvert\mathbf k\rvert<\Lambda}E_{\mathbf k}$, a number: "$(2\pi)^3\delta^3(\mathbf 0) = V$" is the dictionary entry $V\delta_{\mathbf k\mathbf k} = V$.
>
> **Step 4** (density). Each lattice point owns a momentum cell of volume $(2\pi)^3/V$, so $E_0/V \to \int_{\lvert\mathbf p\rvert<\Lambda}\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2 = \frac{1}{4\pi^2}\int_0^\Lambda dp\,p^2\sqrt{p^2 + m^2}$. For $\Lambda \gg m$, $\sqrt{p^2 + m^2} = p + m^2/2p + \dots$ gives $\int_0^\Lambda dp\,p^2\sqrt{p^2 + m^2} = \frac{\Lambda^4}4 + \frac{m^2\Lambda^2}4 + O(m^4\ln\frac\Lambda m)$, so $E_0/V \approx \frac{\Lambda^4}{16\pi^2}$: infrared divergent (extensive) and ultraviolet divergent (quartic).
>
> **(c) Step 1** (drop the constant). $E_0$ multiplies the identity, so $[\hat H, \hat X] = [\int\frac{d^3q}{(2\pi)^3}E_{\mathbf q}\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat X]$ for every $\hat X$.
>
> **Step 2** (one density). $[\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = \hat a^\dagger_{\mathbf q}[\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] + [\hat a^\dagger_{\mathbf q}, \hat a^\dagger_{\mathbf p}]\hat a_{\mathbf q} = (2\pi)^3\delta^3(\mathbf q - \mathbf p)\hat a^\dagger_{\mathbf q}$; integrating against $E_{\mathbf q}$, $[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$. Likewise $[\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a_{\mathbf p}] = [\hat a^\dagger_{\mathbf q}, \hat a_{\mathbf p}]\hat a_{\mathbf q} = -(2\pi)^3\delta^3(\mathbf q - \mathbf p)\hat a_{\mathbf q}$ gives $[\hat H, \hat a_{\mathbf p}] = -E_{\mathbf p}\hat a_{\mathbf p}$.
>
> **Step 3** (spectrum). $:\!\hat H\!: = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$ ends in an annihilator, so $:\!\hat H\!:\lvert0\rangle = 0$, and $\langle\Psi|:\!\hat H\!:|\Psi\rangle = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\lVert\hat a_{\mathbf p}\Psi\rVert^2 \ge 0$: $\lvert0\rangle$ is the ground state. Pushing $:\!\hat H\!:$ through the creators one at a time with $:\!\hat H\!:\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}(:\!\hat H\!: + E_{\mathbf p})$ gives the energy $E_{\mathbf p_1} + \dots + E_{\mathbf p_n}$: $n$ free particles of mass $m$.
>
> *Checked against:* [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-1|Theorem §C2a.3.1]] and [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]] (steps 1–8: the same coefficients $\mp E_{\mathbf p}/4$ and cancellation); [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-2|Theorem §C2a.3.2]] (the box and the meaning of $\delta^3(\mathbf 0)$); [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]] ($E_0$, $\varepsilon_0 \approx \Lambda^4/16\pi^2$); [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]]; [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]]; [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]].

^sol-wq-5

### W6. The momentum in modes

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-6]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-6-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-6-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-6-c]]

> [!success]- Solution
> **Answers.** (a) $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2:\!(\hat a_{\mathbf p}\hat a_{-\mathbf p} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p})\!: = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, the $\hat a\hat a$ and $\hat a^\dagger\hat a^\dagger$ terms being odd in $\mathbf p$. (b) $\frac V2\int\frac{d^3p}{(2\pi)^3}\mathbf p = 0$ for $\hat{\mathbf P}$ (odd integrand, rotation-invariant cutoff); $E_0 = \frac V2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} > 0$ for $\hat H$ (even, positive integrand). (c) $[\hat{\mathbf P}, \hat a^\dagger_{\mathbf p}] = \mathbf p\,\hat a^\dagger_{\mathbf p}$; the vacuum carries $\mathbf 0$, $\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle$ carries $\mathbf p_1 + \mathbf p_2$.
>
> **(a) Step 1** (expansions and gradient). $\hat\pi(x) = -i\int\frac{d^3p}{(2\pi)^3}\sqrt{\frac{E_{\mathbf p}}2}(\hat a_{\mathbf p}e^{-ip\cdot x} - \hat a^\dagger_{\mathbf p}e^{ip\cdot x})$; $\nabla e^{\mp ip\cdot x} = \pm i\mathbf p\,e^{\mp ip\cdot x}$ (the exponent contains $\pm i\mathbf p\cdot\mathbf x$), so $\nabla\hat\phi = \int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}(i\mathbf q\,\hat a_{\mathbf q}e^{-iq\cdot x} - i\mathbf q\,\hat a^\dagger_{\mathbf q}e^{iq\cdot x})$.
>
> **Step 2** ($t = 0$). $\hat{\mathbf P}$ is conserved (a Noether charge), so evaluate at $t = 0$, where $e^{\mp ip\cdot x} = e^{\pm i\mathbf p\cdot\mathbf x}$. Expand inside the colons, apply them at the end. With $(-i)(i) = 1$ and $\sqrt{E_{\mathbf p}/2}/\sqrt{2E_{\mathbf q}} = \sqrt{E_{\mathbf p}/4E_{\mathbf q}}$:
>
> $$
> \hat{\mathbf P} = -\int d^3x\int\frac{d^3p\,d^3q}{(2\pi)^6}\mathbf q\sqrt{\frac{E_{\mathbf p}}{4E_{\mathbf q}}}:\!\Bigl(\hat a_{\mathbf p}\hat a_{\mathbf q}e^{i(\mathbf p + \mathbf q)\cdot\mathbf x} - \hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{i(\mathbf p - \mathbf q)\cdot\mathbf x} - \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{-i(\mathbf p - \mathbf q)\cdot\mathbf x} + \hat a^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{-i(\mathbf p + \mathbf q)\cdot\mathbf x}\Bigr)\!: .
> $$
>
> **Step 3** ($d^3x$, then $\mathbf q$). The outer terms get $(2\pi)^3\delta^3(\mathbf p + \mathbf q)$, the middle ones $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$. The $\mathbf q$ integral sets $\mathbf q = -\mathbf p$ or $\mathbf q = \mathbf p$; the square root becomes $\frac12$ in every term; $-\mathbf q$ becomes $+\mathbf p$ in the outer terms and $-\mathbf p$ in the middle ones, whose minus signs make it $+\mathbf p$:
>
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2:\!\bigl(\hat a_{\mathbf p}\hat a_{-\mathbf p} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p}\bigr)\!: .
> $$
>
> **Step 4** (odd terms). Relabel $\mathbf p \to -\mathbf p$ and use $[\hat a_{\mathbf p}, \hat a_{-\mathbf p}] = 0$: $\int\mathbf p\,\hat a_{\mathbf p}\hat a_{-\mathbf p} = \int(-\mathbf p)\hat a_{-\mathbf p}\hat a_{\mathbf p} = -\int\mathbf p\,\hat a_{\mathbf p}\hat a_{-\mathbf p}$, which is therefore zero; likewise the $\hat a^\dagger\hat a^\dagger$ term. (Here oddness kills them; in $\hat H$ it was the mass shell, W5(a).)
>
> **Step 5** (colons). $:\!\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p}\!: = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, so $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2\cdot2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} = \int\frac{d^3p}{(2\pi)^3}\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$, PS (2.33).
>
> **(b) Step 1** ($\hat{\mathbf P}$). Without colons, $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} = \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$ adds $\int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2(2\pi)^3\delta^3(\mathbf 0) = \frac V2\int\frac{d^3p}{(2\pi)^3}\mathbf p$. In the box this is $\frac12\sum_{\lvert\mathbf k\rvert<\Lambda}\mathbf k = \mathbf 0$ term by term, $\mathbf k$ cancelling $-\mathbf k$: zero for any reflection-symmetric (in particular rotation-invariant) cutoff.
>
> **Step 2** ($\hat H$). The same reordering in W5(b) adds $E_0 = \frac V2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}$: the weight $E_{\mathbf p} > 0$ is even, nothing cancels, and the constant diverges. So the colons remove nothing from $\hat{\mathbf P}$ and the infinite zero-point energy from $\hat H$.
>
> **(c)** As in W5(c) with $\mathbf q$ in place of $E_{\mathbf q}$: $[\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = (2\pi)^3\delta^3(\mathbf q - \mathbf p)\hat a^\dagger_{\mathbf q}$, so $[\hat{\mathbf P}, \hat a^\dagger_{\mathbf p}] = \mathbf p\,\hat a^\dagger_{\mathbf p}$ (and $[\hat{\mathbf P}, \hat a_{\mathbf p}] = -\mathbf p\,\hat a_{\mathbf p}$). $\hat{\mathbf P}\lvert0\rangle = 0$ since every term ends in $\hat a_{\mathbf p}$; then $\hat{\mathbf P}\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle = (\mathbf p_1 + \mathbf p_2)\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle$: the Fourier label is the momentum.
>
> *Checked against:* (a) the submitted solution of PS6.1 as written, [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^ex-c2a-3-1|Example §C2a.3.1]] with [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-ex-c2a-3-1|Example §C2a.3.1, derivation]] (steps 1–7, the same four terms and factors); (b) its step 8 (the user's remark on the omitted constant), [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-5|Theorem §C2a.3.5]] and [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-5|Derivation §C2a.3.5]] (step 7), [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]]; (c) [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-7|Theorem §C2a.3.7]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-1|Theorem §C2a.4.1]].

^sol-wq-6

### W7. States, normalization and the invariant measure

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-7]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-7-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-7-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-7-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-7-d]]

> [!success]- Solution
> **Answers.** (a) $\langle\mathbf p|\mathbf q\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; the four-point overlap is $(2\pi)^6[\delta^3(\mathbf q_1 - \mathbf p_1)\delta^3(\mathbf q_2 - \mathbf p_2) + \delta^3(\mathbf q_1 - \mathbf p_2)\delta^3(\mathbf q_2 - \mathbf p_1)]$: direct plus exchanged, Bose symmetry. (b) $\int dk^0\,\delta(k^2 - m^2)\theta(k^0)F(k) = F(E_{\mathbf k}, \mathbf k)/2E_{\mathbf k}$, so $\int\frac{d^3k}{(2\pi)^3\,2E_{\mathbf k}} = \int\frac{d^4k}{(2\pi)^4}2\pi\,\delta(k^2 - m^2)\theta(k^0)$ is invariant. (c) $2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$ is the kernel that reproduces test functions against the invariant measure; $\delta^3(\mathbf p - \mathbf q) = (E_{\mathbf p'}/E_{\mathbf p})\,\delta^3(\mathbf p' - \mathbf q')$ is not invariant, nor is the normalization of $\hat a^\dagger_{\mathbf p}\lvert0\rangle$. (d) As stated.
>
> **(a) Step 1.** $\langle\mathbf p|\mathbf q\rangle = \sqrt{4E_{\mathbf p}E_{\mathbf q}}\langle0|\hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}|0\rangle = \sqrt{4E_{\mathbf p}E_{\mathbf q}}\langle0|\bigl(\hat a^\dagger_{\mathbf q}\hat a_{\mathbf p} + (2\pi)^3\delta^3(\mathbf p - \mathbf q)\bigr)|0\rangle = 2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, since $\hat a_{\mathbf p}\lvert0\rangle = 0$ and $\sqrt{4E_{\mathbf p}E_{\mathbf q}} = 2E_{\mathbf p}$ on the support. (Lecture 4's slide writes $2\omega_{\mathbf p}\delta^3(\mathbf p - \mathbf q)$; with $[\hat a, \hat a^\dagger] = (2\pi)^3\delta^3$ the $(2\pi)^3$ is required.)
>
> **Step 2.** Move $\hat a_{\mathbf q_1}$ to the right: $\hat a_{\mathbf q_1}\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle = (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_1)\hat a^\dagger_{\mathbf p_2}\lvert0\rangle + (2\pi)^3\delta^3(\mathbf q_1 - \mathbf p_2)\hat a^\dagger_{\mathbf p_1}\lvert0\rangle$; then $\langle0|\hat a_{\mathbf q_2}\hat a^\dagger_{\mathbf p}|0\rangle = (2\pi)^3\delta^3(\mathbf q_2 - \mathbf p)$ gives the two terms of the answer. The exchanged term says $\hat a^\dagger_{\mathbf p_1}\hat a^\dagger_{\mathbf p_2}\lvert0\rangle = \hat a^\dagger_{\mathbf p_2}\hat a^\dagger_{\mathbf p_1}\lvert0\rangle$: the quanta are bosons, inherited from $[\hat a^\dagger, \hat a^\dagger] = 0$. Both sides are distributions, meaningful against wave packets ($\langle\mathbf p|\mathbf p\rangle$ is infinite).
>
> **(b) Step 1** (zeros). $f(k^0) = k^2 - m^2 = (k^0)^2 - E_{\mathbf k}^2$ vanishes at $k^0 = \pm E_{\mathbf k}$, with $\lvert f'(\pm E_{\mathbf k})\rvert = \lvert\pm2E_{\mathbf k}\rvert = 2E_{\mathbf k}$, so $\delta(k^2 - m^2) = \frac{\delta(k^0 - E_{\mathbf k}) + \delta(k^0 + E_{\mathbf k})}{2E_{\mathbf k}}$ (simple zeros, since $E_{\mathbf k} \ge m > 0$).
>
> **Step 2** (the $k^0$ integral). $\theta(k^0)$ removes the root $-E_{\mathbf k}$: $\int dk^0\,\delta(k^2 - m^2)\theta(k^0)F(k^0, \mathbf k) = \frac{F(E_{\mathbf k}, \mathbf k)}{2E_{\mathbf k}}$.
>
> **Step 3** (combine). Split $d^4k = dk^0\,d^3k$: $\int d^4k\,\delta(k^2 - m^2)\theta(k^0)F(k) = \int\frac{d^3k}{2E_{\mathbf k}}F(E_{\mathbf k}, \mathbf k)$ for every scalar $F$. The left side is invariant under proper orthochronous $\Lambda$ (the given invariance of $d^4k$, and of $\delta(k^2 - m^2)\theta(k^0)$ since $k^2$ is a scalar and the sign of $k^0$ is invariant on the timelike shell); so the right side is: $d^3k/2E_{\mathbf k}$ is an invariant measure. The constant factors $(2\pi)^{-3} = (2\pi)^{-4}\cdot2\pi$ change nothing: $\int\frac{d^3k}{(2\pi)^3\,2E_{\mathbf k}} = \int\frac{d^4k}{(2\pi)^4}2\pi\,\delta(k^2 - m^2)\theta(k^0)$.
>
> **(c) Step 1** (reproducing kernel). For a scalar test function $g$ on the shell, $g(\mathbf q) = \int d^3p\,\delta^3(\mathbf p - \mathbf q)g(\mathbf p) = \int\frac{d^3p}{2E_{\mathbf p}}\bigl[2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)\bigr]g(\mathbf p)$. The left side is a scalar and the measure is invariant ((b)), and a distribution is fixed by its action on test functions, so the bracket is invariant; hence so is $\langle\mathbf p|\mathbf q\rangle = (2\pi)^3[2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)]$.
>
> **Step 2** (the bare delta). $\delta^3(\mathbf p - \mathbf q) = \frac{1}{2E_{\mathbf p}}[2E_{\mathbf p}\delta^3(\mathbf p - \mathbf q)] = \frac{2E_{\mathbf p'}}{2E_{\mathbf p}}\delta^3(\mathbf p' - \mathbf q')$ in the boosted frame: not invariant. So $\hat a^\dagger_{\mathbf p}\lvert0\rangle$, with overlap $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$, is normalized in a frame-dependent way; the factor $\sqrt{2E_{\mathbf p}}$ in $\lvert\mathbf p\rangle$ is the inverse of the Jacobian in the measure.
>
> **(d) Step 1** ($t = 0$). In $\hat\phi(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} + \hat a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x})$ the annihilators give $0$ on $\lvert0\rangle$, and $\hat a^\dagger_{\mathbf p}\lvert0\rangle = \lvert\mathbf p\rangle/\sqrt{2E_{\mathbf p}}$: the two factors $1/\sqrt{2E_{\mathbf p}}$ combine into the invariant weight, $\hat\phi(\mathbf x)\lvert0\rangle = \int\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}e^{-i\mathbf p\cdot\mathbf x}\lvert\mathbf p\rangle$ (a vector only after smearing in $\mathbf x$).
>
> **Step 2** (Heisenberg field). Only the $\hat a_{\mathbf q}$ term of W3's expansion contributes to $\langle0|\hat\phi(x)|\mathbf p\rangle$ ($\langle0|\hat a^\dagger_{\mathbf q} = 0$): $\int\frac{d^3q}{(2\pi)^3}\frac{e^{-iq\cdot x}}{\sqrt{2E_{\mathbf q}}}\sqrt{2E_{\mathbf p}}\langle0|\hat a_{\mathbf q}\hat a^\dagger_{\mathbf p}|0\rangle = \int\frac{d^3q}{(2\pi)^3}\frac{\sqrt{2E_{\mathbf p}}}{\sqrt{2E_{\mathbf q}}}e^{-iq\cdot x}(2\pi)^3\delta^3(\mathbf q - \mathbf p) = e^{-ip\cdot x}$: the positive-frequency plane wave, the analogue of $\langle\mathbf x|\mathbf p\rangle$.
>
> *Checked against:* (a) [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-4|Derivation §C2a.4.4]] (step 3), [[§C2a.4 Particles and Relativistic Normalization#^cau-c2a-4-2|§C2a.4, Caution: The slides' normalization drops the (2π)³]], [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-2|Theorem §C2a.4.2]] and [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-2|Derivation §C2a.4.2]]; (b) the submitted solution of PS3.1(d)–(e) (as the course solution), [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-3|Theorem §C2a.4.3]] with [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-3|Derivation §C2a.4.3]] (steps 5–6), [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]]; (c) [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-4|Theorem §C2a.4.4]], [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-4|Derivation §C2a.4.4]] (steps 1–2, 5); (d) [[§C2a.4 Particles and Relativistic Normalization#^thm-c2a-4-6|Theorem §C2a.4.6]], [[§C2a.4 Particles and Relativistic Normalization#^der-c2a-4-6|Derivation §C2a.4.6]], [[§C2b.1 Heisenberg Fields#^thm-c2b-1-5|Theorem §C2b.1.5]].

^sol-wq-7

### W8. The Heisenberg field and translations

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-8]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-8-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-8-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-8-c]]

> [!success]- Solution
> **Answers.** (a) $\hat H\hat a_{\mathbf p} = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})$, hence $\hat H^n\hat a_{\mathbf p} = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})^n$ and $e^{i\hat Ht}\hat a_{\mathbf p}e^{-i\hat Ht} = \hat a_{\mathbf p}e^{-iE_{\mathbf p}t}$; the adjoint gives $\hat a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}$. (b) $\hat\phi(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x})$ and $\partial_t\hat\phi = \hat\pi$. (c) $[\hat\phi(\mathbf x), \hat{\mathbf P}] = -i\nabla\hat\phi(\mathbf x)$; $e^{i\mathbf a\cdot\hat{\mathbf P}}\hat\phi(\mathbf x)e^{-i\mathbf a\cdot\hat{\mathbf P}} = \hat\phi(\mathbf x) - \mathbf a\cdot\nabla\hat\phi(\mathbf x) + O(a^2)$.
>
> **(a) Step 1** (one commutator). By W5(c), $[\hat H, \hat a_{\mathbf p}] = -E_{\mathbf p}\hat a_{\mathbf p}$ (the integration variable named $\mathbf q$ so that it cannot clash with $\mathbf p$; $E_0$ drops out), i.e. $\hat H\hat a_{\mathbf p} = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})$.
>
> **Step 2** (powers). By induction, $\hat H^{n+1}\hat a_{\mathbf p} = \hat H\hat a_{\mathbf p}(\hat H - E_{\mathbf p})^n = \hat a_{\mathbf p}(\hat H - E_{\mathbf p})^{n+1}$.
>
> **Step 3** (exponentiate). $e^{i\hat Ht}\hat a_{\mathbf p} = \sum_n\frac{(it)^n}{n!}\hat H^n\hat a_{\mathbf p} = \hat a_{\mathbf p}e^{i(\hat H - E_{\mathbf p})t} = \hat a_{\mathbf p}e^{i\hat Ht}e^{-iE_{\mathbf p}t}$ ($E_{\mathbf p}$ is a number); multiply by $e^{-i\hat Ht}$ on the right. The adjoint, with $(e^{i\hat Ht})^\dagger = e^{-i\hat Ht}$, gives $e^{i\hat Ht}\hat a^\dagger_{\mathbf p}e^{-i\hat Ht} = \hat a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}$.
>
> **(b) Step 1** (un-relabel). In the $\hat a^\dagger_{-\mathbf p}$ term of $\hat\phi_S$ substitute $\mathbf p \to -\mathbf p$: $\hat\phi_S(\mathbf x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat a_{\mathbf p}e^{i\mathbf p\cdot\mathbf x} + \hat a^\dagger_{\mathbf p}e^{-i\mathbf p\cdot\mathbf x})$, and the same for $\hat\pi_S$ with $-i\sqrt{E_{\mathbf p}/2}$ and the relative minus sign.
>
> **Step 2** (conjugate term by term). $e^{i\hat Ht}$ passes through the numbers $e^{\pm i\mathbf p\cdot\mathbf x}$ and acts on the operators by (a): $\hat a_{\mathbf p}e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x} = \hat a_{\mathbf p}e^{-ip\cdot x}$ and $\hat a^\dagger_{\mathbf p}e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x} = \hat a^\dagger_{\mathbf p}e^{ip\cdot x}$, with $p^0 = E_{\mathbf p}$: the expansion of W3. The same for $\hat\pi$.
>
> **Step 3** (differentiate). $\partial_te^{\mp ip\cdot x} = \mp iE_{\mathbf p}e^{\mp ip\cdot x}$ and $E_{\mathbf p}/\sqrt{2E_{\mathbf p}} = \sqrt{E_{\mathbf p}/2}$: $\partial_t\hat\phi = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}2}(\hat a_{\mathbf p}e^{-ip\cdot x} - \hat a^\dagger_{\mathbf p}e^{ip\cdot x}) = \hat\pi(x)$. In the classical theory a definition, here a theorem.
>
> **(c) Step 1** (field form). $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)\nabla_y\hat\phi(\mathbf y)] = [\hat\phi(\mathbf x), \hat\pi(\mathbf y)]\nabla_y\hat\phi(\mathbf y) + \hat\pi(\mathbf y)\nabla_y[\hat\phi(\mathbf x), \hat\phi(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)\nabla_y\hat\phi(\mathbf y)$, the second term vanishing because $[\hat\phi(\mathbf x), \hat\phi(\mathbf y)] = 0$ for all $\mathbf y$. So $[\hat\phi(\mathbf x), \hat{\mathbf P}] = -\int d^3y\,i\delta^3(\mathbf x - \mathbf y)\nabla_y\hat\phi(\mathbf y) = -i\nabla\hat\phi(\mathbf x)$. (A reordering constant in $\hat{\mathbf P}$ would drop out.)
>
> **Step 2** (mode check). From W6(c) and its adjoint, $[\hat a_{\mathbf p}, \hat{\mathbf P}] = \mathbf p\,\hat a_{\mathbf p}$ and $[\hat a^\dagger_{\mathbf p}, \hat{\mathbf P}] = -\mathbf p\,\hat a^\dagger_{\mathbf p}$. So $[\hat\phi(x), \hat{\mathbf P}] = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\mathbf p\,\hat a_{\mathbf p}e^{-ip\cdot x} - \mathbf p\,\hat a^\dagger_{\mathbf p}e^{ip\cdot x})$, and $-i\nabla e^{\mp ip\cdot x} = \pm\mathbf p\,e^{\mp ip\cdot x}$: this is $-i\nabla\hat\phi(x)$, at every $t$.
>
> **Step 3** (translation). To first order, $e^{i\mathbf a\cdot\hat{\mathbf P}}\hat\phi\,e^{-i\mathbf a\cdot\hat{\mathbf P}} = \hat\phi + ia^k[\hat P^k, \hat\phi] = \hat\phi + ia^k(i\partial_k\hat\phi) = \hat\phi(\mathbf x) - \mathbf a\cdot\nabla\hat\phi(\mathbf x) = \hat\phi(\mathbf x - \mathbf a) + O(a^2)$. This is the space part of $[\hat\phi(x), \hat P^\mu] = i\partial^\mu\hat\phi(x)$: with $\partial^k = -\partial_k$, $[\hat\phi, \hat P^k] = -i\partial_k\hat\phi$; the time part is the Heisenberg equation, $[\hat\phi, \hat H] = i\partial_t\hat\phi$.
>
> *Checked against:* (a)–(b) [[§C2b.1 Heisenberg Fields#^thm-c2b-1-4|Theorem §C2b.1.4]] and [[§C2b.1 Heisenberg Fields#^der-c2b-1-4|Derivation §C2b.1.4]] (steps 1–9); (c) [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-5|Derivation §C2a.3.5]] ("What the derivation shows": the one-line field-form computation), [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]] ($[\hat\phi, \hat P^\mu] = i\partial^\mu\hat\phi$). *Derived here; check:* the mode check (Step 2) and the first-order translation (Step 3), the scalar copy of [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-9|Derivation §C5b.1.9]], step 5 (the same computation for $\hat\psi$).

^sol-wq-8

## The complex scalar field

### W9. Quantizing the complex scalar: two species

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-9]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-9-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-9-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-9-c]]

> [!success]- Solution
> **Answers.** (a) $\pi = \dot\phi^{\ast}$, $\pi^{\ast} = \dot\phi$; $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = [\hat\phi^\dagger(\mathbf x), \hat\pi^\dagger(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, all other equal-time commutators zero (including $[\hat\phi, \hat\pi^\dagger]$ and $[\hat\phi, \hat\phi^\dagger]$); $H$ as stated. (b) $\hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$ with $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = [\hat b_{\mathbf p}, \hat b^\dagger_{\mathbf q}] = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$ and all mixed commutators zero: two independent species, each with $E_{\mathbf p} = \sqrt{\mathbf p^2 + m^2}$, mass $m$. (c) $\hat a$ is built from $(\hat\phi, \hat\pi^\dagger)$, $\hat b$ from $(\hat\phi^\dagger, \hat\pi)$; $[\hat a, \hat b^\dagger] = 0$ because $\hat b^\dagger$ is built from $(\hat\phi, \hat\pi^\dagger)$ too; $[\hat a_{\mathbf p}, \hat b_{\mathbf q}] = -(f_{\mathbf p}, f^{\ast}_{\mathbf q}) = 0$.
>
> **(a) Step 1** (momenta). $\partial_\mu\phi^{\ast}\partial^\mu\phi = \dot\phi^{\ast}\dot\phi - \nabla\phi^{\ast}\cdot\nabla\phi$, so $\mathcal L = \dot\phi^{\ast}\dot\phi - \nabla\phi^{\ast}\cdot\nabla\phi - m^2\phi^{\ast}\phi$, with no $\frac12$. With $\phi$ and $\phi^{\ast}$ independent, $\pi = \partial\mathcal L/\partial\dot\phi = \dot\phi^{\ast}$ and $\pi^{\ast} = \partial\mathcal L/\partial\dot\phi^{\ast} = \dot\phi$: the momentum conjugate to $\phi$ is the velocity of $\phi^{\ast}$.
>
> **Step 2** (commutation relations). Two canonical pairs, $(\phi, \pi)$ and $(\phi^{\ast}, \pi^{\ast})$: at equal times $[\hat\phi(\mathbf x), \hat\pi(\mathbf y)] = [\hat\phi^\dagger(\mathbf x), \hat\pi^\dagger(\mathbf y)] = i\delta^3(\mathbf x - \mathbf y)$, and every other commutator among $\hat\phi$, $\hat\phi^\dagger$, $\hat\pi$, $\hat\pi^\dagger$ vanishes. (The second relation is the adjoint of the first: $[\hat\phi, \hat\pi]^\dagger = [\hat\pi^\dagger, \hat\phi^\dagger] = -i\delta^3$.)
>
> **Step 3** (Hamiltonian). $\mathcal H = \pi\dot\phi + \pi^{\ast}\dot\phi^{\ast} - \mathcal L = \pi\pi^{\ast} + \pi^{\ast}\pi - \bigl(\pi^{\ast}\pi - \nabla\phi^{\ast}\cdot\nabla\phi - m^2\phi^{\ast}\phi\bigr) = \pi^{\ast}\pi + \nabla\phi^{\ast}\cdot\nabla\phi + m^2\phi^{\ast}\phi$, using $\dot\phi = \pi^{\ast}$, $\dot\phi^{\ast} = \pi$. Integrating gives $H$. In real components $\phi = (\phi_1 + i\phi_2)/\sqrt2$ it is the sum of two real-field Hamiltonians.
>
> **(b) Step 1** (expansions). Without a reality condition the two coefficients per momentum are independent: $\hat\phi$ as given, $\hat\phi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}(\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x})$ (adjoint term by term), and with $\partial_te^{\mp ip\cdot x} = \mp iE_{\mathbf p}e^{\mp ip\cdot x}$,
>
> $$
> \hat\pi = \dot{\hat\phi}^\dagger = \int\frac{d^3p}{(2\pi)^3}i\sqrt{\frac{E_{\mathbf p}}2}\bigl(-\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x}\bigr), \qquad \hat\pi^\dagger = \dot{\hat\phi} = \int\frac{d^3p}{(2\pi)^3}i\sqrt{\frac{E_{\mathbf p}}2}\bigl(-\hat a_{\mathbf p}e^{-ip\cdot x} + \hat b^\dagger_{\mathbf p}e^{ip\cdot x}\bigr) .
> $$
>
> **Step 2** (the algebra from the canonical relations). By (c), $\hat a_{\mathbf p} = i\int d^3x\,(f^{\ast}_{\mathbf p}\hat\pi^\dagger - \dot f^{\ast}_{\mathbf p}\hat\phi)$ and $\hat a^\dagger_{\mathbf q} = -i\int d^3y\,(f_{\mathbf q}\hat\pi - \dot f_{\mathbf q}\hat\phi^\dagger)$. Expanding by bilinearity, only $[\hat\pi^\dagger, \hat\phi^\dagger] = -i\delta^3$ and $[\hat\phi, \hat\pi] = i\delta^3$ survive, and as in W4(a), $[\hat a_{\mathbf p}, \hat a^\dagger_{\mathbf q}] = i\int d^3x\,(f^{\ast}_{\mathbf p}\dot f_{\mathbf q} - \dot f^{\ast}_{\mathbf p}f_{\mathbf q}) = (f_{\mathbf p}, f_{\mathbf q}) = (2\pi)^3\delta^3(\mathbf p - \mathbf q)$. With $\hat\phi \leftrightarrow \hat\phi^\dagger$, $\hat\pi \leftrightarrow \hat\pi^\dagger$ the same holds for $\hat b$. The mixed commutators vanish by (c).
>
> **Step 3** (rewrite $H$). By parts (fall-off), $\int d^3x\,\nabla\hat\phi^\dagger\cdot\nabla\hat\phi = -\int d^3x\,\hat\phi^\dagger\nabla^2\hat\phi$, and each mode is on shell, $\ddot{\hat\phi} = (\nabla^2 - m^2)\hat\phi$: so $\hat H = \int d^3x\,(\hat\pi^\dagger\hat\pi - \hat\phi^\dagger\ddot{\hat\phi})$. The mass shell is spent here.
>
> **Step 4** (substitute, all four terms of each product). Variable $\mathbf p$ in the first factor, $\mathbf q$ in the second; $i\cdot i = -1$ in $\hat\pi^\dagger\hat\pi$, and $\ddot{\hat\phi}$ multiplies each mode by $-E_{\mathbf q}^2$:
>
> $$
> \hat\pi^\dagger\hat\pi = \int\!\!\frac{d^3p\,d^3q}{(2\pi)^6}\frac{\sqrt{E_{\mathbf p}E_{\mathbf q}}}2\Bigl(-\hat a_{\mathbf p}\hat b_{\mathbf q}e^{-i(p+q)\cdot x} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf q}e^{i(p-q)\cdot x} - \hat b^\dagger_{\mathbf p}\hat a^\dagger_{\mathbf q}e^{i(p+q)\cdot x}\Bigr) ,
> $$
>
> $$
> -\hat\phi^\dagger\ddot{\hat\phi} = \int\!\!\frac{d^3p\,d^3q}{(2\pi)^6}\frac{E_{\mathbf q}^2}{2\sqrt{E_{\mathbf p}E_{\mathbf q}}}\Bigl(\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x}\Bigr) .
> $$
>
> **Step 5** ($d^3x$, then $\mathbf q$). $\int d^3x\,e^{\mp i(p+q)\cdot x} = e^{\mp i(E_{\mathbf p} + E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p + \mathbf q)$ and $\int d^3x\,e^{\mp i(p-q)\cdot x} = e^{\mp i(E_{\mathbf p} - E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; the $\mathbf q$ integral sets $\mathbf q = \mp\mathbf p$, and in both cases $E_{\mathbf q} = E_{\mathbf p}$, so both prefactors become $E_{\mathbf p}/2$:
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2\Bigl[e^{-2iE_{\mathbf p}t}\bigl(-\hat a_{\mathbf p}\hat b_{-\mathbf p} + \hat b_{\mathbf p}\hat a_{-\mathbf p}\bigr) + e^{2iE_{\mathbf p}t}\bigl(-\hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}\bigr) + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\Bigr] .
> $$
>
> **Step 6** (number-changing terms). Substitute $\mathbf p \to -\mathbf p$ in $-\hat a_{\mathbf p}\hat b_{-\mathbf p}$: the first group becomes $\hat b_{\mathbf p}\hat a_{-\mathbf p} - \hat a_{-\mathbf p}\hat b_{\mathbf p} = [\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$; likewise, $\mathbf p \to -\mathbf p$ in $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p}$ makes the second group $[\hat a^\dagger_{-\mathbf p}, \hat b^\dagger_{\mathbf p}] = 0$. The species commute, the time-dependent terms go, and $\hat H$ is the same on every slice.
>
> **Step 7** (the prescription). Normal ordering from the outset puts $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} \to \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$ and $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} \to \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$ without a commutator, so
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) .
> $$
>
> **Step 8** (particles). As in W5(c), $[\hat H, \hat a^\dagger_{\mathbf p}] = E_{\mathbf p}\hat a^\dagger_{\mathbf p}$ and $[\hat H, \hat b^\dagger_{\mathbf p}] = E_{\mathbf p}\hat b^\dagger_{\mathbf p}$ (the cross terms vanish because the species commute): $\hat a^\dagger_{\mathbf p}\lvert0\rangle$ and $\hat b^\dagger_{\mathbf p}\lvert0\rangle$ have energy $\sqrt{\mathbf p^2 + m^2}$, two independent kinds of particle of the same mass $m$, with independent Fock towers.
>
> **(c) Step 1** (extraction). Write $\hat\phi = \int\frac{d^3q}{(2\pi)^3}(\hat a_{\mathbf q}f_{\mathbf q} + \hat b^\dagger_{\mathbf q}f^{\ast}_{\mathbf q})$ and $\hat\phi^\dagger = \int\frac{d^3q}{(2\pi)^3}(\hat b_{\mathbf q}f_{\mathbf q} + \hat a^\dagger_{\mathbf q}f^{\ast}_{\mathbf q})$. W3(a) and W3(c), with $\hat a^\dagger$ replaced by $\hat b^\dagger$ (resp. the roles exchanged), give $(f_{\mathbf p}, \hat\phi) = \hat a_{\mathbf p}$, $-(f^{\ast}_{\mathbf p}, \hat\phi) = \hat b^\dagger_{\mathbf p}$ and $(f_{\mathbf p}, \hat\phi^\dagger) = \hat b_{\mathbf p}$.
>
> **Step 2** (ingredients). With $\partial_t\hat\phi = \hat\pi^\dagger$ and $\partial_t\hat\phi^\dagger = \hat\pi$: $\hat a_{\mathbf p} = i\int d^3x\,(f^{\ast}_{\mathbf p}\hat\pi^\dagger - \dot f^{\ast}_{\mathbf p}\hat\phi)$ and $\hat b_{\mathbf p} = i\int d^3x\,(f^{\ast}_{\mathbf p}\hat\pi - \dot f^{\ast}_{\mathbf p}\hat\phi^\dagger)$. So $\hat a$ (and $\hat b^\dagger$, from $\hat\phi$ too) is built from $\hat\phi$ and $\hat\pi^\dagger$, never from a canonical pair; $\hat b$ (and $\hat a^\dagger$) from $\hat\phi^\dagger$ and $\hat\pi$.
>
> **Step 3** ($[\hat a, \hat b^\dagger]$). Both are built from $\hat\phi$ and $\hat\pi^\dagger$ only, and $[\hat\phi, \hat\phi] = [\hat\phi, \hat\pi^\dagger] = [\hat\pi^\dagger, \hat\pi^\dagger] = 0$: every term vanishes, with no computation. The same argument gives $[\hat a, \hat a] = [\hat b, \hat b] = 0$.
>
> **Step 4** ($[\hat a, \hat b]$). Prefactor $(i)(i) = -1$; of the four terms only $[\hat\pi^\dagger, \hat\phi^\dagger] = -i\delta^3$ and $[\hat\phi, \hat\pi] = i\delta^3$ survive:
>
> $$
> [\hat a_{\mathbf p}, \hat b_{\mathbf q}] = -\int d^3x\,d^3y\,\bigl(-f^{\ast}_{\mathbf p}\dot f^{\ast}_{\mathbf q}[\hat\pi^\dagger, \hat\phi^{\dagger\prime}] - \dot f^{\ast}_{\mathbf p}f^{\ast}_{\mathbf q}[\hat\phi, \hat\pi']\bigr) = -i\int d^3x\,(f^{\ast}_{\mathbf p}\dot f^{\ast}_{\mathbf q} - \dot f^{\ast}_{\mathbf p}f^{\ast}_{\mathbf q}) = -(f_{\mathbf p}, f^{\ast}_{\mathbf q}) ,
> $$
>
> which is $\propto(E_{\mathbf q} - E_{\mathbf p})\delta^3(\mathbf p + \mathbf q) = 0$ by W2(b), because $E_{-\mathbf p} = E_{\mathbf p}$. This is the one mixed commutator that is not automatic, and it is what kills the number-changing terms of $\hat H$ in Step 6 of (b).
>
> *Checked against:* (a) [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^mod-c2a-5-1|Model §C2a.5.1]]; (b) [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-2|Theorem §C2a.5.2]] with [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-3|Theorem §C2a.5.3]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]] with [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-4|Derivation §C2a.5.4]] (steps 1–7, the same eight terms), [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-2|§C2a.3, Remark: Normal ordering is a choice of quantization]] (the prescription), [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]; the submitted solution of PS3.2(b) as written (derives the algebra from the canonical relations, cancels the number-changing terms by a relabelling and $[\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$; it reorders with the commutator and subtracts the zero-point term, where the sheet asks to reorder before promoting; same final $\hat H$); (c) [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]] (step 6) and [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-3|Derivation §C2a.5.3]] (steps 5–6).

^sol-wq-9

### W10. The charge of the complex field

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10-d]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-10-e]]

> [!success]- Solution
> **Answers.** (a) $\hat Q = \frac12\int\frac{d^3p}{(2\pi)^3}(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}) = \frac12(\hat N_a - \hat N_b)$: $a$-quanta carry $+\frac12$, $b$-quanta $-\frac12$. (b) $[\hat Q, \hat a^\dagger_{\mathbf p}] = \frac12\hat a^\dagger_{\mathbf p}$, $[\hat Q, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$; charges $0$ and $1$. (c) $\hat\phi$ contains $\hat a$ and $\hat b^\dagger$, both lowering $\hat Q$ by $\frac12$. (d) $\int d^3x\,:\!\hat j^0\!: = \hat N_b - \hat N_a = -2\hat Q$; the factor and sign are conventions, the ratio $-1$ of the two charges is physical. (e) $\frac12(\hat N_a - \hat N_b) - \frac12V\int\frac{d^3p}{(2\pi)^3}$: an infinite negative vacuum charge, which would be observable.
>
> **(a) Step 1** (substitute). In $\frac i2\int d^3x\,(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)$ insert the expansions of W9(b) at time $t$, variable $\mathbf p$ in the first factor and $\mathbf q$ in the second. The prefactors are $\frac{1}{\sqrt{2E_{\mathbf p}}}\cdot i\sqrt{\frac{E_{\mathbf q}}2} = \frac i2\sqrt{\frac{E_{\mathbf q}}{E_{\mathbf p}}}$ for $\hat\phi^\dagger\hat\pi^\dagger$ and $\frac i2\sqrt{\frac{E_{\mathbf p}}{E_{\mathbf q}}}$ for $\hat\pi\hat\phi$.
>
> **Step 2** (all four terms of each product).
>
> $$
> (\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x})(-\hat a_{\mathbf q}e^{-iq\cdot x} + \hat b^\dagger_{\mathbf q}e^{iq\cdot x}) = -\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} - \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x} ,
> $$
>
> $$
> (-\hat b_{\mathbf p}e^{-ip\cdot x} + \hat a^\dagger_{\mathbf p}e^{ip\cdot x})(\hat a_{\mathbf q}e^{-iq\cdot x} + \hat b^\dagger_{\mathbf q}e^{iq\cdot x}) = -\hat b_{\mathbf p}\hat a_{\mathbf q}e^{-i(p+q)\cdot x} - \hat b_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{-i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf q}e^{i(p-q)\cdot x} + \hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}e^{i(p+q)\cdot x} .
> $$
>
> **Step 3** ($d^3x$ and the deltas). As in W9(b), Step 5: $\mathbf q = -\mathbf p$ in the $p + q$ terms, $\mathbf q = \mathbf p$ in the $p - q$ terms; $E_{\mathbf q} = E_{\mathbf p}$ in both, so both prefactors become $\frac i2$, and the $p - q$ phases are $1$.
>
> **Step 4** (number-changing terms cancel). First product minus second: $(-\hat b_{\mathbf p}\hat a_{-\mathbf p}) - (-\hat b_{\mathbf p}\hat a_{-\mathbf p}) = 0$ and $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} - \hat a^\dagger_{\mathbf p}\hat b^\dagger_{-\mathbf p} = 0$, term by term, once the energies are equal.
>
> **Step 5** (number-conserving terms double). $(\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}) - (-\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}) = 2\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - 2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$. With the outer $\frac i2$ and the prefactor $\frac i2$, $\frac i2\cdot\frac i2 = -\frac14$:
>
> $$
> \hat Q = -\frac14\int\frac{d^3p}{(2\pi)^3}\bigl(2\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - 2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}\bigr) = \frac12\int\frac{d^3p}{(2\pi)^3}\bigl(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} - \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p}\bigr) .
> $$
>
> **Step 6** (normal order). $:\!\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p}\!: = \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$, so $\hat Q = \frac12(\hat N_a - \hat N_b)$. By (b), an $a$-quantum has charge $+\frac12$ and a $b$-quantum $-\frac12$: particles and antiparticles.
>
> **(b)** As in W5(c), with weight $\frac12$: $[\frac12\int\hat a^\dagger_{\mathbf q}\hat a_{\mathbf q}, \hat a^\dagger_{\mathbf p}] = \frac12\hat a^\dagger_{\mathbf p}$; the $\hat b$ part commutes with $\hat a^\dagger_{\mathbf p}$ (W9(c)). So $[\hat Q, \hat a^\dagger_{\mathbf p}] = \frac12\hat a^\dagger_{\mathbf p}$ and, with weight $-\frac12$, $[\hat Q, \hat b^\dagger_{\mathbf p}] = -\frac12\hat b^\dagger_{\mathbf p}$. $\hat Q\lvert0\rangle = 0$ (every term ends in an annihilator); pushing $\hat Q$ through the creators, $\hat a^\dagger_{\mathbf p}\hat b^\dagger_{\mathbf q}\lvert0\rangle$ has $Q = \frac12 - \frac12 = 0$ and $(\hat a^\dagger_{\mathbf p})^2\lvert0\rangle$ has $Q = \frac12 + \frac12 = 1$.
>
> **(c) Step 1** (annihilators). $\hat Q$ is Hermitian, so $[\hat Q, \hat a^\dagger]^\dagger = \hat a\hat Q - \hat Q\hat a = -[\hat Q, \hat a]$: $[\hat Q, \hat a_{\mathbf p}] = -\frac12\hat a_{\mathbf p}$ and $[\hat Q, \hat b_{\mathbf p}] = +\frac12\hat b_{\mathbf p}$.
>
> **Step 2** (the field). $\hat Q$ passes through the c-number exponentials: $[\hat Q, \hat\phi(x)] = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\bigl([\hat Q, \hat a_{\mathbf p}]e^{-ip\cdot x} + [\hat Q, \hat b^\dagger_{\mathbf p}]e^{ip\cdot x}\bigr) = -\frac12\hat\phi(x)$, since both $\hat a$ and $\hat b^\dagger$ lower the charge by $\frac12$. $\hat\phi^\dagger$ contains $\hat b$ and $\hat a^\dagger$, both raising it: $[\hat Q, \hat\phi^\dagger] = +\frac12\hat\phi^\dagger$.
>
> **Step 3** (finite rotation). $F(\theta) \equiv e^{i\theta\hat Q}\hat\phi\,e^{-i\theta\hat Q}$ has $F'(\theta) = e^{i\theta\hat Q}\,i[\hat Q, \hat\phi]\,e^{-i\theta\hat Q} = -\frac i2F(\theta)$ and $F(0) = \hat\phi$, so $F(\theta) = e^{-i\theta/2}\hat\phi$: $\hat Q$ generates the phase rotation of the field (with the factor $\frac12$ of this normalization).
>
> **(d) Step 1** (the density). $\hat j^0 = i(\hat\phi\,\partial_t\hat\phi^\dagger - \hat\phi^\dagger\partial_t\hat\phi) = i(\hat\phi\hat\pi - \hat\phi^\dagger\hat\pi^\dagger)$. Inside bosonic normal ordering the factors may be written in either order, $:\!\hat\phi\hat\pi\!: = :\!\hat\pi\hat\phi\!:$, so
>
> $$
> :\!\hat j^0\!: = i:\!(\hat\pi\hat\phi - \hat\phi^\dagger\hat\pi^\dagger)\!: = -2\cdot\frac i2:\!(\hat\phi^\dagger\hat\pi^\dagger - \hat\pi\hat\phi)\!: , \qquad \int d^3x\,:\!\hat j^0\!: = -2\hat Q = \hat N_b - \hat N_a .
> $$
>
> **Step 2** (classical check). For $\phi = Ae^{-iEt + i\mathbf p\cdot\mathbf x}$, $j^0 = i(\phi\dot\phi^{\ast} - \phi^{\ast}\dot\phi) = i(iE - (-iE))\lvert A\rvert^2 = -2E\lvert A\rvert^2 < 0$: with $\Delta\phi = +i\phi$ positive frequencies (particles) count negative.
>
> **Step 3** (what is physical). The overall factor ($\frac12$ in Peskin–Schroeder and Problem Set 3, $q$ in Yu) and the overall sign (the sign of $\alpha$; Lecture 3's slide prints the current with the opposite sign, which against the slide's own first line is a slip, not a convention) are conventions. Only the ratio $-1$ between the charges of the two species is physical.
>
> **(e) Step 1** (the constant). Without the colons, Step 5 of (a) reorders with the commutator: $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} = \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$, so $\hat Q = \frac12(\hat N_a - \hat N_b) - \frac12V\int\frac{d^3p}{(2\pi)^3}$. In the box with cutoff the constant is $-\frac12\sum_{\lvert\mathbf k\rvert<\Lambda}1 = -\frac12\mathcal N(V, \Lambda)$, minus half the number of modes, $\mathcal N \approx V\Lambda^3/6\pi^2$.
>
> **Step 2** (forced). For $\hat H$ the constant shifts every energy equally and drops out of every commutator and energy difference. For $\hat Q$ it would give the vacuum an infinite negative charge, which distinguishes particles from antiparticles (it breaks the $\hat a \leftrightarrow \hat b$ symmetry, charge conjugation) and would be observable. The vacuum must be neutral, so here the ordering is fixed by physics; normal ordering achieves it, and so does symmetrizing both species, whose constants $\pm\frac12V\int\frac{d^3p}{(2\pi)^3}$ cancel.
>
> *Checked against:* (a) the submitted solution of PS3.2(c) as written (number-changing terms drop once the deltas set the energies equal; $\hat b\hat b^\dagger$ normal ordered at the end), [[§C2a.5 The Complex Scalar Field and Its Charge#^def-c2a-5-1|Def. §C2a.5.1]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]] and [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-6|Derivation §C2a.5.6]] (steps 1–6, the same prefactors and doubling); (b) [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-6|Derivation §C2a.5.6]] (step 7), [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]; (d) [[§C2a.5 The Complex Scalar Field and Its Charge#^cau-c2a-5-1|§C2a.5, Caution: Normalization and sign of the charge]], [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]], [[§C1b.6 Conserved Charges and Internal Symmetries#^thm-c1b-6-3|Theorem §C1b.6.3]]; (e) [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-6|Derivation §C2a.5.6]] (step 6), [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-2|§C2a.5, Remark: Why the vacuum must be neutral]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^rem-c2a-3-1|§C2a.3, Remark: Why the zero-point energy is dropped]]. *Derived here; check:* (c) has no home box; it follows from the ladder relations of (b) term by term, and its Dirac analogue $[\hat Q, \hat\psi] = -\hat\psi$ is [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]] (charge $1$ per quantum in place of $\frac12$).

^sol-wq-10

### W11. Momentum and energy of the complex field

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-11]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-11-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-11-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-11-c]]

> [!success]- Solution
> **Answers.** (a) The pairs $\hat b_{\mathbf p}\hat a_{-\mathbf p}$, $\hat a_{\mathbf p}\hat b_{-\mathbf p}$ (and their adjoints) combine into $[\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$; the reordering constant $V\int\frac{d^3p}{(2\pi)^3}\mathbf p$ is odd, hence zero. (b) $+\mathbf p$; decided by the relabelling $\mathbf p \to -\mathbf p$ that names the negative-frequency coefficient $\hat b^\dagger_{\mathbf p}$. (c) $2E_0$; a complex field constrained to be real has twice the canonical real Lagrangian.
>
> **(a) Step 1** ($t = 0$ forms). Relabelling $\mathbf p \to -\mathbf p$ in the negative-frequency terms of W9(b): $\hat\phi = \int\frac{d^3p}{(2\pi)^3}\frac{\hat a_{\mathbf p} + \hat b^\dagger_{-\mathbf p}}{\sqrt{2E_{\mathbf p}}}e^{i\mathbf p\cdot\mathbf x}$, $\hat\phi^\dagger$ with $\hat b_{\mathbf p} + \hat a^\dagger_{-\mathbf p}$, $\hat\pi = \int\frac{d^3p}{(2\pi)^3}(-i)\sqrt{\frac{E_{\mathbf p}}2}(\hat b_{\mathbf p} - \hat a^\dagger_{-\mathbf p})e^{i\mathbf p\cdot\mathbf x}$, $\hat\pi^\dagger$ with $\hat a_{\mathbf p} - \hat b^\dagger_{-\mathbf p}$.
>
> **Step 2** (substitute). Variable $\mathbf p$ in the momentum density, $\mathbf p'$ in the gradient, which brings down $i\mathbf p'$; $(-i)(i) = 1$; the factor is $\mathbf p'\sqrt{E_{\mathbf p}}/2\sqrt{E_{\mathbf p'}}$. The $d^3x$ integral gives $(2\pi)^3\delta^3(\mathbf p + \mathbf p')$; $\mathbf p' = -\mathbf p$ turns the factor into $-\mathbf p/2$, and with the overall minus sign into $+\mathbf p/2$:
>
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2\Bigl[(\hat b_{\mathbf p} - \hat a^\dagger_{-\mathbf p})(\hat a_{-\mathbf p} + \hat b^\dagger_{\mathbf p}) + (\hat a_{\mathbf p} - \hat b^\dagger_{-\mathbf p})(\hat b_{-\mathbf p} + \hat a^\dagger_{\mathbf p})\Bigr] .
> $$
>
> **Step 3** (eight terms). $\hat b_{\mathbf p}\hat a_{-\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} - \hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p} - \hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p} + \hat a_{\mathbf p}\hat b_{-\mathbf p} + \hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} - \hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p} - \hat b^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p}$.
>
> **Step 4** (annihilator and creator pairs). In $\mathbf p\,\hat a_{\mathbf p}\hat b_{-\mathbf p}$ substitute $\mathbf p \to -\mathbf p$: $-\mathbf p\,\hat a_{-\mathbf p}\hat b_{\mathbf p}$; with $\mathbf p\,\hat b_{\mathbf p}\hat a_{-\mathbf p}$ this is $\mathbf p\,[\hat b_{\mathbf p}, \hat a_{-\mathbf p}] = 0$. Likewise $-\mathbf p\,\hat b^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p} \to +\mathbf p\,\hat b^\dagger_{\mathbf p}\hat a^\dagger_{-\mathbf p}$, and with $-\mathbf p\,\hat a^\dagger_{-\mathbf p}\hat b^\dagger_{\mathbf p}$ it gives $-\mathbf p\,[\hat a^\dagger_{-\mathbf p}, \hat b^\dagger_{\mathbf p}] = 0$. They die because the species commute (for the real field, by oddness, W6(a)).
>
> **Step 5** (number-conserving terms). $\mathbf p \to -\mathbf p$ turns $-\mathbf p\,\hat a^\dagger_{-\mathbf p}\hat a_{-\mathbf p}$ and $-\mathbf p\,\hat b^\dagger_{-\mathbf p}\hat b_{-\mathbf p}$ into $+\mathbf p\,\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p}$ and $+\mathbf p\,\hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}$:
>
> $$
> \hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\frac{\mathbf p}2\bigl(\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p} + \hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b_{\mathbf p}\hat b^\dagger_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p}\bigr) .
> $$
>
> **Step 6** (no ordering needed). Reordering with the commutators leaves $\frac{\mathbf p}2\cdot2(2\pi)^3\delta^3(\mathbf 0)$ under the integral, i.e. $V\int\frac{d^3p}{(2\pi)^3}\mathbf p$: odd, zero for a rotation-invariant cutoff. So $\hat{\mathbf P} = \int\frac{d^3p}{(2\pi)^3}\mathbf p(\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + \hat b^\dagger_{\mathbf p}\hat b_{\mathbf p})$ with or without colons.
>
> **(b)** By (a) and the computation of W6(c), $[\hat{\mathbf P}, \hat b^\dagger_{\mathbf p}] = \mathbf p\,\hat b^\dagger_{\mathbf p}$, so $\hat b^\dagger_{\mathbf p}\lvert0\rangle$ carries $+\mathbf p$, like $\hat a^\dagger_{\mathbf p}\lvert0\rangle$. The negative-frequency solution $e^{+ip\cdot x} = e^{iE_{\mathbf p}t - i\mathbf p\cdot\mathbf x}$ was obtained from the coefficient of $e^{+iE_{\mathbf k}t + i\mathbf k\cdot\mathbf x}$ by $\mathbf k = -\mathbf p$, and the name $\hat b^\dagger_{\mathbf p}$ was given after this relabelling ($\hat b^\dagger_{\mathbf p} \equiv \hat{\tilde a}_{-\mathbf p}$). Without it the antiparticle label would be minus its momentum; the spatial factor $e^{-i\mathbf p\cdot\mathbf x}$ of the creation term is what a field creating momentum $+\mathbf p$ must carry, as $\hat a^\dagger_{\mathbf p}e^{ip\cdot x}$ in the real field does.
>
> **(c) Step 1** (the constant). Reordering $\hat a_{\mathbf p}\hat a^\dagger_{\mathbf p}$ and $\hat b_{\mathbf p}\hat b^\dagger_{\mathbf p}$ in Step 5 of W9(b) with the commutators adds $2\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2(2\pi)^3\delta^3(\mathbf 0) = 2E_0$: one $\frac12E_{\mathbf p}$ per mode per species (in the box, $\sum_{\lvert\mathbf k\rvert<\Lambda}E_{\mathbf k}$).
>
> **Step 2** (the trap). Imposing $\hat\phi^\dagger = \hat\phi$ on the expansions gives $\hat b = \hat a$ and the real field's expansion. But in $\hat H$ it gives $\int E_{\mathbf p}\,2\hat a^\dagger_{\mathbf p}\hat a_{\mathbf p} + 2E_0$, twice the real field's $\hat H$: a complex field constrained to be real has $\mathcal L = (\partial\phi)^2 - m^2\phi^2$, twice the canonical $\frac12(\partial\phi)^2 - \frac12m^2\phi^2$. The real field is one real component, $\phi_1$ of $\phi = (\phi_1 + i\phi_2)/\sqrt2$, not the complex field made real.
>
> *Checked against:* (a) [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-5|Theorem §C2a.5.5]] and [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-5|Derivation §C2a.5.5]] (steps 1–7); (b) [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-2|Derivation §C2a.5.2]] (steps 1–2), "What the derivation shows" of [[§C2a.5 The Complex Scalar Field and Its Charge#^der-c2a-5-5|Derivation §C2a.5.5]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-7|Theorem §C2a.5.7]]; (c) [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]] (the constant $2E_0$), [[§C2a.5 The Complex Scalar Field and Its Charge#^rem-c2a-5-1|§C2a.5, Remark: The real field is a constrained complex field, with one trap]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^cau-c2a-3-1|§C2a.3, Caution: Names for the zero-point energy]]. Problem 3(b) of [[PHY 513 Practice Midterm]] asks (a) with the same answer.

^sol-wq-11

## The Dirac field

### W12. The Dirac field as a canonical system

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-12]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-12-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-12-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-12-c]]

> [!success]- Solution
> **Answers.** (a) $\pi_\psi = i\psi^\dagger$, $\pi_{\bar\psi} = 0$: not a velocity but the adjoint of the coordinate; canonical pairs $(\psi_a, i\psi^\dagger_a)$, $a = 1, \dots, 4$. (b) Insert $\hat\pi_\psi = i\hat\psi^\dagger$ and divide by $i$; $\{\hat\psi_a(\mathbf x), \hat{\bar\psi}_b(\mathbf y)\} = (\gamma^0)_{ab}\delta^3(\mathbf x - \mathbf y)$. (c) $\mathcal H = \psi^\dagger(-i\boldsymbol\alpha\cdot\nabla + \beta m)\psi$; $\mathbf P = \int d^3x\,\psi^\dagger(-i\nabla)\psi = -\int d^3x\,\pi_\psi\nabla\psi$, the Noether charge, not $\int\pi_\psi$.
>
> **(a) Step 1** (momenta). $\mathcal L = \bar\psi i\gamma^0\partial_0\psi + \bar\psi(i\gamma^j\partial_j - m)\psi$ is linear in $\dot\psi$ and contains no derivative of $\bar\psi$. So $\pi_{\psi,a} = \partial\mathcal L/\partial\dot\psi_a = (\bar\psi i\gamma^0)_a = i(\psi^\dagger\gamma^0\gamma^0)_a = i\psi^\dagger_a$, using $(\gamma^0)^2 = \mathbb 1$, and $\pi_{\bar\psi} = 0$.
>
> **Step 2** (a relation, not a velocity). For the scalar, $\pi = \dot\phi$ is solved for the velocity and $\pi(\mathbf x)$ is data on the slice independent of $\phi(\mathbf x)$. Here $\pi_\psi - i\psi^\dagger = 0$ holds whatever the velocities: it restricts the canonical data rather than adding to them (in Dirac's language, a constraint). The independent data are the four complex $\psi_a(\mathbf x)$; the canonical pairs are $(\psi_a, \pi_a = i\psi^\dagger_a)$, and $\psi^\dagger$, $\bar\psi = -i\pi_\psi\gamma^0$ are not further coordinates. After quantization $\hat\pi_\psi = i\hat\psi^\dagger$ is an identity of operator-valued distributions: there is no momentum operator besides $i\hat\psi^\dagger$.
>
> **(b) Step 1** (momentum form ⇒ field form). Bilinearity and $i$ a number: $\{\hat\psi_a(\mathbf x), \hat\pi_{\psi,b}(\mathbf y)\} = i\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}$. So $\{\hat\psi_a, \hat\pi_{\psi,b}\} = i\delta_{ab}\delta^3$ is $\{\hat\psi_a, \hat\psi^\dagger_b\} = \delta_{ab}\delta^3$ after dividing by $i \ne 0$; the steps reverse.
>
> **Step 2** (momentum with momentum). $\{\hat\pi_{\psi,a}, \hat\pi_{\psi,b}\} = i^2\{\hat\psi^\dagger_a, \hat\psi^\dagger_b\} = -\{\hat\psi^\dagger_a, \hat\psi^\dagger_b\}$, so one vanishes iff the other does; $\{\hat\psi_a, \hat\psi_b\} = 0$ contains no momentum and is the same on both sides. Only bilinearity was used: the same equivalence holds for commutators.
>
> **Step 3** ($\hat{\bar\psi}$). $\hat{\bar\psi}_b = \sum_c\hat\psi^\dagger_c(\gamma^0)_{cb}$ is a combination of momenta, so $\{\hat\psi_a(\mathbf x), \hat{\bar\psi}_b(\mathbf y)\} = \sum_c\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_c(\mathbf y)\}(\gamma^0)_{cb} = \sum_c\delta_{ac}(\gamma^0)_{cb}\delta^3(\mathbf x - \mathbf y) = (\gamma^0)_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **(c) Step 1** (Legendre transform). $\mathcal H = \pi_\psi\dot\psi - \mathcal L = i\psi^\dagger\dot\psi - \bar\psi i\gamma^0\partial_0\psi - \bar\psi(i\gamma^j\partial_j - m)\psi$. The first two terms cancel ($\bar\psi\gamma^0 = \psi^\dagger$): the velocity drops out identically. So $\mathcal H = \bar\psi(-i\gamma^j\partial_j + m)\psi = \psi^\dagger\gamma^0(-i\gamma^j\partial_j + m)\psi = \psi^\dagger(-i\alpha^j\partial_j + \beta m)\psi = \psi^\dagger H_{\text{s.p.}}\psi$, for every configuration.
>
> **Step 2** (on solutions). Multiplying the Dirac equation $(i\gamma^0\partial_0 + i\gamma^j\partial_j - m)\psi = 0$ by $\gamma^0$ gives $i\partial_t\psi = \gamma^0(-i\gamma^j\partial_j + m)\psi = H_{\text{s.p.}}\psi$, so $\mathcal H = i\psi^\dagger\partial_t\psi$ on solutions.
>
> **Step 3** (momentum). From the canonical tensor, $T^{0i} = \frac{\partial\mathcal L}{\partial(\partial_0\psi)}\partial^i\psi - g^{0i}\mathcal L = i\psi^\dagger\partial^i\psi = -i\psi^\dagger\partial_i\psi = -\pi_\psi\partial_i\psi$ ($\bar\psi$ has no derivative in $\mathcal L$ and contributes nothing). So $P^i = \int d^3x\,T^{0i}$ gives, in one equation, $\mathbf P = \int d^3x\,\psi^\dagger(-i\nabla)\psi = -\int d^3x\,\pi_\psi\nabla\psi$. It is the Noether charge of space translations; the canonical momentum $\pi_\psi = i\psi^\dagger$ is the density conjugate to $\psi$, a different object.
>
> *Checked against:* (a) [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-1|Theorem §C5a.8.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]] and [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-1|Derivation §C5b.1.1]] (steps 1–2); (b) [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-1|Derivation §C5b.1.1]] (steps 4–6, including $(\gamma^0)_{ab}\delta^3$); (c) [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-2|Theorem §C5a.8.2]], [[§C5a.7 The Dirac Equation and Its Lagrangian#^def-c5a-7-3|Def. §C5a.7.3]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-6|Theorem §C5a.8.6]], [[§C5b.1 Canonical Quantization of the Dirac Field#^mod-c5b-1-2|Model §C5b.1.2]]. Problem 12(c) of [[PHY 513 Worksheet — Noether Currents]] derives the same $H$ and $\mathbf P$ from $T^{\mu\nu}$.

^sol-wq-12

### W13. Mode expansion and mode extraction

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-13]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-13-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-13-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-13-c]]

> [!success]- Solution
> **Answers.** (a) $\hat\psi^\dagger = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s(\hat a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x} + \hat b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x})$, $\hat{\bar\psi}$ the same with $\bar u$, $\bar v$; $\hat\psi$ ($\hat a$, $\hat b^\dagger$) annihilates particles and creates antiparticles, $\hat\psi^\dagger$ and $\hat{\bar\psi}$ ($\hat a^\dagger$, $\hat b$) create particles and annihilate antiparticles. (b) $u^{s\dagger}(p)u^r(p) = v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ at equal momenta, $u^{s\dagger}(p)v^r(\tilde p) = v^{s\dagger}(p)u^r(\tilde p) = 0$ at opposite three-momenta. (c) The positive product $\int d^3x\,\chi^\dagger\psi$, whose density is the charge density; no minus sign is needed.
>
> **(a)** Take the adjoint term by term: $(\hat a^s_{\mathbf p}u^s(p)e^{-ip\cdot x})^\dagger = \hat a^{s\dagger}_{\mathbf p}u^{s\dagger}(p)e^{ip\cdot x}$ (the spinor becomes a row, the number is conjugated) and $(\hat b^{s\dagger}_{\mathbf p}v^s(p)e^{ip\cdot x})^\dagger = \hat b^s_{\mathbf p}v^{s\dagger}(p)e^{-ip\cdot x}$. Multiplying on the right by $\gamma^0$ turns $u^\dagger$, $v^\dagger$ into $\bar u$, $\bar v$: $\hat{\bar\psi} = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s(\hat b^s_{\mathbf p}\bar v^s(p)e^{-ip\cdot x} + \hat a^{s\dagger}_{\mathbf p}\bar u^s(p)e^{ip\cdot x})$. $\gamma^0$ only rearranges components, so $\hat\psi^\dagger$ and $\hat{\bar\psi}$ have the same operator content. Each field changes the content in two ways with one net effect: $\hat\psi$ removes a particle or adds an antiparticle (both lower the charge by one, W18(b)).
>
> **(b) Step 1** (substitute). Variable $\mathbf q$, spin label $r$; the spinors and exponentials are c-numbers:
>
> $$
> \int d^3x\,e^{ip\cdot x}u^{s\dagger}(p)\hat\psi(x) = \int d^3x\int\frac{d^3q}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf q}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(q)\,\hat a^r_{\mathbf q}\,e^{i(p-q)\cdot x} + u^{s\dagger}(p)v^r(q)\,\hat b^{r\dagger}_{\mathbf q}\,e^{i(p+q)\cdot x}\Bigr) .
> $$
>
> **Step 2** ($d^3x$, then $\mathbf q$). $e^{i(p\mp q)\cdot x} = e^{i(E_{\mathbf p}\mp E_{\mathbf q})t}e^{-i(\mathbf p\mp\mathbf q)\cdot\mathbf x}$ gives $(2\pi)^3\delta^3(\mathbf p \mp \mathbf q)$. In the first term $\mathbf q = \mathbf p$, phase $1$; in the second $\mathbf q = -\mathbf p$, i.e. $q = (E_{\mathbf p}, -\mathbf p) = \tilde p$, phase $e^{2iE_{\mathbf p}t}$:
>
> $$
> \frac{1}{\sqrt{2E_{\mathbf p}}}\sum_r\Bigl(u^{s\dagger}(p)u^r(p)\,\hat a^r_{\mathbf p} + u^{s\dagger}(p)v^r(\tilde p)\,\hat b^{r\dagger}_{-\mathbf p}\,e^{2iE_{\mathbf p}t}\Bigr) .
> $$
>
> **Step 3** (spinor identities). $u^{s\dagger}(p)u^r(p) = 2E_{\mathbf p}\delta^{rs}$ and $u^{s\dagger}(p)v^r(\tilde p) = 0$: the whole $\hat b^\dagger$ term drops, with its time dependence, and what remains is $\sqrt{2E_{\mathbf p}}\,\hat a^s_{\mathbf p}$. Divide by $\sqrt{2E_{\mathbf p}}$.
>
> **Step 4** ($\hat b^\dagger$). The same steps with $e^{-ip\cdot x}v^{s\dagger}(p)$: the $\hat a$ term now has $\int d^3x\,e^{-i(p+q)\cdot x}$, so $\mathbf q = -\mathbf p$ and the factor is $v^{s\dagger}(p)u^r(\tilde p) = 0$; the $\hat b^\dagger$ term has $\mathbf q = \mathbf p$, phase $1$, and $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$. So $\hat b^{s\dagger}_{\mathbf p}$ is as stated. The orthogonality is needed at opposite three-momenta because the $d^3x$ integral pairs $\mathbf p$ with $-\mathbf p$; at equal momenta $u^{r\dagger}(p)v^s(p) \ne 0$ in general.
>
> **(c)** With $f^s_{\mathbf p} = u^s(p)e^{-ip\cdot x}/\sqrt{2E_{\mathbf p}}$ and $g^s_{\mathbf p} = v^s(p)e^{ip\cdot x}/\sqrt{2E_{\mathbf p}}$, (b) reads $\hat a^s_{\mathbf p} = \langle f^s_{\mathbf p}, \hat\psi\rangle$, $\hat b^{s\dagger}_{\mathbf p} = \langle g^s_{\mathbf p}, \hat\psi\rangle$ with $\langle\chi, \psi\rangle = \int d^3x\,\chi^\dagger\psi$: positive definite and conserved for solutions of the Dirac equation (its density $\psi^\dagger\psi$ is the conserved charge density), which is why the result is independent of $t$. The scalar's Klein–Gordon product was indefinite, and the negative-frequency coefficient came with a minus sign, $\hat a^\dagger_{\mathbf p} = -(f^{\ast}_{\mathbf p}, \hat\phi)$ (W3(c)); here both come with a plus. The indefiniteness has moved into the energy (W15(b)).
>
> *Checked against:* (a) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-2|Theorem §C5b.2.2]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^cau-c5b-2-1|§C5b.2, Caution: What anticommutes and what does not]]; (b) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-3|Theorem §C5b.2.3]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-3|Derivation §C5b.2.3]] (steps 1–6), [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-1|Theorem §C5a.10.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-3|Theorem §C5a.10.3]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]]; (c) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-5|§C5b.2, Remark: A positive inner product]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]].

^sol-wq-13

### W14. The anticommutator algebra in both directions

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-14]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-14-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-14-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-14-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-14-d]]

> [!success]- Solution
> **Answers.** (a) $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p-q)\cdot x}u^{r\dagger}(p)u^s(q) = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, and the same for $\hat b$ with $\{\hat\psi^\dagger, \hat\psi\}$ in the opposite order. (b) Both vanish: $u^{r\dagger}(p)v^s(\tilde p) = 0$, resp. $\{\hat\psi, \hat\psi\} = 0$. (c) $\sum_s(u^s_au^{s\ast}_b + v^s_a(\tilde p)v^{s\ast}_b(\tilde p)) = [(\slashed{p} + m) + (\slashed{\tilde p} - m)]\gamma^0 = 2E_{\mathbf p}\delta_{ab}$. (d) $[\hat a, \hat a^\dagger] = +(2\pi)^3\delta^{rs}\delta^3$ but $[\hat b, \hat b^\dagger] = -(2\pi)^3\delta^{rs}\delta^3$: $\hat b$ is extracted from $\hat\psi^\dagger$, so the canonical relation enters in the opposite order, which costs a sign for a commutator and nothing for an anticommutator.
>
> **(a) Step 1** (the canonical relation, both orders). $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$, and an anticommutator is symmetric: $\{\hat\psi^\dagger_b(\mathbf y), \hat\psi_a(\mathbf x)\} = +\delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **Step 2** ($\{\hat a, \hat a^\dagger\}$). By W13(b) at a common time, $\hat a^r_{\mathbf p}$ (variable $\mathbf x$) is built from $\hat\psi$, and its adjoint $\hat a^{s\dagger}_{\mathbf q} = \frac{1}{\sqrt{2E_{\mathbf q}}}\int d^3y\,e^{-iq\cdot y}\hat\psi^\dagger(y)u^s(q)$ from $\hat\psi^\dagger$. The c-number spinors and phases come out of the anticommutator:
>
> $$
> \begin{aligned}\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}\} &= \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\,e^{ip\cdot x - iq\cdot y}u^{r\dagger}_a(p)\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\}u^s_b(q) \\ &= \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p-q)\cdot x}u^{r\dagger}(p)u^s(q) ,\end{aligned}
> $$
>
> the $\mathbf y$ integral done by $\delta^3(\mathbf x - \mathbf y)$ and $\delta_{ab}$ contracting the indices. The $d^3x$ integral is $e^{i(E_{\mathbf p} - E_{\mathbf q})t}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; on its support the phase is $1$, $E_{\mathbf q} = E_{\mathbf p}$ and $u^{r\dagger}(p)u^s(p) = 2E_{\mathbf p}\delta^{rs}$: the result.
>
> **Step 3** ($\{\hat b, \hat b^\dagger\}$). Now $\hat b^r_{\mathbf p} = \frac{1}{\sqrt{2E_{\mathbf p}}}\int d^3x\,e^{ip\cdot x}\hat\psi^\dagger(x)v^r(p)$ is built from $\hat\psi^\dagger$ and $\hat b^{s\dagger}_{\mathbf q}$ from $\hat\psi$:
>
> $$
> \begin{aligned}\{\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}\} &= \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,d^3y\,e^{ip\cdot x - iq\cdot y}v^{s\dagger}_b(q)\{\hat\psi^\dagger_a(\mathbf x), \hat\psi_b(\mathbf y)\}v^r_a(p) \\ &= +\frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p-q)\cdot x}v^{s\dagger}(q)v^r(p)\end{aligned}
> $$
>
> by Step 1, and the same delta with $v^{s\dagger}(p)v^r(p) = 2E_{\mathbf p}\delta^{rs}$ gives $+(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$.
>
> **(b) Step 1** ($\{\hat a, \hat b\}$). $\hat a^r_{\mathbf p}$ from $\hat\psi$, $\hat b^s_{\mathbf q}$ from $\hat\psi^\dagger$: $\{\hat a^r_{\mathbf p}, \hat b^s_{\mathbf q}\} = \frac{1}{\sqrt{4E_{\mathbf p}E_{\mathbf q}}}\int d^3x\,e^{i(p+q)\cdot x}u^{r\dagger}(p)v^s(q) = \frac{e^{2iE_{\mathbf p}t}}{2E_{\mathbf p}}(2\pi)^3\delta^3(\mathbf p + \mathbf q)\,u^{r\dagger}(p)v^s(\tilde p) = 0$: on the support $q = \tilde p$, and the $\pm E_{\mathbf p}$ eigenvectors of $H_{\text{s.p.}}(\mathbf p)$ are orthogonal.
>
> **Step 2** ($\{\hat a, \hat b^\dagger\}$). Both are built from $\hat\psi$ alone, and $\{\hat\psi, \hat\psi\} = 0$: zero term by term. Likewise $\{\hat a, \hat a\}$; $\{\hat b, \hat b\}$ and $\{\hat a^\dagger, \hat b\}$ contain only $\{\hat\psi^\dagger, \hat\psi^\dagger\} = 0$; the rest are adjoints.
>
> **(c) Step 1** (common Fourier factor). At $t = 0$ relabel the antiparticle term by $\mathbf p \to -\mathbf p$, so both terms carry $e^{i\mathbf p\cdot\mathbf x}$; the spinor becomes $v^r(\tilde p)$:
>
> $$
> \begin{aligned}\hat\psi_a(\mathbf x) &= \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\sum_r\bigl(\hat a^r_{\mathbf p}u^r_a(p) + \hat b^{r\dagger}_{-\mathbf p}v^r_a(\tilde p)\bigr), \\ \hat\psi^\dagger_b(\mathbf y) &= \int\frac{d^3p'}{(2\pi)^3}\frac{e^{-i\mathbf p'\cdot\mathbf y}}{\sqrt{2E_{\mathbf p'}}}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p'}u^{s\ast}_b(p') + \hat b^s_{-\mathbf p'}v^{s\ast}_b(\tilde p')\bigr) .\end{aligned}
> $$
>
> **Step 2** (operators first). Only $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf p'}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf p')$ and $\{\hat b^{r\dagger}_{-\mathbf p}, \hat b^s_{-\mathbf p'}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf p')$ survive. Each delta sets $\mathbf p' = \mathbf p$, $s = r$, and $1/\sqrt{2E_{\mathbf p}2E_{\mathbf p'}} \to 1/2E_{\mathbf p}$:
>
> $$
> \{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot(\mathbf x - \mathbf y)}}{2E_{\mathbf p}}\sum_s\bigl(u^s_a(p)u^{s\ast}_b(p) + v^s_a(\tilde p)v^{s\ast}_b(\tilde p)\bigr) .
> $$
>
> **Step 3** (spin sums, with $\gamma^0$ put back). The sums are for $u\bar u$ and $v\bar v$; multiplying on the right by $\gamma^0$, $(\gamma^0)^2 = \mathbb 1$: $\sum_su^su^{s\dagger} = (\slashed{p} + m)\gamma^0$ and $\sum_sv^s(\tilde p)v^{s\dagger}(\tilde p) = (\slashed{\tilde p} - m)\gamma^0$. Adding, the masses cancel and $\slashed{p} + \slashed{\tilde p} = (\gamma^0E_{\mathbf p} - \gamma^ip^i) + (\gamma^0E_{\mathbf p} + \gamma^ip^i) = 2E_{\mathbf p}\gamma^0$, so the bracket is $2E_{\mathbf p}(\gamma^0\gamma^0)_{ab} = 2E_{\mathbf p}\delta_{ab}$.
>
> **Step 4** (Fourier integral). The energies cancel and $\int\frac{d^3p}{(2\pi)^3}e^{i\mathbf p\cdot(\mathbf x - \mathbf y)} = \delta^3(\mathbf x - \mathbf y)$: $\{\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$. $\{\hat\psi, \hat\psi\}$ and $\{\hat\psi^\dagger, \hat\psi^\dagger\}$ contain only vanishing oscillator anticommutators. Both frequencies are needed: the $u$'s alone give $(\slashed{p} + m)\gamma^0$, not a multiple of $\mathbb 1$, and the field would not be local; the $u$'s span only half of $\mathbb C^4$.
>
> **(d) Step 1** (the relation reversed). With commutators, $[\hat\psi^\dagger_b(\mathbf y), \hat\psi_a(\mathbf x)] = -[\hat\psi_a(\mathbf x), \hat\psi^\dagger_b(\mathbf y)] = -\delta_{ab}\delta^3(\mathbf x - \mathbf y)$.
>
> **Step 2.** Step 2 of (a) goes through unchanged ($\hat\psi$ left of $\hat\psi^\dagger$): $[\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf q}] = +(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$. Step 3 has $\hat\psi^\dagger$ left of $\hat\psi$, so it picks up the minus sign of Step 1: $[\hat b^r_{\mathbf p}, \hat b^{s\dagger}_{\mathbf q}] = -(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$. The mixed ones vanish as in (b). The sign comes only from the order in which the canonical relation enters.
>
> *Checked against:* (a)–(b) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-4|Theorem §C5b.2.4]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-4|Derivation §C5b.2.4]] (steps 1–5); (c) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-4b|Derivation §C5b.2.4, second route]] (Lecture 10's direction, steps 1–5), [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-7|Theorem §C5a.10.7]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-8|Theorem §C5a.10.8]], [[§C5a.10 Normalization, Spin Sums and Helicity#^rem-c5a-10-2|§C5a.10, Remark: Why neither spin sum is the identity]]; (d) [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]] and [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^der-c5b-2-5|Derivation §C5b.2.5]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^rem-c5b-2-7|§C5b.2, Remark: One algebraic fact]].

^sol-wq-14

### W15. The energy in modes, and why anticommutators

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-15]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-15-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-15-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-15-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-15-d]]

> [!success]- Solution
> **Answers.** (a) The cross terms carry $u^{r\dagger}(p)v^s(\tilde p) = v^{r\dagger}(\tilde p)u^s(p) = 0$; the diagonal ones $u^{r\dagger}u^s = v^{r\dagger}(\tilde p)v^s(\tilde p) = 2E_{\mathbf p}\delta^{rs}$, and $H_{\text{s.p.}}(\mathbf p)$ gives $+E_{\mathbf p}$ on $u^s(p)$ and $-E_{\mathbf p}$ on $v^s(\tilde p)$. (b) $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\lvert a^s_{\mathbf p}\rvert^2 - \lvert b^s_{\mathbf p}\rvert^2)$, unbounded below; $Q = \sum_s\int\frac{d^3p}{(2\pi)^3}(\lvert a^s_{\mathbf p}\rvert^2 + \lvert b^s_{\mathbf p}\rvert^2) \ge 0$: the opposite of the complex scalar. (c) $\lVert\hat b^{s\dagger}(g)\lvert0\rangle\rVert^2 = -\int\frac{d^3p}{(2\pi)^3}\lvert g\rvert^2 < 0$; with $\hat d = \hat b^\dagger$ the $n$-quantum states have $\langle\hat H\rangle = -n\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\lvert g\rvert^2 \to -\infty$. (d) Integer spin ⇒ commutators, bosons; half-odd-integer spin ⇒ anticommutators, fermions; stated, not proved, in the course.
>
> **(a) Step 1** ($t = 0$). $\hat H$ is time independent, so use the relabelled $t = 0$ expansions of W14(c), with variables $\mathbf p$, $s$ in $\hat\psi$ and $\mathbf p'$, $r$ in $\hat\psi^\dagger$.
>
> **Step 2** ($H_{\text{s.p.}}$ on the coefficients). On $e^{i\mathbf p\cdot\mathbf x}$, $H_{\text{s.p.}}$ acts as the matrix $H_{\text{s.p.}}(\mathbf p) = \gamma^0(\gamma^jp^j + m)$, on the c-number spinors only. Multiplying $(\slashed{p} - m)u^s(p) = 0$ by $\gamma^0$ gives $H_{\text{s.p.}}(\mathbf p)u^s(p) = E_{\mathbf p}u^s(p)$; multiplying $(\slashed{\tilde p} + m)v^s(\tilde p) = 0$ by $\gamma^0$, with $\slashed{\tilde p} = \gamma^0E_{\mathbf p} + \gamma^jp^j$, gives $H_{\text{s.p.}}(\mathbf p)v^s(\tilde p) = -E_{\mathbf p}v^s(\tilde p)$. So $H_{\text{s.p.}}\hat\psi = \int\frac{d^3p}{(2\pi)^3}\frac{e^{i\mathbf p\cdot\mathbf x}}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(E_{\mathbf p}\hat a^s_{\mathbf p}u^s(p) - E_{\mathbf p}\hat b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\bigr)$.
>
> **Step 3** ($d^3x$). $\int d^3x\,e^{-i\mathbf p'\cdot\mathbf x}e^{i\mathbf p\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$ sets $\mathbf p' = \mathbf p$ and leaves $1/2E_{\mathbf p}$:
>
> $$
> \hat H = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\sum_{r,s}\bigl(\hat a^{r\dagger}_{\mathbf p}u^{r\dagger}(p) + \hat b^r_{-\mathbf p}v^{r\dagger}(\tilde p)\bigr)\bigl(E_{\mathbf p}\hat a^s_{\mathbf p}u^s(p) - E_{\mathbf p}\hat b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\bigr) .
> $$
>
> **Step 4** (four terms, operators in the order they stand). $\frac{E_{\mathbf p}}{2E_{\mathbf p}}\bigl[u^{r\dagger}u^s\,\hat a^{r\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - u^{r\dagger}(p)v^s(\tilde p)\,\hat a^{r\dagger}_{\mathbf p}\hat b^{s\dagger}_{-\mathbf p} + v^{r\dagger}(\tilde p)u^s(p)\,\hat b^r_{-\mathbf p}\hat a^s_{\mathbf p} - v^{r\dagger}(\tilde p)v^s(\tilde p)\,\hat b^r_{-\mathbf p}\hat b^{s\dagger}_{-\mathbf p}\bigr]$. The two cross terms, which would create or destroy a pair, vanish by orthogonality at opposite three-momenta; the diagonal ones give $2E_{\mathbf p}\delta^{rs}$. So $\hat H = \int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\sum_s(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{-\mathbf p}\hat b^{s\dagger}_{-\mathbf p})$, and $\mathbf p \to -\mathbf p$ in the $\hat b$ term gives the statement. No (anti)commutator was used.
>
> **(b) Step 1.** For c-number amplitudes $b^sb^{s\ast} = \lvert b^s\rvert^2$, so (a) becomes $H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\lvert a^s_{\mathbf p}\rvert^2 - \lvert b^s_{\mathbf p}\rvert^2)$. The charge is the same computation with $\hat\psi$ in place of $H_{\text{s.p.}}\hat\psi$: the factor $E_{\mathbf p}$ becomes $1$ and the minus sign of the $\hat b^\dagger$ term a plus, so $Q = \sum_s\int\frac{d^3p}{(2\pi)^3}(\lvert a^s_{\mathbf p}\rvert^2 + \lvert b^s_{\mathbf p}\rvert^2) = \int d^3x\,\psi^\dagger\psi$.
>
> **Step 2.** Take $a = 0$, $b^1 = \lambda g$, $g \ne 0$: $H = -\lambda^2\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\lvert g\rvert^2 \to -\infty$. $Q$ is a sum of squares, zero only for $\psi = 0$. The complex scalar is the opposite: positive classical energy, indefinite Klein–Gordon charge. Quantization has to exchange the two roles.
>
> **(c) Step 1** (negative norm). With $\hat b^s(g) = \int\frac{d^3p}{(2\pi)^3}\overline{g(\mathbf p)}\hat b^s_{\mathbf p}$, W14(d) gives $[\hat b^s(g), \hat b^{s\dagger}(g)] = -\int\frac{d^3p}{(2\pi)^3}\lvert g\rvert^2$. If $\hat b^s(g)\lvert0\rangle = 0$: $\lVert\hat b^{s\dagger}(g)\lvert0\rangle\rVert^2 = \langle0|[\hat b^s(g), \hat b^{s\dagger}(g)]|0\rangle + \langle0|\hat b^{s\dagger}(g)\hat b^s(g)|0\rangle = -\int\frac{d^3p}{(2\pi)^3}\lvert g\rvert^2 < 0$, impossible in a Hilbert space. Meanwhile $[-E_{\mathbf q}\hat b^r_{\mathbf q}\hat b^{r\dagger}_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}] = -E_{\mathbf q}[\hat b^r_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}]\hat b^{r\dagger}_{\mathbf q} = +E_{\mathbf q}(2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\hat b^{r\dagger}_{\mathbf q}$, so $\hat b^\dagger$ still raises the energy: the failure is in the metric.
>
> **Step 2** (energy unbounded). With $\hat d \equiv \hat b^\dagger$ annihilating $\lvert0\rangle$: $[\hat d^r_{\mathbf p}, \hat d^{s\dagger}_{\mathbf q}] = [\hat b^{r\dagger}_{\mathbf p}, \hat b^s_{\mathbf q}] = +(2\pi)^3\delta^{rs}\delta^3(\mathbf p - \mathbf q)$, a bosonic algebra with positive norms, and $-\hat b\hat b^\dagger = -\hat d^\dagger\hat d$, so $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^{s\dagger}\hat a^s - \hat d^{s\dagger}\hat d^s)$. Each $\hat d^{s\dagger}(g)$ lowers the energy by the packet's mean energy, and since the $\hat d^\dagger$ commute, $n$ quanta can share one packet: the normalized $(n!)^{-1/2}\hat d^{s\dagger}(g)^n\lvert0\rangle$ ($\int\frac{d^3p}{(2\pi)^3}\lvert g\rvert^2 = 1$) has $\langle\hat H\rangle = -n\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\lvert g\rvert^2$, unbounded below as $n \to \infty$. A Fock vacuum must be annihilated by one of $\hat b$, $\hat b^\dagger$ in each mode, so there is no third option: commutators give no positive-norm space with energy bounded below.
>
> **(d)** The course's statement: a field of integer spin ($j_+ + j_-$ an integer) must be quantized with commutators and describes bosons; a field of half-odd-integer spin must be quantized with anticommutators and describes fermions; the ingredients are Lorentz invariance, locality, positive energies and norms, and causality (microcausality of observables). The proof is not given in the course ("The proof is complicated"). What is checked: the Dirac field with commutators fails positivity ((c)) and causality, and with anticommutators has positive energies, positive norms and commuting observables at spacelike separation; the scalar with commutators has positive energies and norms and is microcausal. The exclusion principle is then an output.
>
> *Checked against:* (a) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-2|Theorem §C5b.3.2]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-2b|Derivation §C5b.3.2, second route]] (Lecture 10's route at $t = 0$, steps 1–6), [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-1|Theorem §C5b.3.1]]; (b) [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-2|Theorem §C5b.5.2]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-2|Derivation §C5b.5.2]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-1|Derivation §C5b.5.1]] (the charge as the same computation); (c) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-3|Theorem §C5b.3.3]] and [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-3|Derivation §C5b.3.3]] (steps 1–6), [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-5|Theorem §C5b.2.5]]; (d) [[§C5b.1 Canonical Quantization of the Dirac Field#^pr-c5b-1-7|Principle §C5b.1.7]], [[§C5b.9 Spin and Statistics#^thm-c5b-9-1|Theorem §C5b.9.1]], [[§C5b.1 Canonical Quantization of the Dirac Field#^rem-c5b-1-6|§C5b.1, Remark: Spin and statistics are an output]].

^sol-wq-15

### W16. The Dirac Hamiltonian: fermionic reordering and the zero-point energy

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-16]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-16-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-16-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-16-c]]

> [!success]- Solution
> **Answers.** (a) $E_0^{(\rm D)} = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} = -4E_0$: $-\frac12E_{\mathbf p}$ for each of the four modes per momentum; $:\!\hat H\!: = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^{s\dagger}\hat a^s + \hat b^{s\dagger}\hat b^s) \ge 0$. (b) $E(\hat c^\dagger\hat c - \frac12) = \frac E2[\hat c^\dagger, \hat c]$, ground-state energy $-\frac E2$; the boson is $\frac\omega2\{\hat a^\dagger, \hat a\}$ with $+\frac\omega2$. (c) $[\hat H, \hat b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$, $[\hat H, \hat a^s_{\mathbf p}] = -E_{\mathbf p}\hat a^s_{\mathbf p}$; the phases follow; $\hat H$ and $:\!\hat H\!:$ give the same, since they differ by a c-number.
>
> **(a) Step 1** (reorder with the anticommutator). $\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p} = -\hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p} + \{\hat b^s_{\mathbf p}, \hat b^{s\dagger}_{\mathbf p}\} = -\hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p} + (2\pi)^3\delta^3(\mathbf 0)$, so $-\hat b^s\hat b^{s\dagger} = +\hat b^{s\dagger}\hat b^s - (2\pi)^3\delta^3(\mathbf 0)$: the minus sign of W15(a) (from the eigenvalue $-E_{\mathbf p}$ of the negative-frequency spinor) is turned into a plus by the reordering sign. Two minus signs make a plus.
>
> **Step 2** (collect). $\hat H = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}) + E_0^{(\rm D)}$ with
>
> $$
> E_0^{(\rm D)} = -\sum_{s=1,2}\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(2\pi)^3\delta^3(\mathbf 0) = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} = -4\cdot V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2 = -4E_0 .
> $$
>
> In a box with cutoff, $E_0^{(\rm D)}(V, \Lambda) = -2\sum_{\lvert\mathbf k\rvert<\Lambda}E_{\mathbf k}$, density $\approx -\Lambda^4/4\pi^2$: four times the scalar's, with the opposite sign.
>
> **Step 3** (normal order). With the fermionic rule, $:\!\hat a^\dagger\hat a\!: = \hat a^\dagger\hat a$ and $:\!-\hat b\hat b^\dagger\!: = +\hat b^\dagger\hat b$ (one exchange, one sign), so $:\!\hat H\!:$ is the operator part. Every term ends in an annihilator, $:\!\hat H\!:\lvert0\rangle = 0$, and $\langle\Psi|:\!\hat H\!:|\Psi\rangle = \sum_s\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}\bigl(\lVert\hat a^s_{\mathbf p}\Psi\rVert^2 + \lVert\hat b^s_{\mathbf p}\Psi\rVert^2\bigr) \ge 0$. Both species carry positive energy $E_{\mathbf p}$ per quantum.
>
> **(b)** In the box (after rescaling by $V$, $\{\hat c, \hat c^\dagger\} = 1$ per mode), $\hat H = \sum_{\mathbf k,s}E_{\mathbf k}(\hat a^\dagger\hat a - \hat b\hat b^\dagger)$ and $-\hat b\hat b^\dagger = \hat b^\dagger\hat b - 1$. Writing $\hat c^\dagger\hat c = \frac12[\hat c^\dagger, \hat c] + \frac12\{\hat c, \hat c^\dagger\} = \frac12[\hat c^\dagger, \hat c] + \frac12$, $\hat H = \sum E_{\mathbf k}\bigl[(\hat a^\dagger\hat a - \frac12) + (\hat b^\dagger\hat b - \frac12)\bigr] + \sum E_{\mathbf k}(\frac12 + \frac12 - 1)$, the last sum zero. So each of the four modes per momentum (two spins, two species) is a fermionic oscillator $E(\hat c^\dagger\hat c - \frac12) = \frac E2[\hat c^\dagger, \hat c]$, with eigenvalues $\pm\frac E2$ for $\hat c^\dagger\hat c = 1, 0$: ground-state energy $-\frac E2$. The bosonic oscillator is $\omega(\hat a^\dagger\hat a + \frac12) = \frac\omega2\{\hat a^\dagger, \hat a\}$, ground-state energy $+\frac\omega2$: the sign of the zero-point energy is the sign that turns $\{\cdot, \cdot\}$ into $[\cdot, \cdot]$.
>
> **(c) Step 1** (the identity). $A\{B, C\} - \{A, C\}B = ABC + ACB - ACB - CAB = [AB, C]$.
>
> **Step 2** ($\hat b^\dagger$). $[\hat b^{r\dagger}_{\mathbf q}\hat b^r_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}] = \hat b^{r\dagger}_{\mathbf q}\{\hat b^r_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}\} - \{\hat b^{r\dagger}_{\mathbf q}, \hat b^{s\dagger}_{\mathbf p}\}\hat b^r_{\mathbf q} = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\hat b^{r\dagger}_{\mathbf q}$; the $\hat a$ part gives zero (mixed anticommutators vanish). Integrating against $E_{\mathbf q}$ and summing over $r$: $[\hat H, \hat b^{s\dagger}_{\mathbf p}] = E_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}$. The bilinear $\hat H$ has an ordinary commutator with each mode operator although the modes anticommute.
>
> **Step 3** ($\hat a$). $[\hat a^{r\dagger}_{\mathbf q}\hat a^r_{\mathbf q}, \hat a^s_{\mathbf p}] = \hat a^{r\dagger}_{\mathbf q}\{\hat a^r_{\mathbf q}, \hat a^s_{\mathbf p}\} - \{\hat a^{r\dagger}_{\mathbf q}, \hat a^s_{\mathbf p}\}\hat a^r_{\mathbf q} = -(2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\hat a^r_{\mathbf q}$, so $[\hat H, \hat a^s_{\mathbf p}] = -E_{\mathbf p}\hat a^s_{\mathbf p}$.
>
> **Step 4** (time dependence). $F(t) \equiv e^{i\hat Ht}\hat a^s_{\mathbf p}e^{-i\hat Ht}$ has $F'(t) = e^{i\hat Ht}\,i[\hat H, \hat a^s_{\mathbf p}]\,e^{-i\hat Ht} = -iE_{\mathbf p}F(t)$ and $F(0) = \hat a^s_{\mathbf p}$, so $F(t) = \hat a^s_{\mathbf p}e^{-iE_{\mathbf p}t}$; likewise $G(t) = e^{i\hat Ht}\hat b^{s\dagger}_{\mathbf p}e^{-i\hat Ht}$ has $G' = +iE_{\mathbf p}G$ and $G(t) = \hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$. Inserted into the $t = 0$ field, $e^{-iE_{\mathbf p}t}e^{i\mathbf p\cdot\mathbf x} = e^{-ip\cdot x}$ and $e^{iE_{\mathbf p}t}e^{-i\mathbf p\cdot\mathbf x} = e^{ip\cdot x}$: the Heisenberg field is the covariant expansion of W13. Both $\hat a^\dagger$ and $\hat b^\dagger$ add $+E_{\mathbf p}$, which is why the time dependence taken from the classical solutions agrees with the one generated by $\hat H$.
>
> **Step 5.** $\hat H - :\!\hat H\!: = E_0^{(\rm D)}$ is a c-number: it drops out of every commutator and cancels between $e^{i\hat Ht}$ and $e^{-i\hat Ht}$. It does not matter which is used.
>
> *Checked against:* (a) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-5|Theorem §C5b.3.5]] and [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-5|Derivation §C5b.3.5]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^rem-c5b-3-1|§C5b.3, Remark: Two minus signs make a plus]]; (b) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-6|Derivation §C5b.3.6]] (step 2, the same mode-by-mode decomposition); (c) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-8|Theorem §C5b.3.8]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]] and [[§C5b.6 The Heisenberg Dirac Field#^der-c5b-6-1|Derivation §C5b.6.1]] (steps 1–3).

^sol-wq-16

### W17. Momentum and charge in modes

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-17]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-17-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-17-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-17-c]]

> [!success]- Solution
> **Answers.** (a) Before ordering $\int d^3x\,\hat\psi^\dagger\hat\psi = \sum_s\int\frac{d^3p}{(2\pi)^3}(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p})$, and $:\!\hat b\hat b^\dagger\!: = -\hat b^\dagger\hat b$ gives PS (3.113). (b) Before ordering $\sum_s\int\frac{d^3p}{(2\pi)^3}\mathbf p(\hat a^{s\dagger}\hat a^s - \hat b^s\hat b^{s\dagger})$; normal ordered, $+\mathbf p\,\hat b^{s\dagger}\hat b^s$. (c) $\hat Q$: $+2V\int\frac{d^3p}{(2\pi)^3}$, a positive infinite vacuum charge (the complex scalar's is negative, $-\frac12V\int\frac{d^3p}{(2\pi)^3}$); $\hat{\mathbf P}$: $-2V\int\frac{d^3p}{(2\pi)^3}\mathbf p = 0$.
>
> **(a) Step 1** ($t = 0$). $\hat Q$ is conserved, so evaluate it at $t = 0$ with the relabelled expansions of W14(c), Step 1 (variables $\mathbf p$, $s$ in $\hat\psi$; $\mathbf p'$, $r$ in $\hat\psi^\dagger$), expanding inside the colons and applying them at the end.
>
> **Step 2** ($d^3x$). $\int d^3x\,e^{-i\mathbf p'\cdot\mathbf x}e^{i\mathbf p\cdot\mathbf x} = (2\pi)^3\delta^3(\mathbf p - \mathbf p')$ sets $\mathbf p' = \mathbf p$, cancels one $(2\pi)^3$ and leaves $1/2E_{\mathbf p}$:
>
> $$
> \hat Q = \int\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\mathbf p}}\sum_{r,s}:\!\bigl(\hat a^{r\dagger}_{\mathbf p}u^{r\dagger}(p) + \hat b^r_{-\mathbf p}v^{r\dagger}(\tilde p)\bigr)\bigl(\hat a^s_{\mathbf p}u^s(p) + \hat b^{s\dagger}_{-\mathbf p}v^s(\tilde p)\bigr)\!: .
> $$
>
> **Step 3** (four terms and the spinor products). $u^{r\dagger}(p)u^s(p)\,\hat a^{r\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + u^{r\dagger}(p)v^s(\tilde p)\,\hat a^{r\dagger}_{\mathbf p}\hat b^{s\dagger}_{-\mathbf p} + v^{r\dagger}(\tilde p)u^s(p)\,\hat b^r_{-\mathbf p}\hat a^s_{\mathbf p} + v^{r\dagger}(\tilde p)v^s(\tilde p)\,\hat b^r_{-\mathbf p}\hat b^{s\dagger}_{-\mathbf p}$. The cross terms vanish: $u^{r\dagger}(p)v^s(\tilde p) = v^{r\dagger}(\tilde p)u^s(p) = 0$ (orthogonality at opposite three-momenta, needed because the $d^3x$ integral paired $\mathbf p$ with $-\mathbf p$). The diagonal products are $2E_{\mathbf p}\delta^{rs}$ ($E_{-\mathbf p} = E_{\mathbf p}$), which cancel the $1/2E_{\mathbf p}$ and one spin sum:
>
> $$
> \hat Q = \sum_s\int\frac{d^3p}{(2\pi)^3}:\!\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^s_{-\mathbf p}\hat b^{s\dagger}_{-\mathbf p}\bigr)\!: = \sum_s\int\frac{d^3p}{(2\pi)^3}:\!\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\bigr)\!: ,
> $$
>
> after $\mathbf p \to -\mathbf p$ in the $\hat b$ term. Where $\hat H$ had a relative minus sign (W15(a)), $\hat Q$ has a plus: the positive density $\psi^\dagger\psi$.
>
> **Step 4** (fermionic normal ordering). $:\!\hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p}\!: = -\hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}$ (one exchange of two fermion operators):
>
> $$
> \hat Q = \int\frac{d^3p}{(2\pi)^3}\sum_s\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr) = \hat N_a - \hat N_b ,
> $$
>
> PS eq. (3.113). (At general $t$ the cross terms carry $e^{\pm2iE_{\mathbf p}t}$ and vanish by the same orthogonality.)
>
> **(b) Step 1** (gradient). In the relabelled $t = 0$ form both terms of $\hat\psi$ carry $e^{i\mathbf p\cdot\mathbf x}$, and $-i\nabla e^{i\mathbf p\cdot\mathbf x} = \mathbf p\,e^{i\mathbf p\cdot\mathbf x}$: $(-i\nabla)\hat\psi$ is $\hat\psi$ with an extra factor $\mathbf p$ under the integral.
>
> **Step 2** (as in (a)). Steps 2–3 of (a) with this factor: $\hat{\mathbf P} = \sum_s\int\frac{d^3p}{(2\pi)^3}\mathbf p:\!(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^s_{-\mathbf p}\hat b^{s\dagger}_{-\mathbf p})\!:$, the cross terms again killed by $u^\dagger(p)v(\tilde p) = 0$. Relabelling $\mathbf p \to -\mathbf p$ in the $\hat b$ term now flips the sign of the factor: $\sum_s\int\frac{d^3p}{(2\pi)^3}\mathbf p:\!(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} - \hat b^s_{\mathbf p}\hat b^{s\dagger}_{\mathbf p})\!:$. (In the time-dependent form the same minus sign comes from $-i\nabla e^{iq\cdot x} = -\mathbf q\,e^{iq\cdot x}$ on the negative-frequency modes.)
>
> **Step 3** (normal order). $:\!-\hat b\hat b^\dagger\!: = +\hat b^\dagger\hat b$:
>
> $$
> \hat{\mathbf P} = \sum_s\int\frac{d^3p}{(2\pi)^3}\,\mathbf p\,\bigl(\hat a^{s\dagger}_{\mathbf p}\hat a^s_{\mathbf p} + \hat b^{s\dagger}_{\mathbf p}\hat b^s_{\mathbf p}\bigr) :
> $$
>
> fermions and antifermions of label $\mathbf p$ both carry momentum $\mathbf p$, the antifermion because of the relabelling that names $\hat b^{s\dagger}_{\mathbf p}$.
>
> **(c) Step 1** ($\hat Q$). Without colons, $\hat b^s\hat b^{s\dagger} = -\hat b^{s\dagger}\hat b^s + (2\pi)^3\delta^3(\mathbf 0)$ in Step 3 of (a) gives $\int\hat\psi^\dagger\hat\psi = \hat N_a - \hat N_b + 2V\int\frac{d^3p}{(2\pi)^3}$ (two spins), in the box $+2\mathcal N(V, \Lambda)$: a positive infinite vacuum charge. The complex scalar's unordered $\hat Q$ had $-\frac12V\int\frac{d^3p}{(2\pi)^3}$ (W10(e)): opposite sign, because there the reordering used a commutator and the $\hat b\hat b^\dagger$ term entered with a minus sign. In both cases an observable vacuum charge, so the order is forced by physics; for the Dirac field the antisymmetrized density $\frac12[\hat\psi^\dagger_a, \hat\psi_a]$ removes it too.
>
> **Step 2** ($\hat{\mathbf P}$). The same reordering in (b) leaves $-\sum_s\int\frac{d^3p}{(2\pi)^3}\mathbf p(2\pi)^3\delta^3(\mathbf 0) = -2V\int\frac{d^3p}{(2\pi)^3}\mathbf p$, an odd integrand: zero for a rotation-invariant cutoff ($\mathbf k$ and $-\mathbf k$ pair off in the box). $\hat{\mathbf P}$ needs no ordering prescription, as for the scalar (W6(b)).
>
> *Checked against:* (a) the submitted solution of PS6.2 as written ($t = 0$, $\tilde p$ for the flipped momentum, spinor products from PS (3.61), (3.67), $:\!\hat b\hat b^\dagger\!: = -\hat b^\dagger\hat b$ dropping $(2\pi)^3\delta^3(\mathbf 0)$), [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-1|Theorem §C5b.5.1]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-1|Derivation §C5b.5.1]] (which records that the two routes agree term by term), [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-3|Derivation §C5b.5.3]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]]; (b) [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]] and [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-7|Derivation §C5b.3.7]] (time-dependent route; the $t = 0$ route here gives the same unordered form); (c) [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-3|Derivation §C5b.5.3]] (step 2), [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-1|§C5b.5, Remark: The vacuum charge, and why the order is forced]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^der-c5b-3-7|Derivation §C5b.3.7]] (step 3).

^sol-wq-17

### W18. Charges of states and fields; translations

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-18]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-18-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-18-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-18-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-18-d]]

> [!success]- Solution
> **Answers.** (a) $[\hat Q, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{s\dagger}_{\mathbf p}$, $[\hat Q, \hat b^{s\dagger}_{\mathbf p}] = -\hat b^{s\dagger}_{\mathbf p}$; charges $+1$, $-1$, $0$. (b) $\hat\psi$ contains $\hat a$ and $\hat b^\dagger$, both lowering $\hat Q$ by one; $e^{i\alpha\hat Q}\hat\psi e^{-i\alpha\hat Q} = e^{-i\alpha}\hat\psi$; $\hat\psi$ destroys a particle or creates an antiparticle, both of which lower the charge by one unit. (c) $\int d^3x\,:\!\hat j^0_{\rm N}\!: = -\hat Q = \hat N_b - \hat N_a$. (d) $[\hat\psi_a(\mathbf x), \hat P^k] = -i\int d^3y\,\delta_{ab}\delta^3(\mathbf x - \mathbf y)\partial_k\hat\psi_b(\mathbf y) = -i\partial_k\hat\psi_a(\mathbf x)$.
>
> **(a) Step 1** (one density). With $[AB, C] = A\{B, C\} - \{A, C\}B$ (W16(c)): $[\hat a^{r\dagger}_{\mathbf q}\hat a^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{r\dagger}_{\mathbf q}\{\hat a^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\} - \{\hat a^{r\dagger}_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\}\hat a^r_{\mathbf q} = (2\pi)^3\delta^{rs}\delta^3(\mathbf q - \mathbf p)\hat a^{r\dagger}_{\mathbf q}$, and $[\hat b^{r\dagger}_{\mathbf q}\hat b^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}] = \hat b^{r\dagger}_{\mathbf q}\{\hat b^r_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\} - \{\hat b^{r\dagger}_{\mathbf q}, \hat a^{s\dagger}_{\mathbf p}\}\hat b^r_{\mathbf q} = 0$.
>
> **Step 2** (weights). $\hat Q = \sum_r\int\frac{d^3q}{(2\pi)^3}(\hat a^{r\dagger}_{\mathbf q}\hat a^r_{\mathbf q} - \hat b^{r\dagger}_{\mathbf q}\hat b^r_{\mathbf q})$; integrating the delta, $[\hat Q, \hat a^{s\dagger}_{\mathbf p}] = \hat a^{s\dagger}_{\mathbf p}$, and the same computation for $\hat b^\dagger$ with weight $-1$ gives $[\hat Q, \hat b^{s\dagger}_{\mathbf p}] = -\hat b^{s\dagger}_{\mathbf p}$. The unordered $\hat Q$ differs by a c-number and gives the same commutators.
>
> **Step 3** (states). $\hat Q\lvert0\rangle = 0$; $\hat Q\hat a^{s\dagger}_{\mathbf p}\lvert0\rangle = [\hat Q, \hat a^{s\dagger}_{\mathbf p}]\lvert0\rangle = \hat a^{s\dagger}_{\mathbf p}\lvert0\rangle$, so $\hat Q\lvert\mathbf p, s\rangle = +\lvert\mathbf p, s\rangle$; likewise $\hat Q\lvert\mathbf p, s\rangle^c = -\lvert\mathbf p, s\rangle^c$; and pushing $\hat Q$ through both creators, $\hat a^{r\dagger}_{\mathbf p}\hat b^{s\dagger}_{\mathbf q}\lvert0\rangle$ has charge $1 - 1 = 0$.
>
> **(b) Step 1** (annihilators). $\hat Q$ is Hermitian: $[\hat Q, \hat a^\dagger]^\dagger = -[\hat Q, \hat a]$, so $[\hat Q, \hat a^s_{\mathbf p}] = -\hat a^s_{\mathbf p}$ and $[\hat Q, \hat b^s_{\mathbf p}] = +\hat b^s_{\mathbf p}$.
>
> **Step 2** (fields). $\hat Q$ commutes with the c-number spinors and exponentials, so term by term $[\hat Q, \hat\psi] = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\sum_s\bigl(-\hat a^s_{\mathbf p}u^se^{-ip\cdot x} - \hat b^{s\dagger}_{\mathbf p}v^se^{ip\cdot x}\bigr) = -\hat\psi$; $\hat{\bar\psi}$ contains $\hat b$ and $\hat a^\dagger$, both raising $\hat Q$: $[\hat Q, \hat{\bar\psi}] = +\hat{\bar\psi}$.
>
> **Step 3** (finite rotation). $F(\alpha) = e^{i\alpha\hat Q}\hat\psi e^{-i\alpha\hat Q}$ has $F' = e^{i\alpha\hat Q}i[\hat Q, \hat\psi]e^{-i\alpha\hat Q} = -iF$, $F(0) = \hat\psi$: $F(\alpha) = e^{-i\alpha}\hat\psi$. The pairing of $\hat a$ with $\hat b^\dagger$ in $\hat\psi$ is a pairing by charge, not by energy: destroying a particle releases energy, creating an antiparticle costs it, and both lower $\hat Q$ by one.
>
> **(c)** In the course's recipe $j^\mu_{\rm N} = \frac{\partial\mathcal L}{\partial(\partial_\mu\psi)}\Delta\psi = \bar\psi i\gamma^\mu(i\psi) = -\bar\psi\gamma^\mu\psi$ ($\bar\psi$ has no derivative in $\mathcal L$, $\mathcal J = 0$). So $\int d^3x\,:\!\hat j^0_{\rm N}\!: = -\int d^3x\,:\!\hat\psi^\dagger\hat\psi\!: = -\hat Q = \hat N_b - \hat N_a$: the Noether sign counts particles negative, as for the complex scalar, whose $\int:\!\hat j^0\!: = \hat N_b - \hat N_a = -2\hat Q$ (W10(d)). The Dirac charge $\hat Q = \int:\!\hat\psi^\dagger\hat\psi\!:$ has no factor $\frac12$: one unit per quantum.
>
> **(d) Step 1** (identity). $[A, BC] = \{A, B\}C - B\{A, C\}$: expand, $ABC + BAC - BAC - BCA = ABC - BCA$.
>
> **Step 2.** All fields at one time; $\hat P^k = -i\int d^3y\,\hat\psi^\dagger_b(\mathbf y)\partial^y_k\hat\psi_b(\mathbf y)$. With $A = \hat\psi_a(\mathbf x)$, $B = \hat\psi^\dagger_b(\mathbf y)$, $C = \partial^y_k\hat\psi_b(\mathbf y)$: $\{A, B\} = \delta_{ab}\delta^3(\mathbf x - \mathbf y)$ and $\{A, C\} = \partial^y_k\{\hat\psi_a(\mathbf x), \hat\psi_b(\mathbf y)\} = 0$ (it vanishes for all $\mathbf y$). So $[\hat\psi_a(\mathbf x), \hat P^k] = -i\int d^3y\,\delta_{ab}\delta^3(\mathbf x - \mathbf y)\partial^y_k\hat\psi_b(\mathbf y) = -i\partial_k\hat\psi_a(\mathbf x)$: a commutator although the fields anticommute, because $\hat{\mathbf P}$ is bilinear. With $\partial^k = -\partial_k$ it is $[\hat\psi_a, \hat P^k] = i\partial^k\hat\psi_a$, the space part of $[\hat\psi, \hat P^\mu] = i\partial^\mu\hat\psi$, and $e^{i\mathbf a\cdot\hat{\mathbf P}}\hat\psi(\mathbf x)e^{-i\mathbf a\cdot\hat{\mathbf P}} = \hat\psi(\mathbf x - \mathbf a)$ to first order: the Noether momentum generates translations.
>
> *Checked against:* (a)–(b) [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]] and [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^der-c5b-5-4|Derivation §C5b.5.4]] (steps 1–7), [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-1|Theorem §C5b.4.1]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^rem-c5b-5-2|§C5b.5, Remark: Destroying a particle is not creating an antiparticle]]; (c) [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^def-c5b-5-1|Def. §C5b.5.1]], [[§C5a.8 Canonical Structure and Noether Currents of the Dirac Field#^thm-c5a-8-3|Theorem §C5a.8.3]], [[§C1b.6 Conserved Charges and Internal Symmetries#^cau-c1b-6-3|§C1b.6, Caution: Sign and normalization of the U(1) current]]; (d) [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-9|Theorem §C5b.1.9]] and [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-9|Derivation §C5b.1.9]] (steps 1–3, 5). *Derived here; check:* the finite rotation in (b), by the differential equation of W10(c), consistent with $\hat\psi \to e^{-i\alpha}\hat\psi$ lowering the charge.

^sol-wq-18

### W19. The physical spin of the antiparticle

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-19]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-19-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-19-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-19-c]]

> [!success]- Solution
> **Answers.** (a) $[\hat J_z, \hat a^{s\dagger}_{\mathbf 0}] = \frac{1}{2m}\sum_r\bigl(u^{r\dagger}(0)\frac12\Sigma^3u^s(0)\hat a^{r\dagger}_{\mathbf 0} + v^{r\dagger}(0)\frac12\Sigma^3u^s(0)e^{-2imt}\hat b^r_{\mathbf 0}\bigr)$, with $u^{r\dagger}\Sigma^3u^s = 2m\,\xi^{r\dagger}\sigma^3\xi^s$ and $v^{r\dagger}\Sigma^3u^s = 0$. (b) The operator $\hat\psi$ now stands to the right of the spinor: the term $-\{\hat\psi^\dagger, \hat b^\dagger\}M\hat\psi$ of the identity, and the order of the $\hat b$'s is reversed. (c) $\hat a^{1\dagger}_{\mathbf 0}\lvert0\rangle$: $+\frac12$, $\hat a^{2\dagger}_{\mathbf 0}\lvert0\rangle$: $-\frac12$; $\hat b^{s\dagger}_{\mathbf 0}\lvert0\rangle$ with $\eta^s = \xi^s$: $\mp\frac12$ (opposite to the label); with $\eta^s = \xi^{-s}$: $\pm\frac12$, the same physical spin as the particle.
>
> **(a) Step 1** (reduce to a commutator). $\hat J_z\lvert0\rangle = 0$, so $\hat J_z\hat a^{s\dagger}_{\mathbf 0}\lvert0\rangle = [\hat J_z, \hat a^{s\dagger}_{\mathbf 0}]\lvert0\rangle$. With $\hat J_z = \int d^3x\,\hat\psi^\dagger_aM_{ab}\hat\psi_b$, $M = (\mathbf x\times(-i\nabla))_z + \frac12\Sigma^3$, the identity $[AB, C] = A\{B, C\} - \{A, C\}B$ gives $[\hat\psi^\dagger_aM_{ab}\hat\psi_b, C] = \hat\psi^\dagger_aM_{ab}\{\hat\psi_b, C\} - \{\hat\psi^\dagger_a, C\}M_{ab}\hat\psi_b$ (the ordering constant commutes).
>
> **Step 2** (anticommutators). From the expansion and $\{\hat a^r_{\mathbf p}, \hat a^{s\dagger}_{\mathbf 0}\} = (2\pi)^3\delta^{rs}\delta^3(\mathbf p)$: $\{\hat\psi(x), \hat a^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}u^s(0)e^{-imt}$ ($E_{\mathbf 0} = m$), and $\{\hat\psi^\dagger(x), \hat a^{s\dagger}_{\mathbf 0}\} = 0$. So $[\hat J_z, \hat a^{s\dagger}_{\mathbf 0}] = \frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,\hat\psi^\dagger(x)Mu^s(0)$.
>
> **Step 3** (orbital part). $u^s(0)$ is constant in $\mathbf x$, so $(\mathbf x\times(-i\nabla))_zu^s(0) = 0$.
>
> **Step 4** (spin part). $\int d^3x\,\hat\psi^\dagger(x) = \frac{1}{\sqrt{2m}}\sum_r\bigl(\hat a^{r\dagger}_{\mathbf 0}u^{r\dagger}(0)e^{imt} + \hat b^r_{\mathbf 0}v^{r\dagger}(0)e^{-imt}\bigr)$ (the $d^3x$ integral gives $(2\pi)^3\delta^3(\mathbf p)$), hence the expression in the answer.
>
> **Step 5** (rest-frame spinors). $u^s(0) = \sqrt m(\xi^s, \xi^s)$, $v^s(0) = \sqrt m(\eta^s, -\eta^s)$, $\Sigma^3 = \mathrm{diag}(\sigma^3, \sigma^3)$: $u^{r\dagger}(0)\Sigma^3u^s(0) = m(\xi^{r\dagger}\sigma^3\xi^s + \xi^{r\dagger}\sigma^3\xi^s) = 2m\,\xi^{r\dagger}\sigma^3\xi^s$ and $v^{r\dagger}(0)\Sigma^3u^s(0) = m(\eta^{r\dagger}\sigma^3\xi^s - \eta^{r\dagger}\sigma^3\xi^s) = 0$. The $\hat b$ term drops identically, and $\hat J_z\hat a^{s\dagger}_{\mathbf 0}\lvert0\rangle = \sum_r(\xi^{r\dagger}\frac{\sigma^3}2\xi^s)\hat a^{r\dagger}_{\mathbf 0}\lvert0\rangle$.
>
> **(b) Step 1** (anticommutators). $\{\hat\psi(x), \hat b^{s\dagger}_{\mathbf 0}\} = 0$ and, from $\hat\psi^\dagger \ni \hat b^r_{\mathbf p}v^{r\dagger}(p)e^{-ip\cdot x}$, $\{\hat\psi^\dagger(x), \hat b^{s\dagger}_{\mathbf 0}\} = \frac{1}{\sqrt{2m}}v^{s\dagger}(0)e^{-imt}$. Only the second term of the identity survives: $[\hat J_z, \hat b^{s\dagger}_{\mathbf 0}] = -\frac{e^{-imt}}{\sqrt{2m}}\int d^3x\,v^{s\dagger}(0)M\hat\psi(x)$. This is the minus sign: the operator now stands on the right of the spinor.
>
> **Step 2** (orbital part). $\int d^3x\,v^{s\dagger}(0)(x\partial_y - y\partial_x)(-i)\hat\psi = 0$ by parts (fall-off), since $\partial_yx = \partial_xy = 0$.
>
> **Step 3** (spin part). $\int d^3x\,\hat\psi = \frac{1}{\sqrt{2m}}\sum_r\bigl(\hat a^r_{\mathbf 0}u^r(0)e^{-imt} + \hat b^{r\dagger}_{\mathbf 0}v^r(0)e^{imt}\bigr)$; on $\lvert0\rangle$ the $\hat a$ term gives zero. With $v^{s\dagger}(0)\Sigma^3v^r(0) = m(\eta^{s\dagger}\sigma^3\eta^r + \eta^{s\dagger}\sigma^3\eta^r) = 2m\,\eta^{s\dagger}\sigma^3\eta^r$ and the phases $e^{-imt}e^{imt} = 1$: $\hat J_z\hat b^{s\dagger}_{\mathbf 0}\lvert0\rangle = -\sum_r(\eta^{s\dagger}\frac{\sigma^3}2\eta^r)\hat b^{r\dagger}_{\mathbf 0}\lvert0\rangle$.
>
> **(c) Step 1** (particle). $\sigma^3\xi^1 = \xi^1$, $\sigma^3\xi^2 = -\xi^2$, so $\xi^{r\dagger}\frac{\sigma^3}2\xi^s = \pm\frac12\delta^{rs}$: $J_z = +\frac12$ for $s = 1$, $-\frac12$ for $s = 2$.
>
> **Step 2** ($\eta^s = \xi^s$). $\eta^{s\dagger}\frac{\sigma^3}2\eta^r = \pm\frac12\delta^{rs}$, so with the minus sign of (b) $\hat b^{1\dagger}_{\mathbf 0}\lvert0\rangle$ has $J_z = -\frac12$ and $\hat b^{2\dagger}_{\mathbf 0}\lvert0\rangle$ has $+\frac12$: opposite to the two-spinor (as a hole in a state of $J_z = +\frac12$ would).
>
> **Step 3** ($\eta^s = \xi^{-s}$). $\eta^1 = \xi^{-1} = \xi^2 = (0, 1)^{\mathsf T}$ and $\eta^2 = \xi^{-2} = -\xi^1 = (-1, 0)^{\mathsf T}$ (from $-i\sigma^2(\xi^s)^{\ast}$). Then $\eta^{1\dagger}\sigma^3\eta^1 = -1$, $\eta^{2\dagger}\sigma^3\eta^2 = +1$, off-diagonal zero: $\hat b^{1\dagger}_{\mathbf 0}\lvert0\rangle$ has $J_z = -(-\frac12) = +\frac12$ and $\hat b^{2\dagger}_{\mathbf 0}\lvert0\rangle$ has $-\frac12$. With the course's choice, $\hat a^{s\dagger}$ and $\hat b^{s\dagger}$ create particle and antiparticle with the same physical spin, although the antiparticle's wave-function spin is the opposite.
>
> *Checked against:* [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^thm-c5b-4-3|Theorem §C5b.4.3]] and [[§C5b.4 Fermions, Fock Space and the Pauli Principle#^der-c5b-4-3|Derivation §C5b.4.3]] (steps 1–6, the same anticommutators, the minus sign and the rest-frame products); [[§C5a.9 Plane-Wave Solutions#^thm-c5a-9-3|Theorem §C5a.9.3]]; [[§C9.5 Charge Conjugation on Oscillators and Spinors#^def-c9-5-5|Def. §C9.5.5]]; [[§C9.7 Physical Spin versus Wave-Function Spin#^thm-c9-7-3|Theorem §C9.7.3]].

^sol-wq-19

## All fields

### W20. Short response: quantization in modes

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-a]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-b]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-c]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-d]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-e]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-f]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-g]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-h]]

![[PHY 513 Worksheet — Canonical Quantization in Modes#^wq-20-i]]

> [!success]- Answers
> 1. (a) $(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $\sqrt{2E_{\mathbf p}}$; $2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p - \mathbf q)$; $\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}$. [[§C2a.2 Mode Expansion and the Mode Algebra#^thm-c2a-2-6|Theorem §C2a.2.6]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-1|Def. §C2a.4.1]], [[§C2a.4 Particles and Relativistic Normalization#^def-c2a-4-2|Def. §C2a.4.2]].
> 2. (b) $\pi = \dot\phi$; $\pi = \dot\phi^{\ast}$ (the velocity of the conjugate field); $\pi_\psi = i\psi^\dagger$. [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-2|Theorem §C1b.4.2]], [[§C1b.4 Hamiltonian Field Theory#^thm-c1b-4-3|Theorem §C1b.4.3]], [[§C5b.1 Canonical Quantization of the Dirac Field#^thm-c5b-1-1|Theorem §C5b.1.1]].
> 3. (c) $\hat a^\dagger_{\mathbf q}\hat a_{\mathbf p}$; $-\hat b^{s\dagger}_{\mathbf q}\hat b^r_{\mathbf p}$. [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^def-c2a-3-1|Def. §C2a.3.1]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^def-c5b-3-1|Def. §C5b.3.1]].
> 4. (d) $E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{E_{\mathbf p}}2$; $2E_0$; $E_0^{(\rm D)} = -2V\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p} = -4E_0$. [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^thm-c2a-3-4|Theorem §C2a.3.4]], [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-4|Theorem §C2a.5.4]], [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-6|Theorem §C5b.3.6]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^cau-c2a-3-1|§C2a.3, Caution: Names for the zero-point energy]].
> 5. (e) Complex scalar: $\frac12(\hat N_a - \hat N_b)$, charge $-\frac12$; Dirac: $\hat N_a - \hat N_b$, charge $-1$. [[§C2a.5 The Complex Scalar Field and Its Charge#^thm-c2a-5-6|Theorem §C2a.5.6]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-3|Theorem §C5b.5.3]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]].
> 6. (f) $-i\nabla\hat\phi(\mathbf x)$; $-\hat\psi$; $\hat b^{s\dagger}_{\mathbf p}e^{iE_{\mathbf p}t}$. [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-5|Derivation §C2a.3.5]], [[§C3.5 Covariant Quantum Fields and the Free Scalar's Representation#^thm-c3-5-6|Theorem §C3.5.6]], [[§C5b.5 The U(1) Charge, Particles and Antiparticles#^thm-c5b-5-4|Theorem §C5b.5.4]], [[§C5b.6 The Heisenberg Dirac Field#^thm-c5b-6-1|Theorem §C5b.6.1]].
> 7. (g) $+\mathbf p$; $v^s(p)\,e^{ip\cdot x}$. [[§C5b.3 Energy, Momentum and the Zero-Point Energy#^thm-c5b-3-7|Theorem §C5b.3.7]], [[§C5b.2 Mode Expansion and the Anticommutator Algebra#^thm-c5b-2-1|Theorem §C5b.2.1]].
> 8. (h) $(\gamma^0)_{ab}\delta^3(\mathbf x - \mathbf y)$; $0$ (orthogonality at opposite three-momenta). [[§C5b.1 Canonical Quantization of the Dirac Field#^der-c5b-1-1|Derivation §C5b.1.1]], [[§C5a.10 Normalization, Spin Sums and Helicity#^thm-c5a-10-6|Theorem §C5a.10.6]].
> 9. (i) $\hat a_{\mathbf p}\hat a_{-\mathbf p}$ and $\hat a^\dagger_{-\mathbf p}\hat a^\dagger_{\mathbf p}$ in both; in $\hat H$ the mass shell $\mathbf p^2 + m^2 = E_{\mathbf p}^2$ cancels them, in $\hat{\mathbf P}$ they are odd in $\mathbf p$ and vanish because $[\hat a_{\mathbf p}, \hat a_{-\mathbf p}] = 0$. [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-1|Derivation §C2a.3.1]], [[§C2a.3 Energy, Momentum and the Zero-Point Energy#^der-c2a-3-5|Derivation §C2a.3.5]].
>
> *Checked against:* the boxes named in each line.

^sol-wq-20
