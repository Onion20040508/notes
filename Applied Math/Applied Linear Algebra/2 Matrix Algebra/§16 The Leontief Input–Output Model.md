---
type: section
subject: "[[Applied Linear Algebra]]"
chapter: 2
section: 16
lay: "2.6"
aliases: ["Lay 2.6"]
tags: [applied-linear-algebra, math235]
---
← [[§15 Matrix Factorizations]] · ↑ [[· 2 Matrix Algebra]] · [[§17 Applications to Computer Graphics]] →

*Lay, Section 2.6.*

Wassily Leontief's Nobel prize–winning input–output model asks whether an economy can produce exactly what is demanded, when producing goods itself consumes goods. Each sector's needs per unit of output form a column of a consumption matrix $C$, and the balance "production = intermediate demand + final demand" is the linear system $\mathbf{x} = C\mathbf{x} + \mathbf{d}$, that is, $(I - C)\mathbf{x} = \mathbf{d}$. When every column of $C$ sums to less than 1, $I - C$ is invertible, the production vector is nonnegative, and $(I - C)^{-1}$ is the sum of the matrix geometric series $I + C + C^2 + \cdots$, each term being one more round of demand. The entries of $(I - C)^{-1}$ say how production must change when final demand changes.

## The Model

Suppose a nation's economy is divided into $n$ sectors that produce goods or services, and another part, the **open sector**, that only consumes. All quantities are measured in millions of dollars (prices held constant).

> [!definition] Definition §16.1: Production, Final Demand and Consumption
> - The **production vector** $\mathbf{x}$ in $\mathbb{R}^n$ lists the output of each sector for one year.
> - The **final demand vector** (or bill of final demands) $\mathbf{d}$ lists the values of the goods and services demanded from the sectors by the open sector: consumer demand, government consumption, surplus production, exports, and other external demands.
> - The **unit consumption vector** $\mathbf{c}_j$ of sector $j$ lists the inputs that sector $j$ needs per unit of its output. The **consumption matrix** is $C = [\,\mathbf{c}_1 \ \cdots \ \mathbf{c}_n\,]$.
>
> If sector $j$ produces $x_j$ units, it consumes $x_j\mathbf{c}_j$ in the process. So the total **intermediate demand** of all sectors is
>
> $$
> x_1\mathbf{c}_1 + \cdots + x_n\mathbf{c}_n = C\mathbf{x} .
> $$
>
> *Lay: 2.6 (text)*

^def-16-1

Leontief asked whether there is a production level $\mathbf{x}$ at which the amounts produced exactly balance the total demand for that production: $\{\text{amount produced}\} = \{\text{intermediate demand}\} + \{\text{final demand}\}$.

> [!definition] Definition §16.2: The Leontief Input–Output Model (Production Equation)
> The **Leontief input–output model**, or **production equation**, is
>
> $$
> \underset{\text{amount produced}}{\mathbf{x}} = \underset{\text{intermediate demand}}{C\mathbf{x}} + \underset{\text{final demand}}{\mathbf{d}} . \tag{4}
> $$
>
> Since $\mathbf{x} = I\mathbf{x}$, it can be written $I\mathbf{x} - C\mathbf{x} = \mathbf{d}$, that is,
>
> $$
> (I - C)\mathbf{x} = \mathbf{d} . \tag{5}
> $$
>
> *Lay: 2.6, The Leontief Input–Output Model, or Production Equation*

^def-16-2

