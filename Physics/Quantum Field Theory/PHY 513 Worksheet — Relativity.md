---
type: review
subject: "[[Quantum Field Theory]]"
tags: [quantum-field-theory, phy513, review]
---
↑ [[Quantum Field Theory]] · [[PHY 513 Midterm Review|Midterm Review]] · [[PHY 513 Worksheet — Relativity (Solutions)|Solutions]] · [[PHY 513 Practice Midterm|Practice Midterm]] · [[PHY 513 PS Drill|PS Drill]]

# PHY 513 Worksheet — Relativity

Special relativity as the course uses it, in twenty homework-sized problems for the midterm (Fri Oct 16). The problems follow the lectures: Lecture 1 (Aug 31: the Lorentz group, rapidity, index notation, the Levi-Civita symbol, invariants and kinematics, derivatives with four-vectors, electrodynamics; §C1a.4–§C1a.7 and Problem Set 1), Lecture 2 (Sep 2: natural units, causality; §C1a.2–§C1a.3), Lecture 7 (Sep 23: generators, the algebra, finite transformations, the labels $(j_+, j_-)$, how fields transform; §C1a.6, §C3.2–§C3.3, §CB.5–§CB.6), and a short-response problem in the format of Problem Set 7, Problem 1. The grey line under each problem or part says where it comes from: *[HW-literal PSk.n(x)]* a homework part as it stood, *[variation of …]* the same computation on an object the book or the homework does not work out, *[extension of …]* one step further, *[new]* a problem built from the lectures. Problem Set 1, Problem 5(e)–(f) and all of Problem 6 (marked "skipped for now, to be redone" in [[PHY 513 PS Drill]]) are here as they stood: Problems 6, 8 and 9. Solutions, each checked against its home box: [[PHY 513 Worksheet — Relativity (Solutions)]]. Printable copies: `~/Downloads/PHY513_worksheet_relativity.pdf` and `~/Downloads/PHY513_worksheet_relativity_solutions.pdf`.

