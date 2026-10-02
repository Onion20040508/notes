---
type: section
subject: "[[Complex Variables]]"
chapter: 1
section: 9
bc: "9"
aliases: ["B&C 9"]
tags: [complex-variables, math342]
---
← [[§8 Products and Powers in Exponential Form]] · ↑ [[· 1 Complex Numbers]] · [[§10 Roots of Complex Numbers]] →

*Brown–Churchill, Section 9.*

The product formula of [[§8 Products and Powers in Exponential Form|§8]] says that arguments add under multiplication: $\arg(z_1z_2) = \arg z_1 + \arg z_2$. Since $\arg$ is multiple-valued, this is an identity between sets of numbers, not between single values, and it must be read with care: choose values of any two of the three arguments, and some value of the third makes the equation true. The principal argument does not behave as well. $\operatorname{Arg}(z_1z_2)$ can differ from $\operatorname{Arg} z_1 + \operatorname{Arg} z_2$ by $\pm 2\pi$, because the sum can leave the interval $(-\pi, \pi]$. The same bookkeeping reappears for logarithms ([[§34 Some Identities Involving Logarithms|§34]]), where $\log(z_1z_2) = \log z_1 + \log z_2$ holds in the same set sense and fails for $\operatorname{Log}$.

## Arguments of Products

> [!theorem] Theorem §9.1: The Argument of a Product
> For nonzero $z_1$, $z_2$,
>
> $$
> \arg(z_1z_2) = \arg z_1 + \arg z_2 , \qquad (2)
> $$
>
> interpreted as follows: if values of two of the three (multiple-valued) arguments are specified, then there is a value of the third such that the equation holds. Equivalently, the set of all values of $\arg(z_1z_2)$ is the set of all sums $\theta_1 + \theta_2$ with $\theta_1$ a value of $\arg z_1$ and $\theta_2$ a value of $\arg z_2$.
>
> *B&C: Sec. 9, Equation (2)*

^thm-9-1

> [!proof]+ Proof
> Let $\theta_1$ and $\theta_2$ denote any values of $\arg z_1$ and $\arg z_2$, so $z_1 = r_1e^{i\theta_1}$, $z_2 = r_2e^{i\theta_2}$. By (1) of §8,
>
> $$
> z_1z_2 = (r_1r_2)e^{i(\theta_1 + \theta_2)} , \qquad (1)
> $$
>
> with $r_1r_2 = |z_1||z_2| = |z_1z_2| > 0$. So $\theta_1 + \theta_2$ is a value of $\arg(z_1z_2)$ (Fig. 9 of B&C), which settles the case where $\arg z_1$ and $\arg z_2$ are specified.
>
> If, on the other hand, values of $\arg(z_1z_2)$ and $\arg z_1$ are specified, then by (2) of §7 they correspond to particular choices of $n$ and $n_1$ in the expressions
>
> $$
> \arg(z_1z_2) = (\theta_1 + \theta_2) + 2n\pi \quad (n = 0, \pm1, \ldots) \qquad\text{and}\qquad \arg z_1 = \theta_1 + 2n_1\pi \quad (n_1 = 0, \pm1, \ldots) .
> $$
>
> Since
>
> $$
> (\theta_1 + \theta_2) + 2n\pi = (\theta_1 + 2n_1\pi) + \big[\theta_2 + 2(n - n_1)\pi\big] ,
> $$
>
> equation (2) is satisfied when the value $\arg z_2 = \theta_2 + 2(n - n_1)\pi$ is chosen. The case where values of $\arg(z_1z_2)$ and $\arg z_2$ are specified follows from this one, since (2) can also be written $\arg(z_2z_1) = \arg z_2 + \arg z_1$.
>
> For the set form: every sum of a value of $\arg z_1$ and a value of $\arg z_2$ is a value of $\arg(z_1z_2)$ by the first case, and every value of $\arg(z_1z_2)$ is such a sum by the second.

^pf-9-1

