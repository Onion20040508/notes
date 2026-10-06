---
type: section
subject: "[[Logic and Proofs]]"
chapter: 5
section: "22b"
tags: [logic-and-proofs, mat250]
---
← [[§22a Constructing ℚ and ℤ]] · ↑ [[· 5 Modular Arithmetic]] · [[§23 The Sequence of Prime Numbers]] →

*The congruence $290x \equiv 5 \pmod357$ is the textbook's worked example of the Euclidean-algorithm method for linear congruences. Its appearances are gathered here in course order; the items themselves stay in their sections.*

The Euclidean algorithm on $357$ and $290$ gives $290 \times (-16) + 357 \times 13 = 1$, and multiplying by $5$ solves the congruence: $x \equiv 277 \pmod357$.

![[§20 Linear Congruences#^ex-20-4]]

The same identity says that $290$ is invertible modulo $357$ with inverse $[-16]_{357} = [341]_{357}$, so every congruence $290x \equiv b \pmod357$ is solved by $x \equiv -16\, b$, part (c) below:

![[§21 Congruence Classes and the Arithmetic of Remainders#^ex-21-5]]
