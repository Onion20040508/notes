---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 1
section: 10
lay: "1.10"
aliases: ["Lay 1.10"]
tags: [applied-linear-algebra, math235]
---
← [[§9 The Matrix of a Linear Transformation]] · ↑ [[· 1 Linear Equations in Linear Algebra]] · [[§11 Matrix Operations]] →

*Lay, Section 1.10.*

Three linear models, each a vector or matrix equation: a diet assembled from foodstuffs (the prototype of linear programming), the loop currents of an electrical network (Ohm's and Kirchhoff's laws as a matrix equation $R\mathbf{i} = \mathbf{v}$), and the migration between a city and its suburbs (a linear difference equation $\mathbf{x}_{k+1} = M\mathbf{x}_k$). In each case linearity reflects a property of the system: amounts are proportional to their causes, and contributions from different sources add. Linear models matter because natural phenomena are often linear or nearly linear when the variables stay within reasonable bounds, and because they suit computer calculation better than nonlinear ones.

## Constructing a Nutritious Weight-Loss Diet

> [!example] Example §10.1: The Cambridge Diet
> Three ingredients of the Cambridge Diet supply the following nutrients per 100 g (one unit):
>
> | Nutrient | Nonfat milk | Soy flour | Whey | Supplied by the diet in one day |
> |---|---|---|---|---|
> | Protein | 36 | 51 | 13 | 33 |
> | Carbohydrate | 52 | 34 | 74 | 45 |
> | Fat | 0 | 7 | 1.1 | 3 |
>
> If possible, find a combination of nonfat milk, soy flour and whey providing exactly the daily amounts of protein, carbohydrate and fat.
>
> **Vector equation.** Let $x_1, x_2, x_3$ be the numbers of units of the three foodstuffs. Instead of an equation per nutrient, use a *nutrient vector* per foodstuff: $x_1$ units of nonfat milk supply $(x_1 \text{ units}) \cdot (\text{nutrients per unit}) = x_1\mathbf{a}_1$, where $\mathbf{a}_1$ is the first column of the table. With $\mathbf{a}_2$, $\mathbf{a}_3$ the columns for soy flour and whey and $\mathbf{b}$ the last column, the requirement is
>
> $$
> x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + x_3\mathbf{a}_3 = \mathbf{b}, \qquad\text{that is,}\qquad
> \begin{bmatrix} 36 & 51 & 13 \\ 52 & 34 & 74 \\ 0 & 7 & 1.1 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 33 \\ 45 \\ 3 \end{bmatrix}
> $$
>
> (the matrix equation $A\mathbf{x} = \mathbf{b}$ of Lay's Practice Problem).
>
> **Solution.** Row reduction gives
>
> $$
> \begin{bmatrix} 36 & 51 & 13 & 33 \\ 52 & 34 & 74 & 45 \\ 0 & 7 & 1.1 & 3 \end{bmatrix} \sim \cdots \sim \begin{bmatrix} 1 & 0 & 0 & .277 \\ 0 & 1 & 0 & .392 \\ 0 & 0 & 1 & .233 \end{bmatrix} ,
> $$
>
> so to three significant digits the diet needs $.277$ units of nonfat milk, $.392$ units of soy flour and $.233$ units of whey. **Check:** $36(.277) + 51(.392) + 13(.233) \approx 9.97 + 19.99 + 3.03 = 32.99$; $52(.277) + 34(.392) + 74(.233) \approx 14.40 + 13.33 + 17.24 = 44.97$; $7(.392) + 1.1(.233) \approx 2.74 + .26 = 3.00$ (the small discrepancies are rounding).
>
> **Feasibility.** The solution must be nonnegative to be physically meaningful (one cannot use $-.233$ units of whey). With many nutrient requirements, more foodstuffs may be needed to get a system with a nonnegative solution; the manufacturer supplied 31 nutrients in precise amounts using 33 ingredients. Such problems are usually treated by linear programming.
>
> *Lay: Example 1.10.1; 1.10, Practice Problem*

^ex-10-1

The model is linear because the nutrients supplied by a foodstuff are *proportional* to the amount used (a scalar multiple of a vector), and each nutrient in the mixture is the *sum* of the amounts from the various foodstuffs.

## Linear Equations and Electrical Networks

> [!definition] Definition §10.1: Loop Currents, Ohm's Law, Kirchhoff's Voltage Law
> In an electrical network, a voltage source such as a battery forces a current through the network. **Ohm's law:** the voltage drop across a resistor is
>
> $$
> V = RI,
> $$
>
> with $V$ in volts, the resistance $R$ in ohms ($\Omega$) and the current $I$ in amperes. A **loop current** is assigned to each closed loop, in an arbitrarily chosen direction; a negative value means the actual flow is opposite to the chosen direction. A battery counts positive if the chosen direction runs from its positive (longer) side around to its negative (shorter) side, negative otherwise.
>
> **Kirchhoff's voltage law.** The algebraic sum of the $RI$ voltage drops in one direction around a loop equals the algebraic sum of the voltage sources in the same direction around the loop.
>
> **Kirchhoff's current law** (used for branch currents): the current in a branch is the algebraic sum of the loop currents passing through it.
>
> *Lay: 1.10, Kirchhoff's Voltage Law; 1.10 (text)*

^def-10-1

> [!remark]- Connections
> - The physics of these laws (conservation of energy around a loop, of charge at a junction): [[§A6.3 Kirchhoff's Rules]] in Electromagnetism; Ohm's law in [[§A5.3 Resistivity, Resistance and Ohm's Law]].

> [!example] Example §10.2: Loop Currents in a Three-Loop Network
> Lay's Figure 1 is a ladder of three loops, one above another, all loop currents $I_1, I_2, I_3$ chosen counterclockwise:
> - loop 1 (top): a 30-volt battery and resistors of $4\,\Omega$, $4\,\Omega$, and $3\,\Omega$ in the branch $AB$ shared with loop 2;
> - loop 2 (middle): branch $AB$ ($3\,\Omega$), two $1\,\Omega$ resistors on the sides, and the branch $CD$ shared with loop 3, containing a $1\,\Omega$ resistor and a 5-volt battery;
> - loop 3 (bottom): branch $CD$, two $1\,\Omega$ resistors on the sides, and a 20-volt battery.
>
> Determine the loop currents.
>
> **Loop 1.** $I_1$ flows through three resistors, with drops $4I_1 + 4I_1 + 3I_1 = 11I_1$. Current $I_2$ also flows through branch $AB$, opposite to $I_1$ there, adding the drop $-3I_2$. The source is $+30$ volts, so $11I_1 - 3I_2 = 30$.
>
> **Loop 2.** $-3I_1$ comes from $I_1$ in branch $AB$ (opposite to $I_2$); $6I_2$ is the sum $3 + 1 + 1 + 1$ of all resistances in loop 2 times $I_2$; $-I_3 = -1 \cdot I_3$ comes from $I_3$ in the $1\,\Omega$ resistor of branch $CD$, opposite to $I_2$. With the 5-volt source, $-3I_1 + 6I_2 - I_3 = 5$.
>
> **Loop 3.** $-I_2 + 3I_3 = -25$: $3I_3$ comes from the three $1\,\Omega$ resistors of loop 3, $-I_2$ from $I_2$ in the $1\,\Omega$ resistor of branch $CD$ (opposite to $I_3$ there); the 5-volt battery in $CD$ counts $-5$ for loop 3 because of the direction of $I_3$, and the 20-volt battery is negative for the same reason.
>
> **Solving**
>
> $$
> \begin{aligned}
> 11I_1 - 3I_2 \phantom{{}- I_3} &= 30 \\
> -3I_1 + 6I_2 - I_3 &= 5 \\
> -I_2 + 3I_3 &= -25 .
> \end{aligned} \qquad (3)
> $$
>
> From the first and third equations, $I_1 = (30 + 3I_2)/11$ and $I_3 = (I_2 - 25)/3$. Substituting into the second and multiplying by $33$: $-9(30 + 3I_2) + 198I_2 - 11(I_2 - 25) = 165$, i.e. $160I_2 + 5 = 165$, so $I_2 = 1$. Then $I_1 = 33/11 = 3$ and $I_3 = -24/3 = -8$. (Row reduction of the augmented matrix gives the same.) So $I_1 = 3$ amps, $I_2 = 1$ amp, $I_3 = -8$ amps: the actual current in loop 3 flows opposite to the chosen direction. **Check:** $33 - 3 = 30$; $-9 + 6 + 8 = 5$; $-1 - 24 = -25$.
>
> **Branch currents** (Kirchhoff's current law): in branch $AB$ the current is $I_1 - I_2 = 3 - 1 = 2$ amps, in the direction of $I_1$; in branch $CD$ it is $I_2 - I_3 = 1 - (-8) = 9$ amps. A branch with one loop current, such as from $B$ to $D$, carries that loop current.
>
> *Lay: Example 1.10.2*

^ex-10-2

> [!remark] Remark: Ohm's Law in Matrix Form, and Superposition
> System (3) as a vector equation is
>
> $$
> I_1\underbrace{\begin{bmatrix} 11 \\ -3 \\ 0 \end{bmatrix}}_{\mathbf{r}_1} + I_2\underbrace{\begin{bmatrix} -3 \\ 6 \\ -1 \end{bmatrix}}_{\mathbf{r}_2} + I_3\underbrace{\begin{bmatrix} 0 \\ -1 \\ 3 \end{bmatrix}}_{\mathbf{r}_3} = \underbrace{\begin{bmatrix} 30 \\ 5 \\ -25 \end{bmatrix}}_{\mathbf{v}} . \qquad (4)
> $$
>
> Entry $k$ of each vector concerns loop $k$. The **resistor vector** $\mathbf{r}_1$ lists the resistance in the various loops through which $I_1$ flows, written negatively where $I_1$ flows against the direction of another loop. With $R = [\,\mathbf{r}_1\ \mathbf{r}_2\ \mathbf{r}_3\,]$ and $\mathbf{i} = (I_1, I_2, I_3)$, (4) reads
>
> $$
> R\mathbf{i} = \mathbf{v},
> $$
>
> a matrix version of Ohm's law. If all loop currents are chosen in the same direction, all off-diagonal entries of $R$ are negative (or zero). Linearity is visible at a glance: doubling the voltage vector doubles the current vector, and a **superposition principle** holds. The solution of (4) is the sum of the solutions of
>
> $$
> R\mathbf{i} = \begin{bmatrix} 30 \\ 0 \\ 0 \end{bmatrix}, \qquad R\mathbf{i} = \begin{bmatrix} 0 \\ 5 \\ 0 \end{bmatrix}, \qquad R\mathbf{i} = \begin{bmatrix} 0 \\ 0 \\ -25 \end{bmatrix},
> $$
>
> each the circuit with only one voltage source (the others replaced by wires): by [[§4 The Matrix Equation Ax = b#^thm-4-5|Theorem §4.5]], if $R\mathbf{i}_k = \mathbf{v}_k$ for $k = 1, 2, 3$, then $R(\mathbf{i}_1 + \mathbf{i}_2 + \mathbf{i}_3) = \mathbf{v}_1 + \mathbf{v}_2 + \mathbf{v}_3$. The model is linear because Ohm's law (drop *proportional* to current) and Kirchhoff's law (*sum* of drops equals *sum* of sources) are linear.

^rem-10-1

## Difference Equations

> [!definition] Definition §10.2: Linear Difference Equation
> A dynamic system measured at discrete times gives a sequence of vectors $\mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots$, the entries of $\mathbf{x}_k$ describing the state of the system at the $k$th measurement. If there is a matrix $A$ such that $\mathbf{x}_1 = A\mathbf{x}_0$, $\mathbf{x}_2 = A\mathbf{x}_1$ and, in general,
>
> $$
> \mathbf{x}_{k+1} = A\mathbf{x}_k \qquad \text{for } k = 0, 1, 2, \ldots, \qquad (5)
> $$
>
> then (5) is a **linear difference equation** (or **recurrence relation**). Given $\mathbf{x}_0$, it determines $\mathbf{x}_1, \mathbf{x}_2, \ldots$ in turn. Formulas for $\mathbf{x}_k$ and its behavior as $k \to \infty$ come later: [[§30 Applications to Difference Equations#^prop-30-8|Proposition §30.8]] (difference equations as first-order systems), [[§31 Applications to Markov Chains#^thm-31-3|Theorem §31.3]] (Markov chains) and, in Chapter 5, [[§37 Discrete Dynamical Systems#^thm-37-1|Theorem §37.1]] (the eigenvector decomposition).
>
> *Lay: 1.10 (text)*

^def-10-2

> [!definition] Definition §10.3: Migration Matrix
> Model the populations of a city and its suburbs: fix an initial year (2014) and let $\mathbf{x}_0 = (r_0, s_0)$ be the city and suburban populations that year, and $\mathbf{x}_k = (r_k, s_k)$ those $k$ years later. Suppose that each year about 5% of the city's population moves to the suburbs (95% stays) and 3% of the suburban population moves to the city (97% stays); ignore births, deaths and migration into or out of the region. After one year, the $r_0$ city residents are distributed as $r_0(.95, .05)$ and the $s_0$ suburban residents as $s_0(.03, .97)$, so
>
> $$
> \begin{bmatrix} r_1 \\ s_1 \end{bmatrix} = r_0\begin{bmatrix} .95 \\ .05 \end{bmatrix} + s_0\begin{bmatrix} .03 \\ .97 \end{bmatrix} = \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix}\begin{bmatrix} r_0 \\ s_0 \end{bmatrix}, \qquad \mathbf{x}_1 = M\mathbf{x}_0 . \qquad (8)
> $$
>
> The **migration matrix** $M$ has columns "from city", "from suburbs" and rows "to city", "to suburbs". If the percentages stay constant, $\mathbf{x}_{k+1} = M\mathbf{x}_k$ for $k = 0, 1, 2, \ldots$: a linear difference equation, and $\{\mathbf{x}_0, \mathbf{x}_1, \mathbf{x}_2, \ldots\}$ describes the population of the region over the years.
>
> *Lay: 1.10 (text)*

^def-10-3

> [!example] Example §10.3: City and Suburbs
> The population in 2014 was 600,000 in the city and 400,000 in the suburbs. Compute the populations for 2015 and 2016.
>
> $$
> \mathbf{x}_1 = M\mathbf{x}_0 = \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix}\begin{bmatrix} 600{,}000 \\ 400{,}000 \end{bmatrix} = \begin{bmatrix} 570{,}000 + 12{,}000 \\ 30{,}000 + 388{,}000 \end{bmatrix} = \begin{bmatrix} 582{,}000 \\ 418{,}000 \end{bmatrix},
> $$
>
> $$
> \mathbf{x}_2 = M\mathbf{x}_1 = \begin{bmatrix} .95 & .03 \\ .05 & .97 \end{bmatrix}\begin{bmatrix} 582{,}000 \\ 418{,}000 \end{bmatrix} = \begin{bmatrix} 552{,}900 + 12{,}540 \\ 29{,}100 + 405{,}460 \end{bmatrix} = \begin{bmatrix} 565{,}440 \\ 434{,}560 \end{bmatrix} .
> $$
>
> The total stays $1{,}000{,}000$, since each column of $M$ sums to $1$: everyone is somewhere. The model is linear because $\mathbf{x}_k \mapsto \mathbf{x}_{k+1}$ is a linear transformation: the number of people who move is *proportional* to the number in each area, and the cumulative effect is found by *adding* the movements from the different areas. ($M$ is a stochastic matrix, [[§31 Applications to Markov Chains#^def-31-1|Definition §31.1]]; the long-run behavior of $\mathbf{x}_k$ is given by [[§31 Applications to Markov Chains#^thm-31-3|Theorem §31.3]].)
>
> *Lay: Example 1.10.3*

^ex-10-3