**Conventions** (the course's, [[Larsen PHY 513]]): $\hbar = c = 1$; $g = \operatorname{diag}(+1, -1, -1, -1)$; $\varepsilon^{0123} = +1$; $\Lambda$ acts **actively** ($x \mapsto \Lambda x$ moves the object); $\Lambda = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ with $(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$; $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$; rapidity $\eta$ with $\tanh\eta = v$, $\cosh\eta = \gamma$, $\sinh\eta = \gamma v$; $B_x(\eta)$, $B_y(\eta)$, $B_z(\eta)$ the active boosts and $R_x(\theta)$, $R_y(\theta)$, $R_z(\theta)$ the active rotations (counterclockwise seen from the tip of the axis); $\mathcal P = \operatorname{diag}(1, -1, -1, -1)$, $\mathcal T = \operatorname{diag}(-1, 1, 1, 1)$; $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ with $F^{0i} = -E^i$, $F^{ij} = -\varepsilon_{ijk}B^k$ (Heaviside–Lorentz).

---

## Lecture 1. The Lorentz group, tensors and electrodynamics

### Problem 1. The defining condition and the four components

A Lorentz transformation is a real $4\times4$ matrix $\Lambda = [\Lambda^\mu{}_\nu]$ with $\Lambda^{\mathsf T}g\Lambda = g$.
*[extension of PS1.3 (its preamble)]*

^wr-1

(a) Write $\Lambda^{\mathsf T}g\Lambda = g$ in index form. From its $00$ component derive $(\Lambda^0{}_0)^2 = 1 + \sum_i(\Lambda^i{}_0)^2$, and from its determinant derive $\det\Lambda = \pm1$.

^wr-1-a

(b) Show that $(\Lambda^{-1})^\mu{}_\nu = \Lambda_\nu{}^\mu \equiv g_{\nu\rho}\Lambda^\rho{}_\sigma g^{\sigma\mu}$. Check it on the boost $B_z(\eta)$: which matrix is $\Lambda_\nu{}^\mu$?

^wr-1-b

(c) Give $(\det\Lambda, \operatorname{sgn}\Lambda^0{}_0)$, and name the component of $O(1,3)$, for $\mathcal P$, $\mathcal T$, $\mathcal P\mathcal T$ and $B_z(\eta)R_z(\theta)$. Which of these four can be written as $\exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$? Why is $SO(1,3) = \{\Lambda : \det\Lambda = 1\}$ not the group meant by "Lorentz invariant"?

^wr-1-c

### Problem 2. Rapidity

The active boost $B_z(\eta)$ acts on $(t, z)$ as $\begin{pmatrix}\cosh\eta & \sinh\eta\\ \sinh\eta & \cosh\eta\end{pmatrix}$ and as the identity on $(x, y)$; it gives a particle at rest the velocity $v = \tanh\eta$ along $+z$.
*[new]*

^wr-2

(a) Show $B_z(\eta_1)B_z(\eta_2) = B_z(\eta_1 + \eta_2)$, and derive from it the addition law of collinear velocities. A particle moving with $v_1 = 0.6$ along $z$ is boosted by $B_z(\eta_2)$ with $\tanh\eta_2 = 0.8$: what is its final velocity?

^wr-2-a

(b) In the light-cone coordinates $x^\pm = t \pm z$, show that $B_z(\eta)$ acts as $x^\pm \mapsto e^{\pm\eta}x^\pm$. What are the eigenvalues and eigenvectors of $B_z(\eta)$ on the $(t, z)$ plane, and why does this make the invariance of $t^2 - z^2$ obvious?

^wr-2-b

(c) The rapidity of a particle with four-momentum $p = (E, p_x, p_y, p_z)$ is $y = \frac12\ln\frac{E + p_z}{E - p_z}$. Show $\tanh y = p_z/E$; show that $B_z(\eta)$ sends $y \mapsto y + \eta$ and leaves $p_x$, $p_y$ unchanged; conclude that differences of rapidities along $z$ are boost invariant. Give $y$ for $E = 5$, $p_z = 4$, $p_x = p_y = 0$.

^wr-2-c

### Problem 3. Index placement and covariance

Decide whether each expression or equation is legal. If it is, give the tensor type of its free indices (scalar, vector, covector, $(2,0)$ tensor, …); if it is not, repair it with the metric, changing as little as possible.
*[variation of PS1.1 and PS1.2(b)]*

^wr-3

(a) $\partial_\mu F^{\mu\nu} = J_\nu$.

^wr-3-a

(b) $\varepsilon^{\mu\alpha\beta\gamma}p_\mu F_{\alpha\beta}\,q^\nu$. Is it a tensor or a pseudotensor?

^wr-3-b

(c) $T^{\mu\nu}{}_\nu = S_\mu$.

^wr-3-c

(d) $\Lambda^\mu{}_\nu\,\Lambda_\mu{}^\rho = \delta_\nu{}^\rho$. If legal, is it true?

^wr-3-d

(e) $\partial_\mu\phi\,\partial_\mu\phi$. What is it in terms of $\partial_t\phi$ and $\nabla\phi$?

^wr-3-e

(f) Place indices on $B$ so that $A^\mu{}_\nu\,g^{\nu\rho}\,C_{\rho\sigma}\,D^{\sigma\lambda} = B$ is covariant, and write the left-hand side as a product of matrices.

^wr-3-f

(g) Why does "the same free indices at the same heights on both sides" guarantee that an equation true in one frame is true in every frame?

^wr-3-g

### Problem 4. Symmetric meets antisymmetric

$S^{\mu\nu}$ is symmetric, $A_{\mu\nu}$ antisymmetric; $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ and $\tilde F^{\mu\nu} = \frac12\varepsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$.
*[extension of PS1.2(d)]*

^wr-4

(a) Show $S^{\mu\nu}A_{\mu\nu} = 0$.

^wr-4-a

(b) Use (a) to show that $\partial_\mu F^{\mu\nu} = J^\nu$ can hold only if $\partial_\nu J^\nu = 0$.

^wr-4-b

(c) Show $\tilde F^{\mu\nu} = \varepsilon^{\mu\nu\rho\sigma}\partial_\rho A_\sigma$, and that $\partial_\mu\tilde F^{\mu\nu} = 0$ holds identically.

^wr-4-c

(d) For an arbitrary two-tensor $T^{\mu\nu}$, show $T^{\mu\nu}F_{\mu\nu} = T^{[\mu\nu]}F_{\mu\nu}$ with $T^{[\mu\nu]} = \frac12(T^{\mu\nu} - T^{\nu\mu})$, and evaluate $F^\mu{}_\mu$ and $F^{\mu\nu}F_{\nu\mu}$ in terms of $F_{\mu\nu}F^{\mu\nu}$.

^wr-4-d

### Problem 5. The Levi-Civita symbol

$\varepsilon^{\mu\nu\rho\sigma}$ is totally antisymmetric with $\varepsilon^{0123} = +1$ (the course's sign; Peskin–Schroeder use $-1$).

^wr-5

(a) Give $\varepsilon^{3012}$, $\varepsilon^{3210}$, $\varepsilon^{0213}$, $\varepsilon_{0123}$ and $\varepsilon_{1032}$. Which of the five change in Peskin–Schroeder's convention?
*[variation of PS1.3(a)]*

^wr-5-a

(b) Show $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\sigma} = -24$ by counting terms, and then $\varepsilon_{\mu\nu\rho\sigma}\varepsilon^{\mu\nu\rho\delta} = -6\,\delta^\delta{}_\sigma$.
*[new]*

^wr-5-b

(c) $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma}$ is invariant under proper Lorentz transformations $SO(1,3)$ ($p_{i\mu}$ four distinct four-momenta). Show that $\varepsilon^{\mu\nu\rho\sigma}p_{1\mu}p_{2\nu}p_{3\rho}p_{4\sigma} = 0$ if the four momenta satisfy $\sum_{i=1}^4p_i^\mu = 0$.
*[HW-literal PS1.3(b)]*

