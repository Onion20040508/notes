---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 39
tags: [applied-linear-algebra, math235]
---
← [[§38 Applications to Markov Chains]] · ↑ [[· 4 Vector Spaces]] · [[§40 Eigenvectors and Eigenvalues]] →

*Lay, Sections 4.1, 4.4, 4.8 and 4.9 (examples revisited) · MATH 235 lectures L13, L14, L15, L18.*

*The recurring examples of Chapter 4, gathered in course order: the Fibonacci numbers and the city–suburb migration. Each part embeds the chapter's items about one example; the items themselves stay in their sections.*

## The Fibonacci Numbers

The Fibonacci recursion $x_{n+1} = x_n + x_{n-1}$ recurs through Chapter 4.

The sequences satisfying the recursion form a subspace of the space of sequences, part (e) below.

![[§29 Vector Spaces and Subspaces#^ex-29-2]]

This subspace is isomorphic to $\mathbb{R}^2$, part (c) below: a sequence is determined by its first two terms.

![[§32 Coordinate Systems#^ex-32-3]]

The auxiliary equation $r^2 - r - 1 = 0$ gives a fundamental set of solutions, the closed formula for $F_k$, and the limit of $F_{k+1}/F_k$, the golden ratio.

![[§37 Solution Sets of Linear Difference Equations#^ex-37-2]]

*Chain: later in [[§40 Eigenvectors and Eigenvalues#^ex-40-4|Chapter 5]]*

## City and Suburbs

The migration matrix $M$ of [[§11 Linear Models in Business, Science, and Engineering#^ex-11-3|Example §11.3]] is a stochastic matrix, so the populations of the city and its suburbs form a Markov chain.

![[§38 Applications to Markov Chains#^ex-38-1]]

Its steady-state vector is part (b) below.

![[§38 Applications to Markov Chains#^ex-38-4]]

*Chain: earlier in [[§11 Linear Models in Business, Science, and Engineering#^ex-11-3|Chapter 1]] · later in [[§41 The Characteristic Equation#^ex-41-4|Chapter 5]]*
