---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: "31a"
tags: [applied-linear-algebra, math235]
---
← [[§31 Applications to Markov Chains]] · ↑ [[· 4 Vector Spaces]] · [[§32 Eigenvectors and Eigenvalues]] →

*Lay, Sections 4.1, 4.4, 4.8 and 4.9 (examples revisited) · MATH 235 lectures L13, L14, L15, L18.*

*The recurring examples of Chapter 4, gathered in course order: the Fibonacci numbers and the city–suburb migration. Each part embeds the chapter's items about one example; the items themselves stay in their sections.*

## The Fibonacci Numbers

The Fibonacci recursion $x_{n+1} = x_n + x_{n-1}$ recurs through Chapter 4.

The sequences satisfying the recursion form a subspace of the space of sequences, part (e) below.

![[§23 Vector Spaces and Subspaces#^ex-23-2]]

This subspace is isomorphic to $\mathbb{R}^2$, part (c) below: a sequence is determined by its first two terms.

![[§26 Coordinate Systems#^ex-26-3]]

The auxiliary equation $r^2 - r - 1 = 0$ gives a fundamental set of solutions, the closed formula for $F_k$, and the limit of $F_{k+1}/F_k$, the golden ratio.

![[§30a Solution Sets of Linear Difference Equations#^ex-30-4]]

*Chain: later in [[§32 Eigenvectors and Eigenvalues#^ex-32-4|Chapter 5]]*

## City and Suburbs

The migration matrix $M$ of [[§10 Linear Models in Business, Science, and Engineering#^ex-10-3|Example §10.3]] is a stochastic matrix, so the populations of the city and its suburbs form a Markov chain.

![[§31 Applications to Markov Chains#^ex-31-1]]

Its steady-state vector is part (b) below.

![[§31 Applications to Markov Chains#^ex-31-4]]

*Chain: earlier in [[§10 Linear Models in Business, Science, and Engineering#^ex-10-3|Chapter 1]] · later in [[§33 The Characteristic Equation#^ex-33-4|Chapter 5]]*