^wr-5-c

(d) Using $\varepsilon_{\mu\nu\rho\sigma}A^\mu{}_\alpha A^\nu{}_\beta A^\rho{}_\gamma A^\sigma{}_\delta = (\det A)\,\varepsilon_{\alpha\beta\gamma\delta}$, show that the contraction of (c) is multiplied by $\det\Lambda$ under any Lorentz transformation, so it changes sign under $\mathcal P$.
*[extension of PS1.3(b)]*

^wr-5-d

### Problem 6. Elastic scattering and the momentum transfer

A particle of mass $m_2$ is at rest in the laboratory. It is struck by a particle of mass $m_1$, momentum $p_{\rm lab}$ and energy $E_{\rm lab}$; the two become particles of masses $m_3$, $m_4$. In the centre-of-mass system (cms) the initial momenta are $\mathbf p'$ and $-\mathbf p'$, the final ones $\mathbf q'$ and $-\mathbf q'$, and particle 3 moves at the angle $\theta'$ to particle 1. Mandelstam: $s = (p_1 + p_2)^2$, $t = (p_1 - p_3)^2$, $u = (p_1 - p_4)^2$.

^wr-6

(a) Define the four-momentum transfer $q = p_1 - p_3$. For elastic scattering ($m_1 = m_3$, $m_2 = m_4$) show that $t \equiv q^2 = -2m_4(E_4 - m_4)$, where $E_4$ is the final laboratory energy of the particle initially at rest.
*[HW-literal PS1.5(e)]*

^wr-6-a

(b) Show that for elastic scattering $s \equiv (p_1 + p_2)^2 = E_{\rm cms}^2$ and $t = -4p'^2\sin^2(\theta'/2)$, with $p' = \lvert\mathbf p'\rvert$ the cms momentum and $\theta'$ the cms scattering angle.
*[HW-literal PS1.5(f)]*

^wr-6-b

(c) Show $s + t + u = m_1^2 + m_2^2 + m_3^2 + m_4^2$. For elastic scattering with all four masses equal to $m$, express $u$ through $p'$ and $\theta'$, give the physical ranges of $t$ and $u$, and say at which angle each vanishes.
*[extension of PS1.5(e)–(f)]*

^wr-6-c

### Problem 7. Invariants in a convenient frame: thresholds and colliders

Take $m_p = 938.3$ MeV and $m_{\pi^0} = 135.0$ MeV.
*[variation of PS1.4(a) and PS1.5(b)–(c)]*

^wr-7

