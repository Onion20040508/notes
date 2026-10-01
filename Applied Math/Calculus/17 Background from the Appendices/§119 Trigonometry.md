---
type: section
subject: "[[Calculus]]"
chapter: 17
section: 119
stewart: "Appendix D"
aliases: ["Stewart Appendix D"]
tags: [calculus]
---
← [[§118 Graphs of Second-Degree Equations]] · ↑ [[· 17 Background from the Appendices]] · [[§120 Sigma Notation]] →

*Stewart, Appendix D.*

The trigonometry used throughout the course: radian measure (the reason the derivative of $\sin x$ is $\cos x$, [[§16 Derivatives of Trigonometric Functions#^thm-16-1|Theorem §16.1]]), the six trigonometric functions of a general angle, the identities, with everything after the Pythagorean identity derived from the two addition formulas, the Laws of Sines and Cosines, and the graphs. The half-angle formulas are the workhorse of trigonometric integrals ([[§45 Trigonometric Integrals#^thm-45-1|Theorem §45.1]], with the product identities in [[§45 Trigonometric Integrals#^thm-45-4|Theorem §45.4]]), and the definitions by a point $(x, y)$ at distance $r$ are what make $x = r\cos\theta$, $y = r\sin\theta$ valid for all angles ([[§65 Polar Coordinates#^thm-65-2|Theorem §65.2]]).

## Angles

> [!definition] Definition §119.1: Radian Measure
> Angles are measured in degrees or in **radians** (rad). A complete revolution is $360°$, or $2\pi$ rad, so
>
> $$
> \pi \text{ rad} = 180° , \qquad (1)
> $$
>
> $$
> 1 \text{ rad} = \Big(\frac{180}{\pi}\Big)° \approx 57.3° , \qquad 1° = \frac{\pi}{180} \text{ rad} \approx 0.017 \text{ rad} . \qquad (2)
> $$
>
> To convert degrees to radians multiply by $\pi/180$; radians to degrees, multiply by $180/\pi$. In calculus angles are measured in radians unless otherwise indicated.
>
> | degrees | $0°$ | $30°$ | $45°$ | $60°$ | $90°$ | $120°$ | $135°$ | $150°$ | $180°$ | $270°$ | $360°$ |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | radians | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
>
> *Stewart: Appendix D, Equations 1 and 2*

^def-119-1

> [!theorem] Theorem §119.1: Arc Length and Central Angle
> In a circle of radius $r$, a central angle $\theta$ subtends an arc of length $a$, where
>
> $$
> \theta = \frac ar , \qquad a = r\theta \qquad (3)
> $$
>
> These equations are valid **only when $\theta$ is measured in radians**. In particular, $1$ rad is the angle subtended at the center by an arc equal in length to the radius.
>
> *Stewart: Appendix D, Equations 3*

^thm-119-1

> [!proof]+ Proof
> The length of the arc is proportional to the size of the angle, and the whole circle has circumference $2\pi r$ and central angle $2\pi$. So $\dfrac{\theta}{2\pi} = \dfrac{a}{2\pi r}$; solving for $\theta$ and for $a$ gives (3). Putting $a = r$ gives $\theta = 1$.

^pf-119-1

*Uses:* [[§119 Trigonometry#^def-119-1|Def. §119.1]]

> [!example] Example §119.1: Converting Angles; Arcs
> **(a)** $60° = 60\big(\frac{\pi}{180}\big) = \frac{\pi}{3}$ rad, and $\frac{5\pi}{4}$ rad $= \frac{5\pi}{4}\big(\frac{180}{\pi}\big) = 225°$.
>
> **(b)** In a circle of radius $5$ cm, an arc of $6$ cm subtends the angle $\theta = \frac65 = 1.2$ rad. In a circle of radius $3$ cm, a central angle of $3\pi/8$ rad subtends an arc of length $a = r\theta = 3\big(\frac{3\pi}{8}\big) = \frac{9\pi}{8}$ cm.
>
> *Stewart: Appendix D, Examples 1 and 2*

^ex-119-1

> [!definition] Definition §119.2: Standard Position
> An angle is in **standard position** when its vertex is at the origin and its **initial side** is on the positive $x$-axis. A **positive** angle is obtained by rotating the initial side counterclockwise until it coincides with the **terminal side**, a **negative** angle by rotating clockwise. Different angles can have the same terminal side: $3\pi/4$, $-5\pi/4 = 3\pi/4 - 2\pi$ and $11\pi/4 = 3\pi/4 + 2\pi$ do, since $2\pi$ is a complete revolution.
>
> *Stewart: Appendix D (text)*

^def-119-2

## The Trigonometric Functions

> [!definition] Definition §119.3: Trigonometric Functions of an Acute Angle
> For an acute angle $\theta$ in a right triangle,
>
> $$
> \sin\theta = \frac{\text{opp}}{\text{hyp}}, \quad \cos\theta = \frac{\text{adj}}{\text{hyp}}, \quad \tan\theta = \frac{\text{opp}}{\text{adj}}, \quad \csc\theta = \frac{\text{hyp}}{\text{opp}}, \quad \sec\theta = \frac{\text{hyp}}{\text{adj}}, \quad \cot\theta = \frac{\text{adj}}{\text{opp}} . \qquad (4)
> $$
>
> *Stewart: Appendix D, (4)*

^def-119-3

> [!definition] Definition §119.4: Trigonometric Functions of a General Angle
> For a general angle $\theta$ in standard position, let $P(x, y)$ be any point other than $O$ on the terminal side of $\theta$, and let $r = |OP|$. Then
>
> $$
> \sin\theta = \frac yr, \quad \cos\theta = \frac xr, \quad \tan\theta = \frac yx, \quad \csc\theta = \frac ry, \quad \sec\theta = \frac rx, \quad \cot\theta = \frac xy . \qquad (5)
> $$
>
> $\tan\theta$ and $\sec\theta$ are undefined when $x = 0$, and $\csc\theta$ and $\cot\theta$ when $y = 0$. The values do not depend on the choice of $P$ (similar triangles), and for acute $\theta$ they agree with (4). Taking $r = 1$: the point on the unit circle at angle $\theta$ is $P(\cos\theta, \sin\theta)$.
>
> If $\theta$ is a number, $\sin\theta$ means the sine of the angle whose **radian** measure is $\theta$: $\sin 3 \approx 0.14112$, whereas $\sin 3° \approx 0.05234$.
>
> *Stewart: Appendix D, (5)*

^def-119-4

> [!remark]- Connections
> - Rigorous construction: in 451, $\sin$ and $\cos$ are defined by their power series, and all the properties used on credit (addition formulas, $\pi$, periodicity) are derived from them: [[§26 Differentiation and Integration of Power Series#^ex-26-8|451 Ex. §26.8]], [[§26 Differentiation and Integration of Power Series#^rem-26-1|451 Remark: Repaying the trigonometric debt]].

> [!remark] Remark: Exact Values and Signs
> From the right triangles with angles $\frac{\pi}{4}, \frac{\pi}{4}$ (sides $1, 1, \sqrt2$) and $\frac{\pi}{6}, \frac{\pi}{3}$ (sides $1, \sqrt3, 2$):
>
> $$
> \sin\tfrac{\pi}{4} = \cos\tfrac{\pi}{4} = \tfrac{1}{\sqrt2}, \quad \tan\tfrac{\pi}{4} = 1; \qquad \sin\tfrac{\pi}{6} = \cos\tfrac{\pi}{3} = \tfrac12, \quad \cos\tfrac{\pi}{6} = \sin\tfrac{\pi}{3} = \tfrac{\sqrt3}{2}; \qquad \tan\tfrac{\pi}{6} = \tfrac{1}{\sqrt3}, \quad \tan\tfrac{\pi}{3} = \sqrt3 .
> $$
>
> | $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $\sin\theta$ | $0$ | $\frac12$ | $\frac{1}{\sqrt2}$ | $\frac{\sqrt3}{2}$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $0$ | $-1$ | $0$ |
> | $\cos\theta$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $0$ | $-\frac12$ | $-\frac{1}{\sqrt2}$ | $-\frac{\sqrt3}{2}$ | $-1$ | $0$ | $1$ |
>
> **Signs.** "All Students Take Calculus": in quadrant I all ratios are positive, in II $\sin$ (and $\csc$), in III $\tan$ (and $\cot$), in IV $\cos$ (and $\sec$), since $r > 0$ and the signs of $x$, $y$ are those of the quadrant.

^rem-119-1

> [!example] Example §119.2: Exact Trigonometric Ratios
> **(a)** Find the six ratios for $\theta = 2\pi/3$. The terminal side makes the angle $\pi/3$ with the negative $x$-axis, so the point $P(-1, \sqrt3)$ lies on it, with $r = \sqrt{1 + 3} = 2$. By (5), with $x = -1$, $y = \sqrt3$, $r = 2$:
>
> $$
> \sin\tfrac{2\pi}{3} = \tfrac{\sqrt3}{2}, \quad \cos\tfrac{2\pi}{3} = -\tfrac12, \quad \tan\tfrac{2\pi}{3} = -\sqrt3, \quad \csc\tfrac{2\pi}{3} = \tfrac{2}{\sqrt3}, \quad \sec\tfrac{2\pi}{3} = -2, \quad \cot\tfrac{2\pi}{3} = -\tfrac{1}{\sqrt3} .
> $$
>
> **(b)** If $\cos\theta = \frac25$ and $0 < \theta < \pi/2$, find the other five functions. Label a right triangle with hypotenuse $5$ and adjacent side $2$. The opposite side $x$ satisfies $x^2 + 4 = 25$ (Pythagorean Theorem), so $x = \sqrt{21}$, and by (4)
>
> $$
> \sin\theta = \tfrac{\sqrt{21}}{5}, \quad \tan\theta = \tfrac{\sqrt{21}}{2}, \quad \csc\theta = \tfrac{5}{\sqrt{21}}, \quad \sec\theta = \tfrac52, \quad \cot\theta = \tfrac{2}{\sqrt{21}} .
> $$
>
> (With a calculator, sides follow from one angle as well: in a right triangle with angle $40°$ whose opposite side is $16$ and adjacent side $x$, $\tan 40° = 16/x$ gives $x = 16/\tan 40° \approx 19.07$.)
>
> *Stewart: Appendix D, Examples 3, 4 and 5*

^ex-119-2

> [!theorem] Theorem §119.2: Area of a Triangle
> The area of a triangle with sides of lengths $a$ and $b$ and included angle $\theta$ is
>
> $$
> \mathcal{A} = \tfrac12 ab\sin\theta . \qquad (6)
> $$
>
> *Stewart: Appendix D, (6)*

^thm-119-2

> [!proof]+ Proof
> Take the side of length $a$ as the base. If $\theta$ is acute, the height is $h = b\sin\theta$ (right triangle with hypotenuse $b$ and angle $\theta$), so $\mathcal{A} = \frac12(\text{base})(\text{height}) = \frac12 ab\sin\theta$. If $\theta$ is obtuse, the foot of the height lies on the extension of the base and the right triangle has angle $\pi - \theta$, so $h = b\sin(\pi - \theta)$. Now $\sin(\pi - \theta) = \sin\theta$ (Stewart's Exercise 44): if $P(x, y)$ is on the terminal side of $\theta$, then $(-x, y)$, its mirror image in the $y$-axis, is on the terminal side of $\pi - \theta$, at the same distance $r$, so both sines equal $y/r$. Hence again $h = b\sin\theta$. If $\theta = \pi/2$, $h = b = b\sin\theta$.

^pf-119-2

*Uses:* [[§119 Trigonometry#^def-119-3|Def. §119.3]], [[§119 Trigonometry#^def-119-4|Def. §119.4]]

For instance, an equilateral triangle with side $a$ has all angles $\pi/3$, so its area is $\frac12 a^2\sin\frac{\pi}{3} = \frac{\sqrt3}{4}a^2$ (Stewart's Example 6).

## Trigonometric Identities

> [!theorem] Theorem §119.3: Reciprocal and Quotient Identities
> $$
> \csc\theta = \frac{1}{\sin\theta}, \qquad \sec\theta = \frac{1}{\cos\theta}, \qquad \cot\theta = \frac{1}{\tan\theta}, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta}, \qquad \cot\theta = \frac{\cos\theta}{\sin\theta} . \qquad (7)
> $$
>
> *Stewart: Appendix D, (7)*

^thm-119-3

> [!proof]+ Proof
> Immediate from (5): for instance $\dfrac{\sin\theta}{\cos\theta} = \dfrac{y/r}{x/r} = \dfrac yx = \tan\theta$ and $\dfrac{1}{\sin\theta} = \dfrac ry = \csc\theta$.

^pf-119-3

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]]

> [!theorem] Theorem §119.4: Pythagorean Identities
> $$
> \sin^2\theta + \cos^2\theta = 1 \qquad (8) \qquad\qquad \tan^2\theta + 1 = \sec^2\theta \qquad (9) \qquad\qquad 1 + \cot^2\theta = \csc^2\theta \qquad (10)
> $$
>
> *Stewart: Appendix D, (8), (9), (10)*

^thm-119-4

> [!proof]+ Proof
> With $P(x, y)$ and $r$ as in (5), the Distance Formula gives $x^2 + y^2 = r^2$, so
>
> $$
> \sin^2\theta + \cos^2\theta = \frac{y^2}{r^2} + \frac{x^2}{r^2} = \frac{x^2 + y^2}{r^2} = \frac{r^2}{r^2} = 1 .
> $$
>
> Dividing (8) by $\cos^2\theta$ and using (7) gives (9); dividing by $\sin^2\theta$ gives (10).

^pf-119-4

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]], [[§119 Trigonometry#^thm-119-3|§119.3]], [[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]]

> [!theorem] Theorem §119.5: Symmetry and Periodicity
> $$
> \sin(-\theta) = -\sin\theta \quad (11a), \qquad \cos(-\theta) = \cos\theta \quad (11b), \qquad \sin(\theta + 2\pi) = \sin\theta, \quad \cos(\theta + 2\pi) = \cos\theta \quad (12).
> $$
>
> So sine is an odd function and cosine an even function ([[§1 Four Ways to Represent a Function#^def-1-7|Definition §1.7]]), and both are periodic with period $2\pi$.
>
> *Stewart: Appendix D, (11a), (11b), (12)*

^thm-119-5

> [!proof]+ Proof
> The angles $\theta$ and $-\theta$ in standard position are mirror images in the $x$-axis, so if $P(x, y)$ is on the terminal side of $\theta$, then $(x, -y)$ is on that of $-\theta$, at the same distance $r$. By (5), $\sin(-\theta) = -y/r = -\sin\theta$ and $\cos(-\theta) = x/r = \cos\theta$. The angles $\theta$ and $\theta + 2\pi$ have the same terminal side, so (5) gives the same values.

^pf-119-5

*Uses:* [[§119 Trigonometry#^def-119-2|Def. §119.2]], [[§119 Trigonometry#^def-119-4|Def. §119.4]]

> [!theorem] Theorem §119.6: Addition Formulas
> $$
> \sin(x + y) = \sin x\cos y + \cos x\sin y \qquad (13a)
> $$
>
> $$
> \cos(x + y) = \cos x\cos y - \sin x\sin y \qquad (13b)
> $$
>
> All the remaining identities below are consequences of these two.
>
> *Stewart: Appendix D, (13a) and (13b)*

^thm-119-6

> [!proof]- Proof
> Stewart outlines the proof in Exercises 89–91; here it is in full.
>
> **Step 1: $\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta$** (Exercise 89). Let $A = (\cos\alpha, \sin\alpha)$ and $B = (\cos\beta, \sin\beta)$, the points of the unit circle at angles $\alpha$ and $\beta$, and let $c = |AB|$. The angle $\gamma$ of the triangle $AOB$ at $O$ is $\alpha - \beta$ up to sign and multiples of $2\pi$: $\gamma = \pm(\alpha - \beta) + 2\pi k$, so $\cos\gamma = \cos(\alpha - \beta)$ by (11b) and (12) (Theorem §119.5). If $A$, $O$, $B$ form a triangle, the Law of Cosines ([[§119 Trigonometry#^thm-119-11|Theorem §119.11]] below; its proof uses only (5), (8) and the Distance Formula, never the addition formulas, so the argument is not circular) with $|OA| = |OB| = 1$ gives
>
> $$
> c^2 = 1 + 1 - 2\cos(\alpha - \beta) = 2 - 2\cos(\alpha - \beta) .
> $$
>
> (This also holds when $A = B$ or $A$, $O$, $B$ are collinear, where $\cos(\alpha - \beta) = \pm1$ and $c = 0$ or $2$.) By the Distance Formula and (8),
>
> $$
> c^2 = (\cos\alpha - \cos\beta)^2 + (\sin\alpha - \sin\beta)^2 = 2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta) .
> $$
>
> Comparing the two expressions gives Step 1.
>
> **Step 2: (13b)** (Exercise 90). By Step 1 with $\alpha = x$, $\beta = -y$, and (11),
>
> $$
> \cos(x + y) = \cos x\cos(-y) + \sin x\sin(-y) = \cos x\cos y - \sin x\sin y .
> $$
>
> **Step 3: cofunctions.** Step 1 with $\alpha = \pi/2$, $\beta = \theta$ gives $\cos(\frac{\pi}{2} - \theta) = 0 \cdot \cos\theta + 1 \cdot \sin\theta = \sin\theta$. Replacing $\theta$ by $\frac{\pi}{2} - \theta$ gives $\cos\theta = \sin(\frac{\pi}{2} - \theta)$.
>
> **Step 4: (13a)** (Exercise 91). By Step 3 and Step 1,
>
> $$
> \sin(x - y) = \cos\big(\tfrac{\pi}{2} - x + y\big) = \cos\big((\tfrac{\pi}{2} - x) - (-y)\big) = \cos(\tfrac{\pi}{2} - x)\cos y - \sin(\tfrac{\pi}{2} - x)\sin y = \sin x\cos y - \cos x\sin y ,
> $$
>
> using $\cos(-y) = \cos y$, $\sin(-y) = -\sin y$. Replacing $y$ by $-y$ gives (13a).

^pf-119-6

*Uses:* [[§119 Trigonometry#^thm-119-4|§119.4]], [[§119 Trigonometry#^thm-119-5|§119.5]], [[§119 Trigonometry#^thm-119-11|§119.11]], [[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]]

![[m233-119-1.svg]]
*The proof of the addition formulas. The points $A$ and $B$ at angles $\alpha$ and $\beta$ on the unit circle are at distance $c$, computed in two ways: by the Law of Cosines in the triangle $AOB$ with angle $\alpha - \beta$ at $O$, $c^2 = 2 - 2\cos(\alpha - \beta)$, and by the Distance Formula, $c^2 = 2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta)$.*

> [!theorem] Corollary §119.7: Subtraction Formulas and Tangent Formulas
> $$
> \sin(x - y) = \sin x\cos y - \cos x\sin y \quad (14a), \qquad \cos(x - y) = \cos x\cos y + \sin x\sin y \quad (14b),
> $$
>
> $$
> \tan(x + y) = \frac{\tan x + \tan y}{1 - \tan x\tan y} \quad (15a), \qquad \tan(x - y) = \frac{\tan x - \tan y}{1 + \tan x\tan y} \quad (15b).
> $$
>
> *Stewart: Appendix D, (14a), (14b), (15a), (15b)*

^cor-119-7

> [!proof]+ Proof
> Substitute $-y$ for $y$ in (13a) and (13b) and use (11a), (11b). For (15a), divide (13a) by (13b) and then divide numerator and denominator by $\cos x\cos y$:
>
> $$
> \tan(x + y) = \frac{\sin x\cos y + \cos x\sin y}{\cos x\cos y - \sin x\sin y} = \frac{\frac{\sin x}{\cos x} + \frac{\sin y}{\cos y}}{1 - \frac{\sin x}{\cos x}\frac{\sin y}{\cos y}} = \frac{\tan x + \tan y}{1 - \tan x\tan y} .
> $$
>
> (15b) follows in the same way from (14), or from (15a) with $-y$, since $\tan(-y) = -\tan y$.

^pf-119-7

*Uses:* [[§119 Trigonometry#^thm-119-6|§119.6]], [[§119 Trigonometry#^thm-119-5|§119.5]], [[§119 Trigonometry#^thm-119-3|§119.3]]

> [!theorem] Corollary §119.8: Double-Angle and Half-Angle Formulas
> $$
> \sin 2x = 2\sin x\cos x \quad (16a), \qquad \cos 2x = \cos^2 x - \sin^2 x \quad (16b),
> $$
>
> $$
> \cos 2x = 2\cos^2 x - 1 \quad (17a), \qquad \cos 2x = 1 - 2\sin^2 x \quad (17b),
> $$
>
> $$
> \cos^2 x = \frac{1 + \cos 2x}{2} \quad (18a), \qquad \sin^2 x = \frac{1 - \cos 2x}{2} \quad (18b).
> $$
>
> *Stewart: Appendix D, (16)–(18)*

^cor-119-8

> [!proof]+ Proof
> Put $y = x$ in (13a) and (13b) to get (16). Replace $\sin^2 x$ by $1 - \cos^2 x$, or $\cos^2 x$ by $1 - \sin^2 x$, in (16b), using (8), to get (17a) and (17b). Solve (17a) for $\cos^2 x$ and (17b) for $\sin^2 x$ to get (18).

^pf-119-8

*Uses:* [[§119 Trigonometry#^thm-119-6|§119.6]], [[§119 Trigonometry#^thm-119-4|§119.4]]

> [!theorem] Corollary §119.9: Product Identities
> $$
> \sin x\cos y = \tfrac12[\sin(x + y) + \sin(x - y)] \quad (19a)
> $$
>
> $$
> \cos x\cos y = \tfrac12[\cos(x + y) + \cos(x - y)] \quad (19b)
> $$
>
> $$
> \sin x\sin y = \tfrac12[\cos(x - y) - \cos(x + y)] \quad (19c)
> $$
>
> *Stewart: Appendix D, (19a)–(19c)*

^cor-119-9

> [!proof]+ Proof
> Add (13a) and (14a): $\sin(x + y) + \sin(x - y) = 2\sin x\cos y$. Add (13b) and (14b): $\cos(x + y) + \cos(x - y) = 2\cos x\cos y$. Subtract (13b) from (14b): $\cos(x - y) - \cos(x + y) = 2\sin x\sin y$. Divide by $2$.

^pf-119-9

*Uses:* [[§119 Trigonometry#^thm-119-6|§119.6]], [[§119 Trigonometry#^cor-119-7|§119.7]]

> [!example] Example §119.3: A Trigonometric Equation
> Find all $x$ in $[0, 2\pi]$ with $\sin x = \sin 2x$.
>
> By (16a) the equation is $\sin x = 2\sin x\cos x$, or $\sin x\,(1 - 2\cos x) = 0$. So $\sin x = 0$, giving $x = 0, \pi, 2\pi$, or $1 - 2\cos x = 0$, i.e. $\cos x = \frac12$, giving $x = \frac{\pi}{3}, \frac{5\pi}{3}$. The equation has five solutions: $0, \frac{\pi}{3}, \pi, \frac{5\pi}{3}, 2\pi$. (Dividing by $\sin x$ at the start would have lost three of them.)
>
> *Stewart: Appendix D, Example 7*

^ex-119-3

## The Law of Sines and the Law of Cosines

Label the vertices of a triangle $A$, $B$, $C$, use the same letters for the angles there, and let $a$, $b$, $c$ be the lengths of the opposite sides.

> [!theorem] Theorem §119.10: Law of Sines
> In any triangle $ABC$,
>
> $$
> \frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c} .
> $$
>
> The sides are proportional to the sines of the opposite angles.
>
> *Stewart: Appendix D, Law of Sines*

^thm-119-10

> [!proof]+ Proof
> By Formula 6, the area of the triangle is $\frac12 ab\sin C$, and by the same formula applied to the other two angles it is also $\frac12 ac\sin B$ and $\frac12 bc\sin A$. So $\frac12 bc\sin A = \frac12 ac\sin B = \frac12 ab\sin C$, and multiplying by $2/(abc)$ gives the Law of Sines.

^pf-119-10

*Uses:* [[§119 Trigonometry#^thm-119-2|§119.2]]

> [!theorem] Theorem §119.11: Law of Cosines
> In any triangle $ABC$,
>
> $$
> a^2 = b^2 + c^2 - 2bc\cos A, \qquad b^2 = a^2 + c^2 - 2ac\cos B, \qquad c^2 = a^2 + b^2 - 2ab\cos C .
> $$
>
> *Stewart: Appendix D, Law of Cosines*

^thm-119-11

> [!proof]+ Proof
> We prove the first formula; the others follow by relabeling. Place the triangle with $A$ at the origin and $B$ at $(c, 0)$ on the positive $x$-axis. The side $AC$ has length $b$ and makes the angle $A$ with the positive $x$-axis, so by (5) $C = (b\cos A, b\sin A)$, whether $A$ is acute or obtuse. By the Distance Formula and (8),
>
> $$
> a^2 = (b\cos A - c)^2 + (b\sin A - 0)^2 = b^2\cos^2 A - 2bc\cos A + c^2 + b^2\sin^2 A = b^2(\cos^2 A + \sin^2 A) - 2bc\cos A + c^2 = b^2 + c^2 - 2bc\cos A .
> $$

^pf-119-11

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]], [[§119 Trigonometry#^thm-119-4|§119.4]], [[§117 Coordinate Geometry and Lines#^thm-117-1|§117.1]]

> [!remark]- Connections
> - In vector form, $|\mathbf{u} - \mathbf{v}|^2 = |\mathbf{u}|^2 + |\mathbf{v}|^2 - 2\,\mathbf{u} \cdot \mathbf{v}$: it is how Stewart proves $\mathbf{u} \cdot \mathbf{v} = |\mathbf{u}||\mathbf{v}|\cos\theta$ ([[§82 The Dot Product#^thm-82-2|Theorem §82.2]]); the abstract version is the expansion of $\|u - v\|^2$ in an inner product space (Pythagorean theorem, [[§19 Inner Products and Norms#^ladr-6-12|LADR 6.12]]).

> [!theorem] Theorem §119.12: Heron's Formula
> The area of any triangle $ABC$ is
>
> $$
> \mathcal{A} = \sqrt{s(s - a)(s - b)(s - c)} , \qquad\text{where } s = \tfrac12(a + b + c)
> $$
>
> is the **semiperimeter** of the triangle.
>
> *Stewart: Appendix D, Heron's Formula*

^thm-119-12

> [!proof]+ Proof
> By the Law of Cosines, $\cos C = \dfrac{a^2 + b^2 - c^2}{2ab}$, so
>
> $$
> 1 + \cos C = \frac{2ab + a^2 + b^2 - c^2}{2ab} = \frac{(a + b)^2 - c^2}{2ab} = \frac{(a + b + c)(a + b - c)}{2ab} ,
> $$
>
> and similarly
>
> $$
> 1 - \cos C = \frac{2ab - a^2 - b^2 + c^2}{2ab} = \frac{c^2 - (a - b)^2}{2ab} = \frac{(c + a - b)(c - a + b)}{2ab} .
> $$
>
> Then by Formula 6 and (8),
>
> $$
> \begin{aligned}
> \mathcal{A}^2 &= \tfrac14 a^2b^2\sin^2 C = \tfrac14 a^2b^2(1 - \cos^2 C) = \tfrac14 a^2b^2(1 + \cos C)(1 - \cos C) \\
> &= \tfrac14 a^2b^2 \cdot \frac{(a + b + c)(a + b - c)}{2ab} \cdot \frac{(c + a - b)(c - a + b)}{2ab}
> = \frac{a + b + c}{2} \cdot \frac{a + b - c}{2} \cdot \frac{c + a - b}{2} \cdot \frac{c - a + b}{2} \\
> &= s(s - c)(s - b)(s - a) .
> \end{aligned}
> $$
>
> Taking the (positive) square root gives Heron's formula.

^pf-119-12

*Uses:* [[§119 Trigonometry#^thm-119-11|§119.11]], [[§119 Trigonometry#^thm-119-2|§119.2]], [[§119 Trigonometry#^thm-119-4|§119.4]]

## Graphs of the Trigonometric Functions

> [!theorem] Proposition §119.13: Properties of the Graphs
> (a) $\sin x = 0$ exactly when $x = n\pi$, $n$ an integer; and $\cos x = \sin(x + \frac{\pi}{2})$, so the graph of cosine is the graph of sine shifted $\pi/2$ to the left.
>
> (b) Sine and cosine have domain $(-\infty, \infty)$ and range $[-1, 1]$: for all $x$,
>
> $$
> -1 \le \sin x \le 1, \qquad -1 \le \cos x \le 1 .
> $$
>
> (c) Tangent and cotangent have range $(-\infty, \infty)$ and period $\pi$; cosecant and secant have range $(-\infty, -1] \cup [1, \infty)$ and period $2\pi$. Tangent and secant are undefined at the odd multiples of $\pi/2$, cotangent and cosecant at the multiples of $\pi$.
>
> *Stewart: Appendix D (text)*

^prop-119-13

> [!proof]+ Proof
> (a) $\sin x = y/r = 0$ exactly when the terminal side lies on the $x$-axis, i.e. $x$ is a multiple of $\pi$. By (13a), $\sin(x + \frac{\pi}{2}) = \sin x\cos\frac{\pi}{2} + \cos x\sin\frac{\pi}{2} = \cos x$.
>
> (b) With $r = 1$, $(\cos x, \sin x)$ is a point of the unit circle, so $|\cos x| \le 1$ and $|\sin x| \le 1$, and every value in $[-1, 1]$ is taken (every point of the unit circle is at some angle).
>
> (c) $\tan(x + \pi) = \dfrac{\sin(x + \pi)}{\cos(x + \pi)} = \dfrac{-\sin x}{-\cos x} = \tan x$ by (13), and likewise for $\cot$; $\csc$ and $\sec$ inherit the period $2\pi$ from $\sin$ and $\cos$, and since $|\sin x|, |\cos x| \le 1$ their reciprocals have absolute value $\ge 1$. The undefined points are the zeros of $\cos$ and $\sin$ (from (a) and $\cos x = \sin(x + \frac{\pi}{2})$). That $\tan$ takes every real value: on $(-\frac{\pi}{2}, \frac{\pi}{2})$ it is continuous ([[§10 Continuity#^thm-10-4|Theorem §10.4]]) and tends to $\pm\infty$ at the ends, so by the Intermediate Value Theorem ([[§10 Continuity#^thm-10-10|Theorem §10.10]]), applied on closed subintervals $[c, d]$ with $\tan c$ below and $\tan d$ above the target value, it takes every value; the same holds for $\cot$ on $(0, \pi)$, and $\csc$, $\sec$ take every value with absolute value $\ge 1$ as reciprocals of $\sin$, $\cos$, which take every value in $[-1, 1]$.

^pf-119-13

*Uses:* [[§119 Trigonometry#^def-119-4|Def. §119.4]], [[§119 Trigonometry#^thm-119-6|§119.6]], [[§10 Continuity#^thm-10-4|§10.4]], [[§10 Continuity#^thm-10-10|§10.10]]
