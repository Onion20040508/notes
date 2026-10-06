---
type: section
subject: "[[Calculus]]"
chapter: 9
section: "62a"
tags: [calculus]
---
← [[§62 Predator-Prey Systems]] · ↑ [[· 9 Differential Equations]] · [[§63 Curves Defined by Parametric Equations]] →

*Stewart, Sections 9.2, 9.3 and 9.5 (examples revisited).*

## The RL Circuit

Chapter 9 returns three times to the same electric circuit: a battery or generator, a resistor of $12\ \Omega$ and an inductor of $4$ H, with the switch closed at $t = 0$. Each section treats it with its own method. The circuit equation $L\,dI/dt + RI = E(t)$ is first read off a direction field and approximated by Euler's method:

![[§58 Direction Fields and Euler's Method#^def-58-2]]

![[§58 Direction Fields and Euler's Method#^ex-58-2]]

![[§58 Direction Fields and Euler's Method#^ex-58-4]]

With a constant voltage the equation is separable, and [[§59 Separable Equations|§59]] solves it exactly: $I(t) = 5 - 5e^{-3t}$. As a first-order linear equation it is solved with an integrating factor, for a battery and for a generator:

![[§61 Linear Equations#^def-61-3]]

![[§61 Linear Equations#^ex-61-4]]

![[§61 Linear Equations#^ex-61-5]]
