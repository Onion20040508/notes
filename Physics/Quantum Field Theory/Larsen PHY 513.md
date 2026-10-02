---
type: convention
source: "PHY 513 (Larsen)"
---
# Larsen PHY 513

Conventions of [[Quantum Field Theory]], as in the user's PHY 513 notes (App. B, Concordance), compared with Peskin & Schroeder (PS, the course textbook) and Yu Zhao-Huan's lecture notes.

| Item | These notes | PS | Yu |
| --- | --- | --- | --- |
| Metric | $g=\mathrm{diag}(+1,-1,-1,-1)$ | same | same (1.19) |
| Units | natural, $\hbar=c=1$ ([[§C1.2 Natural Units and Dimensional Analysis#^def-c1-2-1\|Def. §C1.2.1]]); Heaviside–Lorentz, $\alpha=e^2/4\pi$ ([[§C1.7 Relativistic Electrodynamics in Index Form#^def-c1-7-1\|Def. §C1.7.1]]) | same | same |
| Levi-Civita | $\varepsilon^{0123}=+1$ ([[§C1.5 Vectors, Tensors and Index Notation#^cau-c1-5-5\|§C1.5, Caution: The sign of ε⁰¹²³]]) | $-1$ | $+1$ (1.104) |
| Lorentz transformations | read actively, $t'=\gamma(t+vz)$ ([[§C1.4 The Lorentz Group#^def-c1-4-1\|Def. §C1.4.1]]); $\Lambda=\exp(-\tfrac i2\omega_{\mu\nu}\mathcal J^{\mu\nu})$, $\mathcal J=iM$ ([[§C1.6 Infinitesimal Lorentz Transformations and Generators#^def-c1-6-1\|Def. §C1.6.1]]); boost generator $K^i=J^{0i}$ ([[§C1.6 Infinitesimal Lorentz Transformations and Generators#^def-c1-6-2\|Def. §C1.6.2]]; not the Noether boost charge, [[§C1.12 Spacetime Symmetries꞉ Energy–Momentum and Angular Momentum#^cau-c1-12-2\|§C1.12, Caution: Notation in Yu and in the conventions table]]) | same | passive, $t'=\gamma(t-\beta x)$; same in $\omega_{\mu\nu}$ |
| Fourier transform (4d) | $f(x)=\int\frac{d^4p}{(2\pi)^4}\tilde f(p)\,e^{-ip\cdot x}$ | same | same |
| Mode expansion | $\phi=\int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\mathbf p}}}\big(a_{\mathbf p}e^{-ip\cdot x}+a^\dagger_{\mathbf p}e^{ip\cdot x}\big)$, $[a_{\mathbf p},a^\dagger_{\mathbf q}]=(2\pi)^3\delta^3(\mathbf p-\mathbf q)$ | same | same (2.122) |
| State normalization | $\lvert\mathbf p\rangle=\sqrt{2E_{\mathbf p}}\,a^\dagger_{\mathbf p}\lvert0\rangle$, $\langle\mathbf p\vert\mathbf q\rangle=2E_{\mathbf p}(2\pi)^3\delta^3(\mathbf p-\mathbf q)$; invariant measure $\frac{d^3p}{(2\pi)^3\,2E_{\mathbf p}}$ | same | same (2.152) |
| Energy | $E_{\mathbf p}=\sqrt{\mathbf p^2+m^2}$ (the lectures write $\omega_{\mathbf p}$ in L4–L5) | $E_{\mathbf p}$ | $E_{\mathbf p}$ |
| Green's functions | $(\partial^2+m^2)D_C=-i\delta^4$; $\tilde D_F=\dfrac{i}{p^2-m^2+i\epsilon}$; names $D_W$ (PS: $D$), $D$ with $iD=\langle0\vert[\phi,\phi]\vert0\rangle$, $D_1$, $D_R$, $D_A$, $D_F$, $D_{\bar F}$, $\bar D$, $D_E$ | $\tilde D_F$ same | same (6.207)–(6.211); $D_{\rm PJ}=iD$ |
| Complex-field charge | $Q=\tfrac12(N_a-N_b)$ (as PS and Problem Set 3; the Noether current gives $N_b-N_a$, [[§C1.11 Noether's Theorem#^cau-c1-11-3\|§C1.11, Caution: Sign and normalization of the U(1) current]]) | $\tfrac12(N_a-N_b)$ | $q(N_a-N_b)$ |
| Dirac matrices | chiral (Weyl) basis; $S^{\mu\nu}=\tfrac i4[\gamma^\mu,\gamma^\nu]$; $\bar\psi=\psi^\dagger\gamma^0$ | same | same |

Index conventions: Einstein summation; Greek indices $0,\dots,3$, Latin $1,2,3$. Srednicki uses the mostly-plus metric and is not used for formulas.
