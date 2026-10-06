---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 10
bc: "10"
aliases: ["B&C 10"]
tags: [complex-variables, math342]
---
← [[§9 Arguments of Products and Quotients]] · ↑ [[· 1 Complex Numbers]] · [[§11 Examples (Roots of Complex Numbers)]] →

*Brown–Churchill, Section 10 · MAT 342 HW 2.*

Every nonzero complex number $z_0$ has exactly $n$ distinct $n$th roots, and exponential form finds them all at once. Two numbers in exponential form are equal exactly when their moduli agree and their angles differ by a multiple of $2\pi$; applied to $z^n = r^ne^{in\theta} = r_0e^{i\theta_0}$, this gives $r = \sqrt[n]{r_0}$ and $n$ inequivalent angles $\theta_0/n + 2k\pi/n$. So the roots sit at the vertices of a regular $n$-gon inscribed in the circle $|z| = \sqrt[n]{r_0}$, each obtained from the previous one by a rotation through $2\pi/n$. Unlike the real case, there is no sign ambiguity to resolve and no number without roots; the price is that "$z_0^{1/n}$" denotes a set of $n$ values, the first multiple-valued function of the subject.

## Equality in Exponential Form

As $\theta$ increases, the point $z = re^{i\theta}$ moves counterclockwise around the circle of radius $r$ about the origin, and when $\theta$ is increased or decreased by $2\pi$ it returns to its starting point (B&C, Fig. 10). This is the content of the following statement.

> [!theorem] Proposition §10.1: Equality in Exponential Form
> Two nonzero complex numbers $z_1 = r_1e^{i\theta_1}$ and $z_2 = r_2e^{i\theta_2}$ are equal if and only if
>
> $$
> r_1 = r_2 \qquad\text{and}\qquad \theta_1 = \theta_2 + 2k\pi
> $$
>
> for some integer $k$ ($k = 0, \pm1, \pm2, \ldots$).
>
> *B&C: Sec. 10 (text)*

^prop-10-1

> [!proof]+ Proof
> B&C call this evident from the figure; here is why. If $r_1 = r_2$ and $\theta_1 = \theta_2 + 2k\pi$, then $\cos\theta_1 = \cos\theta_2$ and $\sin\theta_1 = \sin\theta_2$ by periodicity, so $z_1 = z_2$. Conversely, suppose $z_1 = z_2$. Taking moduli, $r_1 = |z_1| = |z_2| = r_2$. Dividing, by (2) of [[§8 Products and Powers in Exponential Form#^thm-8-1|Theorem §8.1]],
>
> $$
> 1 = \frac{z_1}{z_2} = \frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)} = \cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2) ,
> $$
>
> so $\cos(\theta_1 - \theta_2) = 1$. The cosine equals $1$ exactly at the integer multiples of $2\pi$, so $\theta_1 - \theta_2 = 2k\pi$.

^pf-10-1