*Uses:* [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]], [[§7 Exponential Form#^def-7-1|Def. §7.1]], [[§6 Complex Conjugates#^thm-6-4|§6.4]]

> [!remark]- Connections
> - The computational treatment states this with single values (multiplication adds arguments): [[§53 Complex Numbers#^thm-53-5|235 Thm. §53.5]]. The set interpretation is what makes the statement exactly true.

Statement (2) is sometimes valid when $\arg$ is replaced everywhere by $\operatorname{Arg}$ ([[§9 Arguments of Products and Quotients#^ex-9-4|Example §9.4]]), but not always ([[§9 Arguments of Products and Quotients#^ex-9-1|Example §9.1]]).

> [!theorem] Corollary §9.2: Arguments of Inverses and Quotients
> For nonzero $z_1$, $z_2$,
>
> $$
> \arg\big(z_2^{-1}\big) = -\arg z_2 , \qquad (3)
> $$
>
> in the sense that the set of all values on the left is the same as the set of all values on the right, and
>
> $$
> \arg\Big(\frac{z_1}{z_2}\Big) = \arg z_1 - \arg z_2 , \qquad (4)
> $$
>
> interpreted in the same way as (2).
>
> *B&C: Sec. 9, Equations (3)–(4)*

^cor-9-2

> [!proof]+ Proof
> **(3)** If $z_2 = r_2e^{i\theta_2}$, then by (3) of §8, $z_2^{-1} = \frac{1}{r_2}e^{-i\theta_2}$. So $-\theta_2$ is a value of $\arg(z_2^{-1})$, and by (2) of §7 the set of all values is $\{-\theta_2 + 2n\pi\} = \{-(\theta_2 + 2(-n)\pi)\}$, which, as $n$ runs over the integers, is the set of negatives of all values of $\arg z_2$.
>
> **(4)** By Theorem §9.1 applied to $z_1/z_2 = z_1z_2^{-1}$,
>
> $$
> \arg\Big(\frac{z_1}{z_2}\Big) = \arg\big(z_1z_2^{-1}\big) = \arg z_1 + \arg\big(z_2^{-1}\big) ,
> $$
>
> and by (3) the values of $\arg(z_2^{-1})$ are exactly the negatives of the values of $\arg z_2$.

^pf-9-2

*Uses:* [[§9 Arguments of Products and Quotients#^thm-9-1|§9.1]], [[§8 Products and Powers in Exponential Form#^thm-8-1|§8.1]], [[§7 Exponential Form#^def-7-1|Def. §7.1]]

## Examples

> [!example] Example §9.1: Arg Is Not Additive
> When $z_1 = -1$ and $z_2 = i$,
>
> $$
> \operatorname{Arg}(z_1z_2) = \operatorname{Arg}(-i) = -\frac\pi2 \qquad\text{but}\qquad \operatorname{Arg} z_1 + \operatorname{Arg} z_2 = \pi + \frac\pi2 = \frac{3\pi}{2} .
> $$
>
> If, however, we keep these values of $\arg z_1$ and $\arg z_2$ and select the value $\operatorname{Arg}(z_1z_2) + 2\pi = -\frac\pi2 + 2\pi = \frac{3\pi}{2}$ of $\arg(z_1z_2)$, equation (2) is satisfied, as Theorem §9.1 promises.
>
> *B&C: Sec. 9, Example 1*

^ex-9-1

> [!example] Example §9.2: The Principal Argument of a Quotient
> Find $\operatorname{Arg} z$ when $z = \dfrac{i}{-1 - i}$.
>
> By (4), $\arg z = \arg i - \arg(-1 - i)$. Since $\operatorname{Arg} i = \frac\pi2$ and $\operatorname{Arg}(-1 - i) = -\frac{3\pi}{4}$ ([[§7 Exponential Form#^ex-7-1|Example §7.1]]), one value of $\arg z$ is $\frac\pi2 + \frac{3\pi}{4} = \frac{5\pi}{4}$. This is not a principal value, since it is not in $(-\pi, \pi]$; adding $-2\pi$,
>
> $$
> \operatorname{Arg}\Big(\frac{i}{-1 - i}\Big) = \frac{5\pi}{4} - 2\pi = -\frac{3\pi}{4} .
> $$
>
> Check: $\dfrac{i}{-1 - i} = \dfrac{i(-1 + i)}{(-1 - i)(-1 + i)} = \dfrac{-1 - i}{2}$, which lies in the third quadrant on the ray of $-1 - i$.
>
> *B&C: Sec. 9, Example 2*

^ex-9-2

> [!example] Example §9.3: Principal Arguments
> Find $\operatorname{Arg} z$ when **(a)** $z = \dfrac{-2}{1 + \sqrt3\,i}$; **(b)** $z = (\sqrt3 - i)^6$.
>
> **(a)** By (4), $\arg z = \arg(-2) - \arg(1 + \sqrt3\,i)$. With the values $\pi$ and $\frac\pi3$, one value of $\arg z$ is $\pi - \frac\pi3 = \frac{2\pi}{3}$. It lies in $(-\pi, \pi]$, so $\operatorname{Arg} z = \frac{2\pi}{3}$.
>
> **(b)** $\sqrt3 - i = 2e^{-i\pi/6}$ (fourth quadrant, reference angle $\frac\pi6$), so by (4) of §8, $z = 2^6e^{-i\pi} = -64$. A negative real number has $\operatorname{Arg} z = \pi$ (not $-\pi$, although $-\pi = 6\cdot(-\frac\pi6)$ is the value of $\arg z$ produced by the computation).
>
> *B&C: Sec. 9, Exercise 1*

^ex-9-3

> [!example] Example §9.4: When Arg Is Additive
> Show that if $\operatorname{Re} z_1 > 0$ and $\operatorname{Re} z_2 > 0$, then $\operatorname{Arg}(z_1z_2) = \operatorname{Arg} z_1 + \operatorname{Arg} z_2$.
>
> Let $\Theta_k = \operatorname{Arg} z_k$. Since $\operatorname{Re} z_k = |z_k|\cos\Theta_k > 0$, $\cos\Theta_k > 0$, and with $-\pi < \Theta_k \le \pi$ this forces $-\frac\pi2 < \Theta_k < \frac\pi2$. Hence $-\pi < \Theta_1 + \Theta_2 < \pi$. By Theorem §9.1, $\Theta_1 + \Theta_2$ is a value of $\arg(z_1z_2)$, and it lies in $(-\pi, \pi]$, so it is the principal value: $\operatorname{Arg}(z_1z_2) = \Theta_1 + \Theta_2$. (Example §9.1 shows that some hypothesis is needed: there $\operatorname{Re} z_1 = -1 < 0$.)
>
> *B&C: Sec. 9, Exercise 6*

^ex-9-4
