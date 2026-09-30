---
type: summary
subject: "[[Group Theory]]"
tags: [group-theory, math493]
---
↑ [[Group Theory]]

# Conventions and Notation

| Symbol | Meaning | Where |
|---|---|---|
| $e$, $e_G$ | The identity element; the subscript names the group when several are in play ($\varphi(e_G) = e_H$). Worksheet 1 writes $1$. Exceptions by established convention: $0$ in additive groups, $[0]$ in $\mathbb{Z}/n\mathbb{Z}$, $[1]$ in $U_n$, $I_n$ for matrices, and the number $1$ in $k^\times$ and $\{\pm 1\}$. | [[§1 The Definition of a Group#^def-1-1\|Def. §1.1]]; [[§1 The Definition of a Group#^rem-1-1\|Notation]] |
| $gh$, $g^{-1}$, $g^n$ | Product, inverse, integer power. Additively: $g + h$, $-g$, $ng$. | [[§1 The Definition of a Group#^def-1-1\|Def. §1.1]], [[§4 Subgroups#^def-4-2\|Def. §4.2]]; [[§1 The Definition of a Group#^rem-1-1\|Notation]] |
| $\langle g \rangle$, $\langle g_1, \ldots, g_k \rangle$ | Subgroup generated. | [[§4 Subgroups#^def-4-3\|Def. §4.3]], [[§4 Subgroups#^def-4-4\|Def. §4.4]] |
| $\vert G \vert$, $\operatorname{ord}(g)$ | Order of a group; order of an element. | [[§4 Subgroups#^def-4-5\|Def. §4.5]] |
| $[G : H]$, $G/H$, $H\backslash G$ | Index; left cosets; right cosets. | [[§27 The Index and Lagrange's Theorem#^def-27-1\|Def. §27.1]], [[§26 Left and Right Cosets#^def-26-2\|Def. §26.2]] |
| $S_X$, $S_n$ | Bijections of $X$; of $\{1, \ldots, n\}$. Composition is right-to-left: $(\sigma\tau)(i) = \sigma(\tau(i))$. | [[§3 Basic Examples of Groups#^def-3-5\|Def. §3.5]]; [[§10 Cycle Notation and the Group S₃#^rem-10-1\|Convention Warning]] |
| $(a_1\ a_2\ \cdots\ a_r)$ | Cycle notation. | [[§10 Cycle Notation and the Group S₃#^def-10-1\|Def. §10.1]] |
| $\operatorname{sgn}$, $A_n$ | Sign of a permutation and its kernel. The problem sets write $\varepsilon$. | [[§20 The Sign Homomorphism and the Alternating Group#^def-20-2\|Def. §20.2]], [[§20 The Sign Homomorphism and the Alternating Group#^def-20-3\|Def. §20.3]] |
| $GL_n(k)$, $SL_n(k)$, $O(n)$, $SO(n)$ | Linear groups; $M(\sigma)$ is the permutation matrix. | [[§3 Basic Examples of Groups#^def-3-6\|Def. §3.6]], [[§3 Basic Examples of Groups#^def-3-7\|Def. §3.7]]; [[§19 Polynomial Rings, Permutation Matrices, and Representations#^def-19-5\|Def. §19.5]] |
| $\mathbb{Z}/n\mathbb{Z}$, $U_n$ | Integers modulo $n$; unit group $(\mathbb{Z}/n\mathbb{Z})^\times$. | [[§7 The Group ℤ∕nℤ#^def-7-1\|Def. §7.1]], [[§8 Invertibility and Unit Groups#^def-8-4\|Def. §8.4]] |
| $\varphi(n)$ | Euler's totient $\vert U_n \vert$. (Elsewhere $\varphi$ usually denotes a homomorphism; context decides.) | [[§8 Invertibility and Unit Groups#^def-8-3\|Def. §8.3]] |
| $\operatorname{Ker}\varphi$, $\operatorname{Im}\varphi$, $\cong$ | Kernel, image, isomorphism. | [[§15 Homomorphisms#^def-15-2\|Def. §15.2]], [[§16 Isomorphisms#^def-16-1\|Def. §16.1]] |
| $c_a$, $\operatorname{Aut}(G)$ | Conjugation by $a$; automorphism group. | [[§18 Conjugation, Products, and Pointwise Products#^def-18-2\|Def. §18.2]], [[§18 Conjugation, Products, and Pointwise Products#^def-18-1\|Def. §18.1]] |
| $\operatorname{Conj}(g)$, $C_G(g)$, $Z(G)$ | Conjugacy class; centralizer (PS 3 writes $Z(g)$); center. | [[§31 Conjugacy Classes#^def-31-1\|Def. §31.1]], [[§32 Conjugation as an Action and the Class Equation#^def-32-1\|Def. §32.1]] ([[§32 Conjugation as an Action and the Class Equation#^rem-32-1\|notation]]), [[§33 The Center#^def-33-1\|Def. §33.1]] |
| $g \star x$, $G \curvearrowright X$, $X \curvearrowleft G$ | Action; left action; right action. | [[§23 Actions#^def-23-1\|Def. §23.1]], [[§23 Actions#^def-23-2\|Def. §23.2]] |
| $\operatorname{Stab}(x)$, $\operatorname{Fix}(g)$, $Gx$ | Stabilizer, fixed points, orbit. | [[§24 Stabilizers and Fixed Points#^def-24-1\|Def. §24.1]], [[§25 Orbits#^def-25-1\|Def. §25.1]] |
| $G\backslash X$, $X/G$ | Orbit spaces of a left and a right action. | [[§25 Orbits#^def-25-1\|Def. §25.1]], [[§25 Orbits#^def-25-2\|Def. §25.2]] |
| $H \trianglelefteq G$, $[G, G]$ | Normal subgroup; commutator subgroup. | [[§35 Normal Subgroups#^def-35-1\|Def. §35.1]]; [[§41 Commutators#^def-41-2\|Def. §41.2]] |
| $G/N$, $\pi$ | Quotient group by a normal subgroup; canonical projection $g \mapsto gN$. | [[§37 Quotient Groups#^def-37-1\|Def. §37.1]] |
| $PSL_n(F)$ | Projective special linear group $SL_n(F)/Z$. | [[§39 Simple Groups#^def-39-2\|Def. §39.2]] |
| *WS $k.m$*, *PS $k.m$* | Provenance tags: Worksheet $k$ / Problem Set $k$, Problem $m$. | [[493 Problem Set 1\|PS 1]], [[493 Problem Set 2\|PS 2]], [[493 Problem Set 3\|PS 3]] |
