---
type: section
subject: "[[Complex Variables]]"
chapter: 9
section: "113★"
bc: "113"
aliases: ["B&C 113"]
tags: [complex-variables, math342, extension]
---
← [[§112★ Preservation of Angles and Scale Factors]] · ↑ [[· 9★ Conformal Mapping]] · [[§114★ Local Inverses]] →

*Brown–Churchill, Section 113 (with Exercises 1–5 of Section 114).*
★ *Beyond MAT 342: the course skipped this section or left it optional; it is included from Brown–Churchill.*

This section checks the angle and scale statements of [[§112★ Preservation of Angles and Scale Factors|§112]] on explicit curves. For $w = z^2$ the images of half lines are computed, the angles between the image curves are measured from their tangents, and the results are compared with the angle of rotation $\arg f'(z_0)$ and the scale factor $|f'(z_0)|$. The examples show how both quantities change from point to point, and that a right angle stays a right angle at every point where the map is conformal.

## Two Examples with w = z²

> [!remark] Remark: Method — Checking Conformality at a Point
> To check, or use, conformality of $w = f(z)$ at $z_0$:
> 1. **Conformal?** Check that $f$ is analytic at $z_0$ and $f'(z_0) \ne 0$ ([[§112★ Preservation of Angles and Scale Factors#^def-112-2|Definition §112.2]]).
> 2. **Rotation and scale.** Compute $\psi_0 = \arg f'(z_0)$ and $|f'(z_0)|$.
> 3. **Images of curves.** Parametrize each curve $C$ through $z_0$ and write its image as $u = u(x(t), y(t))$, $v = v(x(t), y(t))$.
> 4. **Tangent inclinations.** The direction of the image at $w_0$ is that of $(du/dt, dv/dt)$; equivalently, it is $\psi_0$ plus the inclination of $C$ ([[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]]). Angles between image curves equal the angles between the original curves, in size and sense.

^rem-113-1

> [!example] Example §113.1: Two Half Lines Through 1 + i
> The function $f(z) = z^2 = x^2 - y^2 + i\,2xy$ is entire, and $f'(z) = 2z$ is zero only at the origin, so $w = z^2$ is conformal at $z_0 = 1 + i$, where the half lines
>
> $$
> C_1\colon\ y = x \ (x \ge 0) \qquad\text{and}\qquad C_2\colon\ x = 1 \ (y \ge 0) \qquad (1)
> $$
>
> intersect. Both are directed upward. Find their images and verify that the angle between them is preserved.
>
> **In the $z$ plane.** $C_1$ has inclination $\pi/4$ and $C_2$ has inclination $\pi/2$, so the angle from $C_1$ to $C_2$ at $1 + i$ is $\pi/4$.
>
> **Images.** The image of $z = (x, y)$ has coordinates
>
> $$
> u = x^2 - y^2 \qquad\text{and}\qquad v = 2xy . \qquad (2)
> $$
>
> On $C_1$, $y = x$, so the image $\Gamma_1$ is
>
> $$
> u = 0, \qquad v = 2x^2 \qquad (0 \le x < \infty), \qquad (3)
> $$
>
> the upper half $v \ge 0$ of the $v$ axis. On $C_2$, $x = 1$, so the image $\Gamma_2$ is
>
> $$
> u = 1 - y^2, \qquad v = 2y \qquad (0 \le y < \infty). \qquad (4)
> $$
>
> Eliminating $y = v/2$ from (4) gives $u = 1 - v^2/4$, so $\Gamma_2$ is the upper half of the parabola $v^2 = -4(u - 1)$. In each case the image is traversed upward, since $v$ increases with the parameter.
>
> **Angle in the $w$ plane.** Along $\Gamma_2$,
>
> $$
> \frac{dv}{du} = \frac{dv/dy}{du/dy} = \frac{2}{-2y} = -\frac2v ,
> $$
>
> so $dv/du = -1$ at $w = f(1 + i) = 2i$, where $v = 2$. Since $\Gamma_2$ is traversed upward and to the left there, its inclination is $3\pi/4$, while $\Gamma_1$ has inclination $\pi/2$. The angle from $\Gamma_1$ to $\Gamma_2$ at $2i$ is $3\pi/4 - \pi/2 = \pi/4$, as conformality requires.
>
> **Rotation and scale.** The angle of rotation at $1 + i$ is a value of
>
> $$
> \arg f'(1 + i) = \arg\big[2(1 + i)\big] = \frac\pi4 + 2n\pi \qquad (n = 0, \pm1, \pm2, \ldots),
> $$
>
> and indeed each inclination went up by $\pi/4$: $\pi/4 \mapsto \pi/2$ and $\pi/2 \mapsto 3\pi/4$. The scale factor is $|f'(1 + i)| = |2(1 + i)| = 2\sqrt2$.
>
> *B&C: Sec. 113, Example 1*