(a) Neutral-pion production on a fixed target, $p + p \to p + p + \pi^0$, the target proton at rest. Find the threshold kinetic energy of the beam proton. Why is it larger than $m_{\pi^0}$?

^wr-7-a

(b) At threshold, with what velocity does the cms move in the laboratory, and what are the final particles doing in the cms?

^wr-7-b

(c) Two beams of particles of mass $m$ and energy $E$ each collide head-on. Show $s = 4E^2$, and find the beam energy $E_{\rm lab}$ of a fixed-target experiment with the same $s$. Evaluate it for $E = 6.8$ TeV protons.

^wr-7-c

### Problem 8. Derivatives with four-vectors, I

$\rho = x_\mu x^\mu$ is a radial coordinate on spacetime (a length squared; do not also use $\rho$ as a dummy index). Notation: $\partial_\mu = \partial/\partial x^\mu$, $\Box = \partial_\mu\partial^\mu$.
*[HW-literal PS1.6(a)–(d)]*

^wr-8

(a) Compute $\partial_\mu\rho$.

^wr-8-a

(b) Compute $\partial_\mu\partial_\nu\rho$.

^wr-8-b

(c) Compute $\Box\rho$.

^wr-8-c

(d) Compute $\Box^2\rho^2$.

^wr-8-d

### Problem 9. Derivatives with four-vectors, II

Notation as in Problem 8.

^wr-9

(a) Compute $\partial_\sigma\bigl(x^\mu\partial_\mu f(\rho)\bigr)$ for any function $f(\rho)$.
*[HW-literal PS1.6(e)]*

^wr-9-a

(b) Show that $f(\rho) = c_1/\rho + c_2$ solves $\Box f = 0$ for $\rho \ne 0$.
*[HW-literal PS1.6(f)]*

^wr-9-b

(c) In $d$ spacetime dimensions show $\Box f(\rho) = 4\rho f''(\rho) + 2d\,f'(\rho)$, and find all $f(\rho)$ with $\Box f = 0$ away from $\rho = 0$ ($d > 2$). Check $d = 4$ against (b).
*[extension of PS1.6(f)]*

^wr-9-c

(d) Why is $\rho \ne 0$ needed in (b)? Does $1/x^2$ satisfy $\Box(1/x^2) = 0$ on all of spacetime, as a distribution? Answer in words.
*[extension of PS1.6(f)]*

^wr-9-d

### Problem 10. Derivatives with respect to a four-vector or a tensor

*[new]*

^wr-10

(a) Treating the four $p^\mu$ as independent, compute $\partial(p\cdot q)/\partial p^\mu$, $\ \partial(p^2)^2/\partial p_\mu$ and $\ \partial/\partial p^\mu\,\bigl[1/(p^2 - m^2 + i\epsilon)\bigr]$.

^wr-10-a

(b) Treating the sixteen $\partial_\mu A_\nu$ as independent, show $\partial(F_{\alpha\beta}F^{\alpha\beta})/\partial(\partial_\mu A_\nu) = 4F^{\mu\nu}$, and read off the Euler–Lagrange equation of $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu$.

^wr-10-b

(c) Why must $p^0$ be treated as independent of $\mathbf p$ when you differentiate with respect to $p^\mu$, even for a particle on its mass shell?

^wr-10-c

### Problem 11. Maxwell's equations in covariant form

