---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 37
bc: "37"
aliases: ["B&C 37"]
tags: [complex-variables, math342]
---
← [[§36 Examples (The Power Function)]] · ↑ [[· 3 Elementary Functions]] · [[§38 Zeros and Singularities of Trigonometric Functions]] →

*Brown–Churchill, Section 37 · MAT 342 HW 4 · Practice Finals (Fall 1999, Fall 2002, Spring 2005, Fall 2009).*

Euler's formula expresses $\sin x$ and $\cos x$ through $e^{\pm ix}$, and the same formulas, with $z$ in place of $x$, define $\sin z$ and $\cos z$. They are entire, with the familiar derivatives, parity, periods and addition formulas; all of these are consequences of the law of exponents for $e^z$. What is new appears off the real axis: $\sin(iy) = i\sinh y$, so $|\sin z|^2 = \sin^2x + \sinh^2y$, and $\sin z$ and $\cos z$ are *unbounded* in the plane. The zeros are found in [[§38 Zeros and Singularities of Trigonometric Functions|§38]].

## Definition and Derivatives

Euler's formula ([[§7 Exponential Form#^def-7-2|Definition §7.2]]) gives $e^{ix} = \cos x + i\sin x$ and $e^{-ix} = \cos x - i\sin x$ for every real $x$. Subtracting and adding, $e^{ix} - e^{-ix} = 2i\sin x$ and $e^{ix} + e^{-ix} = 2\cos x$, that is,

$$
\sin x = \frac{e^{ix} - e^{-ix}}{2i} \qquad\text{and}\qquad \cos x = \frac{e^{ix} + e^{-ix}}{2} .
$$

> [!definition] Definition §37.1: Sine and Cosine of a Complex Variable
> For every complex $z$,
>
> $$
> \sin z = \frac{e^{iz} - e^{-iz}}{2i} \qquad\text{and}\qquad \cos z = \frac{e^{iz} + e^{-iz}}{2} . \qquad (1)
> $$
>
> For real $z = x$ these are the sine and cosine of calculus.
>
> *B&C: Sec. 37, Equation (1)*

^def-37-1