^ex-113-1

> [!example] Example §113.2: A Right Angle at z₀ = 1
> With the same map $w = z^2$, consider the half line $C_2$ of Example §113.1 and the half line $C_3\colon y = 0$ $(x \ge 0)$, directed to the right. They meet at $z_0 = 1$, where the angle from $C_3$ to $C_2$ is $\pi/2$.
>
> The image of $C_2$ is the half parabola $\Gamma_2$ of Example §113.1. Since $y = 0$ on $C_3$, equations (2) give its image
>
> $$
> \Gamma_3\colon\ u = x^2, \qquad v = 0 \qquad (0 \le x < \infty),
> $$
>
> the positive $u$ axis, directed to the right. At $w = f(1) = 1$ (where $y = 0$ on $C_2$), the tangent of $\Gamma_2$ is $(du/dy, dv/dy) = (-2y, 2) = (0, 2)$, pointing straight up. So the angle from $\Gamma_3$ to $\Gamma_2$ is $\pi/2$: the right angle is preserved. Here the angle of rotation is $\arg f'(1) = \arg 2 = 0$, so the directions themselves are unchanged, and the scale factor is $|f'(1)| = 2$, smaller than the $2\sqrt2$ at $1 + i$.
>
> *B&C: Sec. 113, Example 2*

^ex-113-2

![[m342-113-1.svg]]
*Examples §113.1 and §113.2 under $w = z^2$. Left: the half lines $C_1\colon y = x$ (blue), $C_2\colon x = 1$ (red) and $C_3\colon y = 0$ (green). Right: their images, the positive $v$ axis $\Gamma_1$, the half parabola $\Gamma_2\colon v^2 = -4(u - 1)$, and the positive $u$ axis $\Gamma_3$. The angle $\pi/4$ at $1 + i$ reappears at $2i$, and the right angle at $1$ reappears at $1$; the directions at $1 + i$ are turned by $\arg f'(1 + i) = \pi/4$, those at $1$ not at all.*

## Rotation and Scale for Other Maps

