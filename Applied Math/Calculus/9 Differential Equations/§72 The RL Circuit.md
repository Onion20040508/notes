---
type: section
subject: "[[Calculus]]"
chapter: 9
section: 72
tags: [calculus]
---
← [[§71 Predator-Prey Systems]] · ↑ [[· 9 Differential Equations]] · [[§73 Curves Defined by Parametric Equations]] →

*Stewart, Sections 9.2, 9.3 and 9.5 (examples revisited).*

## The RL Circuit

Chapter 9 returns three times to the same electric circuit: a battery or generator, a resistor of $12\ \Omega$ and an inductor of $4$ H, with the switch closed at $t = 0$. Each section treats it with its own method. The circuit equation $L\,dI/dt + RI = E(t)$ is first read off a direction field and approximated by Euler's method:

![[§67 Direction Fields and Euler's Method#^def-67-2]]

![[§67 Direction Fields and Euler's Method#^ex-67-2]]

![[§67 Direction Fields and Euler's Method#^ex-67-4]]

With a constant voltage the equation is separable, and [[§68 Separable Equations|§68]] solves it exactly: $I(t) = 5 - 5e^{-3t}$. As a first-order linear equation it is solved with an integrating factor, for a battery and for a generator:

![[§70 Linear Equations#^def-70-3]]

![[§70 Linear Equations#^ex-70-4]]

![[§70 Linear Equations#^ex-70-5]]
