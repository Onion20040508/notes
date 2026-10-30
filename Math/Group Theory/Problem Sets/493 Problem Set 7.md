---
type: problem-set
subject: "[[Group Theory]]"
problem_set: 7
tags: [group-theory, math493]
---
← [[493 Problem Set 6]] · ↑ [[Group Theory]]

# Problem Set 7

*Due Thursday, October 29; submitted. Each problem is treated in the main text, at the location indicated.*

> [!question] Problem 7.1: Subgroups of $A_n$ and Simple Groups of Order $60$
> Let $n \geq 5$ and let $H$ be a subgroup of $A_n$, other than $A_n$ itself.
>
> 1. Show that $[A_n : H] \geq n$. Hint: Think about $H$ acting on $A_n/H$.
> 2. Suppose that $[A_n : H] = n$. Show that $H \cong A_{n-1}$. Hint: Think harder about $H$ acting on $A_n/H$.
>
> In particular, now let $G$ be a simple group of order $60$.
>
> 3. Use the $5$-Sylows to show that $G$ is a subgroup of $A_6$, and conclude that $G \cong A_5$.

^hw-7-1

*Treated in [[§56 Simple Groups of Small Order|§56]] (Proposition [[§56 Simple Groups of Small Order#^prop-56-10|§56.10]], Lemma [[§56 Simple Groups of Small Order#^lem-56-11|§56.11]], Proposition [[§56 Simple Groups of Small Order#^prop-56-12|§56.12]], Theorem [[§56 Simple Groups of Small Order#^thm-56-13|§56.13]]).*

> [!question] Problem 7.2: Groups of Order $2 \bmod 4$
> Let $G$ be a finite group with $|G| \equiv 2 \bmod 4$ and $|G| > 2$. In this problem, we will show that $G$ is not simple. In particular, this shows that there are no simple groups of order $30$ or $90$.
>
> 1. Show that $G$ contains an element $t$ of order $2$.
>
> Let $G$ act on itself by left multiplication. This gives an embedding $\phi : G \to S_{4k+2}$ (as in Problem 3.1).
>
> 2. Show that $\operatorname{sgn} \phi(t) = -1$.
> 3. Explain why this means that $G$ is not simple.

^hw-7-2

*Treated in [[§56 Simple Groups of Small Order|§56]] (Proposition [[§56 Simple Groups of Small Order#^prop-56-7|§56.7]]).*

> [!question] Problem 7.3: No Simple Group of Order $56$
> In this problem, we will show that there are no simple groups of order $56$. Suppose, to the contrary, that $G$ is a simple group of order $56$.
>
> 1. Show that $G$ has eight $7$-Sylow subgroups and seven $2$-Sylow subgroups.
>
> Let $P_1, P_2, \dots, P_7$ be the $2$-Sylows, and let $Q_1, Q_2, \dots, Q_8$ be the $7$-Sylows.
>
> 2. Show that $|P_1 \cup P_2| \geq 12$ and that $|Q_1 \cup Q_2 \cup \cdots \cup Q_8| = 49$.
> 3. Deduce a contradiction.
>
> This kind of counting elements approach can also handle a number of other cases – for example, you might enjoy working it out for $30$. I enjoy the hands on concreteness, but it is harder to state it as a general tool.

^hw-7-3

*Treated in [[§56 Simple Groups of Small Order|§56]] (Proposition [[§56 Simple Groups of Small Order#^prop-56-8|§56.8]]).*

> [!question] Problem 7.4: Two Normal Subgroups with Simple Quotients
> Let $G$ be a finite group and let $N_1$ and $N_2$ be distinct normal subgroups (so $N_1 \neq N_2$). Assume that $G/N_1$ and $G/N_2$ are both simple. We will show that $G/N_1 \cong N_2/(N_1 \cap N_2)$ and $G/N_2 \cong N_1/(N_1 \cap N_2)$. I expect to use this lemma in Friday's class.
>
> 1. Show that $N_1 N_2 = G$.
> 2. Show that $G/N_1 \cong N_2/(N_1 \cap N_2)$ and $G/N_2 \cong N_1/(N_1 \cap N_2)$, as claimed.
>
> Remark: We can further show, in this situation, that $G/(N_1 \cap N_2) \cong N_1/(N_1 \cap N_2) \times N_2/(N_1 \cap N_2)$.

^hw-7-4

*Treated in [[§50 Composition Series|§50]] (Lemma [[§50 Composition Series#^lem-50-3|§50.3]]).*
