---
type: subject
discipline: applied math
course: MAT 342 Applied Complex Analysis (Stony Brook), Fall 2024
instructor: Olga Plamenevskaya
textbook: "Brown & Churchill, Complex Variables and Applications, 9th ed."
status: completed
aliases: ["MAT 342", "Brown–Churchill", "Complex Analysis", "Applied Complex Analysis"]
tags: [subject, complex-variables]
---
# Complex Variables

Complex numbers, analytic functions, contour integration, Cauchy's theorem and integral formula, Taylor and Laurent series, residues and their applications, and conformal mapping with its applications to steady temperatures, electrostatics and fluid flow — following James W. Brown and Ruel V. Churchill, *Complex Variables and Applications*, 9th edition (McGraw-Hill, 2014), section by section through all 140 sections; note §N is Brown–Churchill's Section N (alias "B&C N"). The course, MAT 342 at Stony Brook (Olga Plamenevskaya, Fall 2024), covered Chapters 1–7 with some sections optional; those and Chapters 8–12 are included and marked ★.

This is the vault's home for complex analysis: every proof Brown and Churchill give is written out (Cauchy–Goursat, the Cauchy integral formula and its extension, Liouville, the maximum modulus principle, Taylor's and Laurent's theorems, the residue theorem, the argument principle, Rouché), with worked examples from the course homework and past finals. The real-variable tools are in [[Single Variable Analysis]] and [[Multivariable Analysis]]; the potential problems of Chapters 9–12 meet [[Fourier Series and PDEs]] (Chapter 4).

## How the chapters build on each other
Solid arrows: a chapter's proofs and examples rely on the earlier chapter (arrows implied by others are omitted; exact counts are in each chapter note). Dashed arrows labelled "on credit": results used before they are proved. Dashed arrows to the Math subjects: where the rigorous treatment is, labelled with the number of *Connections* links (only arrows with 3 or more are drawn).

```mermaid
graph TD
  C1["1 Complex Numbers"]
  C2["2 Analytic Functions"]
  C3["3 Elementary Functions"]
  C4["4 Integrals"]
  C5["5 Series"]
  C6["6 Residues and Poles"]
  C7["7 Applications of Residues"]
  C8["8★ Mapping by Elementary Functions"]
  C9["9★ Conformal Mapping"]
  C10["10★ Applications of Conformal Mapping"]
  C11["11★ The Schwarz–Christoffel Transformation"]
  C12["12★ Integral Formulas of the Poisson Type"]
  X1["Single Variable Analysis (451)"]
  X2["Multivariable Analysis (452)"]
  X3["Topology (590)"]
  X4["Linear Algebra (LADR)"]
  X5["Applied Linear Algebra (235)"]
  X6["Ordinary Differential Equations (331)"]
  X7["Fourier Series and PDEs (341)"]
  X8["Calculus"]
  C1 --> C2
  C2 --> C3
  C3 --> C4
  C4 --> C5
  C4 --> C8
  C5 --> C6
  C5 --> C9
  C6 --> C7
  C7 --> C11
  C7 --> C12
  C8 --> C9
  C9 --> C10
  C10 --> C11
  C10 --> C12
  C3 -.->|on credit| C2
  C4 -.->|on credit| C1
  C4 -.->|on credit| C2
  C4 -.->|on credit| C3
  C5 -.->|on credit| C2
  C5 -.->|on credit| C4
  C6 -.->|on credit| C2
  C6 -.->|on credit| C4
  C6 -.->|on credit| C5
  C7 -.->|on credit| C4
  C7 -.->|on credit| C6
  C12 -.->|on credit| C5
  C12 -.->|on credit| C10
  C1 -.->|14| X5
  C1 -.->|3| X8
  C1 -.->|16| X4
  C1 -.->|3| X2
  C1 -.->|5| X3
  C2 -.->|4| X5
  C2 -.->|3| X8
  C2 -.->|3| X7
  C2 -.->|17| X2
  C2 -.->|13| X1
  C2 -.->|8| X3
  C3 -.->|3| X5
  C3 -.->|24| X8
  C3 -.->|3| X6
  C4 -.->|16| X8
  C4 -.->|10| X7
  C4 -.->|4| X4
  C4 -.->|5| X2
  C4 -.->|7| X1
  C4 -.->|9| X3
  C5 -.->|11| X8
  C5 -.->|4| X7
  C5 -.->|31| X1
  C6 -.->|3| X8
  C6 -.->|5| X7
  C6 -.->|3| X3
  C7 -.->|14| X7
  C7 -.->|4| X6
  C7 -.->|3| X1
  C7 -.->|7| X3
  C8 -.->|5| X3
  C9 -.->|6| X7
  C9 -.->|7| X2
  C10 -.->|8| X8
  C10 -.->|12| X7
  C10 -.->|3| X2
  C12 -.->|13| X7
  C12 -.->|4| X2
```