*Uses:* [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]], [[§7 Exponential Form#^def-7-2|Def. §7.2]], [[§119 Trigonometry#^thm-119-5|Calc Thm. §119.5]] (periodicity)

## The nth Roots

An **$n$th root** of a nonzero complex number $z_0$ ($n = 2, 3, \ldots$) is a number $z$ with $z^n = z_0$; every such $z$ is nonzero.

> [!theorem] Theorem §10.2: The nth Roots of a Complex Number
> Let $z_0 = r_0e^{i\theta_0}$ be nonzero and $n = 2, 3, \ldots$. Then $z_0$ has exactly $n$ distinct $n$th roots, namely
>
> $$
> c_k = \sqrt[n]{r_0}\exp\Big[i\Big(\frac{\theta_0}{n} + \frac{2k\pi}{n}\Big)\Big] \qquad (k = 0, 1, 2, \ldots, n - 1) , \qquad (1)
> $$
>
> where $\sqrt[n]{r_0}$ denotes the unique positive $n$th root of the positive real number $r_0$. They all lie on the circle $|z| = \sqrt[n]{r_0}$ about the origin and are equally spaced every $2\pi/n$ radians, starting with argument $\theta_0/n$. When $n = 2$ they lie at opposite ends of a diameter of that circle, $c_1 = -c_0$; when $n \ge 3$ they lie at the vertices of a regular polygon of $n$ sides inscribed in it.
>
> *B&C: Sec. 10, Equation (1)*

^thm-10-2

> [!proof]+ Proof
> **All roots.** A nonzero $z = re^{i\theta}$ is an $n$th root of $z_0$ if and only if $z^n = z_0$, that is, by (4) of [[§8 Products and Powers in Exponential Form#^thm-8-2|Theorem §8.2]],
>
> $$
> r^ne^{in\theta} = r_0e^{i\theta_0} .
> $$
>
> By Proposition §10.1 this holds if and only if $r^n = r_0$ and $n\theta = \theta_0 + 2k\pi$ for some integer $k$, that is,
>
> $$
> r = \sqrt[n]{r_0} \qquad\text{and}\qquad \theta = \frac{\theta_0 + 2k\pi}{n} = \frac{\theta_0}{n} + \frac{2k\pi}{n} \qquad (k = 0, \pm1, \pm2, \ldots) .
> $$
>
> So the $n$th roots of $z_0$ are exactly the numbers $\sqrt[n]{r_0}\exp\big[i\big(\frac{\theta_0}{n} + \frac{2k\pi}{n}\big)\big]$, $k$ any integer.
>
> **Exactly $n$ of them are distinct.** (B&C: "evidently"; here is why.) The values $k = 0, 1, \ldots, n - 1$ give distinct numbers: if two of them, with $0 \le j < k \le n - 1$, were equal, Proposition §10.1 would give $\frac{2(k - j)\pi}{n} = 2m\pi$ for an integer $m$, that is, $k - j = mn$, impossible since $0 < k - j < n$. No further roots arise from other values of $k$: dividing, $k = qn + s$ with $q$ an integer and $0 \le s \le n - 1$, and then
>
> $$
> \frac{\theta_0}{n} + \frac{2k\pi}{n} = \Big(\frac{\theta_0}{n} + \frac{2s\pi}{n}\Big) + 2q\pi ,
> $$
>
> so by Proposition §10.1 the $k$th number equals $c_s$.
>
> **Geometry.** All $c_k$ have modulus $\sqrt[n]{r_0}$, and the argument of $c_{k+1}$ exceeds that of $c_k$ by $2\pi/n$. For $n = 2$, $c_1 = \sqrt{r_0}\,e^{i\theta_0/2}e^{i\pi} = -c_0$, since $e^{i\pi} = -1$.

^pf-10-2

*Uses:* [[§8 Products and Powers in Exponential Form#^thm-8-2|§8.2]], [[§10 Roots of Complex Numbers#^prop-10-1|§10.1]]

> [!remark]- Connections
> - Theorem §10.2 shows that the polynomial $z^n - z_0$ has exactly $n$ distinct zeros. That a polynomial of degree $n$ has at most $n$ zeros is [[§13 Polynomials#^ladr-4-8|LADR 4.8]]; that every nonconstant polynomial has a zero is the fundamental theorem of algebra, [[§13 Polynomials#^ladr-4-12|LADR 4.12]] (hub [[Fundamental theorem of algebra, first version]]), proved in this subject in [[§58 Liouville's Theorem and the Fundamental Theorem of Algebra#^thm-58-2|Theorem §58.2]].

> [!definition] Definition §10.1: The Set of Roots; Principal Root
> The symbol $z_0^{1/n}$ denotes the **set** of $n$th roots of $z_0$. In particular, if $z_0$ is a positive real number $r_0$, the symbol $r_0^{1/n}$ denotes the entire set of roots, and $\sqrt[n]{r_0}$ is reserved for the one positive root. When the value of $\theta_0$ used in (1) is the principal value $\operatorname{Arg} z_0$ ($-\pi < \theta_0 \le \pi$), the number $c_0$ is called the **principal root**. Thus when $z_0$ is a positive real number $r_0$, its principal root is $\sqrt[n]{r_0}$.
>
> *B&C: Sec. 10 (text)*

^def-10-1

> [!theorem] Proposition §10.3: Roots Through a Root of Unity
> Let
>
> $$
> \omega_n = \exp\Big(i\frac{2\pi}{n}\Big) . \qquad (2)
> $$
>
> Then
>
> $$
> \omega_n^k = \exp\Big(i\frac{2k\pi}{n}\Big) \quad (k = 0, 1, \ldots, n - 1) , \qquad (3) \qquad\qquad c_k = c_0\,\omega_n^k \quad (k = 0, 1, \ldots, n - 1) . \qquad (4)
> $$
>
> The number $c_0$ here can be replaced by any particular $n$th root $c$ of $z_0$: the $n$th roots of $z_0$ are $c, c\,\omega_n, \ldots, c\,\omega_n^{n-1}$.
>
> *B&C: Sec. 10, Equations (2)–(4)*

^prop-10-3

> [!proof]+ Proof
> Equation (3) is de Moivre's formula (5) of §8. Writing (1) as
>
> $$
> c_k = \sqrt[n]{r_0}\exp\Big(i\frac{\theta_0}{n}\Big)\exp\Big(i\frac{2k\pi}{n}\Big) = c_0\,\omega_n^k
> $$
>
> by the law of exponents gives (4).
>
> **Any root may serve as $c_0$.** (B&C justify this by noting that $\omega_n$ represents a counterclockwise rotation through $2\pi/n$; here is the computation.) Let $c$ be any $n$th root of $z_0$. Since $\omega_n^n = e^{i2\pi} = 1$, each $c\,\omega_n^k$ is an $n$th root: $(c\,\omega_n^k)^n = c^n(\omega_n^n)^k = z_0$. The $n$ numbers $\omega_n^k$, $k = 0, \ldots, n - 1$, are distinct (they are the $c_k$ of Theorem §10.2 for $z_0 = 1$), and $c \ne 0$, so by the cancellation law the $c\,\omega_n^k$ are distinct too. By Theorem §10.2 there are only $n$ roots, so these are all of them.

^pf-10-3

*Uses:* [[§10 Roots of Complex Numbers#^thm-10-2|§10.2]], [[§8 Products and Powers in Exponential Form#^cor-8-3|§8.3]], [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]], [[§3 Further Algebraic Properties#^prop-3-3|§3.3]]

> [!remark]- Connections
> - Multiplication by $\omega_n$ is the rotation of the plane through $2\pi/n$, whose matrix is the rotation matrix of [[§53 Complex Numbers#^rem-53-3|235 Remark: Complex Numbers as 2 × 2 Matrices]] with $r = 1$, $\varphi = 2\pi/n$. Its $n$th power is the identity.

> [!remark] Remark: Method — Finding nth Roots
> A convenient way to remember (1):
> 1. **Write $z_0$ in its most general exponential form**
>
> $$
> z_0 = r_0\,e^{i(\theta_0 + 2k\pi)} \qquad (k = 0, \pm1, \pm2, \ldots) , \qquad (5)
> $$
>
> with $\theta_0 = \operatorname{Arg} z_0$ if the principal root is wanted ([[§7 Exponential Form#^rem-7-1|Method — Writing z in Exponential Form]]).
> 2. **Apply the laws of fractional exponents formally**, keeping in mind that there are precisely $n$ roots:
>
> $$
> c_k = \big[r_0\,e^{i(\theta_0 + 2k\pi)}\big]^{1/n} = \sqrt[n]{r_0}\exp\Big[\frac{i(\theta_0 + 2k\pi)}{n}\Big] = \sqrt[n]{r_0}\exp\Big[i\Big(\frac{\theta_0}{n} + \frac{2k\pi}{n}\Big)\Big] \qquad (k = 0, 1, \ldots, n - 1) .
> $$
>
> 3. **Convert** to $x + iy$ if asked, using $\cos$ and $\sin$ of the angles $\frac{\theta_0}{n} + \frac{2k\pi}{n}$.
> 4. **Check the picture:** the roots lie on $|z| = \sqrt[n]{r_0}$, spaced $2\pi/n$ apart, starting at angle $\theta_0/n$; and $c_k = c_0\,\omega_n^k$.
>
> The "laws of exponents" in step 2 are only a mnemonic: Theorem §10.2 is what guarantees that the result is correct and complete. Getting $\theta_0$ right, sign included, matters: a wrong $\theta_0$ still produces $n$ equally spaced points on the right circle, but they are the roots of a different number.

^rem-10-1

## Examples

> [!example] Example §10.1: The Cube Roots of −27
> Find all solutions of $z^3 = -27$ and convert them to the form $x + iy$.
>
> Since $-27 = 27\,e^{i(\pi + 2k\pi)}$ and $\sqrt[3]{27} = 3$,
>
> $$
> c_k = 3\exp\Big[i\Big(\frac\pi3 + \frac{2k\pi}{3}\Big)\Big] \qquad (k = 0, 1, 2) .
> $$
>
> The angles are $\frac\pi3$, $\pi$, $\frac{5\pi}{3}$ (principal values $\frac\pi3$, $\pi$, $-\frac\pi3$), so
>
> $$
> c_0 = 3e^{i\pi/3} = \frac32 + \frac{3\sqrt3}{2}i, \qquad c_1 = 3e^{i\pi} = -3, \qquad c_2 = 3e^{-i\pi/3} = \frac32 - \frac{3\sqrt3}{2}i .
> $$
>
> They are the vertices of an equilateral triangle inscribed in $|z| = 3$, one vertex at the real root $-3$; $c_0$ is the principal root ($\theta_0 = \operatorname{Arg}(-27) = \pi$). Check: $c_0^3 = 27e^{i\pi} = -27$.
>
> *Source: 342 HW 2, Problem 1(a)*

^ex-10-1

> [!example] Example §10.2: The Eighth Roots of 16
> Find all solutions of $z^8 = 16$ and convert them to the form $x + iy$.
>
> Since $16 = 16\,e^{i(0 + 2k\pi)}$ and $\sqrt[8]{16} = 16^{1/8} = \sqrt2$,
>
> $$
> c_k = \sqrt2\exp\Big(i\frac{2k\pi}{8}\Big) = \sqrt2\,e^{ik\pi/4} \qquad (k = 0, 1, \ldots, 7) .
> $$
>
> With $\sqrt2\,e^{i\pi/4} = \sqrt2\big(\frac{1}{\sqrt2} + \frac{i}{\sqrt2}\big) = 1 + i$ and its rotations by multiples of $\frac\pi4$:
>
> $$
> \sqrt2, \quad 1 + i, \quad \sqrt2\,i, \quad -1 + i, \quad -\sqrt2, \quad -1 - i, \quad -\sqrt2\,i, \quad 1 - i .
> $$
>
> They form a regular octagon inscribed in $|z| = \sqrt2$; the principal root is the positive root $\sqrt2$. Since $\omega_8 = e^{i\pi/4}$, the list is $\sqrt2\,\omega_8^k$ (Proposition §10.3).
>
> *Source: 342 HW 2, Problem 1(b)*

^ex-10-2

> [!example] Example §10.3: The Fifth Roots of 1 − i
> Find all solutions of $z^5 = 1 - i$, in exponential form.
>
> **Exponential form of $z_0$.** $|1 - i| = \sqrt2$, and $1 - i$ is in the fourth quadrant with reference angle $\frac\pi4$, so $\operatorname{Arg}(1 - i) = -\frac\pi4$ and
>
> $$
> 1 - i = \sqrt2\,e^{i(-\pi/4 + 2k\pi)} \qquad (k = 0, \pm1, \ldots) .
> $$
>
> **Roots.** $\sqrt[5]{\sqrt2} = 2^{1/10}$ and $\big(-\frac\pi4 + 2k\pi\big)/5 = -\frac{\pi}{20} + \frac{2k\pi}{5} = \frac{(8k - 1)\pi}{20}$, so
>
> $$
> c_k = 2^{1/10}\exp\Big[i\Big(-\frac{\pi}{20} + \frac{2k\pi}{5}\Big)\Big] \qquad (k = 0, 1, 2, 3, 4) :
> $$
>
> $$
> c_0 = 2^{1/10}e^{-i\pi/20}, \quad c_1 = 2^{1/10}e^{i7\pi/20}, \quad c_2 = 2^{1/10}e^{i3\pi/4}, \quad c_3 = 2^{1/10}e^{-i17\pi/20}, \quad c_4 = 2^{1/10}e^{-i9\pi/20} ,
> $$
>
> where $c_3$ and $c_4$ have been written with their principal arguments ($\frac{23\pi}{20} - 2\pi$ and $\frac{31\pi}{20} - 2\pi$). They form a regular pentagon inscribed in $|z| = 2^{1/10} \approx 1.072$, and $c_0$ is the principal root.
>
> **Check.** One root has a simple rectangular form: $c_2 = 2^{1/10}e^{i3\pi/4} = 2^{1/10}\cdot\frac{-1 + i}{\sqrt2} = 2^{-2/5}(-1 + i)$, and $(-1 + i)^5 = (\sqrt2)^5e^{i15\pi/4} = 4\sqrt2\,e^{-i\pi/4} = 4(1 - i)$, so $c_2^5 = 2^{-2}\cdot 4(1 - i) = 1 - i$.
>
> The sign of the argument matters: starting from $+\frac\pi4$ instead of $-\frac\pi4$ produces the angles $\frac{\pi}{20} + \frac{2k\pi}{5}$, which are the fifth roots of $1 + i$, the conjugates of the $c_k$.
>
> *Source: 342 HW 2, Problem 1(c)*

^ex-10-3

![[m342-10-1.svg]]
*The roots of Examples §10.1–§10.3: the cube roots of $-27$ on $|z| = 3$ (left), the eighth roots of $16$ on $|z| = \sqrt2$ (middle), and the fifth roots of $1 - i$ on $|z| = 2^{1/10}$ (right, with $1 - i$ itself marked in gray). In each case the roots are equally spaced, $2\pi/n$ apart, starting from the principal root $c_0$ (red) at angle $\operatorname{Arg} z_0/n$.*
