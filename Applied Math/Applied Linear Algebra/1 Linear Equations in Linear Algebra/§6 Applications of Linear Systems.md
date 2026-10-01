---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 6
lay: "1.6"
aliases: ["Lay 1.6"]
tags: [applied-linear-algebra, math235]
---
← [[§5 Solution Sets of Linear Systems]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§7 Linear Independence]] →

*Lay, Section 1.6.*

Real problems often lead to linear systems with infinitely many solutions, and the free variables then carry meaning. Three applications show this. In Leontief's exchange model of an economy, equilibrium prices form a line of solutions, fixed only up to a common scale. Balancing a chemical equation leads to a homogeneous system whose smallest whole-number solution is wanted. In a network, conservation of flow at each junction gives one linear equation, and the free variables describe the possible flow patterns.

## A Homogeneous System in Economics

Suppose a nation's economy is divided into sectors (manufacturing, communication, services, …), and for each sector its total output for one year is known, together with exactly how this output is divided ("exchanged") among the sectors.

> [!definition] Definition §6.1: Exchange Table, Price, Equilibrium Prices
> In Leontief's **exchange model**, the **exchange table** of an economy lists, in the column of each sector, the fractions of that sector's total output purchased by each sector (one row per purchasing sector); each column sums to $1$, since all output is accounted for. The **price** of a sector's output is the total dollar value of that output. Prices are **equilibrium prices** if the income of each sector exactly balances its expenses.
>
> A sector looks *down its column* to see where its output goes, and *across its row* to see what it needs as inputs.
>
> *Lay: 1.6 (text)*

^def-6-1

> [!theorem] Theorem §6.1: Existence of Equilibrium Prices (Leontief)
> There exist equilibrium prices that can be assigned to the total outputs of the various sectors in such a way that the income of each sector exactly balances its expenses.
>
> *Lay: 1.6 (text)*

^thm-6-1