> [!example] Example §16.1: A Three-Sector Economy
> An economy has three sectors, manufacturing, agriculture and services, with unit consumption vectors given by the inputs consumed per unit of output:
>
> | Purchased from: | Manufacturing | Agriculture | Services |
> |---|---|---|---|
> | Manufacturing | .50 | .40 | .20 |
> | Agriculture | .20 | .30 | .10 |
> | Services | .10 | .10 | .30 |
> | | $\mathbf{c}_1$ | $\mathbf{c}_2$ | $\mathbf{c}_3$ |
>
> **(a)** What will manufacturing consume if it decides to produce 100 units? Compute
>
> $$
> 100\mathbf{c}_1 = 100\begin{bmatrix} .50 \\ .20 \\ .10 \end{bmatrix} = \begin{bmatrix} 50 \\ 20 \\ 10 \end{bmatrix} .
> $$
>
> To produce 100 units, manufacturing orders and consumes 50 units from manufacturing itself, 20 from agriculture and 10 from services.
>
> **(b)** The consumption matrix is
>
> $$
> C = \begin{bmatrix} .50 & .40 & .20 \\ .20 & .30 & .10 \\ .10 & .10 & .30 \end{bmatrix} . \tag{3}
> $$
>
> Suppose the final demand is 50 units for manufacturing, 30 for agriculture and 20 for services. Find the production level $\mathbf{x}$ that satisfies it. The coefficient matrix of (5) is
>
> $$
> I - C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} - \begin{bmatrix} .5 & .4 & .2 \\ .2 & .3 & .1 \\ .1 & .1 & .3 \end{bmatrix} = \begin{bmatrix} .5 & -.4 & -.2 \\ -.2 & .7 & -.1 \\ -.1 & -.1 & .7 \end{bmatrix} .
> $$
>
> Row reduce the augmented matrix, first multiplying each row by 10, then moving row 3 to the top and scaling it by $-1$:
>
> $$
> \begin{bmatrix} .5 & -.4 & -.2 & 50 \\ -.2 & .7 & -.1 & 30 \\ -.1 & -.1 & .7 & 20 \end{bmatrix}
> \sim \begin{bmatrix} 5 & -4 & -2 & 500 \\ -2 & 7 & -1 & 300 \\ -1 & -1 & 7 & 200 \end{bmatrix}
> \sim \begin{bmatrix} 1 & 1 & -7 & -200 \\ 5 & -4 & -2 & 500 \\ -2 & 7 & -1 & 300 \end{bmatrix}
> \xrightarrow[R_3 + 2R_1]{R_2 - 5R_1}
> \begin{bmatrix} 1 & 1 & -7 & -200 \\ 0 & -9 & 33 & 1500 \\ 0 & 9 & -15 & -100 \end{bmatrix}
> \xrightarrow{R_3 + R_2}
> \begin{bmatrix} 1 & 1 & -7 & -200 \\ 0 & -9 & 33 & 1500 \\ 0 & 0 & 18 & 1400 \end{bmatrix} .
> $$
>
> Back substitution: $x_3 = 1400/18 = 700/9$; $-9x_2 = 1500 - 33 \cdot \tfrac{700}{9} = \tfrac{13500 - 23100}{9} = -\tfrac{9600}{9}$, so $x_2 = \tfrac{3200}{27}$; and $x_1 = -200 - x_2 + 7x_3 = \tfrac{-5400 - 3200 + 14700}{27} = \tfrac{6100}{27}$. So
>
> $$
> \mathbf{x} = \begin{bmatrix} 6100/27 \\ 3200/27 \\ 700/9 \end{bmatrix} \approx \begin{bmatrix} 225.9 \\ 118.5 \\ 77.8 \end{bmatrix} .
> $$
>
> Rounded to whole units: manufacturing must produce about 226 units, agriculture 119 units, and services only 78 units.
>
> *Lay: Examples 2.6.1 and 2.6.2*

^ex-16-1

The **column sum** of a column is the sum of its entries. Ordinarily the column sums of a consumption matrix are less than 1, because a sector should need less than one unit's worth of inputs to produce one unit of output.

## A Formula for (I − C)⁻¹

Imagine that the demand $\mathbf{d}$ is presented to the industries at the start of the year, and they respond by setting production at $\mathbf{x} = \mathbf{d}$, exactly the final demand. To produce $\mathbf{d}$ they order inputs, which creates an intermediate demand $C\mathbf{d}$. To meet that, they need additional inputs $C(C\mathbf{d}) = C^2\mathbf{d}$, which creates a second round of demand, then a third round $C(C^2\mathbf{d}) = C^3\mathbf{d}$, and so on:

| | Demand that must be met | Inputs needed to meet this demand |
|---|---|---|
| Final demand | $\mathbf{d}$ | $C\mathbf{d}$ |
| Intermediate demand, 1st round | $C\mathbf{d}$ | $C(C\mathbf{d}) = C^2\mathbf{d}$ |
| 2nd round | $C^2\mathbf{d}$ | $C(C^2\mathbf{d}) = C^3\mathbf{d}$ |
| 3rd round | $C^3\mathbf{d}$ | $C(C^3\mathbf{d}) = C^4\mathbf{d}$ |
| ⋮ | ⋮ | ⋮ |

The production level that meets all of this demand is

$$
\mathbf{x} = \mathbf{d} + C\mathbf{d} + C^2\mathbf{d} + C^3\mathbf{d} + \cdots = (I + C + C^2 + C^3 + \cdots)\mathbf{d} . \tag{6}
$$

(In real life the rounds would not take place in such a rigid sequence.) To make sense of (6):

