---
type: section
subject: "[[Complex Variables]]"
chapter: 3
section: 38
bc: "38"
aliases: ["B&C 38"]
tags: [complex-variables, math342]
---
← [[§37 The Trigonometric Functions sin z and cos z]] · ↑ [[· 3 Elementary Functions]] · [[§39★ Hyperbolic Functions]] →

*Brown–Churchill, Section 38 · MAT 342 Practice Finals (Fall 2002, Spring 2005, Fall 2009).*

Extending the domain can create new zeros ($z^2 + 1$ has none on the real line and two in the plane), but $\sin z$ and $\cos z$ gain none: their zeros are exactly the real ones, $n\pi$ and $\frac\pi2 + n\pi$. This fixes where $\tan z$, $\cot z$, $\sec z$ and $\csc z$ fail to be analytic, and those isolated singular points are the poles whose residues are computed in Chapters 6 and 7 (for instance [[§81 Examples (Residues at Poles)|§81]]). The section ends with the equations $\sin z = w_0$ and $\cos z = w_0$, which, unlike their real versions, have solutions for every $w_0$.

## Zeros of sin z and cos z

> [!definition] Definition §38.1: Zero of a Function
> A **zero** of a given function $f$ is a number $z_0$ such that $f(z_0) = 0$.
>
> *B&C: Sec. 38 (text)*

^def-38-1

It is possible for a function of a real variable to have more zeros when its domain of definition is enlarged.

> [!example] Example §38.1: New Zeros of z² + 1
> The function $f(x) = x^2 + 1$, defined on the real line, has no zeros. But the function $f(z) = z^2 + 1$, defined on the complex plane, has the zeros $z = \pm i$.
>
> *B&C: Sec. 38, Example*

^ex-38-1

Since $\sin z$ becomes the usual $\sin x$ when $z$ is real, the real numbers $z = n\pi$ $(n = 0, \pm1, \pm2, \ldots)$ are zeros of $\sin z$. One might ask whether there are other zeros in the plane, and a similar question can be asked about $\cos z$.

> [!theorem] Theorem §38.1: Zeros of sin z and cos z
> The zeros of $\sin z$ and $\cos z$ in the complex plane are the same as the zeros of $\sin x$ and $\cos x$ on the real line. That is,
>
> $$
> \sin z = 0 \quad\text{if and only if}\quad z = n\pi \quad (n = 0, \pm1, \pm2, \ldots)
> $$
>
> and
>
> $$
> \cos z = 0 \quad\text{if and only if}\quad z = \frac\pi2 + n\pi \quad (n = 0, \pm1, \pm2, \ldots) .
> $$
>
> *B&C: Sec. 38, Theorem*

^thm-38-1

