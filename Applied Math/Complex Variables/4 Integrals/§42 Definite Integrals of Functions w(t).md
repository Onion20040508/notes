---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 42
bc: "42"
aliases: ["B&C 42"]
tags: [complex-variables, math342]
---
← [[§41 Derivatives of Functions w(t)]] · ↑ [[· 4 Integrals]] · [[§43 Contours]] →

*Brown–Churchill, Section 42.*

The definite integral of a complex-valued function $w(t)$ of a real variable is defined component by component, so linearity (now with complex constants), additivity over subintervals and the fundamental theorem of calculus carry over from real calculus. Every contour integral of [[§44 Contour Integrals#^def-44-1|§44]] is an integral of this kind over a parameter interval, so these rules are used in every later computation. As with derivatives, not everything carries over: the mean value theorem for integrals fails. The examples also show the most useful trick of the section, computing two real integrals at once as the real and imaginary parts of one complex integral.

## The Definite Integral

> [!definition] Definition §42.1: Definite Integral of a Function w(t)
> When $w(t) = u(t) + iv(t)$ (1) with $u$ and $v$ real-valued, the **definite integral** of $w(t)$ over an interval $a \le t \le b$ is
>
> $$
> \int_a^b w(t)\,dt = \int_a^b u(t)\,dt + i\int_a^b v(t)\,dt , \qquad (2)
> $$
>
> provided the individual integrals on the right exist. Thus
>
> $$
> \operatorname{Re}\int_a^b w(t)\,dt = \int_a^b \operatorname{Re}[w(t)]\,dt \qquad\text{and}\qquad \operatorname{Im}\int_a^b w(t)\,dt = \int_a^b \operatorname{Im}[w(t)]\,dt . \qquad (3)
> $$
>
> Improper integrals of $w(t)$ over unbounded intervals are defined in the same way, from the improper integrals of $u$ and $v$.
>
> *B&C: Sec. 42 (text)*

^def-42-1

> [!definition] Definition §42.2: Piecewise Continuous Function
> A real-valued function on $a \le t \le b$ is **piecewise continuous** if it is continuous everywhere in the interval except possibly at finitely many points where, although discontinuous, it has one-sided limits. Only the right-hand limit is required at $a$, and only the left-hand limit at $b$. A function $w = u + iv$ is **piecewise continuous** when both $u$ and $v$ are.
>
> *B&C: Sec. 42 (text)*

^def-42-2

B&C states that the integrals in (2) exist when $u$ and $v$ are piecewise continuous, and that the expected rules for complex constant multiples, sums, interchanging the limits and splitting the interval "are easy to verify by recalling corresponding results in calculus". Here they are.

> [!theorem] Proposition §42.1: Existence and Rules for Integrals of w(t)
> Let $w$, $w_1$, $w_2$ be piecewise continuous on $a \le t \le b$, and let $z_0$ be a complex constant. Then:
>
> **(a)** $\int_a^b w(t)\,dt$ exists;
>
> **(b)** $\displaystyle\int_a^b z_0w(t)\,dt = z_0\int_a^b w(t)\,dt$ and $\displaystyle\int_a^b \big[w_1(t) + w_2(t)\big]dt = \int_a^b w_1(t)\,dt + \int_a^b w_2(t)\,dt$;
>
> **(c)** $\displaystyle\int_b^a w(t)\,dt = -\int_a^b w(t)\,dt$;
>
> **(d)** $\displaystyle\int_a^b w(t)\,dt = \int_a^c w(t)\,dt + \int_c^b w(t)\,dt$ for $a < c < b$.
>
> *B&C: Sec. 42 (text)*

^prop-42-1

> [!proof]+ Proof
> **(a)** It suffices to show that a piecewise continuous real function $u$ is integrable. Let $a = t_0 < t_1 < \cdots < t_n = b$ include all points where $u$ is discontinuous. On each $[t_{k-1}, t_k]$, redefine $u$ at the two endpoints as its one-sided limits there; the result is continuous on the closed interval, hence integrable, and changing a function at finitely many points changes neither integrability nor the integral. By additivity over subintervals, $u$ is integrable on $[a, b]$. Apply this to $u$ and $v$.
>
> **(b)** Let $z_0 = x_0 + iy_0$. Then $z_0w = (x_0u - y_0v) + i(y_0u + x_0v)$, and by (2) and linearity of real integrals,
>
> $$
> \int_a^b z_0w\,dt = \Big(x_0\int u - y_0\int v\Big) + i\Big(y_0\int u + x_0\int v\Big) = (x_0 + iy_0)\Big(\int u + i\int v\Big) = z_0\int_a^b w\,dt .
> $$
>
> The sum rule is linearity applied to the real and imaginary parts.
>
> **(c), (d)** These hold for $u$ and $v$ (the first is the convention $\int_b^a = -\int_a^b$, the second additivity over subintervals); combine them by (2).

^pf-42-1

*Uses:* [[§42 Definite Integrals of Functions w(t)#^def-42-1|Def. §42.1]], [[§42 Definite Integrals of Functions w(t)#^def-42-2|Def. §42.2]], [[§32 The Definition of the Riemann Integral#^thm-32-7|451 Thm. §32.7]] (continuous functions are integrable), [[§33 Properties of the Riemann Integral#^thm-33-2|451 Thm. §33.2]] (linearity), [[§33 Properties of the Riemann Integral#^thm-33-5|451 Thm. §33.5]] (additivity)

## The Fundamental Theorem of Calculus

> [!theorem] Theorem §42.2: Fundamental Theorem of Calculus for w(t)
> Suppose that $w(t) = u(t) + iv(t)$ and $W(t) = U(t) + iV(t)$ are continuous on $a \le t \le b$ and that $W'(t) = w(t)$ when $a \le t \le b$. Then
>
> $$
> \int_a^b w(t)\,dt = W(b) - W(a) = W(t)\Big]_a^b . \qquad (4)
> $$
>
> *B&C: Sec. 42 (text)*

^thm-42-2

> [!proof]+ Proof
> By [[§41 Derivatives of Functions w(t)#^def-41-1|Definition §41.1]], $W' = w$ means $U'(t) = u(t)$ and $V'(t) = v(t)$ (one-sided derivatives at $a$ and $b$). Since $u$ and $v$ are continuous, they are integrable, and the real fundamental theorem of calculus gives $\int_a^b u\,dt = U(b) - U(a)$ and $\int_a^b v\,dt = V(b) - V(a)$. Hence, by definition (2),
>
> $$
> \int_a^b w(t)\,dt = \big[U(t)\big]_a^b + i\big[V(t)\big]_a^b = \big[U(b) + iV(b)\big] - \big[U(a) + iV(a)\big] = W(b) - W(a) .
> $$

^pf-42-2

*Uses:* [[§41 Derivatives of Functions w(t)#^def-41-1|Def. §41.1]], [[§42 Definite Integrals of Functions w(t)#^def-42-1|Def. §42.1]], [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]

> [!remark]- Connections
> - The real theorem is [[§34 Fundamental Theorem of Calculus#^thm-34-1|451 Thm. §34.1]]; for plane curves it is [[§101 Derivatives and Integrals of Vector Functions#^thm-101-5|Calc Thm. §101.5]], the same statement and the same proof.
> - [[§49 Proof of the Theorem (Antiderivatives)#^thm-49-1|Theorem §49.1]] lifts this theorem from the parameter interval to contours in the plane: $\int_C f(z)\,dz = F(z_2) - F(z_1)$ when $F' = f$.

## Examples

> [!example] Example §42.1: The Integral of eⁱᵗ over [0, π/4], Two Ways
> **By definition (2).**
>
> $$
> \int_0^{\pi/4} e^{it}\,dt = \int_0^{\pi/4}(\cos t + i\sin t)\,dt = \int_0^{\pi/4}\cos t\,dt + i\int_0^{\pi/4}\sin t\,dt = \big[\sin t\big]_0^{\pi/4} + i\big[-\cos t\big]_0^{\pi/4} = \frac{1}{\sqrt2} + i\Big(-\frac{1}{\sqrt2} + 1\Big) .
> $$
>
> **By Theorem §42.2.** By [[§41 Derivatives of Functions w(t)#^ex-41-2|Example §41.2]] and [[§41 Derivatives of Functions w(t)#^prop-41-1|Proposition §41.1]](b),
>
> $$
> \frac{d}{dt}\Big(\frac{e^{it}}{i}\Big) = \frac1i\,\frac{d}{dt}e^{it} = \frac1i\,ie^{it} = e^{it} ,
> $$
>
> so
>
> $$
> \int_0^{\pi/4} e^{it}\,dt = \frac{e^{it}}{i}\bigg]_0^{\pi/4} = \frac{e^{i\pi/4}}{i} - \frac1i = \frac1i\Big(\frac{1}{\sqrt2} + \frac{i}{\sqrt2} - 1\Big) = \frac{1}{\sqrt2} + \frac1i\Big(\frac{1}{\sqrt2} - 1\Big) .
> $$
>
> Because $1/i = -i$, this is $\frac{1}{\sqrt2} + i\big(-\frac{1}{\sqrt2} + 1\big) \approx 0.7071 + 0.2929i$, as before.
>
> *B&C: Sec. 42, Examples 1 and 2*

^ex-42-1

> [!example] Example §42.2: The Mean Value Theorem for Integrals Fails
> Let $w(t)$ be continuous on $a \le t \le b$. Unlike the real case ([[§33 Properties of the Riemann Integral#^thm-33-9|451 Thm. §33.9]]), it is not necessarily true that there is a number $c$ in $a < t < b$ such that
>
> $$
> \int_a^b w(t)\,dt = w(c)(b - a) . \qquad (5)
> $$
>
> Take $a = 0$, $b = 2\pi$ and $w(t) = e^{it}$, as in [[§41 Derivatives of Functions w(t)#^ex-41-3|Example §41.3]]. Then
>
> $$
> \int_0^{2\pi} e^{it}\,dt = \frac{e^{it}}{i}\bigg]_0^{2\pi} = 0 ,
> $$
>
> but for every $c$ with $0 < c < 2\pi$, $|w(c)(b - a)| = |e^{ic}|\,2\pi = 2\pi$. The left side of (5) is zero and the right side is not.
>
> *B&C: Sec. 42, Example 3*

^ex-42-2

> [!example] Example §42.3: Two Real Integrals from One Complex Integral
> By definition (2),
>
> $$
> \int_0^{\pi} e^{(1+i)x}\,dx = \int_0^{\pi} e^x\cos x\,dx + i\int_0^{\pi} e^x\sin x\,dx .
> $$
>
> Evaluate the two real integrals by evaluating the single integral on the left. By [[§41 Derivatives of Functions w(t)#^ex-41-2|Example §41.2]], $e^{(1+i)x}/(1+i)$ is an antiderivative, and $e^{(1+i)\pi} = e^{\pi}e^{i\pi} = -e^{\pi}$, so by Theorem §42.2
>
> $$
> \int_0^{\pi} e^{(1+i)x}\,dx = \frac{e^{(1+i)\pi} - 1}{1 + i} = -\frac{1 + e^{\pi}}{1 + i} = -\frac{(1 + e^{\pi})(1 - i)}{2} = -\frac{1 + e^{\pi}}{2} + i\,\frac{1 + e^{\pi}}{2} .
> $$
>
> Taking real and imaginary parts,
>
> $$
> \int_0^{\pi} e^x\cos x\,dx = -\frac{1 + e^{\pi}}{2}, \qquad \int_0^{\pi} e^x\sin x\,dx = \frac{1 + e^{\pi}}{2}
> $$
>
> (about $\mp 12.070$), with no integration by parts.
>
> *B&C: Sec. 42, Exercise 4*

^ex-42-3

> [!example] Example §42.4: Orthogonality of the Exponentials e^(inθ)
> Show that if $m$ and $n$ are integers,
>
> $$
> \int_0^{2\pi} e^{im\theta}e^{-in\theta}\,d\theta = \begin{cases} 0 & \text{when } m \ne n, \\ 2\pi & \text{when } m = n. \end{cases}
> $$
>
> The integrand is $e^{i(m - n)\theta}$. If $m = n$ it is $1$, and the integral is $2\pi$. If $m \ne n$, then by [[§41 Derivatives of Functions w(t)#^ex-41-2|Example §41.2]] an antiderivative is $e^{i(m - n)\theta}/\big(i(m - n)\big)$, and by Theorem §42.2
>
> $$
> \int_0^{2\pi} e^{i(m - n)\theta}\,d\theta = \frac{e^{i(m - n)2\pi} - 1}{i(m - n)} = 0 ,
> $$
>
> because $e^{2\pi ik} = 1$ for every integer $k$. This is used in [[§44 Contour Integrals#^ex-44-2|Example §44.2]] to integrate $z^m\bar z^n$ around the unit circle.
>
> *B&C: Sec. 42, Exercise 3*

^ex-42-4

> [!remark]- Connections
> - Taking real and imaginary parts gives the orthogonality relations of the real Fourier system, [[§9 Periodic Functions and Fourier Series#^prop-9-3|341 Prop. §9.3]]; in complex form it is what makes the coefficients of the complex Fourier series $\frac{1}{2\pi}\int f(\theta)e^{-in\theta}\,d\theta$, [[§19★ Complex Methods#^thm-19-1|341 Thm. §19.1]].

> [!example] Example §42.5: An Improper Integral
> Show that $\displaystyle\int_0^{\infty} e^{-zt}\,dt = \frac1z$ when $\operatorname{Re} z > 0$.
>
> Let $z = x + iy$ with $x > 0$. For $T > 0$, by [[§41 Derivatives of Functions w(t)#^ex-41-2|Example §41.2]] (with $z_0 = -z$) and Theorem §42.2,
>
> $$
> \int_0^{T} e^{-zt}\,dt = \frac{e^{-zt}}{-z}\bigg]_0^{T} = \frac{1 - e^{-zT}}{z} .
> $$
>
> Since $|e^{-zT}| = e^{-xT} \to 0$ as $T \to \infty$, the real and imaginary parts of the right side tend to those of $1/z$, so both improper integrals in definition (2) converge and the value is $1/z$. (For $z = 0.7 + 1.3i$ numerical quadrature gives $0.32110 - 0.59633i = 1/z$.)
>
> *B&C: Sec. 42, Exercise 2(d)*

^ex-42-5

> [!remark]- Connections
> - With $z = s$ this is the Laplace transform $\mathcal{L}\{1\} = 1/s$, [[§26 Definition of the Laplace Transform#^ex-26-2|331 Ex. §26.2]], now valid for complex $s$ with $\operatorname{Re} s > 0$. Inverting Laplace transforms by contour integrals is [[§95★ Inverse Laplace Transforms|§95★]].