> [!theorem] Proposition §16.2: The Matrix Geometric Sum
> For any square matrix $C$ and any $m \ge 0$,
>
> $$
> (I - C)(I + C + C^2 + \cdots + C^m) = I - C^{m+1} . \tag{7}
> $$
>
> If the entries of $C$ are nonnegative and its column sums are all less than 1, then $I - C$ is invertible, $C^m \to 0$ as $m \to \infty$, and
>
> $$
> (I - C)^{-1} \approx I + C + C^2 + C^3 + \cdots + C^m, \tag{8}
> $$
>
> in the sense that the right side can be made as close to $(I - C)^{-1}$ as desired by taking $m$ large enough: $(I - C)^{-1} = \lim_{m \to \infty}(I + C + \cdots + C^m)$, entry by entry.
>
> *Lay: 2.6, Equations (7) and (8)*

^prop-16-2

> [!proof]+ Proof
> **Identity (7).** By the distributive law the left side is
>
> $$
> (I + C + \cdots + C^m) - (C + C^2 + \cdots + C^{m+1}) = I - C^{m+1},
> $$
>
> since all the middle terms cancel. (This is the matrix version of $(1 - t)(1 + t + \cdots + t^m) = 1 - t^{m+1}$.)
>
> **The limit.** (Lay says only "it can be shown", comparing it with $t^m \to 0$ for $0 < t < 1$; here is why.) Lay states it for a consumption matrix, whose entries are nonnegative, and that is needed: $C = \begin{bmatrix} 0 & -2 \\ -2 & 0 \end{bmatrix}$ has column sums $-2 < 1$, but $C^2 = 4I$, so $C^m \not\to 0$. There are finitely many columns, so all column sums are at most some $s < 1$. Write $\mathbf{1} = (1, \ldots, 1)$; the column sums of a matrix $M$ are the entries of the row $\mathbf{1}^TM$.
> - **$C^m \to 0$.** We have $\mathbf{1}^TC \le s\,\mathbf{1}^T$ entrywise. Multiplying an entrywise inequality between rows on the right by a matrix with nonnegative entries preserves it, so (multiplying by $C^{m-1}$, then $C^{m-2}$, and so on) $\mathbf{1}^TC^m \le s\,\mathbf{1}^TC^{m-1} \le s^2\,\mathbf{1}^TC^{m-2} \le \cdots \le s^m\mathbf{1}^T$. So every column sum of $C^m$ is at most $s^m$. The entries of $C^m$ are nonnegative, so each entry is at most its column sum, hence lies between $0$ and $s^m$, and $s^m \to 0$.
> - **The partial sums converge.** Since every $C^k$ has nonnegative entries, each entry of $S_m = I + C + \cdots + C^m$ increases with $m$, and it is at most $1 + s + s^2 + \cdots + s^m < 1/(1 - s)$. A bounded increasing sequence converges, so $S_m \to S$ entry by entry, for some matrix $S$ with nonnegative entries.
> - **$S = (I - C)^{-1}$.** Each entry of $(I - C)S_m$ is a fixed linear combination of entries of $S_m$, so $(I - C)S_m \to (I - C)S$. By (7), $(I - C)S_m = I - C^{m+1} \to I$. Hence $(I - C)S = I$, and by [[§13 Characterizations of Invertible Matrices#^cor-13-2|Corollary §13.2]] the square matrix $I - C$ is invertible with $(I - C)^{-1} = S = \lim_{m\to\infty} S_m$, which is (8).

^pf-16-2

*Uses:* [[§11 Matrix Operations#^thm-11-6|§11.6]], [[§13 Characterizations of Invertible Matrices#^cor-13-2|§13.2]], [[§69 Sequences#^thm-69-8|Calc Thm. §69.8]] ($s^m \to 0$), [[§69 Sequences#^thm-69-9|Calc Thm. §69.9]] (bounded monotonic sequences converge)

> [!remark]- Connections
> - (8) is the matrix form of the geometric series $\frac{1}{1 - t} = 1 + t + t^2 + \cdots$ for $|t| < 1$, [[§70 Series#^thm-70-1|Calc Thm. §70.1]]; "column sums less than 1" plays the role of $|t| < 1$ (it says that $C$ has norm less than $1$ in the norm given by the largest absolute column sum, which is the operator norm of $C$, [[§26 Boundedness and Continuity#^def-26-2|556 Def. §26.2]], for the norm $|x_1| + \cdots + |x_n|$ on $\mathbb{R}^n$).

In actual input–output models, powers of the consumption matrix approach the zero matrix rather quickly, so (8) is a practical way to compute $(I - C)^{-1}$. Likewise $C^m\mathbf{d} \to \mathbf{0}$ quickly for any $\mathbf{d}$, and (6) is a practical way to solve $(I - C)\mathbf{x} = \mathbf{d}$.

If $I - C$ is invertible, [[§12 The Inverse of a Matrix#^thm-12-3|Theorem §12.3]] applied to (5) gives $\mathbf{x} = (I - C)^{-1}\mathbf{d}$. The next theorem shows that in most practical cases $I - C$ *is* invertible and the production vector is **economically feasible**: its entries are nonnegative.

> [!theorem] Theorem §16.1: Feasible Production
> Let $C$ be the consumption matrix for an economy, and let $\mathbf{d}$ be the final demand. If $C$ and $\mathbf{d}$ have nonnegative entries and if each column sum of $C$ is less than 1, then $(I - C)^{-1}$ exists and the production vector
>
> $$
> \mathbf{x} = (I - C)^{-1}\mathbf{d}
> $$
>
> has nonnegative entries and is the unique solution of
>
> $$
> \mathbf{x} = C\mathbf{x} + \mathbf{d} .
> $$
>
> *Lay: Theorem 11 (2.6)*

^thm-16-1

> [!proof]- Proof
> *Lay gives this as a sketch:* he gives no formal proof, only the discussion of the subsection A Formula for (I − C)⁻¹ (placed above here; in Lay it follows the theorem), which "will suggest why the theorem is true". The step he leaves as "it can be shown" is proved in [[§16 The Leontief Input–Output Model#^prop-16-2|Proposition §16.2]] above, which does not use this theorem.
>
> By [[§16 The Leontief Input–Output Model#^prop-16-2|Proposition §16.2]], $I - C$ is invertible and $(I - C)^{-1}$ is the limit of the partial sums $S_m = I + C + C^2 + \cdots + C^m$. Each $S_m$ has nonnegative entries, because $C$ does and sums and products of matrices with nonnegative entries have nonnegative entries. A limit of nonnegative numbers is nonnegative, so $(I - C)^{-1}$ has nonnegative entries. Then so does $\mathbf{x} = (I - C)^{-1}\mathbf{d}$, since $\mathbf{d}$ does. (This is Lay's remark that (6) shows the entries in $\mathbf{x}$ are nonnegative when those in $C$ and $\mathbf{d}$ are.) Finally, since $I - C$ is invertible, [[§12 The Inverse of a Matrix#^thm-12-3|Theorem §12.3]] says that $(I - C)\mathbf{x} = \mathbf{d}$, which is the same equation as $\mathbf{x} = C\mathbf{x} + \mathbf{d}$, has the unique solution $\mathbf{x} = (I - C)^{-1}\mathbf{d}$.

^pf-16-1

*Uses:* [[§16 The Leontief Input–Output Model#^prop-16-2|§16.2]], [[§12 The Inverse of a Matrix#^thm-12-3|§12.3]]

## The Economic Importance of the Entries of (I − C)⁻¹

The entries of $(I - C)^{-1}$ predict how the production $\mathbf{x}$ must change when the final demand $\mathbf{d}$ changes. Since $\mathbf{x} = (I - C)^{-1}\mathbf{d}$ depends linearly on $\mathbf{d}$, increasing $\mathbf{d}$ by $\mathbf{e}_j$ increases $\mathbf{x}$ by $(I - C)^{-1}\mathbf{e}_j$: **the entries in column $j$ of $(I - C)^{-1}$ are the increased amounts the sectors must produce to satisfy an increase of 1 unit in the final demand for the output of sector $j$.** (Lay's Exercise 8.)

> [!example] Example §16.2: The Inverse for the Three-Sector Economy
> For the consumption matrix (3) of [[§16 The Leontief Input–Output Model#^ex-16-1|Example §16.1]], row reducing $[\,I - C \ \ I\,]$ (or using the inverse formula [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-2|Theorem §22.2]]) gives
>
> $$
> (I - C)^{-1} = \frac{1}{27}\begin{bmatrix} 80 & 50 & 30 \\ 25 & 55 & 15 \\ 15 & 15 & 45 \end{bmatrix} \approx \begin{bmatrix} 2.96 & 1.85 & 1.11 \\ .93 & 2.04 & .56 \\ .56 & .56 & 1.67 \end{bmatrix} .
> $$
>
> (Check, row 1 of $I - C$ times column 1: $\tfrac{1}{27}(.5 \cdot 80 - .4 \cdot 25 - .2 \cdot 15) = \tfrac{1}{27}(40 - 10 - 3) = 1$.) All entries are nonnegative (here even positive), as [[§16 The Leontief Input–Output Model#^thm-16-1|Theorem §16.1]] predicts (the column sums of $C$ are $.8$, $.8$, $.6$).
>
> **Production.** $(I - C)^{-1}\mathbf{d}$ for $\mathbf{d} = (50, 30, 20)$ gives $\tfrac{1}{27}(4000 + 1500 + 600,\ 1250 + 1650 + 300,\ 750 + 450 + 900) = (6100/27,\ 3200/27,\ 2100/27)$, as in [[§16 The Leontief Input–Output Model#^ex-16-1|Example §16.1]] ($2100/27 = 700/9$).
>
> **Rounds of demand.** The partial sums $(I + C + \cdots + C^m)\mathbf{d}$ of (6) approach this production vector:
>
> | $m$ | $1$ | $2$ | $5$ | $10$ | $20$ | limit |
> |---|---|---|---|---|---|---|
> | manufacturing | 91.0 | 122.7 | 179.8 | 213.9 | 225.1 | 225.9 |
> | agriculture | 51.0 | 66.9 | 95.4 | 112.5 | 118.1 | 118.5 |
> | services | 34.0 | 44.4 | 62.9 | 73.9 | 77.5 | 77.8 |
>
> (For $m = 1$: $\mathbf{d} + C\mathbf{d} = (50, 30, 20) + (25 + 12 + 4,\ 10 + 9 + 2,\ 5 + 3 + 6) = (91, 51, 34)$.) Here the convergence is fairly slow, because the column sums $.8$ are not far below $1$.
>
> **Interpretation.** Column 1 of $(I - C)^{-1}$ says that one more unit of final demand for manufactured goods requires about 2.96 more units of manufacturing, .93 of agriculture and .56 of services: the extra unit itself, plus all the rounds of intermediate demand it sets off.
>
> *Lay: 2.6, Equations (6) and (8) and Exercise 8, applied to Example 2.6.2*

^ex-16-2

> [!example] Example §16.3: Setting Up a Two-Sector Model
> An economy has two sectors, goods and services. One unit of output from goods requires inputs of .2 unit from goods and .5 unit from services. One unit of output from services requires .4 unit from goods and .3 unit from services. There is a final demand of 20 units of goods and 30 units of services. Set up the Leontief model.
>
> The unit consumption vectors are the *columns*: $\mathbf{c}_{\text{goods}} = (.2, .5)$ and $\mathbf{c}_{\text{services}} = (.4, .3)$. The model is $\mathbf{x} = C\mathbf{x} + \mathbf{d}$ with
>
> $$
> C = \begin{bmatrix} .2 & .4 \\ .5 & .3 \end{bmatrix}, \qquad \mathbf{d} = \begin{bmatrix} 20 \\ 30 \end{bmatrix} .
> $$
>
> The column sums are $.7$ and $.7$, so [[§16 The Leontief Input–Output Model#^thm-16-1|Theorem §16.1]] applies. Solving with [[§12 The Inverse of a Matrix#^thm-12-2|Theorem §12.2]]: $I - C = \begin{bmatrix} .8 & -.4 \\ -.5 & .7 \end{bmatrix}$ has determinant $.56 - .20 = .36$, so
>
> $$
> \mathbf{x} = (I - C)^{-1}\mathbf{d} = \frac{1}{.36}\begin{bmatrix} .7 & .4 \\ .5 & .8 \end{bmatrix}\begin{bmatrix} 20 \\ 30 \end{bmatrix} = \frac{1}{.36}\begin{bmatrix} 26 \\ 34 \end{bmatrix} \approx \begin{bmatrix} 72.2 \\ 94.4 \end{bmatrix} .
> $$
>
> (Check: $C\mathbf{x} + \mathbf{d} \approx (.2(72.2) + .4(94.4) + 20,\ .5(72.2) + .3(94.4) + 30) = (72.2, 94.4)$.)
>
> *Lay: 2.6, Practice Problem*

^ex-16-3

> [!remark]- Remark: Numerical Note
> Any equation $A\mathbf{x} = \mathbf{b}$, not just in economics, can be written as $(I - C)\mathbf{x} = \mathbf{b}$ with $C = I - A$. If the system is large and sparse (mostly zero entries), it can happen that the column sums of the *absolute values* of the entries of $C$ are less than 1. Then $C^m \to 0$, and if this happens quickly enough, (6) and (8) give practical formulas for solving $A\mathbf{x} = \mathbf{b}$ and finding $A^{-1}$.

^rem-16-1
