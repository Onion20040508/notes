---
subject: math
type: theorem
source: "[[Linear Algebra]] 4.4"
ladr: "4.4"
page: 120
aliases: ["LADR 4.4"]
tags: [linear-algebra, ladr/4]
---
> [!theorem] 4.4 Properties of complex numbers
> For $w,z\in\C$:
> - $z+\bar z=2\operatorname{Re}z$ and $z-\bar z=2(\operatorname{Im}z)\,i$;
> - $z\bar z=|z|^2$;
> - $\overline{w+z}=\bar w+\bar z$, $\overline{wz}=\bar w\,\bar z$, $\bar{\bar z}=z$;
> - $|\operatorname{Re}z|\le|z|$ and $|\operatorname{Im}z|\le|z|$;
> - $|\bar z|=|z|$ and $|wz|=|w|\,|z|$;
> - **triangle inequality** $|w+z|\le|w|+|z|$.

> [!remark] Reverse triangle inequality
> $\big||w|-|z|\big|\le|w-z|$ follows by applying the triangle inequality to $w=(w-z)+z$ and to $z=(z-w)+w$.

> [!proof]-
> All but the last are direct computations from [[Complex conjugate, z, absolute value, ∣z∣]] (e.g. $(a+bi)(a-bi)=a^2+b^2$). *(Filled in: multiplicativity of $|\cdot|$.)* $|wz|^2=wz\,\overline{wz}=(w\bar w)(z\bar z)=|w|^2|z|^2$.
>
> **Triangle inequality.**
> $$
> |w+z|^2=(w+z)(\bar w+\bar z)=|w|^2+|z|^2+w\bar z+\overline{w\bar z}
> =|w|^2+|z|^2+2\operatorname{Re}(w\bar z)\le|w|^2+|z|^2+2|w||z|=(|w|+|z|)^2 ,
> $$
> using $\operatorname{Re}u\le|u|$ and $|w\bar z|=|w||z|$. Take square roots.

## Uses (in the proof)
- [[Complex conjugate, z, absolute value, ∣z∣]] (4.2)

## Connections
- The same proof pattern gives the triangle inequality for norms: [[Triangle inequality]], via [[Cauchy–Schwarz inequality]].