$F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, with $F^{0i} = -E^i$ and $F^{ij} = -\varepsilon_{ijk}B^k$.
*[variation of Lecture 1's boost example]*

^wr-11

(a) Show $F_{\mu\nu}F^{\mu\nu} = 2(\mathbf B^2 - \mathbf E^2)$ and $\varepsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf E\cdot\mathbf B$. What is the second in Peskin–Schroeder's convention?

^wr-11-a

(b) Apply the active boost along $x$, $\Lambda = B_x(\eta)$ ($\gamma = \cosh\eta$, $\gamma v = \sinh\eta$), with $F'^{\mu\nu} = \Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta F^{\alpha\beta}$. Find all six components of $\mathbf E'$ and $\mathbf B'$.

^wr-11-b

(c) Check explicitly that $\mathbf E'\cdot\mathbf B' = \mathbf E\cdot\mathbf B$.

^wr-11-c

(d) Before the boost the field is purely electric, $\mathbf E = E\,\hat{\mathbf y}$, $\mathbf B = 0$. Give $\mathbf E'$ and $\mathbf B'$, and check $\mathbf B' = \mathbf v\times\mathbf E'$ with $\mathbf v = v\hat{\mathbf x}$ the velocity the active boost gives the source.

^wr-11-d

## Lecture 2. Natural units and causality

### Problem 12. Natural units

$\hbar c = 197.3$ MeV fm, $\hbar = 6.582\times10^{-25}$ GeV s, $1$ mb $= 0.1$ fm$^2$.
*[variation of PS1.4(b) and (d)]*

^wr-12

(a) Give the mass dimensions of $x^\mu$, $\partial_\mu$, $d^4x$, $\delta^4(x)$, $d^3p/2E_{\mathbf p}$, $\delta^3(\mathbf p)$, and of a scalar field $\phi$ and a Dirac field $\psi$ in four dimensions. Give three reasons why $\partial_\mu$ has mass dimension $1$.

^wr-12-a

(b) At spacelike separation the Wightman function decays like $e^{-mr}$. Restore $\hbar$ and $c$ in the exponent, and evaluate the decay length for a charged pion, $m_\pi c^2 = 139.6$ MeV.

^wr-12-b

(c) A cross section computed in natural units is $\sigma = 1\ \text{GeV}^{-2}$: convert it to millibarn. A resonance has width $\Gamma = 2.50$ GeV: what is its lifetime in seconds?

^wr-12-c

(d) Restore $c$ in $E_{\rm cms}^2 = m_1^2 + m_2^2 + 2m_2E_{\rm lab}$.

^wr-12-d

### Problem 13. Causality, the light cone and the orbits

Three events: $A$ at the origin, $B = (t, x, y, z) = (1, 2, 0, 0)$, $C = (3, 1, 0, 0)$.
*[new]*

^wr-13

(a) Classify the separations $AB$ and $AC$ (timelike, null, spacelike; future or past).

^wr-13-a

(b) Apply the active boost $B_x(\eta)$ to all three events. For which $\eta$ are $A$ and $B$ simultaneous, and for which is their time order reversed? Show that no $\eta$ reverses the order of $A$ and $C$.

^wr-13-b

(c) Find an explicit $\Lambda \in SO^+(1,3)$ with $\Lambda x_B = -x_B$, in the form of a boost along $x$ times a rotation by $\pi$ about $z$. Why does no element of $SO^+(1,3)$ send $x_C$ to $-x_C$?

^wr-13-c

(d) Use (c) to show that a Lorentz-invariant function satisfies $f(-\xi) = f(\xi)$ at every spacelike $\xi$. Conclude that $\langle0\rvert[\hat\phi(x), \hat\phi(y)]\lvert0\rangle = D_W(x - y) - D_W(y - x)$ vanishes at spacelike separation, and say why the time-ordered product $T\{\hat\phi(x)\hat\phi(y)\}$ is the same in every inertial frame.

^wr-13-d

## Lecture 7. Generators, the algebra and representations

### Problem 14. Generators as 4×4 matrices

$(\mathcal J^{\rho\sigma})^\mu{}_\nu = i(g^{\rho\mu}\delta^\sigma{}_\nu - g^{\sigma\mu}\delta^\rho{}_\nu)$, $J_i = \frac12\varepsilon_{ijk}\mathcal J^{jk}$, $K_i = \mathcal J^{0i}$.
*[variation of PS4.5(a)]*

^wr-14

(a) Show $J_2 = \mathcal J^{31}$, and write $J_1$, $J_2$, $K_2$ and $K_3$ as $4\times4$ matrices.

^wr-14-a

(b) Multiply the matrices to find $[J_2, K_3]$ and $[K_2, K_3]$, and compare with $[J_i, K_j] = i\varepsilon_{ijk}K_k$, $[K_i, K_j] = -i\varepsilon_{ijk}J_k$.

^wr-14-b

(c) Obtain $[K_2, K_3]$ again from $[\mathcal J^{\mu\nu}, \mathcal J^{\rho\sigma}] = i(g^{\nu\rho}\mathcal J^{\mu\sigma} - g^{\mu\rho}\mathcal J^{\nu\sigma} - g^{\nu\sigma}\mathcal J^{\mu\rho} + g^{\mu\sigma}\mathcal J^{\nu\rho})$.

^wr-14-c

(d) Which of the six generators are Hermitian? Is $B_z(\eta) = e^{-i\eta K_3}$ unitary? Why does this not contradict the unitarity of $U(\Lambda)$ on the quantum states?

^wr-14-d

### Problem 15. Finite transformations by exponentiation

Write all matrices as $4\times4$ matrices (no $2\times2$ blocks).
*[variation of PS6.4(a) and (c)]*

^wr-15

(a) Rotation about $y$: $\omega_{31} = -\omega_{13} = \theta$, all other $\omega_{\mu\nu} = 0$. Show $-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu} = -i\theta J_2$, and sum the exponential series for $R_y(\theta) = e^{-i\theta J_2}$. Where does the minus sign of $\sin\theta$ sit, and why there?

