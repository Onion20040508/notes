---
type: section
subject: "[[Complex Variables]]"
chapter: 4
section: 41
bc: "41"
aliases: ["B&C 41"]
tags: [complex-variables, math342]
---
← [[§40★ Inverse Trigonometric and Hyperbolic Functions]] · ↑ [[· 4 Integrals]] · [[§42 Definite Integrals of Functions w(t)]] →

*Brown–Churchill, Section 41.*

Integrals of $f(z)$ along curves will be defined in [[§44 Contour Integrals#^def-44-1|§44]] by pulling them back to integrals over a parameter interval, so the first step is calculus for complex-valued functions $w(t) = u(t) + iv(t)$ of a *real* variable $t$. The derivative is taken component by component, and the familiar rules for sums, products and constant multiples, and the rule $\frac{d}{dt}e^{z_0t} = z_0e^{z_0t}$, follow by applying real calculus to $u$ and $v$. One rule does not carry over: the mean value theorem fails, because $u$ and $v$ would have to take their mean slopes at the same point.

## The Derivative of w(t)

> [!definition] Definition §41.1: Derivative of a Function w(t)
> Let
>
> $$
> w(t) = u(t) + iv(t) , \qquad (1)
> $$
>
> where $u$ and $v$ are *real-valued* functions of the real variable $t$. The **derivative** $w'(t)$, or $\dfrac{d}{dt}w(t)$, of $w$ at a point $t$ is
>
> $$
> w'(t) = u'(t) + iv'(t) , \qquad (2)
> $$
>
> provided each of the derivatives $u'$ and $v'$ exists at $t$.
>
> *B&C: Sec. 41 (text)*

^def-41-1

> [!remark]- Connections
> - A function $w(t) = u(t) + iv(t)$ is a plane curve $\langle u(t), v(t)\rangle$, and (2) is the derivative of a vector function computed component by component: [[§87 Derivatives and Integrals of Vector Functions#^thm-87-1|Calc Thm. §87.1]]. Multiplication by complex numbers is the extra structure that $\mathbb{R}^2$ lacks.

B&C notes that the rules of calculus for sums and products apply to $w(t)$ just as they do to real functions, and that verifications can be based on the corresponding real rules. The rule for $w(-t)$ is used in [[§44 Contour Integrals#^thm-44-2|§44]] to integrate along a reversed contour.

> [!theorem] Proposition §41.1: Rules for Differentiating w(t)
> Let $w$, $w_1$, $w_2$ be complex-valued functions of the real variable $t$ that are differentiable at $t$, and let $z_0 = x_0 + iy_0$ be a complex constant. Then at $t$:
>
> **(a)** $\dfrac{d}{dt}\big[w_1(t) + w_2(t)\big] = w_1'(t) + w_2'(t)$;
>
> **(b)** $\dfrac{d}{dt}\big[z_0w(t)\big] = z_0w'(t)$;
>
> **(c)** $\dfrac{d}{dt}\big[w_1(t)w_2(t)\big] = w_1'(t)w_2(t) + w_1(t)w_2'(t)$;
>
> **(d)** if $w$ is differentiable at $-t$, then $\dfrac{d}{dt}w(-t) = -w'(-t)$, where $w'(-t)$ denotes the derivative of $w(t)$ with respect to $t$, evaluated at $-t$.
>
> *B&C: Sec. 41 (text); Sec. 42, Exercise 1*

^prop-41-1

> [!proof]+ Proof
> Write $w = u + iv$, $w_k = u_k + iv_k$. In each case we write the left side as (real part) $+ i\,$(imaginary part), differentiate the two real functions by the rules of real calculus, and compare with the right side.
>
> **(a)** $w_1 + w_2 = (u_1 + u_2) + i(v_1 + v_2)$, whose derivative by (2) is $(u_1' + u_2') + i(v_1' + v_2') = w_1' + w_2'$.
>
> **(b)** (B&C's suggestion.) $z_0w = (x_0 + iy_0)(u + iv) = (x_0u - y_0v) + i(y_0u + x_0v)$. Its real and imaginary parts are differentiable, and by (2)
>
> $$
> \frac{d}{dt}\big[z_0w(t)\big] = (x_0u' - y_0v') + i(y_0u' + x_0v') = (x_0 + iy_0)(u' + iv') = z_0w'(t) .
> $$
>
> **(c)** $w_1w_2 = (u_1u_2 - v_1v_2) + i(u_1v_2 + v_1u_2)$. By the real product rule its derivative is
>
> $$
> (u_1'u_2 + u_1u_2' - v_1'v_2 - v_1v_2') + i(u_1'v_2 + u_1v_2' + v_1'u_2 + v_1u_2') .
> $$
>
> On the other hand $w_1'w_2 = (u_1' + iv_1')(u_2 + iv_2) = (u_1'u_2 - v_1'v_2) + i(u_1'v_2 + v_1'u_2)$ and $w_1w_2' = (u_1u_2' - v_1v_2') + i(u_1v_2' + v_1u_2')$; their sum is the same expression.
>
> **(d)** $W(t) = w(-t) = u(-t) + iv(-t)$. By the real chain rule $\frac{d}{dt}u(-t) = -u'(-t)$ and $\frac{d}{dt}v(-t) = -v'(-t)$, so $W'(t) = -u'(-t) - iv'(-t) = -w'(-t)$.

^pf-41-1

*Uses:* [[§41 Derivatives of Functions w(t)#^def-41-1|Def. §41.1]], [[§28 Basic Properties of the Derivative#^thm-28-2|451 Thm. §28.2]] (sum and product rules), [[§28 Basic Properties of the Derivative#^thm-28-3|451 Thm. §28.3]] (chain rule)

## Examples

> [!example] Example §41.1: The Derivative of w(t)²
> Assuming that $u(t)$ and $v(t)$ in (1) are differentiable at $t$, prove that
>
> $$
> \frac{d}{dt}\big[w(t)\big]^2 = 2w(t)w'(t) . \qquad (3)
> $$
>
> Write $[w(t)]^2 = (u + iv)^2 = u^2 - v^2 + i2uv$. Then
>
> $$
> \frac{d}{dt}\big[w(t)\big]^2 = (u^2 - v^2)' + i(2uv)' = 2uu' - 2vv' + i2(uv' + u'v) = 2(u + iv)(u' + iv') ,
> $$
>
> which is (3). (It is also the case $w_1 = w_2 = w$ of [[§41 Derivatives of Functions w(t)#^prop-41-1|Proposition §41.1]](c).) Rule (3) gives the antiderivative $\frac12[z(t)]^2$ of $z(t)z'(t)$ used in [[§45 Some Examples (Contour Integrals)#^ex-45-2|Example §45.2]].
>
> *B&C: Sec. 41, Example 1*

^ex-41-1

> [!example] Example §41.2: The Exponential Rule
> Let $z_0 = x_0 + iy_0$. Show that
>
> $$
> \frac{d}{dt}e^{z_0t} = z_0e^{z_0t} . \qquad (4)
> $$
>
> By the definition of the exponential function ([[§30 The Exponential Function#^def-30-1|Definition §30.1]]),
>
> $$
> e^{z_0t} = e^{x_0t}e^{iy_0t} = e^{x_0t}\cos y_0t + ie^{x_0t}\sin y_0t .
> $$
>
> By definition (2) and the real product rule,
>
> $$
> \frac{d}{dt}e^{z_0t} = \big(e^{x_0t}\cos y_0t\big)' + i\big(e^{x_0t}\sin y_0t\big)' = \big(x_0e^{x_0t}\cos y_0t - y_0e^{x_0t}\sin y_0t\big) + i\big(x_0e^{x_0t}\sin y_0t + y_0e^{x_0t}\cos y_0t\big) .
> $$
>
> Multiplying out shows that this equals $(x_0 + iy_0)\big(e^{x_0t}\cos y_0t + ie^{x_0t}\sin y_0t\big) = (x_0 + iy_0)e^{x_0t}e^{iy_0t}$, which is (4). In particular $\frac{d}{dt}e^{it} = ie^{it}$.
>
> *B&C: Sec. 41, Example 2*

^ex-41-2

> [!remark]- Connections
> - The same rule, proved the same way, is what makes $e^{rt}$ with a complex root $r$ of the characteristic equation a solution of a linear ODE: [[§15 Complex Roots of the Characteristic Equation#^prop-15-1|331 Prop. §15.1]].

While many rules of calculus carry over to functions of the form (1), not all of them do.

> [!example] Example §41.3: The Mean Value Theorem Fails
> Suppose that $w(t)$ is continuous on $a \le t \le b$ (that is, $u$ and $v$ are continuous there) and that $w'(t)$ exists when $a < t < b$. It is not necessarily true that there is a number $c$ in $a < t < b$ such that
>
> $$
> w'(c) = \frac{w(b) - w(a)}{b - a} . \qquad (5)
> $$
>
> Take $w(t) = e^{it}$ on $0 \le t \le 2\pi$. By [[§41 Derivatives of Functions w(t)#^ex-41-2|Example §41.2]], $|w'(t)| = |ie^{it}| = 1$, so the left side of (5) is never zero. But
>
> $$
> \frac{w(b) - w(a)}{b - a} = \frac{e^{i2\pi} - e^{i0}}{2\pi} = \frac{1 - 1}{2\pi} = 0 .
> $$
>
> So no number $c$ satisfies (5). The real mean value theorem does apply to $u = \cos t$ and $v = \sin t$ separately, giving $u'(c_1) = 0$ and $v'(c_2) = 0$, for instance at $c_1 = \pi$ and $c_2 = \frac\pi2$; the trouble is that a single $c$ would need $\sin c = \cos c = 0$.
>
> *B&C: Sec. 41, Example 3*

^ex-41-3

> [!remark]- Connections
> - The real theorem: [[§29 The Mean Value Theorem#^thm-29-3|451 Thm. §29.3]]. It fails for curves in the plane for the same reason as here.

> [!remark] Remark: What Survives of the Mean Value Theorem
> The *equality* (5) is lost, but the *inequality* that is usually derived from it survives. If $w'$ is continuous on $[a, b]$, then by the fundamental theorem of calculus for $w(t)$ ([[§42 Definite Integrals of Functions w(t)#^thm-42-2|Theorem §42.2]]) and the inequality $\big|\int w\big| \le \int|w|$ ([[§47 Upper Bounds for Moduli of Contour Integrals#^lem-47-1|Lemma §47.1]]),
>
> $$
> |w(b) - w(a)| = \Big|\int_a^b w'(t)\,dt\Big| \le \int_a^b |w'(t)|\,dt \le (b - a)\max_{a \le t \le b}|w'(t)| .
> $$
>
> For $w = e^{it}$ on $[0, 2\pi]$ this reads $0 \le 2\pi$. Its counterpart for contour integrals is the ML-inequality, [[§47 Upper Bounds for Moduli of Contour Integrals#^thm-47-2|Theorem §47.2]].

^rem-41-1
