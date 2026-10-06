---
type: section
subject: "[[Complex Variables]]"
chapter: 8
section: "111a"
tags: [complex-variables, math342, extension]
---
← [[§111★ Surfaces for Related Functions]] · ↑ [[· 8★ Mapping by Elementary Functions]] · [[§112★ Preservation of Angles and Scale Factors]] →

*The recurring examples of Chapter 8, gathered in course order: three linear fractional maps through prescribed points, the half strip under $w = \sin z$, and a branch of $((z - 1)/(z + 1))^{1/2}$. Each part embeds the chapter's items about one example; the items themselves stay in their sections.*
★ *Beyond MAT 342: the items come from sections the course skipped or left optional.*

## The Map Taking 2, i, −2 onto 1, i, −1

The map is found first by solving for the coefficients of $w = (az + b)/(cz + d)$:

![[§99★ Linear Fractional Transformations#^ex-99-1]]

and again from the implicit form (1) of [[§100★ An Implicit Form#^thm-100-1|§100]]:

![[§100★ An Implicit Form#^ex-100-1]]

## The Map Taking 1, 0, −1 onto i, ∞, 1

A point goes to infinity. First the conditions (6) and (7) of [[§99★ Linear Fractional Transformations#^def-99-2|§99]] force $d = 0$:

![[§99★ Linear Fractional Transformations#^ex-99-2]]

then the factors containing $w_2 = \infty$ are deleted from the implicit form ([[§100★ An Implicit Form#^prop-100-4|Proposition §100.4]]):

![[§100★ An Implicit Form#^ex-100-2]]

## The Map (i − z)∕(i + z)

Found from three boundary points:

![[§100★ An Implicit Form#^ex-100-3]]

and recognized as the case $\alpha = \pi$, $z_0 = i$ of [[§101★ Mappings of the Upper Half Plane#^thm-101-1|Theorem §101.1]], which maps the upper half plane onto the unit disk:

![[§102★ Examples (Mappings of the Upper Half Plane)#^ex-102-1]]

*Chain: later in [[§123★ Examples (Electrostatic Potential)#^ex-123-1|Chapter 10]]*

## The Sine Half Strip

$w = \sin z$ maps the half strip $-\pi/2 \le x \le \pi/2$, $y \ge 0$ one to one onto the upper half plane. This is shown first by vertical half lines:

![[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-1]]

The right half of the strip goes onto the first quadrant:

![[§104★ Mapping Vertical Line Segments by w = sin z#^ex-104-2]]

That right half is the starting point of [[§106★ Some Related Mappings#^ex-106-3|Example §106.3]] ($\cosh z$), [[§107★ Mappings by z²#^ex-107-2|Example §107.2]] ($\sin^2 z$) and [[§108★ Mappings by Branches of z^(1∕2)#^ex-108-4|Example §108.4]] (the square root of $\sin z$). The whole half strip is mapped again by horizontal segments:

![[§105★ Mapping Horizontal Line Segments by w = sin z#^ex-105-2]]

and once more by writing $\sin z$ through $\cosh$:

![[§106★ Some Related Mappings#^ex-106-5]]

*Chain: later in [[§113★ Further Examples (Preservation of Angles and Scale Factors)#^ex-113-3|Chapter 9]] · [[§126a The Heated Segment, the Quadrant, the Sine Half Strip and Flow Around a Corner#The Sine Half Strip|Chapter 10]] · [[§130★ Degenerate Polygons#^ex-130-1|Chapter 11]]*

## The Square Root of (z − 1)∕(z + 1)

The branch that maps the plane, except for the segment $-1 \le x \le 1$, onto the right half plane is found first as the principal square root composed with a linear fractional map:

![[§108★ Mappings by Branches of z^(1∕2)#^ex-108-3]]

and again as a branch with the same cut as $(z^2 - 1)^{1/2}$ ([[§109★ Square Roots of Polynomials#^def-109-1|Definition §109.1]]):

![[§109★ Square Roots of Polynomials#^ex-109-3]]