> [!remark]- Connections
> - The formulas for real $x$ are Euler's formula solved for $\cos$ and $\sin$: [[§15 Complex Roots of the Characteristic Equation#^def-15-1|331 Def. §15.1]], [[§53 Complex Numbers#^rem-53-1|235 Remark: Euler's Formula]]. The Maclaurin series $\sin x = \sum (-1)^nx^{2n+1}/(2n+1)!$ and $\cos x = \sum (-1)^nx^{2n}/(2n)!$ ([[§78 Taylor and Maclaurin Series#^thm-78-7|Calc Thm. §78.7]], [[§78 Taylor and Maclaurin Series#^thm-78-8|Calc Thm. §78.8]]) remain valid for all complex $z$, as the Maclaurin series of these entire functions, [[§64 Examples (Proof of Taylor's Theorem)#^prop-64-1|342 Prop. §64.1]].

> [!theorem] Theorem §37.1: sin z and cos z Are Entire
> The functions $\sin z$ and $\cos z$ are entire, and
>
> $$
> \frac{d}{dz}\sin z = \cos z \qquad\text{and}\qquad \frac{d}{dz}\cos z = -\sin z . \qquad (2)
> $$
>
> *B&C: Sec. 37, Equation (2)*

^thm-37-1

> [!proof]+ Proof
> The functions $e^{iz}$ and $e^{-iz}$ are entire, as compositions of the entire functions $\pm iz$ and $e^z$ ([[§30 The Exponential Function#^thm-30-3|Theorem §30.3]]), and by the chain rule ([[§20 Rules for Differentiation#^thm-20-4|Theorem §20.4]])
>
> $$
> \frac{d}{dz}e^{iz} = ie^{iz} \qquad\text{and}\qquad \frac{d}{dz}e^{-iz} = -ie^{-iz} .
> $$
>
> By (1), $\sin z$ and $\cos z$ are linear combinations of these, hence entire ([[§20 Rules for Differentiation#^thm-20-1|Theorem §20.1]], [[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]), and differentiating (1) term by term,
>
> $$
> \frac{d}{dz}\sin z = \frac{ie^{iz} + ie^{-iz}}{2i} = \frac{e^{iz} + e^{-iz}}{2} = \cos z, \qquad \frac{d}{dz}\cos z = \frac{ie^{iz} - ie^{-iz}}{2} = -\frac{e^{iz} - e^{-iz}}{2i} = -\sin z ,
> $$
>
> using $i/2 = -1/(2i)$ in the last step.

^pf-37-1

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§30 The Exponential Function#^thm-30-3|§30.3]], [[§20 Rules for Differentiation#^thm-20-1|§20.1]], [[§20 Rules for Differentiation#^thm-20-4|§20.4]], [[§25 Analytic Functions#^prop-25-1|§25.1]]

> [!theorem] Proposition §37.2: Parity and Euler's Formula
> For every $z$,
>
> $$
> \sin(-z) = -\sin z, \qquad \cos(-z) = \cos z , \qquad (3)
> $$
>
> and
>
> $$
> e^{iz} = \cos z + i\sin z . \qquad (4)
> $$
>
> When $z$ is real, (4) is Euler's formula.
>
> *B&C: Sec. 37, Equations (3) and (4)*

^prop-37-2

> [!proof]+ Proof
> Replacing $z$ by $-z$ in (1) interchanges $e^{iz}$ and $e^{-iz}$: this changes the sign of the numerator of $\sin z$ and leaves that of $\cos z$ unchanged, which is (3). Adding the two formulas (1),
>
> $$
> \cos z + i\sin z = \frac{e^{iz} + e^{-iz}}{2} + \frac{e^{iz} - e^{-iz}}{2} = e^{iz} .
> $$

^pf-37-2

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]]

## Identities

A variety of identities carry over from trigonometry.

> [!theorem] Theorem §37.3: Addition Formulas
> For all complex $z_1$, $z_2$,
>
> $$
> \sin(z_1 + z_2) = \sin z_1\cos z_2 + \cos z_1\sin z_2 , \qquad (5)
> $$
>
> $$
> \cos(z_1 + z_2) = \cos z_1\cos z_2 - \sin z_1\sin z_2 . \qquad (6)
> $$
>
> *B&C: Sec. 37, Equations (5) and (6) (proved in Sec. 38, Exercises 2 and 3)*

^thm-37-3

> [!proof]+ Proof
> **(5).** By (4), and multiplying out,
>
> $$
> e^{iz_1}e^{iz_2} = (\cos z_1 + i\sin z_1)(\cos z_2 + i\sin z_2) = \cos z_1\cos z_2 - \sin z_1\sin z_2 + i(\sin z_1\cos z_2 + \cos z_1\sin z_2) .
> $$
>
> By (3), $e^{-iz} = \cos(-z) + i\sin(-z) = \cos z - i\sin z$, so in the same way
>
> $$
> e^{-iz_1}e^{-iz_2} = (\cos z_1 - i\sin z_1)(\cos z_2 - i\sin z_2) = \cos z_1\cos z_2 - \sin z_1\sin z_2 - i(\sin z_1\cos z_2 + \cos z_1\sin z_2) .
> $$
>
> By (1) and the law of exponents $e^{i(z_1 + z_2)} = e^{iz_1}e^{iz_2}$ ([[§30 The Exponential Function#^thm-30-2|Theorem §30.2]]),
>
> $$
> \sin(z_1 + z_2) = \frac{1}{2i}\big[e^{i(z_1 + z_2)} - e^{-i(z_1 + z_2)}\big] = \frac{1}{2i}\big[e^{iz_1}e^{iz_2} - e^{-iz_1}e^{-iz_2}\big] ,
> $$
>
> and subtracting the two products above leaves $2i(\sin z_1\cos z_2 + \cos z_1\sin z_2)$ in the bracket. This is (5).
>
> **(6).** Fix $z_2$. By (5), $\sin(z + z_2) = \sin z\cos z_2 + \cos z\sin z_2$ for all $z$. Both sides are entire functions of $z$; differentiate with respect to $z$, using (2) and the chain rule on the left:
>
> $$
> \cos(z + z_2) = \cos z\cos z_2 - \sin z\sin z_2 .
> $$
>
> Setting $z = z_1$ gives (6).

^pf-37-3

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|§37.1]], [[§37 The Trigonometric Functions sin z and cos z#^prop-37-2|§37.2]], [[§30 The Exponential Function#^thm-30-2|§30.2]]

> [!remark]- Connections
> - The real addition formulas, proved geometrically: [[§119 Trigonometry#^thm-119-6|Calc Thm. §119.6]]. Here they follow from the law of exponents alone, and they hold for complex arguments; conversely, for real arguments the proof above is a second proof of the calculus formulas, given Euler's formula. [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|331 Prop. §15.1]] runs the argument the other way, deriving the law of exponents from the real addition formulas.

> [!theorem] Corollary §37.4: Double Angles, Shifts, the Pythagorean Identity, Periods
> For all $z$:
>
> $$
> \sin 2z = 2\sin z\cos z, \qquad \cos 2z = \cos^2z - \sin^2z , \qquad (7)
> $$
>
> $$
> \sin\Big(z + \frac\pi2\Big) = \cos z, \qquad \sin\Big(z - \frac\pi2\Big) = -\cos z , \qquad (8)
> $$
>
> $$
> \sin^2z + \cos^2z = 1 , \qquad (9)
> $$
>
> $$
> \sin(z + 2\pi) = \sin z, \qquad \sin(z + \pi) = -\sin z , \qquad (10)
> $$
>
> $$
> \cos(z + 2\pi) = \cos z, \qquad \cos(z + \pi) = -\cos z . \qquad (11)
> $$
>
> *B&C: Sec. 37, Equations (7)–(11)*

^cor-37-4

> [!proof]+ Proof
> **(7)** Put $z_1 = z_2 = z$ in (5) and (6).
>
> **(8)** Put $z_1 = z$ and $z_2 = \pm\frac\pi2$ in (5); for the real numbers $\pm\frac\pi2$, $\cos(\pm\frac\pi2) = 0$ and $\sin(\pm\frac\pi2) = \pm1$, so $\sin(z \pm \frac\pi2) = \pm\cos z$.
>
> **(9)** (B&C's Exercise 4(a).) Put $z_1 = z$ and $z_2 = -z$ in (6) and use (3):
>
> $$
> 1 = \cos 0 = \cos z\cos(-z) - \sin z\sin(-z) = \cos^2z + \sin^2z .
> $$
>
> **(10), (11)** Put $z_2 = 2\pi$ or $z_2 = \pi$ in (5) and (6), with $\cos 2\pi = 1$, $\sin 2\pi = 0$, $\cos\pi = -1$, $\sin\pi = 0$.

^pf-37-4

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^thm-37-3|§37.3]], [[§37 The Trigonometric Functions sin z and cos z#^prop-37-2|§37.2]]

## Real and Imaginary Parts

When $y$ is real, the hyperbolic functions of calculus are

$$
\sinh y = \frac{e^y - e^{-y}}{2} \qquad\text{and}\qquad \cosh y = \frac{e^y + e^{-y}}{2} .
$$

> [!theorem] Proposition §37.5: Components of sin z and cos z
> For real $y$,
>
> $$
> \sin(iy) = i\sinh y \qquad\text{and}\qquad \cos(iy) = \cosh y , \qquad (12)
> $$
>
> and for $z = x + iy$,
>
> $$
> \sin z = \sin x\cosh y + i\cos x\sinh y , \qquad (13)
> $$
>
> $$
> \cos z = \cos x\cosh y - i\sin x\sinh y . \qquad (14)
> $$
>
> *B&C: Sec. 37, Equations (12)–(14)*

^prop-37-5

> [!proof]+ Proof
> **(12)** By (1) with $z = iy$, so that $iz = -y$,
>
> $$
> \sin(iy) = \frac{e^{-y} - e^{y}}{2i} = i\,\frac{e^y - e^{-y}}{2} = i\sinh y, \qquad \cos(iy) = \frac{e^{-y} + e^{y}}{2} = \cosh y ,
> $$
>
> using $-1/i = i$.
>
> **(13), (14)** Write $z_1 = x$ and $z_2 = iy$ in the addition formulas (5) and (6), and refer to (12):
>
> $$
> \sin(x + iy) = \sin x\cos(iy) + \cos x\sin(iy) = \sin x\cosh y + i\cos x\sinh y ,
> $$
>
> $$
> \cos(x + iy) = \cos x\cos(iy) - \sin x\sin(iy) = \cos x\cosh y - i\sin x\sinh y .
> $$
>
> (Once (13) is known, (14) also follows from [[§21 Cauchy–Riemann Equations#^thm-21-1|Theorem §21.1]]: where $f = u + iv$ is differentiable, $f'(z) = u_x + iv_x$. With $f = \sin z$, $u = \sin x\cosh y$ and $v = \cos x\sinh y$, so $\cos z = f'(z) = \cos x\cosh y - i\sin x\sinh y$.)

^pf-37-5

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^def-37-1|Def. §37.1]], [[§37 The Trigonometric Functions sin z and cos z#^thm-37-3|§37.3]], [[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|§37.1]], [[§21 Cauchy–Riemann Equations#^thm-21-1|§21.1]]

![[m342-37-1.svg]]
*The map $w = \sin z$ on the half strip $-\frac\pi2 \le x \le \frac\pi2$, $y \ge 0$, computed from (13): $u = \sin x\cosh y$, $v = \cos x\sinh y$. A horizontal segment $y = b > 0$ (red; $b = 0.5, 1, 1.5$) goes to the upper half of the ellipse $u^2/\cosh^2b + v^2/\sinh^2b = 1$; a vertical half line $x = a$ (blue; $a = 0, \pm\frac\pi6, \pm\frac\pi3, \pm\frac\pi2$) goes to a branch of the hyperbola $u^2/\sin^2a - v^2/\cos^2a = 1$ (for $a = 0$ the positive $v$ axis, for $a = \pm\frac\pi2$ the rays $u \ge 1$ and $u \le -1$). The ellipses grow like $\cosh b$: $\sin z$ is unbounded. The mapping is studied in [[§104★ Mapping Vertical Line Segments by w = sin z|§104★]] and [[§105★ Mapping Horizontal Line Segments by w = sin z|§105★]].*

> [!theorem] Proposition §37.6: Moduli of sin z and cos z
> For $z = x + iy$,
>
> $$
> |\sin z|^2 = \sin^2x + \sinh^2y , \qquad (15)
> $$
>
> $$
> |\cos z|^2 = \cos^2x + \sinh^2y . \qquad (16)
> $$
>
> Consequently $\sin z$ and $\cos z$ are not bounded in the complex plane ([[§18 Continuity#^def-18-2|Definition §18.2]]), whereas $|\sin x| \le 1$ and $|\cos x| \le 1$ for all real $x$.
>
> *B&C: Sec. 37, Equations (15) and (16) (derived in Sec. 38, Exercise 7)*

^prop-37-6

> [!proof]+ Proof
> By (13), using $\cos^2x = 1 - \sin^2x$ and $\cosh^2y = 1 + \sinh^2y$,
>
> $$
> |\sin z|^2 = \sin^2x\cosh^2y + \cos^2x\sinh^2y = \sin^2x(1 + \sinh^2y) + (1 - \sin^2x)\sinh^2y = \sin^2x + \sinh^2y .
> $$
>
> By (14), in the same way,
>
> $$
> |\cos z|^2 = \cos^2x\cosh^2y + \sin^2x\sinh^2y = \cos^2x(1 + \sinh^2y) + (1 - \cos^2x)\sinh^2y = \cos^2x + \sinh^2y .
> $$
>
> Since $\sinh y \to \infty$ as $y \to \infty$, (15) gives $|\sin(iy)| = |\sinh y| \to \infty$, and (16) gives $|\cos(iy)| = \cosh y \to \infty$: neither function is bounded.

^pf-37-6

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|§37.5]], [[§24 Hyperbolic Functions#^thm-24-1|Calc Thm. §24.1]] ($\cosh^2y - \sinh^2y = 1$)

## Examples

> [!example] Example §37.1: Identities Straight from the Exponentials
> **(a)** $\cos^2z + \sin^2z = 1$ for all complex $z$, directly from (1). Write $a = e^{iz}$, $b = e^{-iz}$, so $ab = e^{iz - iz} = 1$ (Theorem §30.2). Then
>
> $$
> \cos^2z + \sin^2z = \Big(\frac{a + b}{2}\Big)^2 + \Big(\frac{a - b}{2i}\Big)^2 = \frac{(a + b)^2 - (a - b)^2}{4} = \frac{4ab}{4} = 1 .
> $$
>
> **(b)** $\cos(z_1 + z_2) = \cos z_1\cos z_2 - \sin z_1\sin z_2$, directly from (1). Write $a_k = e^{iz_k}$, $b_k = e^{-iz_k}$; by the law of exponents $e^{\pm i(z_1 + z_2)} = e^{\pm iz_1}e^{\pm iz_2}$, so
>
> $$
> \cos(z_1 + z_2) = \frac{a_1a_2 + b_1b_2}{2} .
> $$
>
> On the other side,
>
> $$
> \cos z_1\cos z_2 = \frac{(a_1 + b_1)(a_2 + b_2)}{4} = \frac{a_1a_2 + a_1b_2 + b_1a_2 + b_1b_2}{4}, \qquad \sin z_1\sin z_2 = \frac{(a_1 - b_1)(a_2 - b_2)}{(2i)^2} = -\frac{a_1a_2 - a_1b_2 - b_1a_2 + b_1b_2}{4} .
> $$
>
> Subtracting, the mixed terms $a_1b_2 + b_1a_2$ cancel and $\cos z_1\cos z_2 - \sin z_1\sin z_2 = \frac{2a_1a_2 + 2b_1b_2}{4} = \cos(z_1 + z_2)$.
>
> **(c)** A third proof of (9), by the uniqueness of analytic continuation: $f(z) = \sin^2z + \cos^2z - 1$ is entire and vanishes on the $x$ axis (the identity of calculus), so by [[§28★ Uniquely Determined Analytic Functions#^lem-28-1|Lemma §28.1]] it vanishes everywhere (compare [[§28★ Uniquely Determined Analytic Functions#^ex-28-3|Example §28.3]]).
>
> *B&C: Sec. 38, Exercise 4; Source: 342 HW 4, Problem 2(a), (b)*

^ex-37-1

> [!example] Example §37.2: Sine and Cosine at Complex Points
> Use (13) and (14), with $\cosh(\ln a) = \frac12\big(a + \frac1a\big)$ and $\sinh(\ln a) = \frac12\big(a - \frac1a\big)$ for $a > 0$.
>
> **(a)** $\cosh(\ln 3) = \frac12\big(3 + \frac13\big) = \frac53$ and $\sinh(\ln 3) = \frac12\big(3 - \frac13\big) = \frac43$. So
>
> $$
> \sin\Big(\frac\pi4 + i\ln 3\Big) = \sin\frac\pi4\cosh(\ln 3) + i\cos\frac\pi4\sinh(\ln 3) = \frac{\sqrt2}{2}\cdot\frac53 + i\frac{\sqrt2}{2}\cdot\frac43 = \frac{5\sqrt2}{6} + \frac{2\sqrt2}{3}i \approx 1.1785 + 0.9428i .
> $$
>
> **(b)** $\sin(\pi + i\ln 3) = \sin\pi\cosh(\ln 3) + i\cos\pi\sinh(\ln 3) = -\frac43 i$. (Or by (10): $\sin(\pi + i\ln 3) = -\sin(i\ln 3) = -i\sinh(\ln 3)$.)
>
> **(c)** $\cos\big(\frac\pi2 - i\ln 2\big) = \cos\frac\pi2\cosh(-\ln 2) - i\sin\frac\pi2\sinh(-\ln 2) = i\sinh(\ln 2) = i\cdot\frac12\Big(2 - \frac12\Big) = \frac34 i$.
>
> The keys of the 2002 and 2005 finals compute (a) and (b) directly from (1), as in Example §37.1, and get the same values.
>
> *Source: 342 practice final (Fall 2002), Q2(a); 342 practice final (Spring 2005), Q2(a); 342 sample final (Fall 1999), Q8*

^ex-37-2

> [!example] Example §37.3: sin z Is Unbounded
> Is there a positive number $M$ with $|\sin z| \le M$ for all complex $z$?
>
> No. By (15), $|\sin z|^2 = \sin^2x + \sinh^2y$, and since $0 \le \sin^2x \le 1$ and $1 + \sinh^2y = \cosh^2y$,
>
> $$
> |\sinh y| \le |\sin z| \le \cosh y .
> $$
>
> In particular $|\sin z| \ge |\sinh y| \to \infty$ as $|y| \to \infty$. For instance, any $M$ is exceeded at $z = iy$ with $\sinh y > M$, say $y = \ln(2M + 1)$, where $\sinh y = \frac12\big(2M + 1 - \frac{1}{2M + 1}\big) > M$. Likewise (15) gives $|\sin z| \ge |\sin x|$: off the real axis $|\sin z|$ only gets larger.
>
> Liouville's theorem gives the same conclusion without computation: a bounded entire function is constant ([[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-1|Theorem §58.1]]), and $\sin z$ is entire and not constant.
>
> *B&C: Sec. 38, Exercises 8(a) and 9(a); Source: 342 practice final (Fall 2009), Q1(b)*

^ex-37-3