*Lay omits the proof ("Leontief proved the following result"). That a nonzero solution exists is elementary (Remark below). That it can be chosen with all prices nonnegative is the real content: the exchange table $E$ is a stochastic matrix ([[§31 Applications to Markov Chains#^def-31-1|Definition §31.1]]: nonnegative columns summing to $1$), equilibrium prices are the solutions of $E\mathbf{p} = \mathbf{p}$, and a stochastic matrix has a steady-state vector by [[§31 Applications to Markov Chains#^prop-31-2|Proposition §31.2]]. A steady-state vector $\mathbf{q}$ of $E$ is a probability vector with $E\mathbf{q} = \mathbf{q}$, so it is a nonzero price vector with all entries $\ge 0$, and so is every positive multiple of it.*

> [!remark] Remark: Why a Nonzero Price Vector Exists
> Let $E$ be the exchange table and $\mathbf{p}$ the price vector. Row $i$ of $E$ times $\mathbf{p}$ is the expense of sector $i$, so the equilibrium condition is $\mathbf{p} = E\mathbf{p}$, a homogeneous system with coefficient matrix $I - E$. Each column of $E$ sums to $1$, so each column of $I - E$ sums to $0$: the rows of $I - E$ add up to the zero row. Adding all other rows to the last row is a sequence of replacement operations that turns the last row into zeros. So $I - E$ has a row without a pivot. A square coefficient matrix with fewer pivots than columns has a free variable, so $(I - E)\mathbf{p} = \mathbf{0}$ has a nontrivial solution ([[§5 Solution Sets of Linear Systems#^cor-5-1|Corollary §5.1]]).

^rem-6-1

> [!example] Example §6.1: Coal, Electric, Steel
> An economy has three sectors, Coal, Electric (power) and Steel, with exchange table
>
> | Coal | Electric | Steel | Purchased by |
> |---|---|---|---|
> | .0 | .4 | .6 | Coal |
> | .6 | .1 | .2 | Electric |
> | .4 | .5 | .2 | Steel |
>
> (for instance, Electric's output goes 40% to Coal, 50% to Steel, and 10% to Electric itself, as an operating expense). Find equilibrium prices $p_C$, $p_E$, $p_S$.
>
> **Setting up.** By the first row, Coal pays for 40% of Electric's output and 60% of Steel's, so its expenses are $.4p_E + .6p_S$; it must equal Coal's income $p_C$. The other rows give the requirements for Electric and Steel:
>
> $$
> p_C = .4p_E + .6p_S, \qquad p_E = .6p_C + .1p_E + .2p_S, \qquad p_S = .4p_C + .5p_E + .2p_S .
> $$
>
> Move the unknowns to the left (e.g. $p_E - .1p_E = .9p_E$):
>
> $$
> p_C - .4p_E - .6p_S = 0, \qquad -.6p_C + .9p_E - .2p_S = 0, \qquad -.4p_C - .5p_E + .8p_S = 0 .
> $$
>
> **Row reduction** ($R_2 + .6R_1$: $.9 - .24 = .66$, $-.2 - .36 = -.56$; $R_3 + .4R_1$: $-.5 - .16 = -.66$, $.8 - .24 = .56$; then $R_3 + R_2$):
>
> $$
> \begin{bmatrix} 1 & -.4 & -.6 & 0 \\ -.6 & .9 & -.2 & 0 \\ -.4 & -.5 & .8 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -.4 & -.6 & 0 \\ 0 & .66 & -.56 & 0 \\ 0 & -.66 & .56 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & -.4 & -.6 & 0 \\ 0 & .66 & -.56 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} .
> $$
>
> Dividing row 2 by $.66$ gives $p_E - .85p_S = 0$ (rounded to two places), and adding $.4$ times it to row 1 gives $p_C - .94p_S = 0$:
>
> $$
> \sim
> \begin{bmatrix} 1 & 0 & -.94 & 0 \\ 0 & 1 & -.85 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix},
> \qquad
> \mathbf{p} = \begin{bmatrix} p_C \\ p_E \\ p_S \end{bmatrix} = \begin{bmatrix} .94p_S \\ .85p_S \\ p_S \end{bmatrix} = p_S\begin{bmatrix} .94 \\ .85 \\ 1 \end{bmatrix} .
> $$
>
> Any nonnegative choice of $p_S$ gives equilibrium prices. With $p_S = 100$ (\$100 million): Coal \$94 million, Electric \$85 million, Steel \$100 million. Without rounding, $p_E = \tfrac{.56}{.66}p_S = \tfrac{28}{33}p_S$ and $p_C = .4 \cdot \tfrac{28}{33}p_S + .6p_S = \tfrac{31}{33}p_S$; for instance $(p_C, p_E, p_S) = (31, 28, 33)$. **Check:** $.4(28) + .6(33) = 11.2 + 19.8 = 31$; $.6(31) + .1(28) + .2(33) = 18.6 + 2.8 + 6.6 = 28$; $.4(31) + .5(28) + .2(33) = 12.4 + 14 + 6.6 = 33$.
>
> *Lay: Example 1.6.1*

^ex-6-1

The general input–output ("production") model, of which this is a simpler relative, is [[§16 The Leontief Input–Output Model#^def-16-2|Definition §16.2]].

## Balancing Chemical Equations

> [!example] Example §6.2: Burning Propane
> When propane gas burns, propane ($\mathrm{C_3H_8}$) combines with oxygen ($\mathrm{O_2}$) to form carbon dioxide ($\mathrm{CO_2}$) and water ($\mathrm{H_2O}$):
>
> $$
> (x_1)\,\mathrm{C_3H_8} + (x_2)\,\mathrm{O_2} \to (x_3)\,\mathrm{CO_2} + (x_4)\,\mathrm{H_2O} . \qquad (4)
> $$
>
> To **balance** the equation, find whole numbers $x_1, \ldots, x_4$ such that the numbers of carbon, hydrogen and oxygen atoms agree on both sides (atoms are neither created nor destroyed).
>
> **Vector equation.** List the atoms per molecule as vectors in $\mathbb{R}^3$ (carbon, hydrogen, oxygen):
>
> $$
> \mathrm{C_3H_8}: \begin{bmatrix} 3 \\ 8 \\ 0 \end{bmatrix}, \quad
> \mathrm{O_2}: \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix}, \quad
> \mathrm{CO_2}: \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, \quad
> \mathrm{H_2O}: \begin{bmatrix} 0 \\ 2 \\ 1 \end{bmatrix} .
> $$
>
> Balancing means $x_1(3, 8, 0) + x_2(0, 0, 2) = x_3(1, 0, 2) + x_4(0, 2, 1)$; moving everything to the left,
>
> $$
> x_1\begin{bmatrix} 3 \\ 8 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix} + x_3\begin{bmatrix} -1 \\ 0 \\ -2 \end{bmatrix} + x_4\begin{bmatrix} 0 \\ -2 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} .
> $$
>
> **Row reduction** ($\tfrac13 R_1$; $R_2 - 8R_1$; interchange rows 2 and 3; $\tfrac38 R_3$; $R_2 + 2R_3$ and $\tfrac12 R_2$; $R_1 + \tfrac13 R_3$):
>
> $$
> \begin{bmatrix} 3 & 0 & -1 & 0 & 0 \\ 8 & 0 & 0 & -2 & 0 \\ 0 & 2 & -2 & -1 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & -\tfrac13 & 0 & 0 \\ 0 & 2 & -2 & -1 & 0 \\ 0 & 0 & \tfrac83 & -2 & 0 \end{bmatrix}
> \sim
> \begin{bmatrix} 1 & 0 & 0 & -\tfrac14 & 0 \\ 0 & 1 & 0 & -\tfrac54 & 0 \\ 0 & 0 & 1 & -\tfrac34 & 0 \end{bmatrix} .
> $$
>
> The general solution is $x_1 = \tfrac14 x_4$, $x_2 = \tfrac54 x_4$, $x_3 = \tfrac34 x_4$, with $x_4$ free. The coefficients must be whole numbers, so take $x_4 = 4$: $x_1 = 1$, $x_2 = 5$, $x_3 = 3$, and
>
> $$
> \mathrm{C_3H_8} + 5\,\mathrm{O_2} \to 3\,\mathrm{CO_2} + 4\,\mathrm{H_2O} .
> $$
>
> **Check:** carbon $3 = 3$, hydrogen $8 = 8$, oxygen $10 = 6 + 4$. Doubling all coefficients would also balance the equation, but chemists prefer the smallest whole numbers.
>
> *Lay: 1.6 (text)*

^ex-6-2

## Network Flow

> [!definition] Definition §6.2: Network, Junction, Branch, Conservation of Flow
> A **network** consists of a set of points called **junctions** (or **nodes**), with lines or arcs called **branches** connecting some or all of the junctions. The direction of flow in each branch is indicated, and the flow amount (or rate) is either shown or denoted by a variable. The basic assumption of **network flow** is that *the total flow into the network equals the total flow out of the network, and the total flow into each junction equals the total flow out of the junction*. So each junction gives one linear equation: for instance, $30$ units flowing into a junction that has outgoing flows $x_1$, $x_2$ give $x_1 + x_2 = 30$.
>
> *Lay: 1.6 (text)*

^def-6-2

> [!example] Example §6.3: Traffic in Downtown Baltimore
> The network below shows the traffic flow (vehicles per hour) over several one-way streets in downtown Baltimore during a typical early afternoon. Determine the general flow pattern.
>
> **Equations.** At each intersection, flow in equals flow out:
>
> | Intersection | Flow in | | Flow out |
> |---|---|---|---|
> | A | $300 + 500$ | $=$ | $x_1 + x_2$ |
> | B | $x_2 + x_4$ | $=$ | $300 + x_3$ |
> | C | $100 + 400$ | $=$ | $x_4 + x_5$ |
> | D | $x_1 + x_5$ | $=$ | $600$ |
>
> Also, total flow into the network ($500 + 300 + 100 + 400$) equals total flow out ($300 + x_3 + 600$), so $x_3 = 400$. Together:
>
> $$
> x_1 + x_2 = 800, \quad x_2 - x_3 + x_4 = 300, \quad x_4 + x_5 = 500, \quad x_1 + x_5 = 600, \quad x_3 = 400 .
> $$
>
> **Solving.** Take $x_5$ as the free variable (it is the only nonpivot column when the variables are ordered $x_1, \ldots, x_5$). The fourth and third equations give $x_1 = 600 - x_5$ and $x_4 = 500 - x_5$; the first gives $x_2 = 800 - x_1 = 200 + x_5$; and the second is then automatic: $(200 + x_5) - 400 + (500 - x_5) = 300$. So the reduced system is
>
> $$
> x_1 + x_5 = 600, \quad x_2 - x_5 = 200, \quad x_3 = 400, \quad x_4 + x_5 = 500,
> $$
>
> and the general flow pattern is
>
> $$
> x_1 = 600 - x_5, \qquad x_2 = 200 + x_5, \qquad x_3 = 400, \qquad x_4 = 500 - x_5, \qquad x_5 \text{ free} .
> $$
>
> **Constraints.** A negative flow would mean flow against the indicated direction, which one-way streets forbid. So $x_4 \ge 0$ gives $x_5 \le 500$, and $x_5 \ge 0$. Hence $x_1 = 600 - x_5$ ranges over $100 \le x_1 \le 600$, and $x_2 = 200 + x_5$ over $200 \le x_2 \le 700$ (Lay's Practice Problem 2).
>
> *Lay: Example 1.6.2; 1.6, Practice Problem 2*

^ex-6-3

![[m235-6-1.svg]]
*The street network of Example §6.3 (redrawn). Black arrows are flows into or out of the network, blue arrows the internal branches. Conservation at $A$, $B$, $C$, $D$ gives four equations, and conservation for the whole network gives $x_3 = 400$.*
