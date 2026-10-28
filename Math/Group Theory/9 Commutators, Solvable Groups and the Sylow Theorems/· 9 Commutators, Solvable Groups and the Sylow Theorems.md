---
type: chapter
subject: "[[Group Theory]]"
chapter: 9
tags: [chapter, group-theory]
---
# 9 Commutators, Solvable Groups and the Sylow Theorems
↑ [[Group Theory]]

*Source: Lecture (Wed Sept 23); PS 2.3 and 2.4; Worksheet 9 (Wed Oct 7); Lecture (Fri Oct 9); Lecture and Worksheet 10 (Mon Oct 12); worksheet session (Wed Oct 14); lecture (Fri Oct 16); lecture and slides (Fri Oct 23). Worksheet 10 was handed out with Worksheet 9 (Wed Oct 7). In the Sylow part, proofs from the lecture are given; the worksheet problems not yet done in class are left to be filled in.*

[[§46 Characters#^def-46-1|Characters]] are homomorphisms to abelian groups. They [[§46 Characters#^prop-46-1|cannot distinguish conjugate elements]] and they [[§47 Commutators#^prop-47-1|kill every commutator]], which makes them a practical tool for proving that an element is *not* a commutator; the chapter determines [[§47 Commutators#^thm-47-5|the commutator subgroup]] of $S_n$, and with it [[§47 Commutators#^cor-47-7|all characters]] of $S_n$, and ends with the [[§47 Commutators#^def-47-3|abelianization]] and [[§47 Commutators#^prop-47-8|commuting normal subgroups]] (Problem Set 4). Characters are also the first step toward the representation theory of the second half of the course.

[[§43 Simple Groups#^def-43-1|Simple groups]] are the atoms of group theory; the next question is how they are put together. The [[§48 Solvable Groups#^def-48-1|solvable groups]] are the groups built entirely out of abelian pieces. The middle part of the chapter defines them, shows that the class is closed under [[§48 Solvable Groups#^prop-48-2|subgroups]] and [[§48 Solvable Groups#^prop-48-3|quotients]], and introduces the [[§49 The Derived Series#^def-49-1|derived series]] — the commutator subgroup taken again and again — which gives [[§49 The Derived Series#^thm-49-1|an algorithm for testing solvability]].

The last part of the chapter turns to the Sylow theorems. [[§29 The Index and Lagrange's Theorem#^thm-29-2|Lagrange's theorem]] says that the [[§4 Subgroups#^def-4-6|order]] of a [[§4 Subgroups#^def-4-1|subgroup]] divides $|G|$, and [[§29 The Index and Lagrange's Theorem#^ex-29-1|its converse fails]]; Cauchy's theorem ([[§29 The Index and Lagrange's Theorem#^thm-29-6|Theorem §29.6]]) recovers it for primes. The Sylow theorems treat the largest power of a prime $p$ dividing $|G|$: [[§52 The Sylow Theorems#^thm-52-4|subgroups of that order exist]], and [[§52 The Sylow Theorems#^thm-52-6|any two are conjugate]]. The course's route to them is to embed a finite group into a large matrix group over $\mathbb{F}_p$, where such a subgroup can be written down explicitly ([[§51 p-Groups and Sylow Subgroups#^prop-51-5|the unitriangular matrices]]), and pull it back with a fixed-point argument ([[§52 The Sylow Theorems#^lem-52-1|Lemma §52.1]]).

**Builds on:** [[· 1 Groups and Subgroups|1 Groups and Subgroups]] (26), [[· 2 Arithmetic Modulo n|2 Arithmetic Modulo n]] (6), [[· 3 Permutations|3 Permutations]] (2), [[· 4 Homomorphisms and Isomorphisms|4 Homomorphisms and Isomorphisms]] (18), [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (19), [[· 6 Group Actions, Cosets, and Lagrange's Theorem|6 Group Actions, Cosets, and Lagrange's Theorem]] (35), [[· 7 Conjugacy and the Center|7 Conjugacy and the Center]] (12), [[· 8 Normal Subgroups and Quotient Groups|8 Normal Subgroups and Quotient Groups]] (40), [[· 10 Semidirect Products|10 Semidirect Products]] (1)
**Used by:** [[· 5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups|5 Homomorphisms at Work꞉ Matrices, Signs, and Unit Groups]] (1), [[· 8 Normal Subgroups and Quotient Groups|8 Normal Subgroups and Quotient Groups]] (1), [[· 10 Semidirect Products|10 Semidirect Products]] (2), [[· 11 Composition Series|11 Composition Series]] (1)
**Builds on (other subjects):** [[Linear Algebra]] (2)

## Sections
- [[§46 Characters]]
- [[§47 Commutators]]
- [[§48 Solvable Groups]]
- [[§49 The Derived Series]]
- [[§50 S₃, S₄, Aₙ and GLₙ]]
- [[§51 p-Groups and Sylow Subgroups]]
- [[§52 The Sylow Theorems]]
- [[§53 Simple Groups of Small Order]]

## Central results
- [[Groups of Order p²]] (§51.7)
- [[First Sylow Theorem]] (§52.4)
- [[Second Sylow Theorem]] (§52.6)
- [[Third Sylow Theorem]] (§52.9)
- [[Groups of Order pq]] (§52.11)

## Load-bearing results
Ranked by how many later results depend on them (through the proofs' citations).
- [[§46 Characters#^thm-46-2|Theorem §46.2: A Common Eigenvector Yields a Character]]: 17 later results
- [[§52 The Sylow Theorems#^prop-52-3|Proposition §52.3: Sylow Subgroups of a Subgroup]]: 14 later results
- [[Second Sylow Theorem|Theorem §52.6: The Second Sylow Theorem]]: 12 later results
- [[§51 p-Groups and Sylow Subgroups#^lem-51-2|Lemma §51.2: Invertible Matrices Have Independent Columns]]: 11 later results
