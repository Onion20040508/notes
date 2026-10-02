---
type: section
subject: "[[Fourier Series and PDEs]]"
chapter: 1
section: 16
powers: "1.11"
aliases: ["Powers 1.11"]
tags: [fourier-series-and-pdes, math341, extension]
---
← [[§15★ Complex Methods]] · ↑ [[· 1 Fourier Series and Integrals]] · [[§17 Derivation and Boundary Conditions]] →

*Powers, Section 1.11.*
★ *Beyond MAT 341: the course did not cover this section; it is included from Powers.*

Three applications of Fourier series and integrals that lie outside the rest of the book. A damped oscillator driven by a periodic force responds to each harmonic of the force separately, so its periodic response is found coefficient by coefficient, and a harmonic close to the natural frequency dominates (resonance). A two-point boundary value problem $u'' + pu = f$ is solved by expanding in sine series, which is separation of variables in miniature and an introduction to Chapter 2. Finally the sampling theorem shows that a band-limited signal is completely determined by its values at equally spaced times, the basis of digital recording and communications engineering.

## A. Nonhomogeneous Differential Equation

Many mechanical and electrical systems are described by the differential equation

$$
\ddot y + \alpha\dot y + \beta y = f(t) .
$$

The function $f(t)$ is the forcing function, $\beta y$ the restoring term and $\alpha\dot y$ the damping term. By [[§2★ Nonhomogeneous Linear Equations#^thm-2-4|Theorem §2.4]], a sine or cosine in $f(t)$ causes a response of the same period in $y(t)$, and by [[§2★ Nonhomogeneous Linear Equations#^thm-2-3|Theorem §2.3]], if $f(t)$ is a sum of simpler functions, $y(t)$ is the corresponding sum. Suppose that $f(t)$ is periodic with period $2\pi$, with Fourier series

$$
f(t) = a_0 + \sum_{n=1}^{\infty} a_n\cos(nt) + b_n\sin(nt) .
$$

> [!theorem] Theorem §16.1: The Periodic Response
> Let $f(t)$ be sectionally continuous and periodic with period $2\pi$, with Fourier coefficients $a_0, a_n, b_n$. If $y(t)$ is a particular solution of $\ddot y + \alpha\dot y + \beta y = f(t)$ that is periodic with period $2\pi$, with Fourier series
>
> $$
> y(t) = A_0 + \sum_{n=1}^{\infty} A_n\cos(nt) + B_n\sin(nt) ,
> $$
>
> then its coefficients satisfy
>
> $$
> \beta A_0 = a_0, \qquad (\beta - n^2)A_n + \alpha nB_n = a_n, \qquad -\alpha nA_n + (\beta - n^2)B_n = b_n .
> $$
>
> If $\beta \ne 0$ and $\Delta_n = (\beta - n^2)^2 + \alpha^2n^2 \ne 0$ for all $n$, these determine
>
> $$
> A_0 = \frac{a_0}{\beta}, \qquad A_n = \frac{(\beta - n^2)a_n - \alpha nb_n}{\Delta_n}, \qquad B_n = \frac{(\beta - n^2)b_n + \alpha na_n}{\Delta_n} .
> $$
>
> *Powers: 1.11, Part A*

^thm-16-1

> [!proof]+ Proof
> Powers writes the derivatives of $y$ as the termwise derivatives of its series,
>
> $$
> \dot y(t) = \sum_{n=1}^{\infty} -nA_n\sin(nt) + nB_n\cos(nt), \qquad \ddot y(t) = \sum_{n=1}^{\infty} -n^2A_n\cos(nt) - n^2B_n\sin(nt) ,
> $$
>
> and matches coefficients. (Powers assumes the series can be differentiated; here is why only the coefficients matter. A solution $y$ has a continuous derivative, and $\ddot y = f - \alpha\dot y - \beta y$ is sectionally continuous. For any $2\pi$-periodic $g$ with sectionally continuous derivative, integration by parts over a period, whose boundary terms cancel by periodicity, gives
>
> $$
> \frac1\pi\int_{-\pi}^{\pi}\dot g(t)\cos(nt)\,dt = \frac n\pi\int_{-\pi}^{\pi} g(t)\sin(nt)\,dt, \qquad \frac1\pi\int_{-\pi}^{\pi}\dot g(t)\sin(nt)\,dt = -\frac n\pi\int_{-\pi}^{\pi} g(t)\cos(nt)\,dt ,
> $$
>
> and $\int_{-\pi}^{\pi}\dot g = 0$. Applied to $g = y$ and then to $g = \dot y$, this says that the Fourier coefficients of $\dot y$ and $\ddot y$ are those of the termwise derivatives above, whether or not the series converge.) The two sides of the differential equation are the same function, so they have the same Fourier coefficients:
>
> $$
> \beta A_0 + \sum_{n=1}^{\infty}\big(-n^2A_n + \alpha nB_n + \beta A_n\big)\cos(nt) + \big(-n^2B_n - \alpha nA_n + \beta B_n\big)\sin(nt) = a_0 + \sum_{n=1}^{\infty} a_n\cos(nt) + b_n\sin(nt) .
> $$
>
> Matching the constant terms and the coefficients of $\cos(nt)$ and $\sin(nt)$ gives the three equations. For each $n \ge 1$ they form a $2 \times 2$ linear system for $A_n$, $B_n$ with determinant
>
> $$
> \begin{vmatrix} \beta - n^2 & \alpha n \\ -\alpha n & \beta - n^2 \end{vmatrix} = (\beta - n^2)^2 + \alpha^2n^2 = \Delta_n ,
> $$
>
> and if $\Delta_n \ne 0$, Cramer's rule gives $A_n = \big((\beta - n^2)a_n - \alpha nb_n\big)/\Delta_n$ and $B_n = \big((\beta - n^2)b_n + \alpha na_n\big)/\Delta_n$.

^pf-16-1

*Uses:* [[§6 Periodic Functions and Fourier Series#^def-6-2|Def. §6.2]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] (integration by parts), [[§22 Cramer’s Rule, Volume, and Linear Transformations#^thm-22-1|235 Thm. §22.1]] (Cramer's rule)

> [!remark]- Connections
> - For a single harmonic this is the steady-state response of the forced spring–mass system, [[§20 Forced Periodic Vibrations#^thm-20-1|331 Thm. §20.1]] (with $m = 1$, $\gamma = \alpha$, $k = \beta$, $\omega = n$, and $\Delta_n$ the square of BDP's $\Delta$), and the amplitude $\sqrt{A_n^2 + B_n^2} = \sqrt{a_n^2 + b_n^2}/\sqrt{\Delta_n}$ is BDP's resonance curve, [[§20 Forced Periodic Vibrations#^prop-20-2|331 Prop. §20.2]]. The Fourier series superposes these responses over all harmonics of the force.

Given $f$, the $a$'s and $b$'s can be determined, and with them the $A$'s and $B$'s. The function $y(t)$ represented by the series is the periodic part of the response. Depending on the initial conditions there may also be a transient response, a solution of the homogeneous equation, which dies out as $t$ increases when $\alpha > 0$.

> [!example] Example §16.1: A Damped Oscillator Driven by a Square Wave
> Consider the differential equation
>
> $$
> \ddot y + 0.4\dot y + 1.04y = r(t) .
> $$
>
> **(a) One harmonic.** If $r(t) = \sin(nt)$, then $a_n = 0$, $b_n = 1$ and all other coefficients are $0$. By Theorem §16.1 the corresponding particular solution is
>
> $$
> y(t) = \frac{-0.4n\cos(nt) + (1.04 - n^2)\sin(nt)}{(1.04 - n^2)^2 + (0.4n)^2} .
> $$
>
> **(b) A square wave.** Next, let $r(t)$ be the square wave $r = 1$ on $0 < t < \pi$, $r = -1$ on $-\pi < t < 0$, with Fourier series
>
> $$
> r(t) = \sum_{n=1}^{\infty}\frac{2(1 - \cos(n\pi))}{n\pi}\sin(nt) = \frac4\pi\Big(\sin t + \frac{\sin 3t}{3} + \frac{\sin 5t}{5} + \cdots\Big) .
> $$
>
> By superposition (or by Theorem §16.1 with $a_n = 0$) the corresponding response is
>
> $$
> y(t) = \sum_{n=1}^{\infty}\frac{2(1 - \cos(n\pi))}{n\pi}\cdot\frac{-0.4n\cos(nt) + (1.04 - n^2)\sin(nt)}{(1.04 - n^2)^2 + (0.4n)^2} .
> $$
>
> **Resonance.** The amplitude of the $n$th harmonic of $y$ is $b_n/\sqrt{\Delta_n}$:
>
> | $n$ | $b_n = \frac{4}{n\pi}$ | $\Delta_n$ | amplitude $b_n/\sqrt{\Delta_n}$ |
> |---|---|---|---|
> | 1 | 1.273 | 0.1616 | 3.167 |
> | 3 | 0.424 | 64.80 | 0.0527 |
> | 5 | 0.255 | 578.1 | 0.0106 |
>
> The term for $n = 1$ has a small denominator, causing a large response: the homogeneous equation has characteristic roots $-0.2 \pm i$, so the system's natural frequency is close to $1$, the frequency of the fundamental of the force. The oscillator amplifies the fundamental by a factor $2.5$ and suppresses the higher harmonics, and its response is very nearly the pure sinusoid $3.17\sin(t - \delta)$, with $\delta \approx 84°$ from $\tan\delta = 0.4/0.04 = 10$.
>
> *Powers: 1.11, Example (Part A)*

^ex-16-1

## B. Boundary Value Problems

By way of introduction to the next chapter, apply the idea of Fourier series to the boundary value problem

$$
\frac{d^2u}{dx^2} + pu = f(x), \quad 0 < x < a, \qquad u(0) = 0, \quad u(a) = 0 .
$$

> [!theorem] Theorem §16.2: Sine-Series Solution of a Boundary Value Problem
> Let $f$ be sectionally continuous on $0 < x < a$, with Fourier sine coefficients $b_n$, so that $f(x) = \sum_{n=1}^{\infty} b_n\sin(n\pi x/a)$, and let $u$ be a twice continuously differentiable solution of the boundary value problem above, with Fourier sine series $u(x) = \sum_{n=1}^{\infty} B_n\sin(n\pi x/a)$. Then
>
> $$
> \Big(p - \frac{n^2\pi^2}{a^2}\Big)B_n = b_n, \qquad n = 1, 2, 3, \dots .
> $$
>
> If $p \ne n^2\pi^2/a^2$ for every $n$, then
>
> $$
> B_n = \frac{b_n}{p - n^2\pi^2/a^2}, \qquad u(x) = \sum_{n=1}^{\infty}\frac{a^2b_n}{a^2p - n^2\pi^2}\sin\Big(\frac{n\pi x}{a}\Big) .
> $$
>
> If $p = m^2\pi^2/a^2$ for some positive integer $m$, there is no value of $B_m$ that satisfies $\big(p - \frac{m^2\pi^2}{a^2}\big)B_m = b_m$ unless $b_m = 0$ also, in which case any value of $B_m$ is satisfactory: a zero denominator must be handled separately.
>
> *Powers: 1.11, Part B*

^thm-16-2

> [!proof]+ Proof
> Powers assumes that the sine series of $u$ may be differentiated twice,
>
> $$
> \frac{d^2u}{dx^2} = \sum_{n=1}^{\infty} -\Big(\frac{n^2\pi^2}{a^2}B_n\Big)\sin\Big(\frac{n\pi x}{a}\Big) , \qquad 0 < x < a ,
> $$
>
> inserts the series forms of $u$, $u''$ and $f$ into the differential equation, and matches coefficients of like terms. (Here is why this is legitimate for the coefficients. Let $k = n\pi/a$. Integrating by parts twice,
>
> $$
> \frac2a\int_0^{a} u''(x)\sin(kx)\,dx = \frac2a\Big[u'\sin kx\Big]_0^{a} - \frac{2k}{a}\Big[u\cos kx\Big]_0^{a} - \frac{2k^2}{a}\int_0^{a} u(x)\sin(kx)\,dx = -k^2B_n ,
> $$
>
> because $\sin 0 = \sin(n\pi) = 0$ and $u(0) = u(a) = 0$. So the sine coefficients of $u''$ are $-\frac{n^2\pi^2}{a^2}B_n$, whatever the convergence of the series.) Since $u'' + pu = f$, the sine coefficients of the two sides agree:
>
> $$
> \sum_{n=1}^{\infty}\Big(-\frac{n^2\pi^2}{a^2}B_n + pB_n\Big)\sin\Big(\frac{n\pi x}{a}\Big) = \sum_{n=1}^{\infty} b_n\sin\Big(\frac{n\pi x}{a}\Big), \qquad 0 < x < a ,
> $$
>
> that is, $\big(p - \frac{n^2\pi^2}{a^2}\big)B_n = b_n$ for every $n$. If the factor is nonzero, divide; then $B_n = \frac{a^2b_n}{a^2p - n^2\pi^2}$. If $p = \frac{m^2\pi^2}{a^2}$, the $m$th equation reads $0\cdot B_m = b_m$, which has no solution unless $b_m = 0$, and then every $B_m$ works.

^pf-16-2

*Uses:* [[§7 Arbitrary Period and Half-Range Expansions#^def-7-4|Def. §7.4]], [[§34 Fundamental Theorem of Calculus#^thm-34-3|451 Thm. §34.3]] (integration by parts)

The exceptional values $p = n^2\pi^2/a^2$ are the eigenvalues of $u'' + \lambda u = 0$, $u(0) = u(a) = 0$, with eigenfunctions $\sin(n\pi x/a)$ ([[§3★ Boundary Value Problems#^prop-3-3|Proposition §3.3]]). That the sine functions turn $d^2/dx^2$ into multiplication by $-n^2\pi^2/a^2$ is the reason they appear in heat and wave problems with these boundary conditions, and the solvability condition $b_m = 0$ is the prototype of the Sturm–Liouville alternative ([[§24 Expansion in Series of Eigenfunctions|§24]]).

> [!example] Example §16.2: A Sine-Series Solution
> Consider the boundary value problem
>
> $$
> \frac{d^2u}{dx^2} - u = -x, \quad 0 < x < 1, \qquad u(0) = 0, \quad u(1) = 0 .
> $$
>
> Here $a = 1$ and $p = -1$, which is never of the form $n^2\pi^2$. The sine series of $-x$ is
>
> $$
> -x = \sum_{n=1}^{\infty}\frac{2(-1)^n}{\pi n}\sin(n\pi x), \qquad 0 < x < 1 ,
> $$
>
> since $2\int_0^1 (-x)\sin(n\pi x)\,dx = \frac{2(-1)^n}{n\pi}$. By Theorem §16.2, $B_n = \frac{b_n}{-1 - n^2\pi^2}$, so the solution must be
>
> $$
> u(x) = \sum_{n=1}^{\infty}\frac2\pi\cdot\frac{(-1)^{n+1}}{n(n^2\pi^2 + 1)}\sin(n\pi x), \qquad 0 < x < 1 .
> $$
>
> This particular series belongs to a known function. The general solution of $u'' - u = -x$ is $u = x + c_1\cosh x + c_2\sinh x$; the boundary conditions give $c_1 = 0$ and $c_2 = -1/\sinh 1$, so
>
> $$
> u(x) = x - \frac{\sinh x}{\sinh 1} ,
> $$
>
> and computing $2\int_0^1\big(x - \frac{\sinh x}{\sinh 1}\big)\sin(n\pi x)\,dx$ gives back the coefficients above. In general one would not know any formula for the solution other than its Fourier sine series.
>
> *Powers: 1.11, Example (Part B); the closed form is added*

^ex-16-2

> [!remark] Remark: Method — Solving a Linear Equation by Matching Fourier Coefficients
> 1. Expand the forcing term in the Fourier series suited to the problem: the full series of period $2\pi$ for a periodic response (Part A), the sine series on $0 < x < a$ for $u(0) = u(a) = 0$ (Part B).
> 2. Write the unknown solution as a series of the same functions with unknown coefficients.
> 3. Replace each derivative by its effect on the coefficients: $\frac{d}{dt}$ maps $(A_n, B_n)$ to $(nB_n, -nA_n)$; $\frac{d^2}{dx^2}$ multiplies sine coefficients by $-n^2\pi^2/a^2$.
> 4. Match coefficients and solve the resulting algebraic equation for each $n$ separately. A vanishing denominator signals resonance (Part A) or an eigenvalue (Part B) and must be treated separately.
> 5. Sum the series; usually it is the only available form of the solution.

^rem-16-1

## C. The Sampling Theorem

What the electrical engineer calls a signal is just a function $f(t)$ defined for all $t$. If the function is integrable, there is a Fourier integral representation for it ([[§15★ Complex Methods#^thm-15-2|Theorem §15.2]]):

$$
f(t) = \int_{-\infty}^{\infty} C(\omega)\exp(i\omega t)\,d\omega, \qquad C(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(t)\exp(-i\omega t)\,dt .
$$

> [!definition] Definition §16.1: Band-Limited Signal; Cutoff Frequency
> A signal $f(t)$ is **band limited** if its Fourier transform is zero except on a finite interval, that is, if
>
> $$
> C(\omega) = 0 \qquad\text{for } |\omega| > \Omega .
> $$
>
> Then $\Omega$ is called the **cutoff frequency**, and
>
> $$
> f(t) = \int_{-\Omega}^{\Omega} C(\omega)\exp(i\omega t)\,d\omega . \qquad (1)
> $$
>
> *Powers: 1.11, Part C*

^def-16-1

> [!theorem] Theorem §16.3: The Sampling Theorem
> Let $f$ be band limited with cutoff frequency $\Omega$, as in (1), with $C$ sectionally continuous on $-\Omega < \omega < \Omega$. Then $f$ can be reconstructed from its samples at $t = 0, \pm\pi/\Omega, \pm2\pi/\Omega, \dots$:
>
> $$
> f(t) = \sum_{n=-\infty}^{\infty} f\Big(\frac{n\pi}{\Omega}\Big)\frac{\sin(\Omega t - n\pi)}{\Omega t - n\pi} = \sin(\Omega t)\sum_{n=-\infty}^{\infty} f\Big(\frac{n\pi}{\Omega}\Big)\frac{(-1)^n}{\Omega t - n\pi} \qquad (3)
> $$
>
> for every $t$, the series converging as the limit of its symmetric partial sums $\sum_{-N}^{N}$ (a term with $\Omega t = n\pi$ has the value $f(n\pi/\Omega)$).
>
> *Powers: 1.11, Equation (3); Exercise 1.11.6 (second form)*

^thm-16-3

> [!proof]+ Proof
> **Fourier series of the transform.** Focus on the interval $-\Omega < \omega < \Omega$ and write $C(\omega)$ as a complex Fourier series of period $2\Omega$ ([[§15★ Complex Methods#^thm-15-1|Theorem §15.1]] with $a = \Omega$):
>
> $$
> C(\omega) \sim \sum_{n=-\infty}^{\infty} c_n\exp\Big(\frac{in\pi\omega}{\Omega}\Big), \qquad c_n = \frac{1}{2\Omega}\int_{-\Omega}^{\Omega} C(\omega)\exp\Big(\frac{-in\pi\omega}{\Omega}\Big)\,d\omega . \qquad (2)
> $$
>
> The point of the sampling theorem is that the integral for $c_n$ is a value of $f$: comparing with (1) at $t = -n\pi/\Omega$,
>
> $$
> c_n = \frac{1}{2\Omega}f\Big(\frac{-n\pi}{\Omega}\Big) .
> $$
>
> So the transform of a band-limited function is found from samples (replacing $n$ by $-n$):
>
> $$
> C(\omega) \sim \frac{1}{2\Omega}\sum_{n=-\infty}^{\infty} f\Big(\frac{n\pi}{\Omega}\Big)\exp\Big(\frac{-in\pi\omega}{\Omega}\Big), \qquad -\Omega < \omega < \Omega .
> $$
>
> **Reconstruction.** Use (1) again and integrate term by term:
>
> $$
> \int_{-\Omega}^{\Omega}\exp\Big(\frac{-in\pi\omega}{\Omega}\Big)\exp(i\omega t)\,d\omega = \Big[\frac{e^{i\omega(t - n\pi/\Omega)}}{i(t - n\pi/\Omega)}\Big]_{-\Omega}^{\Omega} = \frac{2\sin(\Omega t - n\pi)}{t - n\pi/\Omega} = 2\Omega\,\frac{\sin(\Omega t - n\pi)}{\Omega t - n\pi} ,
> $$
>
> using $\sin\theta = (e^{i\theta} - e^{-i\theta})/(2i)$. Multiplying by $\frac{1}{2\Omega}f(n\pi/\Omega)$ and summing gives the first form of (3). Since $\sin(\Omega t - n\pi) = (-1)^n\sin(\Omega t)$, the second form follows.
>
> **Term-by-term integration.** (Powers integrates the series term by term without comment; here is why it is allowed.) Let $C_N$ be the symmetric partial sum $\sum_{-N}^{N}$ of the series for $C$. Applying [[§11★ Mean Error and Convergence in Mean#^thm-11-6|Theorem §11.6]] (convergence in mean) to the real and imaginary parts of the sectionally continuous function $C$ gives $\int_{-\Omega}^{\Omega}|C - C_N|^2\,d\omega \to 0$. By the Cauchy–Schwarz inequality,
>
> $$
> \Big|\int_{-\Omega}^{\Omega}\big(C(\omega) - C_N(\omega)\big)e^{i\omega t}\,d\omega\Big| \le \Big(\int_{-\Omega}^{\Omega}|C - C_N|^2\,d\omega\Big)^{1/2}\Big(\int_{-\Omega}^{\Omega} 1\,d\omega\Big)^{1/2} \to 0 .
> $$
>
> So $\int C_Ne^{i\omega t}\,d\omega$, which is the partial sum $\sum_{-N}^{N}$ of (3), tends to $\int Ce^{i\omega t}\,d\omega = f(t)$ for every $t$.

^pf-16-3

*Uses:* [[§16★ Applications of Fourier Series and Integrals#^def-16-1|Def. §16.1]], [[§15★ Complex Methods#^thm-15-1|§15.1]], [[§15★ Complex Methods#^def-15-2|Def. §15.2]], [[§11★ Mean Error and Convergence in Mean#^thm-11-6|§11.6]], [[§17 Cauchy–Schwarz and the Induced Norm#^thm-17-1|556 Thm. §17.1]] (Cauchy–Schwarz in the complex $L^2(-\Omega, \Omega)$)

> [!remark]- Connections
> - The proof is Hilbert-space geometry: $e^{-in\pi\omega/\Omega}/\sqrt{2\Omega}$ is an orthonormal basis of $L^2(-\Omega, \Omega)$ (the Fourier basis of [[§20 Orthonormal Sets and Bases#^thm-20-11|556 Thm. §20.11]], rescaled), the inverse transform carries it to the functions $\frac{\sin(\Omega t - n\pi)}{\Omega t - n\pi}$, and (3) is the expansion of $f$ in this basis of band-limited signals, with the samples as coordinates.

This is the main result of the sampling theorem: a band-limited function $f(t)$ may be reconstructed from its samples at $t = 0, \pm\pi/\Omega, \dots$, two samples per period $2\pi/\Omega$ of the highest frequency present. It is difficult to determine which functions are actually band limited; however, the process usually works quite well. In practice a finite series must be used,

$$
f(t) \cong \sum_{n=-N}^{N} f\Big(\frac{n\pi}{\Omega}\Big)\frac{\sin(\Omega t - n\pi)}{\Omega t - n\pi} . \qquad (4)
$$

Since the sampled values all come from the interval $-N\pi/\Omega$ to $N\pi/\Omega$, the series cannot attempt to approximate the function outside that interval.

> [!example] Example §16.3: Sampling a Signal That Is Not Band Limited
> The function
>
> $$
> f(t) = \frac{t^2 + 2t}{(1 + t^2)^2}
> $$
>
> is not band limited: its transform is $C(\omega) = \big(\frac14(1 - |\omega|) - \frac i2\omega\big)e^{-|\omega|}$ (a computation with residues, not needed here), which vanishes for no finite cutoff. But $C$ decays exponentially, so $f$ is nearly band limited, and it can be approximated satisfactorily from a finite portion of the sum (4). With $N = 100$ (201 terms), the largest error on $-4 \le t \le 8$ is about $0.18$ for $\Omega = 4$ (sample spacing $\pi/4 \approx 0.79$) and about $0.001$ for $\Omega = 10$ (spacing $\approx 0.31$), in line with the neglected part of the spectrum beyond $|\omega| = \Omega$, which decays like $|\omega|e^{-|\omega|}$. Notice the improvement in the figure.
>
> *Powers: 1.11, Example (Part C), Figure 13*

^ex-16-3

![[m341-16-1.svg]]
*Example §16.3: the signal $f(t) = (t^2 + 2t)/(1 + t^2)^2$ (dashed) and its sampling reconstructions (4) with $N = 100$, for cutoff $\Omega = 4$ (orange) and $\Omega = 10$ (blue). With $\Omega = 4$ the samples are too sparse to follow the steep rise near $t = 0$ and the reconstruction ripples; with $\Omega = 10$ it is indistinguishable from $f$.*