> [!proof]+ Proof
> **Sine.** The real numbers $n\pi$ are zeros of $\sin z$, since there $\sin z = \sin x$. To show that there are no other zeros, assume that $\sin z = 0$, $z = x + iy$. By equation (15) of [[§37 The Trigonometric Functions sin z and cos z#^prop-37-6|Proposition §37.6]],
>
> $$
> \sin^2x + \sinh^2y = 0 .
> $$
>
> A sum of two squares of real numbers vanishes only if both vanish:
>
> $$
> \sin x = 0 \qquad\text{and}\qquad \sinh y = 0 .
> $$
>
> Hence $x = n\pi$ $(n = 0, \pm1, \pm2, \ldots)$, and $y = 0$, because $\sinh y = \frac12(e^y - e^{-y}) = 0$ means $e^{2y} = 1$, and $e^t$ is one-to-one on the real line. So $z = n\pi$.
>
> **Cosine.** By the second relation (8) of [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|Corollary §37.4]], $\cos z = -\sin\big(z - \frac\pi2\big)$. So $\cos z = 0$ if and only if $z - \frac\pi2 = n\pi$, by the first part; that is, $z = \frac\pi2 + n\pi$.

^pf-38-1

*Uses:* [[§37 The Trigonometric Functions sin z and cos z#^prop-37-6|§37.6]], [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37.4]], [[§119 Trigonometry#^prop-119-13|Calc Prop. §119.13]] (real zeros of $\sin x$)

> [!remark]- Connections
> - The real zeros: [[§119 Trigonometry#^prop-119-13|Calc Prop. §119.13]] (properties of the graphs of $\sin$ and $\cos$). In the plane, $\sin z$ omits no value at all ([[§38 Zeros and Singularities of Trigonometric Functions#^rem-38-1|Remark: Method — Solving sin z = w₀ and cos z = w₀]]), in contrast with $e^z$, which omits $0$ ([[§30 The Exponential Function#^prop-30-1|Proposition §30.1]]).

## The Other Trigonometric Functions

> [!definition] Definition §38.2: tan, cot, sec, csc
> The other four trigonometric functions are defined by
>
> $$
> \tan z = \frac{\sin z}{\cos z}, \qquad \cot z = \frac{\cos z}{\sin z} , \qquad (1)
> $$
>
> $$
> \sec z = \frac{1}{\cos z}, \qquad \csc z = \frac{1}{\sin z} . \qquad (2)
> $$
>
> *B&C: Sec. 38, Equations (1) and (2)*

^def-38-2

> [!theorem] Proposition §38.2: Singularities, Derivatives and Periods
> **(a)** $\tan z$ and $\sec z$ are analytic everywhere except at the singularities ([[§25 Analytic Functions#^def-25-3|Definition §25.3]])
>
> $$
> z = \frac\pi2 + n\pi \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> the zeros of $\cos z$; and $\cot z$ and $\csc z$ are analytic everywhere except at the zeros of $\sin z$, $z = n\pi$ $(n = 0, \pm1, \pm2, \ldots)$.
>
> **(b)** Where they are analytic,
>
> $$
> \frac{d}{dz}\tan z = \sec^2z, \qquad \frac{d}{dz}\cot z = -\csc^2z , \qquad (3)
> $$
>
> $$
> \frac{d}{dz}\sec z = \sec z\tan z, \qquad \frac{d}{dz}\csc z = -\csc z\cot z . \qquad (4)
> $$
>
> **(c)** These functions are periodic: $\sec z$ and $\csc z$ with period $2\pi$, and
>
> $$
> \tan(z + \pi) = \tan z , \qquad (5)
> $$
>
> and likewise $\cot(z + \pi) = \cot z$.
>
> *B&C: Sec. 38, Equations (3)–(5) and text*

^prop-38-2

> [!proof]+ Proof
> **(a)** A quotient of entire functions is analytic wherever the denominator is not zero ([[§25 Analytic Functions#^prop-25-1|Proposition §25.1]]); the denominators $\cos z$ and $\sin z$ vanish exactly at the points listed (Theorem §38.1). At those points the functions are not even defined, and every neighborhood of such a point contains points where they are analytic, so the points are singular points.
>
> **(b)** (B&C's Exercise 6.) By the quotient rule ([[§20 Rules for Differentiation#^thm-20-2|Theorem §20.2]]), the derivatives (2) of [[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|Theorem §37.1]] and the identity $\sin^2z + \cos^2z = 1$,
>
> $$
> \frac{d}{dz}\tan z = \frac{\cos z\cos z - \sin z(-\sin z)}{\cos^2z} = \frac{1}{\cos^2z} = \sec^2z, \qquad \frac{d}{dz}\cot z = \frac{-\sin z\sin z - \cos z\cos z}{\sin^2z} = -\csc^2z ,
> $$
>
> $$
> \frac{d}{dz}\sec z = \frac{\sin z}{\cos^2z} = \sec z\tan z, \qquad \frac{d}{dz}\csc z = \frac{-\cos z}{\sin^2z} = -\csc z\cot z .
> $$
>
> **(c)** By (10) and (11) of [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|Corollary §37.4]], $\sin$ and $\cos$ have period $2\pi$, so $\sec$ and $\csc$ do; and $\sin(z + \pi) = -\sin z$, $\cos(z + \pi) = -\cos z$, so the signs cancel in the quotients: $\tan(z + \pi) = \frac{-\sin z}{-\cos z} = \tan z$, and similarly for $\cot$.

^pf-38-2

*Uses:* [[§38 Zeros and Singularities of Trigonometric Functions#^def-38-2|Def. §38.2]], [[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|§38.1]], [[§37 The Trigonometric Functions sin z and cos z#^thm-37-1|§37.1]], [[§37 The Trigonometric Functions sin z and cos z#^cor-37-4|§37.4]], [[§20 Rules for Differentiation#^thm-20-2|§20.2]], [[§25 Analytic Functions#^prop-25-1|§25.1]], [[§25 Analytic Functions#^def-25-3|Def. §25.3]]

Mapping properties of $w = \sin z$ are important in applications; they are discussed in [[§104★ Mapping Vertical Line Segments by w = sin z|§104★]] and [[§105★ Mapping Horizontal Line Segments by w = sin z|§105★]] (see also the figure after [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]]).

## Solving sin z = w₀ and cos z = w₀

> [!remark] Remark: Method — Solving sin z = w₀ and cos z = w₀
> Two routes:
> 1. **Real and imaginary parts.** By (13) and (14) of [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]], $\sin z = w_0$ is the pair of real equations $\sin x\cosh y = \operatorname{Re} w_0$, $\cos x\sinh y = \operatorname{Im} w_0$. When $w_0$ is real, the second says $\cos x = 0$ or $y = 0$; treat the two cases separately. This is efficient for real $w_0$.
> 2. **A quadratic in $e^{iz}$.** Put $W = e^{iz}$. Then $\sin z = w_0$ becomes $W - W^{-1} = 2iw_0$, i.e. $W^2 - 2iw_0W - 1 = 0$, and $\cos z = w_0$ becomes $W + W^{-1} = 2w_0$, i.e. $W^2 - 2w_0W + 1 = 0$. Solve by the quadratic formula ([[§11 Examples (Roots of Complex Numbers)#^ex-11-4|Example §11.4]]), then solve $e^{iz} = W$ for each root ([[§30 The Exponential Function#^rem-30-1|Remark: Method — Solving e^g(z) = w₀]]): $iz = \log W$, $z = -i\log W$. This works for every $w_0$ and leads to the formulas for $\sin^{-1}$ and $\cos^{-1}$ in [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-1|Proposition §40.1]] and [[§40★ Inverse Trigonometric and Hyperbolic Functions#^prop-40-2|Proposition §40.2]].
>
> The product of the two roots of each quadratic is $\mp1 \ne 0$, so $W \ne 0$ and there are always solutions: $\sin z$ and $\cos z$ take every complex value, infinitely often.

^rem-38-1

> [!example] Example §38.2: The Zeros by Exponentials
> **(a)** Find all solutions of $\sin z = 0$, and prove the answer. This is Theorem §38.1, proved above with (15). A second proof, by route 2: $\sin z = 0$ means $e^{iz} = e^{-iz}$, i.e. $e^{2iz} = 1$. By [[§30 The Exponential Function#^rem-30-1|the Method of §30]], with $1 = e^{i0}$, $2iz = 0 + 2n\pi i$, so $z = n\pi$.
>
> **(b)** Prove that all solutions of $\cos z = 0$ are real, and find them. $\cos z = 0$ means $e^{iz} = -e^{-iz}$, i.e. $e^{2iz} = -1 = e^{i\pi}$. So $2iz = i(\pi + 2n\pi)$, that is,
>
> $$
> z = \frac\pi2 + n\pi \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> all real. (The step from $e^{2iz} = e^{i\pi}$ to $2iz = i\pi + 2n\pi i$ uses that $e^{w_1} = e^{w_2}$ only when $w_1 - w_2$ is an integer multiple of $2\pi i$, [[§31 The Logarithmic Function#^thm-31-1|Theorem §31.1]].) The 2005 key argues this way and is correct.
>
> *Source: 342 practice final (Fall 2009), Q1(a); 342 practice final (Spring 2005), Q2(b)*

^ex-38-2

> [!example] Example §38.3: sin z = cosh 4, by Real and Imaginary Parts
> By (13) of [[§37 The Trigonometric Functions sin z and cos z#^prop-37-5|Proposition §37.5]], $\sin z = \cosh 4$ means
>
> $$
> \sin x\cosh y = \cosh 4 \qquad\text{and}\qquad \cos x\sinh y = 0 .
> $$
>
> If $\sinh y = 0$, then $y = 0$ and the first equation says $\sin x = \cosh 4 > 1$, impossible. So $\cos x = 0$, $x = \frac\pi2 + n\pi$, and $\sin x = (-1)^n$. The first equation becomes $(-1)^n\cosh y = \cosh 4$; since $\cosh y > 0$, $n$ must be even, $n = 2m$, and then $\cosh y = \cosh 4$, so $y = \pm4$ ($\cosh$ is even and increasing on $y \ge 0$). Hence
>
> $$
> z = \Big(\frac\pi2 + 2m\pi\Big) \pm 4i \qquad (m = 0, \pm1, \pm2, \ldots) .
> $$
>
> Check: $\sin\big(\frac\pi2 \pm 4i\big) = \sin\frac\pi2\cosh 4 \pm i\cos\frac\pi2\sinh 4 = \cosh 4$.
>
> *B&C: Sec. 38, Exercise 15*

^ex-38-3

> [!example] Example §38.4: cos z = i, by a Quadratic in e^(iz)
> Find all solutions of $\cos z = i$.
>
> With $W = e^{iz}$, $\cos z = i$ reads $\frac12(W + W^{-1}) = i$, that is,
>
> $$
> W^2 - 2iW + 1 = 0, \qquad W = \frac{2i \pm \sqrt{-4 - 4}}{2} = i \pm i\sqrt2 .
> $$
>
> So $W_1 = (1 + \sqrt2)\,i$ and $W_2 = (1 - \sqrt2)\,i = -(\sqrt2 - 1)\,i$. Now solve $e^{iz} = W$, i.e. $iz = \log W$:
>
> $$
> \log W_1 = \ln(1 + \sqrt2) + i\Big(\frac\pi2 + 2n\pi\Big), \qquad \log W_2 = \ln(\sqrt2 - 1) + i\Big(-\frac\pi2 + 2n\pi\Big) ,
> $$
>
> since $|W_2| = \sqrt2 - 1$ and $W_2$ lies on the negative imaginary axis. With $\ln(\sqrt2 - 1) = \ln\frac{1}{\sqrt2 + 1} = -\ln(1 + \sqrt2)$ and $z = -i\log W$,
>
> $$
> z = \frac\pi2 + 2n\pi - i\ln(1 + \sqrt2) \qquad\text{or}\qquad z = -\frac\pi2 + 2n\pi + i\ln(1 + \sqrt2) \qquad (n = 0, \pm1, \pm2, \ldots) ,
> $$
>
> that is, $z = \pm\big(\frac\pi2 - i\ln(1 + \sqrt2)\big) + 2n\pi$. The two families are negatives of each other, as they must be, since $\cos$ is even. Check with (14): $\cos\big(\frac\pi2 - i\ln(1 + \sqrt2)\big) = 0 - i\sin\frac\pi2\sinh\big(-\ln(1 + \sqrt2)\big) = i\sinh\ln(1 + \sqrt2) = \frac i2\big((1 + \sqrt2) - (\sqrt2 - 1)\big) = i$.
>
> *The key writes the second family with $\ln(1 - \sqrt2)$, the logarithm of a negative number, in place of $\ln|W_2| = \ln(\sqrt2 - 1)$.*
>
> *Source: 342 practice final (Fall 2002), Q2(b)*

^ex-38-4
