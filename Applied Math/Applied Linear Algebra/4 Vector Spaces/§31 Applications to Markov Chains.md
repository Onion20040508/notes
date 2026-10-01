---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 4
section: 31
lay: "4.9"
aliases: ["Lay 4.9"]
tags: [applied-linear-algebra, math235]
---
← [[§30 Applications to Difference Equations]] · ↑ [[· 4 Vector Spaces]] · [[§32 Eigenvectors and Eigenvalues]] →

*Lay, Section 4.9 · MATH 235 lecture L18.*

A Markov chain models an experiment or measurement repeated many times in the same way, where each outcome is one of finitely many states and depends only on the outcome just before. The state is a probability vector $\mathbf{x}_k$, and one step multiplies it by a stochastic matrix: $\mathbf{x}_{k+1} = P\mathbf{x}_k$, a first-order difference equation as in [[§30 Applications to Difference Equations#^prop-30-8|Proposition §30.8]]. Such chains are used in biology, business, chemistry, engineering and physics. The interesting question is the long run. A steady-state vector $\mathbf{q}$ with $P\mathbf{q} = \mathbf{q}$ is found by solving the homogeneous system $(P - I)\mathbf{x} = \mathbf{0}$, and for a regular stochastic matrix every chain converges to it, whatever the initial state.

## Markov Chains

> [!definition] Definition §31.1: Probability Vector; Stochastic Matrix
> A **probability vector** is a vector with nonnegative entries that add up to $1$. A **stochastic matrix** is a square matrix whose columns are probability vectors.
>
> *Lay: 4.9 (text)*

^def-31-1

> [!definition] Definition §31.2: Markov Chain; State Vector
> A **Markov chain** is a sequence of probability vectors $\mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots$ together with a stochastic matrix $P$ such that
>
> $$
> \mathbf{x}_1 = P\mathbf{x}_0, \quad \mathbf{x}_2 = P\mathbf{x}_1, \quad \mathbf{x}_3 = P\mathbf{x}_2, \quad \ldots ,
> $$
>
> that is, by the first-order difference equation
>
> $$
> \mathbf{x}_{k+1} = P\mathbf{x}_k \qquad \text{for } k = 0, 1, 2, \ldots
> $$
>
> When a Markov chain of vectors in $\mathbb{R}^n$ describes a system or a sequence of experiments, the entries of $\mathbf{x}_k$ list the probabilities that the system is in each of $n$ possible states, or that the outcome of the experiment is each of $n$ possible outcomes. For this reason $\mathbf{x}_k$ is called a **state vector**. Entry $(i, j)$ of $P$ is the probability of a transition from state $j$ to state $i$: column = "from", row = "to".
>
> *Lay: 4.9 (text)*

^def-31-2

> [!theorem] Proposition §31.1: Stochastic Matrices Preserve Probability Vectors
> Let $P$ be an $n \times n$ stochastic matrix and $S = [1\ 1\ \cdots\ 1]$ the $1 \times n$ row of ones.
> 1. A vector $\mathbf{x} \in \mathbb{R}^n$ is a probability vector if and only if its entries are nonnegative and $S\mathbf{x} = 1$; and $SP = S$.
> 2. If $\mathbf{x}$ is a probability vector, so is $P\mathbf{x}$. Every power $P^k$ is stochastic.
> 3. In a Markov chain, $\mathbf{x}_k = P^k\mathbf{x}_0$ for $k = 0, 1, 2, \ldots$, and every $\mathbf{x}_k$ is a probability vector.
>
> *Lay: 4.9, Exercises 19 and 20; Numerical Note*

^prop-31-1

> [!proof]+ Proof
> 1. $S\mathbf{x}$ is the sum of the entries of $\mathbf{x}$. The $j$th entry of $SP$ is $S$ times column $j$ of $P$, the sum of the entries of a probability vector, which is $1$. So $SP = S$.
>
> 2. The entries of $P\mathbf{x}$ are sums of products of nonnegative numbers, so they are nonnegative, and $S(P\mathbf{x}) = (SP)\mathbf{x} = S\mathbf{x} = 1$. Column $j$ of $P^2 = P \cdot P$ is $P$ times column $j$ of $P$, a probability vector, so $P^2$ is stochastic; induction gives $P^k$.
>
> 3. $\mathbf{x}_2 = P\mathbf{x}_1 = P(P\mathbf{x}_0) = P^2\mathbf{x}_0$, and in general $\mathbf{x}_k = P\mathbf{x}_{k-1} = P \cdot P^{k-1}\mathbf{x}_0 = P^k\mathbf{x}_0$ by induction. Each is a probability vector by 2.

^pf-31-1

*Uses:* [[§31 Applications to Markov Chains#^def-31-1|Def. §31.1]], [[§11 Matrix Operations#^prop-11-3|§11.3]] (columns of a product)

> [!remark]- Remark: Numerical Note — Powers or Steps
> To compute a specific vector such as $\mathbf{x}_3$, fewer arithmetic operations are needed to compute $\mathbf{x}_1$, $\mathbf{x}_2$, $\mathbf{x}_3$ one step at a time than to compute $P^3$ and then $P^3\mathbf{x}_0$. For a small matrix (say $30 \times 30$) the machine time is insignificant either way, and a command computing $P^3\mathbf{x}_0$ may be preferred because it takes fewer keystrokes.

^rem-31-1

> [!example] Example §31.1: Migration Between a City and Its Suburbs
> Section 1.10 ([[§10 Linear Models in Business, Science, and Engineering#^ex-10-3|Example §10.3]]) modeled the population movement between a city and its suburbs with the *migration matrix*
>
> $$
> M = \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix} \qquad \text{(columns: from City, Suburbs; rows: to City, Suburbs)} .
> $$
>
> Each year $5\%$ of the city population moves to the suburbs, and $3\%$ of the suburban population moves to the city. The columns of $M$ are probability vectors, so $M$ is stochastic. In 2014 the region had $600{,}000$ people in the city and $400{,}000$ in the suburbs. What is the distribution in 2015? In 2016?
>
> After one year the population vector becomes
>
> $$
> \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix} \begin{bmatrix} 600{,}000 \\ 400{,}000 \end{bmatrix} = \begin{bmatrix} 570{,}000 + 12{,}000 \\ 30{,}000 + 388{,}000 \end{bmatrix} = \begin{bmatrix} 582{,}000 \\ 418{,}000 \end{bmatrix} .
> $$
>
> Divide by the total of $1$ million, using $kM\mathbf{x} = M(k\mathbf{x})$: with $\mathbf{x}_0 = \begin{bmatrix} .60 \\ .40 \end{bmatrix}$ (the fractions in city and suburbs),
>
> $$
> \mathbf{x}_1 = M\mathbf{x}_0 = \begin{bmatrix} .582 \\ .418 \end{bmatrix} ,
> $$
>
> so in 2015, $58.2\%$ of the region lived in the city and $41.8\%$ in the suburbs. For 2016,
>
> $$
> \mathbf{x}_2 = M\mathbf{x}_1 = \begin{bmatrix} .95(.582) + .03(.418) \\ .05(.582) + .97(.418) \end{bmatrix} = \begin{bmatrix} .55290 + .01254 \\ .02910 + .40546 \end{bmatrix} = \begin{bmatrix} .56544 \\ .43456 \end{bmatrix} \approx \begin{bmatrix} .565 \\ .435 \end{bmatrix} .
> $$
>
> *Lay: Example 4.9.1*

^ex-31-1

> [!example] Example §31.2: Voting Patterns
> The outcome of a congressional election at a voting precinct is recorded every two years by a vector $\mathbf{x} \in \mathbb{R}^3$ listing the fractions voting Democratic (D), Republican (R) and Libertarian (L). If the outcome of one election depends only on the preceding one, the sequence of these vectors may be a Markov chain. Take the stochastic matrix
>
> $$
> P = \begin{bmatrix} .70 & .10 & .30 \\ .20 & .80 & .30 \\ .10 & .10 & .40 \end{bmatrix} \qquad \text{(columns: from D, R, L; rows: to D, R, L)} .
> $$
>
> Column D says: of those who voted D, $70\%$ vote D again next time, $20\%$ vote R and $10\%$ vote L. If one election gives $\mathbf{x}_0 = (.55, .40, .05)$, what are the likely outcomes of the next two elections?
>
> $$
> \mathbf{x}_1 = P\mathbf{x}_0 = \begin{bmatrix} .385 + .040 + .015 \\ .110 + .320 + .015 \\ .055 + .040 + .020 \end{bmatrix} = \begin{bmatrix} .440 \\ .445 \\ .115 \end{bmatrix},
> \qquad
> \mathbf{x}_2 = P\mathbf{x}_1 = \begin{bmatrix} .3080 + .0445 + .0345 \\ .0880 + .3560 + .0345 \\ .0440 + .0445 + .0460 \end{bmatrix} = \begin{bmatrix} .3870 \\ .4785 \\ .1345 \end{bmatrix} .
> $$
>
> So $44\%$ will vote D, $44.5\%$ R and $11.5\%$ L in the next election, and $38.7\%$, $47.8\%$, $13.5\%$ in the one after.
>
> **Why $\mathbf{x}_1$ is right.** Suppose $1000$ people voted in the first election: $550$ D, $400$ R, $50$ L. Next time $70\%$ of the $550$ vote D again, $10\%$ of the $400$ switch from R to D, and $30\%$ of the $50$ switch from L to D, so the D vote is
>
> $$
> .70(550) + .10(400) + .30(50) = 385 + 40 + 15 = 440 ,
> $$
>
> that is, $44\%$. This is exactly the computation of the first entry of $P\mathbf{x}_0$; the other entries are analogous.
>
> *Lay: Example 4.9.2*

^ex-31-2

## Predicting the Distant Future

The most interesting aspect of a Markov chain is its long-term behavior: what happens to the voting after many elections, or to the population distribution "in the long run"?

> [!example] Example §31.3: A Chain That Settles Down
> Let $P = \begin{bmatrix} .5 & .2 & .3 \\ .3 & .8 & .3 \\ .2 & 0 & .4 \end{bmatrix}$ and $\mathbf{x}_0 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$. What happens to the system $\mathbf{x}_{k+1} = P\mathbf{x}_k$ as time passes?
>
> $$
> \mathbf{x}_1 = P\mathbf{x}_0 = \begin{bmatrix} .5 \\ .3 \\ .2 \end{bmatrix}, \quad
> \mathbf{x}_2 = P\mathbf{x}_1 = \begin{bmatrix} .25 + .06 + .06 \\ .15 + .24 + .06 \\ .10 + 0 + .08 \end{bmatrix} = \begin{bmatrix} .37 \\ .45 \\ .18 \end{bmatrix}, \quad
> \mathbf{x}_3 = P\mathbf{x}_2 = \begin{bmatrix} .329 \\ .525 \\ .146 \end{bmatrix} .
> $$
>
> Further steps (rounded to four or five significant figures):
>
> | $k$ | $4$ | $5$ | $6$ | $7$ | $8$ | $10$ | $12$ | $15$ |
> |---|---|---|---|---|---|---|---|---|
> | $x_{k,1}$ | $.3133$ | $.3064$ | $.3032$ | $.3016$ | $.3008$ | $.3002$ | $.30005$ | $.30001$ |
> | $x_{k,2}$ | $.5625$ | $.5813$ | $.5906$ | $.5953$ | $.5977$ | $.5994$ | $.59985$ | $.59998$ |
> | $x_{k,3}$ | $.1242$ | $.1123$ | $.1062$ | $.1031$ | $.1016$ | $.1004$ | $.10010$ | $.10001$ |
>
> The vectors seem to approach $\mathbf{q} = (.3, .6, .1)$, and the probabilities hardly change from one $k$ to the next. The following calculation is exact:
>
> $$
> P\mathbf{q} = \begin{bmatrix} .15 + .12 + .03 \\ .09 + .48 + .03 \\ .06 + 0 + .04 \end{bmatrix} = \begin{bmatrix} .30 \\ .60 \\ .10 \end{bmatrix} = \mathbf{q} .
> $$
>
> When the system is in state $\mathbf{q}$, nothing changes from one measurement to the next. Also, every entry of
>
> $$
> P^2 = \begin{bmatrix} .37 & .26 & .33 \\ .45 & .70 & .45 \\ .18 & .04 & .22 \end{bmatrix}
> $$
>
> is strictly positive, so $P$ is regular (Definition §31.4), and Theorem §31.3 explains the convergence.
>
> *Lay: Example 4.9.3 and 4.9 (text)*

^ex-31-3

![[m235-31-1.svg]]
*Example §31.3: the three entries of $\mathbf{x}_k$ for $k = 0, 1, \ldots, 15$, starting from $\mathbf{x}_0 = (1, 0, 0)$. They level off at the entries $.3$, $.6$, $.1$ of the steady-state vector $\mathbf{q}$ (dashed). At every $k$ the three values add up to $1$.*

## Steady-State Vectors

> [!definition] Definition §31.3: Steady-State Vector
> If $P$ is a stochastic matrix, a **steady-state vector** (or **equilibrium vector**) for $P$ is a probability vector $\mathbf{q}$ such that
>
> $$
> P\mathbf{q} = \mathbf{q} .
> $$
>
> In Example §31.3, $\mathbf{q} = (.3, .6, .1)$ is a steady-state vector for $P$.
>
> *Lay: 4.9 (text)*

^def-31-3

> [!theorem] Proposition §31.2: Every Stochastic Matrix Has a Steady-State Vector
> Let $P$ be an $n \times n$ stochastic matrix. Then $P\mathbf{x} = \mathbf{x}$ has a nontrivial solution, and in fact $P$ has a steady-state vector.
>
> *Lay: 4.9 (text, "it can be shown"); Exercise 17*

^prop-31-2

> [!proof]+ Proof
> **A nontrivial solution** (Lay, Exercise 17). Each column of $P$ sums to $1$, so each column of $P - I$ sums to $0$. Hence if all the other rows of $P - I$ are added to the bottom row, the result is a row of zeros: the rows of $P - I$ are linearly dependent. So $\dim \operatorname{Row}(P - I) < n$, that is, $\operatorname{rank}(P - I) < n$, and by the Rank Theorem ([[§28 Rank#^thm-28-3|Theorem §28.3]]) $\dim \operatorname{Nul}(P - I) \ge 1$: $P\mathbf{x} = \mathbf{x}$ has a nontrivial solution.
>
> **A probability vector among the solutions.** Lay leaves this to advanced texts; here is a short argument. Fix a probability vector $\mathbf{x}_0$ and form the averages
>
> $$
> \mathbf{a}_N = \frac{1}{N}\big(\mathbf{x}_0 + P\mathbf{x}_0 + \cdots + P^{N-1}\mathbf{x}_0\big), \qquad N = 1, 2, \ldots
> $$
>
> Each $P^k\mathbf{x}_0$ is a probability vector (Proposition §31.1), so $\mathbf{a}_N$ has nonnegative entries adding up to $\frac{1}{N} \cdot N = 1$: it is a probability vector. Telescoping,
>
> $$
> P\mathbf{a}_N - \mathbf{a}_N = \frac{1}{N}\big(P^N\mathbf{x}_0 - \mathbf{x}_0\big) ,
> $$
>
> and the entries of probability vectors lie in $[0, 1]$, so every entry of $P\mathbf{a}_N - \mathbf{a}_N$ has absolute value at most $1/N$. The probability vectors form a bounded set in $\mathbb{R}^n$, so by the Bolzano–Weierstrass theorem some subsequence $\mathbf{a}_{N_j}$ converges to a vector $\mathbf{q}$. Limits preserve "entries $\ge 0$" and "entries add up to $1$", so $\mathbf{q}$ is a probability vector, and since $\mathbf{x} \mapsto P\mathbf{x} - \mathbf{x}$ is linear, hence continuous,
>
> $$
> P\mathbf{q} - \mathbf{q} = \lim_{j \to \infty} \big(P\mathbf{a}_{N_j} - \mathbf{a}_{N_j}\big) = \mathbf{0} .
> $$

^pf-31-2

*Uses:* [[§28 Rank#^thm-28-3|§28.3]], [[§31 Applications to Markov Chains#^prop-31-1|§31.1]], [[§13 Some Topological Concepts in Metric Spaces#^thm-13-3|451 Thm. §13.3]] (Bolzano–Weierstrass in ℝⁿ)

> [!remark] Remark: Method — Finding a Steady-State Vector
> 1. Form $P - I$ by subtracting $1$ from each diagonal entry of $P$.
> 2. Row reduce the augmented matrix $[\,(P - I)\ \ \mathbf{0}\,]$. With decimal entries, first multiply each row of the *augmented matrix* by $10$ (not $P$ alone, which would change the equation).
> 3. Write the general solution of $(P - I)\mathbf{x} = \mathbf{0}$, and choose a convenient basis vector $\mathbf{w}$ of the solution space, preferably with integer entries.
> 4. Divide $\mathbf{w}$ by the sum of its entries: $\mathbf{q} = \mathbf{w}/(w_1 + \cdots + w_n)$. Check $P\mathbf{q} = \mathbf{q}$.

^rem-31-2

> [!example] Example §31.4: Finding Steady-State Vectors
> **(a)** Find a steady-state vector for $P = \begin{bmatrix} .6 & .3 \\ .4 & .7 \end{bmatrix}$.
>
> Solve $P\mathbf{x} = \mathbf{x}$, that is, $P\mathbf{x} - I\mathbf{x} = \mathbf{0}$, or $(P - I)\mathbf{x} = \mathbf{0}$:
>
> $$
> P - I = \begin{bmatrix} .6 & .3 \\ .4 & .7 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -.4 & .3 \\ .4 & -.3 \end{bmatrix},
> \qquad
> \begin{bmatrix} -.4 & .3 & 0 \\ .4 & -.3 & 0 \end{bmatrix} \sim \begin{bmatrix} -.4 & .3 & 0 \\ 0 & 0 & 0 \end{bmatrix} \sim \begin{bmatrix} 1 & -3/4 & 0 \\ 0 & 0 & 0 \end{bmatrix} .
> $$
>
> So $x_1 = \frac34 x_2$ with $x_2$ free, and the general solution is $x_2\begin{bmatrix} 3/4 \\ 1 \end{bmatrix}$. A basis vector without fractions is $\mathbf{w} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$ ($x_2 = 4$). Every solution is a multiple of $\mathbf{w}$, and the one whose entries add up to $1$ is
>
> $$
> \mathbf{q} = \frac{1}{3 + 4}\,\mathbf{w} = \begin{bmatrix} 3/7 \\ 4/7 \end{bmatrix} .
> \qquad \text{Check: } P\mathbf{q} = \begin{bmatrix} 18/70 + 12/70 \\ 12/70 + 28/70 \end{bmatrix} = \begin{bmatrix} 30/70 \\ 40/70 \end{bmatrix} = \mathbf{q} .
> $$
>
> **(b)** The migration matrix $M$ of Example §31.1. Here $M - I = \begin{bmatrix} -.05 & .03 \\ .05 & -.03 \end{bmatrix}$; the second row is $-1$ times the first, and the first gives $x_1 = \frac35 x_2$. With $x_2 = 5$, $\mathbf{w} = (3, 5)$ and
>
> $$
> \mathbf{q} = \frac18 \begin{bmatrix} 3 \\ 5 \end{bmatrix} = \begin{bmatrix} .375 \\ .625 \end{bmatrix},
> \qquad
> M\mathbf{q} = \begin{bmatrix} .35625 + .01875 \\ .01875 + .60625 \end{bmatrix} = \begin{bmatrix} .375 \\ .625 \end{bmatrix} = \mathbf{q} .
> $$
>
> For a region of $1$ million people this means $375{,}000$ in the city and $625{,}000$ in the suburbs. In one year $(.05)(375{,}000) = 18{,}750$ people leave the city and $(.03)(625{,}000) = 18{,}750$ move in from the suburbs, so both populations stay the same.
>
> *Lay: Examples 4.9.5 and 4.9.4*

^ex-31-4

> [!definition] Definition §31.4: Regular Stochastic Matrix; Convergence
> A stochastic matrix $P$ is **regular** if some matrix power $P^k$ contains only strictly positive entries. A sequence of vectors $\{\mathbf{x}_k : k = 1, 2, \ldots\}$ **converges** to a vector $\mathbf{q}$ as $k \to \infty$ if the entries of $\mathbf{x}_k$ can be made as close as desired to the corresponding entries of $\mathbf{q}$ by taking $k$ sufficiently large.
>
> *Lay: 4.9 (text)*

^def-31-4

> [!remark]- Connections
> - Convergence of a vector sequence is convergence of each entry as a sequence of numbers, [[§69 Sequences#^def-69-2|Calc Def. §69.2]] (precise form [[§69 Sequences#^def-69-3|Calc Def. §69.3]]).

> [!theorem] Theorem §31.3: Convergence to the Steady State
> If $P$ is an $n \times n$ regular stochastic matrix, then $P$ has a unique steady-state vector $\mathbf{q}$. Further, if $\mathbf{x}_0$ is any initial state and $\mathbf{x}_{k+1} = P\mathbf{x}_k$ for $k = 0, 1, 2, \ldots$, then the Markov chain $\{\mathbf{x}_k\}$ converges to $\mathbf{q}$ as $k \to \infty$.
>
> *Lay: Theorem 18 (4.9)*

^thm-31-3

*Lay omits the proof ("proved in standard texts on Markov chains"); Section 5.2 ([[§33 The Characteristic Equation#^ex-33-4|Example §33.4]]) shows why it holds for several of the stochastic matrices studied here. It is a case of the Perron–Frobenius theorem (stated in lecture L18; [[§32 Eigenvectors and Eigenvalues#^rem-32-2|Remark: The Perron–Frobenius Theorem]]), which is not proved in the vault.*

The striking part of the theorem is that the initial state has no effect on the long-term behavior of the chain.

> [!remark] Remark: Why It Works
> Lecture L18 explains the picture for a $2 \times 2$ matrix $A$ with positive entries. $A$ maps the closed first quadrant $\mathbb{R}^2_+$ into a narrower cone $A(\mathbb{R}^2_+)$, the region between the rays through the columns $A\mathbf{e}_1$ and $A\mathbf{e}_2$. Then $A^2(\mathbb{R}^2_+) = A(A(\mathbb{R}^2_+))$ is narrower still, and so on: the cones $A^k(\mathbb{R}^2_+)$ close down on a single ray, by the Perron–Frobenius theorem the ray of a vector $\mathbf{u}$ with positive entries and $A\mathbf{u} = \lambda\mathbf{u}$, $\lambda > 0$. So the direction of $A^k\mathbf{x}$ approaches that of $\mathbf{u}$ for every $\mathbf{x}$ in the quadrant. For a regular stochastic $P$ the same holds in $\mathbb{R}^n$. Here $\lambda = 1$: adding up the entries of $P\mathbf{u} = \lambda\mathbf{u}$ gives $S\mathbf{u} = \lambda S\mathbf{u}$ by $SP = S$ (Proposition §31.1), and $S\mathbf{u} > 0$. Since every $\mathbf{x}_k$ is a probability vector, its entries add up to $1$, so not only the direction but the vector itself converges: to the multiple $\mathbf{q}$ of $\mathbf{u}$ whose entries add up to $1$.
>
> *Source: 235 lecture L18*

^rem-31-3

> [!example] Example §31.5: The Voting Pattern in the Long Run
> In Example §31.2, what percentage of the voters are likely to vote for the Republican candidate in some election many years from now, assuming the election outcomes form a Markov chain?
>
> **The wrong approach** for hand computation: pick some $\mathbf{x}_0$ and compute $\mathbf{x}_1, \ldots, \mathbf{x}_k$ for a large $k$. There is no way of knowing how many vectors to compute, and the limiting values remain uncertain.
>
> **The right approach:** compute the steady-state vector and appeal to Theorem §31.3 ($P$ has only positive entries, so it is regular with $k = 1$). Subtract $1$ from each diagonal entry of $P$ and multiply the augmented matrix by $10$:
>
> $$
> [\,(P - I)\ \ \mathbf{0}\,] = \begin{bmatrix} -.3 & .1 & .3 & 0 \\ .2 & -.2 & .3 & 0 \\ .1 & .1 & -.6 & 0 \end{bmatrix},
> \qquad
> \begin{bmatrix} -3 & 1 & 3 & 0 \\ 2 & -2 & 3 & 0 \\ 1 & 1 & -6 & 0 \end{bmatrix} .
> $$
>
> Interchange rows 1 and 3, then subtract $2 \cdot$(row 1) from row 2 and add $3 \cdot$(row 1) to row 3:
>
> $$
> \begin{bmatrix} 1 & 1 & -6 & 0 \\ 0 & -4 & 15 & 0 \\ 0 & 4 & -15 & 0 \end{bmatrix}
> \sim \begin{bmatrix} 1 & 1 & -6 & 0 \\ 0 & 1 & -15/4 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
> \sim \begin{bmatrix} 1 & 0 & -9/4 & 0 \\ 0 & 1 & -15/4 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
> $$
>
> (add row 2 to row 3, divide row 2 by $-4$, subtract row 2 from row 1). The general solution is $x_1 = \frac94 x_3$, $x_2 = \frac{15}{4}x_3$, $x_3$ free. Choosing $x_3 = 4$ gives a basis vector with integer entries, and dividing by the sum $9 + 15 + 4 = 28$:
>
> $$
> \mathbf{w} = \begin{bmatrix} 9 \\ 15 \\ 4 \end{bmatrix}, \qquad \mathbf{q} = \begin{bmatrix} 9/28 \\ 15/28 \\ 4/28 \end{bmatrix} \approx \begin{bmatrix} .32 \\ .54 \\ .14 \end{bmatrix} .
> $$
>
> (Check, first row of $P\mathbf{q} = \mathbf{q}$: $\frac{1}{28}(.7 \cdot 9 + .1 \cdot 15 + .3 \cdot 4) = \frac{1}{28}(6.3 + 1.5 + 1.2) = \frac{9}{28}$.) The entries of $\mathbf{q}$ describe the distribution of votes at an election many years from now, if the stochastic matrix continues to describe the changes: eventually about $54\%$ of the vote will be Republican.
>
> *Lay: Example 4.9.6*

^ex-31-5
