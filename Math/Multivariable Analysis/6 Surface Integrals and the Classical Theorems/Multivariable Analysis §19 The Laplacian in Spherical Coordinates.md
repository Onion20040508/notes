---
type: section
subject: "[[Multivariable Analysis]]"
chapter: 6
section: 19
tags: [multivariable-analysis, math452]
---
← [[Multivariable Analysis §18 Surface Integrals]] · ↑ [[Multivariable Analysis — 6 Surface Integrals and the Classical Theorems]] · [[Multivariable Analysis §20 Stokes' Theorem in ℝ³]] →

In Cartesian coordinates, the Laplacian ([[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Def. §17.2]]) is $\Delta u = u_{xx} + u_{yy} + u_{zz}$. What is the corresponding expression in spherical coordinates? Computing this by brute-force [[Multivariable Chain Rule|chain rule]] is extremely tedious (it requires second derivatives of the coordinate transformation). The [[Divergence Theorem in ℝ³|Divergence Theorem]] provides a much cleaner derivation.

![[m452-19-1.svg]]
*The spherical coordinate system used in §19: $r$ is the distance from the origin, $\theta$ the polar angle from the $z$-axis, $\psi$ the azimuthal angle in the $xy$-plane. The Laplacian's spherical form — and the $\sin\theta$ in the volume element — both come from how these coordinates distort lengths, exactly the Gram matrix computation of [[Multivariable Analysis §18 Surface Integrals#^def-18-4|§18]].*

### Setup and Notation

**Spherical coordinates:**

$$
x = r\sin\theta\cos\psi, \qquad y = r\sin\theta\sin\psi, \qquad z = r\cos\theta,
$$

where $r \geq 0$ is the radial distance, $\theta \in [0, \pi]$ is the polar angle (from the $z$-axis), and $\psi \in [0, 2\pi)$ is the azimuthal angle (in the $xy$-plane).

**Two names for the same function:**

$$
v(\psi, \theta, r) = u\big(x(\psi, \theta, r), \; y(\psi, \theta, r), \; z(\psi, \theta, r)\big).
$$

Here $u(x,y,z)$ is the function in Cartesian coordinates and $v(\psi, \theta, r)$ is the *same* function re-expressed in spherical coordinates. Using two different names is essential: $\frac{\partial v}{\partial r}$ (holding $\psi, \theta$ fixed) is *not* the same as $\frac{\partial u}{\partial r}$ (which is not even well-defined in Cartesian coordinates).

**Goal:** Express $\Delta u = u_{xx} + u_{yy} + u_{zz}$ in terms of $v_r, v_\theta, v_\psi$ and their derivatives.

## The Spherical Brick

Since $\Delta u = \nabla \cdot (\nabla u)$, the Divergence Theorem ([[Divergence Theorem in ℝ³|Theorem §18.2]]) says: for any region $V$,

$$
\iiint_V \Delta u \, dV = \iint_{\partial V} \nabla u \cdot \hat{n} \, dS.
$$

**Strategy:** Choose $V$ to be an infinitesimal “spherical brick” — the region

$$
V = \{(\psi, \theta, r) : \psi_0 \leq \psi \leq \psi_0 + d\psi, \;\; \theta_0 \leq \theta \leq \theta_0 + d\theta, \;\; r_0 \leq r \leq r_0 + dr\}.
$$

This brick has three pairs of faces. We compute the net flux of $\nabla u$ through each pair, then divide by the volume to extract $\Delta u$.

### Geometry of the Brick

The spherical coordinate system is **orthogonal**: the unit vectors $\hat{r}$, $\hat{\theta}$, $\hat{\psi}$ are mutually perpendicular. The **scale factors** (edge lengths per unit coordinate change) are:

$$
h_r = 1, \qquad h_\theta = r, \qquad h_\psi = r\sin\theta.
$$

These come from the metric: an infinitesimal displacement in each coordinate direction has length

$$
dr, \qquad r \, d\theta, \qquad r\sin\theta \, d\psi.
$$

![[m452-19-2.svg]]
*The volume element of spherical coordinates: a coordinate box $dr \times d\theta \times d\psi$ maps to a curvilinear cell with three mutually orthogonal edges of lengths $dr$ (radial), $r\,d\theta$ (meridional), and $r\sin\theta\,d\psi$ (azimuthal). Multiplying them: $dV = r^2\sin\theta\,dr\,d\theta\,d\psi$ — the Jacobian of the spherical map ([[Multivariable Analysis §15 Multivariable Integration#^ex-15-6|Ex. §15.6]]), read off geometrically. This is the 3D sibling of the polar picture in [[Multivariable Analysis §15 Multivariable Integration#^thm-15-7|§15]]: near the $z$-axis ($\sin\theta \to 0$) the azimuthal edge collapses and $J \to 0$, exactly where spherical coordinates degenerate.*

The brick has:
- **Edge lengths:** $dr$ (radial), $r \, d\theta$ (polar), $r\sin\theta \, d\psi$ (azimuthal).
- **Volume:** $dV = r^2 \sin\theta \, dr \, d\theta \, d\psi$.
- **Face areas:**
    - Two $r$-faces (constant $r$): area $= r^2 \sin\theta \, d\theta \, d\psi$, normal $\pm\hat{r}$.
    - Two $\theta$-faces (constant $\theta$): area $= r\sin\theta \, dr \, d\psi$, normal $\pm\hat{\theta}$.
    - Two $\psi$-faces (constant $\psi$): area $= r \, dr \, d\theta$, normal $\pm\hat{\psi}$.

![[m452-19-3.svg]]
*The brick cut by the half-plane $\psi = \psi_0$ (the $z$-axis vertical, $\theta$ measured from it). Its edges in this plane are $dr$ and $r\,d\theta$; the third edge, $r\sin\theta\,d\psi$, points out of the page, and its length is (distance to the $z$-axis) $\times\, d\psi$. The outward normals are $\pm\hat{r}$ on the two $r$-faces (red) and $\pm\hat{\theta}$ on the two $\theta$-faces (green). The outer $r$-face is larger than the inner one — area $(r_0+dr)^2\sin\theta\,d\theta\,d\psi$ versus $r_0^2\sin\theta\,d\theta\,d\psi$ — which is why the net flux is $\partial_r(r^2 v_r)$ and not $r^2\,\partial_r v_r$.*

### The Gradient in Spherical Coordinates

The gradient ([[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Def. §17.2]]) expressed in the orthonormal basis $\{\hat{r}, \hat{\theta}, \hat{\psi}\}$ is:

$$
\nabla u = \frac{1}{h_r}\frac{\partial v}{\partial r}\hat{r} + \frac{1}{h_\theta}\frac{\partial v}{\partial \theta}\hat{\theta} + \frac{1}{h_\psi}\frac{\partial v}{\partial \psi}\hat{\psi} = v_r \, \hat{r} + \frac{1}{r}v_\theta \, \hat{\theta} + \frac{1}{r\sin\theta}v_\psi \, \hat{\psi}.
$$

The factor $1/h_i$ appears because the gradient measures the rate of change *per unit length*, not per unit coordinate: moving $d\theta$ in the $\theta$-direction corresponds to a physical distance $r \, d\theta$, so $\nabla u \cdot \hat{\theta} = v_\theta / r$, not $v_\theta$.

## Computing the Net Flux

**Flux through the $r$-faces** (top and bottom of the brick, at $r_0 + dr$ and $r_0$):

The component of $\nabla u$ normal to these faces is $v_r$. The face area at radius $r$ is $r^2\sin\theta \, d\theta \, d\psi$.

$$
\begin{aligned}
\text{Net flux} &= v_r\big|_{r_0 + dr} \cdot (r_0 + dr)^2 \sin\theta \, d\theta \, d\psi \;-\; v_r\big|_{r_0} \cdot r_0^2 \sin\theta \, d\theta \, d\psi \\
&= \frac{\partial}{\partial r}\big(r^2 \sin\theta \cdot v_r\big) \, dr \, d\theta \, d\psi \\
&= \sin\theta \, \frac{\partial}{\partial r}\big(r^2 v_r\big) \, dr \, d\theta \, d\psi.
\end{aligned}
$$

(The second line is the definition of the derivative ([[Single Variable Analysis §28 Basic Properties of the Derivative#^def-28-1|451 §28.1]]): $f(r_0 + dr) - f(r_0) \approx f'(r_0) \, dr$.)

**Flux through the $\theta$-faces** (at $\theta_0 + d\theta$ and $\theta_0$):

The component of $\nabla u$ normal to these faces is $\frac{1}{r}v_\theta$. The face area at angle $\theta$ is $r\sin\theta \, dr \, d\psi$.

$$
\begin{aligned}
\text{Net flux} &= \frac{1}{r}v_\theta\big|_{\theta_0 + d\theta} \cdot r\sin(\theta_0 + d\theta) \, dr \, d\psi \;-\; \frac{1}{r}v_\theta\big|_{\theta_0} \cdot r\sin\theta_0 \, dr \, d\psi \\
&= \frac{\partial}{\partial \theta}\big(\sin\theta \cdot v_\theta\big) \, dr \, d\theta \, d\psi.
\end{aligned}
$$

**Flux through the $\psi$-faces** (at $\psi_0 + d\psi$ and $\psi_0$):

The component of $\nabla u$ normal to these faces is $\frac{1}{r\sin\theta}v_\psi$. The face area at angle $\psi$ is $r \, dr \, d\theta$.

$$
\begin{aligned}
\text{Net flux} &= \frac{1}{r\sin\theta}v_\psi\big|_{\psi_0 + d\psi} \cdot r \, dr \, d\theta \;-\; \frac{1}{r\sin\theta}v_\psi\big|_{\psi_0} \cdot r \, dr \, d\theta \\
&= \frac{1}{\sin\theta}\frac{\partial v_\psi}{\partial \psi} \, dr \, d\theta \, d\psi = \frac{1}{\sin\theta}v_{\psi\psi} \, dr \, d\theta \, d\psi.
\end{aligned}
$$

## Assembling the Laplacian

By the Divergence Theorem:

$$
\Delta u \cdot dV = \text{total net flux through all six faces}.
$$

Substituting $dV = r^2\sin\theta \, dr \, d\theta \, d\psi$ and the three flux terms:

$$
\Delta u \cdot r^2\sin\theta \, dr \, d\theta \, d\psi = \left[\sin\theta \, \frac{\partial}{\partial r}(r^2 v_r) + \frac{\partial}{\partial \theta}(\sin\theta \, v_\theta) + \frac{v_{\psi\psi}}{\sin\theta}\right] dr \, d\theta \, d\psi.
$$

Dividing both sides by $r^2\sin\theta \, dr \, d\theta \, d\psi$:

> [!theorem] Theorem §19.1: Laplacian in Spherical Coordinates
> If $v(\psi, \theta, r) = u(x(\psi, \theta, r), y(\psi, \theta, r), z(\psi, \theta, r))$, then:
>
> $$
> \boxed{\Delta u = \frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2 \frac{\partial v}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\!\left(\sin\theta \, \frac{\partial v}{\partial \theta}\right) + \frac{1}{r^2\sin^2\!\theta}\frac{\partial^2 v}{\partial \psi^2}}
> $$

^thm-19-1

*Uses:* [[Divergence Theorem in ℝ³|§18.2]], [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^def-17-2|Def. §17.2]], [[Multivariable Analysis §15 Multivariable Integration#^ex-15-6|Ex. §15.6]], [[Single Variable Analysis §28 Basic Properties of the Derivative#^def-28-1|451 §28.1]]

> [!remark]- Connections
> - The volume factor $r^2\sin\theta$ is the Jacobian of [[Multivariable Analysis §15 Multivariable Integration#^ex-15-6|Spherical Coordinates in ℝ³]]; the scale factors are the square roots of the diagonal of the Gram matrix ([[Multivariable Analysis §18 Surface Integrals#^def-18-4|Def. §18.4]]) of the coordinate map.
> - The 2D radial analogue: [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|Fundamental Solution of the 2D Laplacian]].

> [!remark] Remark: Reading the Formula
> Each term has the structure $\frac{1}{\text{volume factor}} \cdot \frac{\partial}{\partial q_i}\!\left(\frac{\text{area of face}_i}{\text{edge length}_i} \cdot v_{q_i}\right)$:
> - **$r$-term:** face area $r^2\sin\theta$, edge length $1$, volume $r^2\sin\theta$ $\Rightarrow$ $\frac{1}{r^2}\frac{\partial}{\partial r}(r^2 v_r)$.
> - **$\theta$-term:** face area $r\sin\theta$, edge length $r$, volume $r^2\sin\theta$ $\Rightarrow$ $\frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}(\sin\theta \, v_\theta)$.
> - **$\psi$-term:** face area $r$, edge length $r\sin\theta$, volume $r^2\sin\theta$ $\Rightarrow$ $\frac{1}{r^2\sin^2\theta}v_{\psi\psi}$.
>
> The denominators are *not* arbitrary — they are forced by the geometry of the spherical coordinate system. Each denominator compensates for how the coordinate grid distorts areas and volumes.

^rem-19-1

> [!remark] Remark: Verification: Radial Functions
> For a radial function $v = f(r)$ (independent of $\theta, \psi$), the $\theta$- and $\psi$-terms vanish, and:
>
> $$
> \Delta u = \frac{1}{r^2}\frac{d}{dr}\!\left(r^2 f'(r)\right) = \frac{1}{r^2}\big(2r f'(r) + r^2 f''(r)\big) = f''(r) + \frac{2}{r}f'(r).
> $$
>
> Setting $\Delta u = 0$: $f'' + \frac{2}{r}f' = 0$. With $g = f'$: $g' + \frac{2}{r}g = 0$, so $g = C/r^2$, hence $f(r) = -C/r + C'$.
>
> This is the **3D fundamental solution** $\phi = C/r$ (compare with the 2D result $\phi = C\ln r$ from [[Multivariable Analysis §17 The Divergence Theorem in Higher Dimensions and Green's Identities#^thm-17-5|Theorem §17.5]]). The different power ($1/r$ vs $\ln r$) reflects the different rate at which surface area grows: $4\pi r^2$ in 3D ([[Multivariable Analysis §18 Surface Integrals#^ex-18-2|Ex. §18.2]]) vs $2\pi r$ in 2D.

^rem-19-2

> [!remark] Remark: General Orthogonal Coordinates
> The same Divergence Theorem argument works for *any* orthogonal coordinate system $(q_1, q_2, q_3)$ with scale factors $(h_1, h_2, h_3)$. The result is:
>
> $$
> \Delta v = \frac{1}{h_1 h_2 h_3}\left[\frac{\partial}{\partial q_1}\!\left(\frac{h_2 h_3}{h_1} v_{q_1}\right) + \frac{\partial}{\partial q_2}\!\left(\frac{h_1 h_3}{h_2} v_{q_2}\right) + \frac{\partial}{\partial q_3}\!\left(\frac{h_1 h_2}{h_3} v_{q_3}\right)\right].
> $$
>
> Substituting $h_r = 1$, $h_\theta = r$, $h_\psi = r\sin\theta$ recovers the spherical formula. This general formula also gives the Laplacian in cylindrical coordinates ($h_r = 1$, $h_\theta = r$, $h_z = 1$), ellipsoidal coordinates, and any other orthogonal system.

^rem-19-3
