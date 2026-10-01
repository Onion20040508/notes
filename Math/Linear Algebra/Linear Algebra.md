---
type: subject
discipline: math
source: "Sheldon Axler, Linear Algebra Done Right, 4th ed. (Springer 2024)"
aliases: ["LADR", "Axler LADR", "Linear Algebra Done Right"]
tags: [subject, linear-algebra]
---
# Linear Algebra

Built on Axler, *Linear Algebra Done Right*, 4th edition (Springer, 2024), open access under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Statements and proofs in these notes are written in my own words following Axler's numbering and proof routes; item numbers and titles are Axler's. PDF: `refs/Axler LADR.pdf` (from https://linear.axler.net).

## How the chapters build on each other
Arrows show which chapters a chapter's proofs rely on (redundant arrows implied by others are omitted; exact counts are in each chapter note).

```mermaid
graph TD
  C1["1 Vector Spaces"]
  C2["2 Finite-Dimensional Vector Spaces"]
  C3["3 Linear Maps"]
  C4["4 Polynomials"]
  C5["5 Eigenvalues and Eigenvectors"]
  C6["6 Inner Product Spaces"]
  C7["7 Operators on Inner Product Spaces"]
  C8["8 Operators on Complex Vector Spaces"]
  C9["9 Multilinear Algebra and Determinants"]
  C1 --> C2
  C2 --> C3
  C2 --> C4
  C3 --> C5
  C4 --> C5
  C5 --> C6
  C6 --> C7
  C7 --> C8
  C8 --> C9
```

## Chapters
- [[· 1 Vector Spaces]]
- [[· 2 Finite-Dimensional Vector Spaces]]
- [[· 3 Linear Maps]]
- [[· 4 Polynomials]]
- [[· 5 Eigenvalues and Eigenvectors]]
- [[· 6 Inner Product Spaces]]
- [[· 7 Operators on Inner Product Spaces]]
- [[· 8 Operators on Complex Vector Spaces]]
- [[· 9 Multilinear Algebra and Determinants]]