^wr-15-a

(b) Boost along $y$: $\omega_{02} = -\omega_{20} = \eta$. Compute $B_y(\eta) = e^{-i\eta K_2}$ and check that it sends $(m, 0, 0, 0)$ to $(m\cosh\eta, 0, m\sinh\eta, 0)$.

^wr-15-b

(c) Show that $R_z(\theta)B_x(\eta)R_z(\theta)^{-1}$ is the boost of rapidity $\eta$ along $\hat{\mathbf n} = (\cos\theta, \sin\theta, 0)$, and relate the first-order version to $[J_3, K_1] = iK_2$.
*[new]*

^wr-15-c

### Problem 16. Two boosts make a rotation

$\tanh\eta_1 = 3/5$, $\tanh\eta_2 = 4/5$.
*[new]*

^wr-16

(a) Compute $\Lambda = B_y(\eta_2)B_x(\eta_1)$. Check that it is a Lorentz transformation, and show that it is not a pure boost.

^wr-16-a

(b) Write $\Lambda = B(u)R$, where $B(u)$ is the pure boost taking $e_0$ to $u = \Lambda e_0$ and $R = \operatorname{diag}(1, O)$ is a rotation. Find the velocity and $\gamma$ of the boost part, and the axis and angle of $R$. Compare the rapidity of the boost part with $\eta_1 + \eta_2$.

^wr-16-b

(c) For small $a$, $b$, show $B_x(a)B_y(b)B_x(-a)B_y(-b) = \mathbb 1 + iab\,J_3 + O(3)$, a rotation by $-ab$ about $z$, and name the commutator responsible. With which sign would the same computation come out in the Euclidean rotation group $SO(4)$, and why?

^wr-16-c

### Problem 17. The four-vector is (½, ½)

$\mathbf J_\pm = \frac12(\mathbf J \pm i\mathbf K)$; on a joint eigenvector, $J_3 = m_+ + m_-$ and $K_3 = -i(m_+ - m_-)$.
*[variation of PS7.1(d) and PS5.1(b)]*

^wr-17

(a) On the vector representation compute $\mathbf J^2$, $\mathbf K^2$ and $\mathbf J\cdot\mathbf K$, then $\mathbf J_\pm^2$, and read off $(j_+, j_-)$.

^wr-17-a

(b) Show that $e_0 \pm e_3$ and $e_1 \pm ie_2$ are joint eigenvectors of $J_3$ and $K_3$; give the eigenvalues, the labels $(m_+, m_-)$, and the factor by which $B_z(\eta)$ multiplies each.

^wr-17-b

(c) Give the dimension, the spins under rotations and the sign of a $2\pi$ rotation of $(\frac12, \frac12)$, $(1, 0)\oplus(0, 1)$, $(1, 1)$ and $(1, \frac12)$, and name the field of the course (if any) that carries each.

^wr-17-c

(d) $(1, 0)\oplus(0, 0)$ also has dimension $4$, rotation content $0\oplus1$ and sign $+1$. Give a test that tells it apart from the four-vector.

^wr-17-d

### Problem 18. Two-index tensors; the field strength is (1, 0) ⊕ (0, 1)