> [!example] Example §113.3: Angles of Rotation and Scale Factors
> **(a) $w = z^2$ at $z_0 = 2 + i$.** $f'(z_0) = 2(2 + i) = 4 + 2i$, so the angle of rotation is $\arctan\frac12 \approx 0.4636$ (about $26.6°$) and the scale factor is $|4 + 2i| = \sqrt{20} = 2\sqrt5$. Illustration: the horizontal line $y = 1$, directed to the right, has image $u = x^2 - 1$, $v = 2x$, the parabola $u = v^2/4 - 1$; at $x = 2$ its tangent $(du/dx, dv/dx) = (2x, 2) = (4, 2)$ has inclination $\arctan\frac12 = 0 + \arg f'(z_0)$, as (3) of [[§112★ Preservation of Angles and Scale Factors#^thm-112-1|Theorem §112.1]] requires.
>
> **(b) $w = 1/z$.** $f'(z) = -1/z^2$. At $z_0 = 1$, $f'(1) = -1$, angle of rotation $\pi$; at $z_0 = i$, $f'(i) = -1/i^2 = 1$, angle of rotation $0$.
>
> **(c) $w = z^n$ $(n = 1, 2, \ldots)$ at $z_0 = r_0e^{i\theta_0} \ne 0$.** $f'(z_0) = nz_0^{n-1} = nr_0^{n-1}e^{i(n-1)\theta_0}$, so the angle of rotation is $(n - 1)\theta_0$ and the scale factor is $nr_0^{n-1}$. (For $n = 2$, $z_0 = 1 + i = \sqrt2e^{i\pi/4}$: rotation $\pi/4$, scale $2\sqrt2$, as in Example §113.1.)
>
> **(d) $w = \sin z$.** $\sin z$ is entire with $(\sin z)' = \cos z$, whose zeros are exactly $z = \frac\pi2 + n\pi$ $(n = 0, \pm1, \pm2, \ldots)$ ([[§38 Zeros and Singularities of Trigonometric Functions#^thm-38-1|Theorem §38.1]]). So $w = \sin z$ is conformal at all other points. At $z_0 = \frac\pi2$, $\sin z = 1 - \frac12(z - \frac\pi2)^2 + \cdots$, so $m = 2$ in [[§112★ Preservation of Angles and Scale Factors#^thm-112-3|Theorem §112.3]] and angles at $\frac\pi2$ are doubled: the right angle between the segment $0 \le x \le \frac\pi2$ of the real axis and the vertical line $x = \frac\pi2$ opens out to the straight angle at $w = 1$, where both go onto the real axis ([[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1|Example §104.1]]).
>
> *B&C: Sec. 114, Exercises 1, 2, 4 and 5*

^ex-113-3

*Chain: the sine half strip earlier in [[§111a Three Linear Fractional Maps, the Sine Half Strip and ((z − 1)∕(z + 1))^(1∕2)#The Sine Half Strip|Chapter 8]] · later in [[§126a The Heated Segment, the Quadrant, the Sine Half Strip and Flow Around a Corner#The Sine Half Strip|Chapter 10]] · [[§130★ Degenerate Polygons#^ex-130-1|Chapter 11]]*

> [!example] Example §113.4: Two Lines and Their Images Under 1/z
> Show that $w = 1/z$ maps the lines $y = x - 1$ and $y = 0$ onto the circle $u^2 + v^2 - u - v = 0$ and the line $v = 0$ (with $w = 0$ corresponding to $z = \infty$), and verify conformality at $z_0 = 1$.
>
> **The line $y = 0$.** For real $z = x \ne 0$, $w = 1/x$ is real: the image lies on $v = 0$.
>
> **The line $y = x - 1$.** Put $z = x + i(x - 1)$ and $D = x^2 + (x - 1)^2 = 2x^2 - 2x + 1 > 0$. Then
>
> $$
> w = \frac{1}{z} = \frac{x - i(x - 1)}{D}, \qquad u = \frac xD, \qquad v = -\frac{x - 1}{D} .
> $$
>
> So $u^2 + v^2 = \dfrac{x^2 + (x - 1)^2}{D^2} = \dfrac1D$ and $u + v = \dfrac{x - (x - 1)}{D} = \dfrac1D$. Hence $u^2 + v^2 - u - v = 0$: the image lies on the circle with center $\frac12 + \frac i2$ and radius $1/\sqrt2$, which passes through $0$ and $1$.
>
> **Directions at $z_0 = 1$**, both lines directed by increasing $x$. In the $z$ plane, $y = x - 1$ has inclination $\pi/4$ and $y = 0$ has inclination $0$: the angle from the first to the second is $-\pi/4$. In the $w$ plane: on $v = 0$, $u = 1/x$ decreases, so the image runs to the left, inclination $\pi$. On the circle, at $x = 1$ (where $D = 1$, $D' = 4x - 2 = 2$),
>
> $$
> \frac{du}{dx} = \frac{D - xD'}{D^2} = -1, \qquad \frac{dv}{dx} = \frac{-D + (x - 1)D'}{D^2} = -1 ,
> $$
>
> so the image runs in the direction $(-1, -1)$, inclination $5\pi/4$. The angle from the circle to the line is $\pi - \frac{5\pi}{4} = -\frac\pi4$, the same as in the $z$ plane, and each inclination has increased by $\pi = \arg f'(1)$ (Example §113.3(b)). The scale factor $|f'(1)| = 1$.
>
> *B&C: Sec. 114, Exercise 3*

^ex-113-4

*Chain: the function $1/z$ earlier in [[§59a The Function 1∕z|Chapter 4]] · [[§98★ Mappings by 1∕z|Chapter 8]]*