## Chapters
- [[· 1 Complex Numbers]]
- [[· 2 Analytic Functions]]
- [[· 3 Elementary Functions]]
- [[· 4 Integrals]]
- [[· 5 Series]]
- [[· 6 Residues and Poles]]
- [[· 7 Applications of Residues]]
- [[· 8★ Mapping by Elementary Functions]]
- [[· 9★ Conformal Mapping]]
- [[· 10★ Applications of Conformal Mapping]]
- [[· 11★ The Schwarz–Christoffel Transformation]]
- [[· 12★ Integral Formulas of the Poisson Type]]

## Central results
- [[Cauchy–Riemann Equations]] (§21.1)
- [[Sufficient Conditions for Complex Differentiability]] (§23.1)
- [[Analytic Functions Have Harmonic Components]] (§27.1)
- [[Branches of the Complex Logarithm]] (§33.1)
- [[ML-Inequality]] (§47.2)
- [[Antiderivatives and Independence of Path (complex)]] (§49.1)
- [[Cauchy–Goursat Theorem]] (§51.3)
- [[Principle of Deformation of Paths]] (§53.2)
- [[Cauchy Integral Formula]] (§54.1)
- [[Cauchy Integral Formula for Derivatives]] (§56.1)
- [[Morera's Theorem]] (§57.3)
- [[Liouville's Theorem]] (§58.1)
- [[Fundamental Theorem of Algebra (Liouville proof)]] (§58.2)
- [[Maximum Modulus Principle]] (§59.3)
- [[Taylor's Theorem for Analytic Functions]] (§63.1)
- [[Laurent's Theorem]] (§67.1)
- [[Cauchy's Residue Theorem]] (§76.1)
- [[Residues at Poles]] (§80.1)
- [[Casorati–Weierstrass Theorem]] (§84.3)
- [[Jordan's Lemma]] (§88.2)
- [[Argument Principle]] (§93.4)
- [[Rouché's Theorem]] (§94.1)
- [[Bromwich Inversion Formula]] (§95.4)
- [[Linear Fractional Transformation Through Three Points]] (§100.1)
- [[Conformal Mappings Preserve Angles]] (§112.1)
- [[Harmonic Functions Under Conformal Maps]] (§116.1)
- [[Schwarz–Christoffel Transformation]] (§128.4)

## Course record (MAT 342, Fall 2024)
Twice-weekly lectures (no lecture notes in the course folder), weekly homework (15%), quizzes (15%), midterm on Chapters 1–5 (30%), final (40%) with a reference page attached.

| Weeks | Sections | Notes |
|---|---|---|
| 1–2 | complex numbers, roots, functions, limits, continuity | §1–§18 |
| 3–4 | derivatives, Cauchy–Riemann, analytic and elementary functions | §19–§38 |
| 5–8 | contour integrals, antiderivatives, Cauchy–Goursat, Cauchy integral formula, Liouville, maximum modulus | §41–§59 |
| 10–11 | Taylor and Laurent series | §60–§68 |
| 12–13 | residues, singular points, zeros and poles | §74–§84 |
| 14 | improper integrals by residues, argument principle, Rouché | §85–§87, §93–§94 |

Examples marked *Source: 342 …* come from the homework (most of it Brown–Churchill exercises) and past finals.

## Rigorous treatment
Number of *Connections* links from these notes to each other subject: [[Calculus]] (72), [[Fourier Series and PDEs]] (67), [[Single Variable Analysis]] (58), [[Multivariable Analysis]] (42), [[Topology]] (39), [[Applied Linear Algebra]] (23), [[Linear Algebra]] (21), [[Ordinary Differential Equations]] (10), [[Differentiable Manifolds]] (2), [[Logic and Proofs]] (1), [[Functional Analysis]] (1), [[Group Theory]] (1).