$T'^{\mu\nu} = \Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta T^{\alpha\beta}$; infinitesimally $\delta F^{\mu\nu} = \omega^\mu{}_\alpha F^{\alpha\nu} + \omega^\nu{}_\beta F^{\mu\beta}$.

^wr-18

(a) Show that the symmetric traceless part, the antisymmetric part and the trace of $T^{\mu\nu}$ are each mapped into themselves by $\Lambda$. Count their dimensions, give their $(j_+, j_-)$ labels, and check the count against $(\frac12, \frac12)\otimes(\frac12, \frac12)$.
*[variation of PS7.1(d)]*

^wr-18-a

(b) For the infinitesimal boost along $x$, $\omega_{01} = -\omega_{10} = \eta$, find $\delta\mathbf E$ and $\delta\mathbf B$, and compare with Problem 11(b) to first order in $\eta$.
*[new]*

^wr-18-b

(c) Show $\delta(\mathbf E - i\mathbf B) = -i\eta\,\hat{\mathbf x}\times(\mathbf E - i\mathbf B)$ and $\delta(\mathbf E + i\mathbf B) = +i\eta\,\hat{\mathbf x}\times(\mathbf E + i\mathbf B)$. Together with rotations, $\delta(\mathbf E \mp i\mathbf B) = (\boldsymbol\theta \mp i\boldsymbol\eta)\times(\mathbf E \mp i\mathbf B)$: which combination carries $(1, 0)$? Why can a real $F^{\mu\nu}$ not carry $(1, 0)$ alone?
*[new]*

^wr-18-c

### Problem 19. Orbital generators and how fields transform

$L^{\mu\nu} = i(x^\mu\partial^\nu - x^\nu\partial^\mu)$; a scalar field transforms as $\phi'(x) = \phi(\Lambda^{-1}x)$, a vector field as $A'^\mu(x) = \Lambda^\mu{}_\nu A^\nu(\Lambda^{-1}x)$.
*[new]*

^wr-19

(a) For the boost $\omega_{03} = -\omega_{30} = \eta$, expand $\phi(\Lambda^{-1}x)$ to first order in $\eta$ and show $\phi' = (1 - i\eta L^{03})\phi$ with $L^{03} = -i(t\,\partial_z + z\,\partial_t)$, in agreement with the formula for $L^{\mu\nu}$.

^wr-19-a

(b) Show $\partial_\mu\phi'(x) = \Lambda_\mu{}^\nu\,(\partial_\nu\phi)(\Lambda^{-1}x)$, and conclude that $\partial_\mu\phi\,\partial^\mu\phi$ is a scalar field.

^wr-19-b

(c) Show that to first order $A'^\alpha = A^\alpha - \frac i2\omega_{\mu\nu}\bigl(L^{\mu\nu}A^\alpha + (\mathcal J^{\mu\nu})^\alpha{}_\beta A^\beta\bigr)$: orbital plus spin.

^wr-19-c

## Short response

### Problem 20. Short response

Short answers: a formula, a number, or a phrase. No derivations are needed.
*[variation of PS7.1]*

^wr-20

(a) $\varepsilon^{1023}$ and $\varepsilon_{3210}$. (b) $s + t + u$ for $e^-\mu^- \to e^-\mu^-$. (c) The mass dimensions of $\delta^4(p)$ and of $\partial/\partial p^\mu$. (d) $\Box(x^2)^2$. (e) The rapidity of a particle with $E = 13$ GeV and $\mathbf p = 12$ GeV $\hat{\mathbf z}$. (f) $[K_3, J_1]$. (g) The component of $O(1,3)$ that contains $-\mathbb 1$, and whether $-\mathbb 1 = \exp(-\frac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$ for some $\omega$. (h) The $(j_+, j_-)$ labels of $\partial_\mu\phi$, of $g_{\mu\nu}T^{\mu\nu}$ and of the symmetric traceless part of $T^{\mu\nu}$. (i) $\mathbf E^2 - \mathbf B^2$ and $\mathbf E\cdot\mathbf B$ for a plane electromagnetic wave. (j) The factor by which a four-vector is multiplied under a rotation by $2\pi$, and the factor by which $B_z(\eta)$ multiplies $e_0 + e_3$.

^wr-20-a
