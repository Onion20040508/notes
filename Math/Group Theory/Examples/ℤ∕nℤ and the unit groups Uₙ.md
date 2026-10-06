---
subject: math
type: example
source: "[[Group Theory]]"
tags: ["math493", "workhorse"]
---
The cyclic group $\mathbb{Z}/n\mathbb{Z}$ of residue classes modulo $n$ under addition, and inside it the unit group $U_n = (\mathbb{Z}/n\mathbb{Z})^\times$ of classes coprime to $n$ under multiplication. They are the course's supply of concrete abelian groups: every finite cyclic group is some $\mathbb{Z}/n\mathbb{Z}$, and the small $U_n$ ($U_5 \cong \mathbb{Z}/4\mathbb{Z}$, $U_7 \cong \mathbb{Z}/6\mathbb{Z}$, $U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$) are the test cases for isomorphism and invariants. The construction is also the model for well-definedness and quotient groups: $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by $n\mathbb{Z}$. Its uses in MATH 493:

- $(\mathbb{Z}/n\mathbb{Z}, +)$ is a group; the nonzero classes form a group under multiplication iff $n$ is prime ([[§3 Basic Examples of Groups#^ex-3-1|§3]])
- Orders of elements: $3$ generates $U_7$, and $U_8$ is not cyclic ([[§4 Subgroups#^rem-4-5|§4]])
- Residue classes $[a] = a + n\mathbb{Z}$ ([[§6 Divisibility and Congruence#^def-6-4|§6]])
- The cyclic group $\mathbb{Z}/n\mathbb{Z} = C_n$ ([[§7 The Group ℤ∕nℤ#^def-7-1|§7]])
- Addition of residue classes is well defined ([[§7 The Group ℤ∕nℤ#^prop-7-1|§7]])
- The Descent Lemma: when a map on $\mathbb{Z}$ descends to $\mathbb{Z}/n\mathbb{Z}$ ([[§7 The Group ℤ∕nℤ#^lem-7-2|§7]])
- Inverses modulo $5$ and modulo $8$ ([[§8 Invertibility and Unit Groups#^ex-8-1|§8]])
- $[a]$ is invertible modulo $n$ iff $\gcd(a, n) = 1$ ([[§8 Invertibility and Unit Groups#^prop-8-1|§8]])
- Euler's totient counts the units ([[§8 Invertibility and Unit Groups#^def-8-3|§8]])
- The unit groups $U_n$ for $n \leq 12$ ([[§8 Invertibility and Unit Groups#^ex-8-5|§8]])
- The unit group $U_n = (\mathbb{Z}/n\mathbb{Z})^\times$ ([[§8 Invertibility and Unit Groups#^def-8-4|§8]])
- $U_n$ is a group, with inverses from Bézout ([[§8 Invertibility and Unit Groups#^prop-8-3|§8]])
- $\mathbb{Z}/n\mathbb{Z}$ is a field iff $n$ is prime ([[§8 Invertibility and Unit Groups#^prop-8-4|§8]])
- The Chinese Remainder Theorem: $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ for coprime $m, n$ ([[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3|§9]])
- The tables of $\mathbb{Z}/4\mathbb{Z}$ and $U_5$ ([[§14 Multiplication Tables#^ex-14-1|§14]])
- The table of $\mathbb{Z}/6\mathbb{Z}$ ([[§14 Multiplication Tables#^ex-14-2|§14]])
- The table of $U_7$ ([[§14 Multiplication Tables#^ex-14-3|§14]])
- The table of $U_8$: every element squares to $1$ ([[§14 Multiplication Tables#^ex-14-4|§14]])
- Reduction $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ is a homomorphism with kernel $n\mathbb{Z}$ ([[§15 Homomorphisms#^ex-15-1|§15]])
- $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$: a homomorphism that is not injective ([[§15 Homomorphisms#^ex-15-2|§15]])
- $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ ([[§16 Isomorphisms#^prop-16-3|§16]])
- $\mathbb{Z}/4\mathbb{Z} \cong U_5$ via $k \mapsto 2^k$ ([[§16 Isomorphisms#^prop-16-7|§16]])
- $U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ is not cyclic, while $U_7 \cong \mathbb{Z}/6\mathbb{Z}$ ([[§16 Isomorphisms#^prop-16-8|§16]])
- Every cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$ ([[§17 Cyclic Groups#^thm-17-1|§17]])
- Generators and subgroups of a finite cyclic group ([[§17 Cyclic Groups#^cor-17-6|§17]])
- The six subgroups of $\mathbb{Z}/12\mathbb{Z}$ ([[§17 Cyclic Groups#^ex-17-1|§17]])
- $U_n$ is the product of the unit groups of its prime-power factors ([[§22 The Structure of Uₙ#^thm-22-2|§22]])
- Euler's totient formula ([[§22 The Structure of Uₙ#^cor-22-3|§22]])
- Examples: $U_{15}$, $U_{10}$, $U_{24}$ as products of cyclic groups ([[§22 The Structure of Uₙ#^ex-22-1|§22]])
- $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle, and $\mathbb{Z}/4\mathbb{Z}$ acting unfaithfully on two points ([[§25 Actions#^ex-25-3|§25]])
- Fermat's little theorem, from Lagrange applied to $U_p$ ([[§29 The Index and Lagrange's Theorem#^cor-29-4|§29]])
- Every group of prime order $p$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$ ([[§29 The Index and Lagrange's Theorem#^thm-29-7|§29]])
- One group of each prime order; two of order $4$ and two of order $6$ ([[§29 The Index and Lagrange's Theorem#^rem-29-3|§29]])
- $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by $n\mathbb{Z}$ ([[§40 Quotient Groups#^ex-40-1|§40]])
- $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ computed with representatives ([[§40 Quotient Groups#^ex-40-2|§40]])
- $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\} \cong \mathbb{Z}/2\mathbb{Z}$ is not realized by a subgroup of representatives ([[§40 Quotient Groups#^rem-40-3|§40]])
- The First Isomorphism Theorem for $\mathbb{Z}/6\mathbb{Z} \to U_7$ ([[§41 The First and Second Isomorphism Theorems#^ex-41-1|§41]])
- The abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$ ([[§43 Simple Groups#^thm-43-1|§43]])

## Chapter by chapter

Revisit parts for $\mathbb{Z}/n\mathbb{Z}$ and $U_n$, chapter by chapter: [[§5 A Zoo of Subgroups#ℤ∕nℤ and Uₙ|Chapter 1]] · [[· 2 Arithmetic Modulo n|Chapter 2]] · [[§19 S₃, ℤ∕nℤ and Uₙ#ℤ∕nℤ and Uₙ|Chapter 4]] · [[§23 S₃, Aₙ, Uₙ and GLₙ#ℤ∕nℤ and Uₙ|Chapter 5]] · [[§32 Linear Groups, the Cube, S₃ and A₄#ℤ∕nℤ and Uₙ|Chapter 6]] · [[§45 S₃, S₄, A₄ and A₅#ℤ∕nℤ and Uₙ|Chapter 8]].

## $(\mathbb{Z}/n\mathbb{Z}, +)$ is a group; the nonzero classes form a group under multiplication iff $n$ is prime
![[§3 Basic Examples of Groups#^ex-3-1]]

## Orders of elements: $3$ generates $U_7$, and $U_8$ is not cyclic
![[§4 Subgroups#^rem-4-5]]

## Residue classes $[a] = a + n\mathbb{Z}$
![[§6 Divisibility and Congruence#^def-6-4]]

## The cyclic group $\mathbb{Z}/n\mathbb{Z} = C_n$
![[§7 The Group ℤ∕nℤ#^def-7-1]]

## Addition of residue classes is well defined
![[§7 The Group ℤ∕nℤ#^prop-7-1]]

## The Descent Lemma: when a map on $\mathbb{Z}$ descends to $\mathbb{Z}/n\mathbb{Z}$
![[§7 The Group ℤ∕nℤ#^lem-7-2]]

## Inverses modulo $5$ and modulo $8$
![[§8 Invertibility and Unit Groups#^ex-8-1]]

## $[a]$ is invertible modulo $n$ iff $\gcd(a, n) = 1$
![[§8 Invertibility and Unit Groups#^prop-8-1]]

## Euler's totient counts the units
![[§8 Invertibility and Unit Groups#^def-8-3]]

## The unit groups $U_n$ for $n \leq 12$
![[§8 Invertibility and Unit Groups#^ex-8-5]]

## The unit group $U_n = (\mathbb{Z}/n\mathbb{Z})^\times$
![[§8 Invertibility and Unit Groups#^def-8-4]]

## $U_n$ is a group, with inverses from Bézout
![[§8 Invertibility and Unit Groups#^prop-8-3]]

## $\mathbb{Z}/n\mathbb{Z}$ is a field iff $n$ is prime
![[§8 Invertibility and Unit Groups#^prop-8-4]]

## The Chinese Remainder Theorem: $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ for coprime $m, n$
![[§9 Euclid's Lemma, Unique Factorization, and the Chinese Remainder Theorem#^thm-9-3]]

## The tables of $\mathbb{Z}/4\mathbb{Z}$ and $U_5$
![[§14 Multiplication Tables#^ex-14-1]]

## The table of $\mathbb{Z}/6\mathbb{Z}$
![[§14 Multiplication Tables#^ex-14-2]]

## The table of $U_7$
![[§14 Multiplication Tables#^ex-14-3]]

## The table of $U_8$: every element squares to $1$
![[§14 Multiplication Tables#^ex-14-4]]

## Reduction $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ is a homomorphism with kernel $n\mathbb{Z}$
![[§15 Homomorphisms#^ex-15-1]]

## $\mathbb{Z}/6\mathbb{Z} \to U_7$, $k \mapsto 2^k$: a homomorphism that is not injective
![[§15 Homomorphisms#^ex-15-2]]

## $\mathbb{Z}/4\mathbb{Z} \not\cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$
![[§16 Isomorphisms#^prop-16-3]]

## $\mathbb{Z}/4\mathbb{Z} \cong U_5$ via $k \mapsto 2^k$
![[§16 Isomorphisms#^prop-16-7]]

## $U_8 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ is not cyclic, while $U_7 \cong \mathbb{Z}/6\mathbb{Z}$
![[§16 Isomorphisms#^prop-16-8]]

## Every cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$
![[§17 Cyclic Groups#^thm-17-1]]

## Generators and subgroups of a finite cyclic group
![[§17 Cyclic Groups#^cor-17-6]]

## The six subgroups of $\mathbb{Z}/12\mathbb{Z}$
![[§17 Cyclic Groups#^ex-17-1]]

## $U_n$ is the product of the unit groups of its prime-power factors
![[§22 The Structure of Uₙ#^thm-22-2]]

## Euler's totient formula
![[§22 The Structure of Uₙ#^cor-22-3]]

## Examples: $U_{15}$, $U_{10}$, $U_{24}$ as products of cyclic groups
![[§22 The Structure of Uₙ#^ex-22-1]]

## $\mathbb{Z}/3\mathbb{Z}$ rotating a triangle, and $\mathbb{Z}/4\mathbb{Z}$ acting unfaithfully on two points
![[§25 Actions#^ex-25-3]]

## Fermat's little theorem, from Lagrange applied to $U_p$
![[§29 The Index and Lagrange's Theorem#^cor-29-4]]

## Every group of prime order $p$ is isomorphic to $\mathbb{Z}/p\mathbb{Z}$
![[§29 The Index and Lagrange's Theorem#^thm-29-7]]

## One group of each prime order; two of order $4$ and two of order $6$
![[§29 The Index and Lagrange's Theorem#^rem-29-3]]

## $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by $n\mathbb{Z}$
![[§40 Quotient Groups#^ex-40-1]]

## $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\}$ computed with representatives
![[§40 Quotient Groups#^ex-40-2]]

## $(\mathbb{Z}/4\mathbb{Z})/\{0, 2\} \cong \mathbb{Z}/2\mathbb{Z}$ is not realized by a subgroup of representatives
![[§40 Quotient Groups#^rem-40-3]]

## The First Isomorphism Theorem for $\mathbb{Z}/6\mathbb{Z} \to U_7$
![[§41 The First and Second Isomorphism Theorems#^ex-41-1]]

## The abelian simple groups are exactly the $\mathbb{Z}/p\mathbb{Z}$
![[§43 Simple Groups#^thm-43-1]]
