---
type: subject
discipline: math
course: MATH 590
term: Winter 2026
instructor: Linh Truong
textbook: "Munkres, Topology, 2nd ed."
status: completed
aliases: ["MATH 590", "Point-Set Topology", "Introduction to Topology"]
tags: [subject, topology]
---
# Topology

MATH 590 (Winter 2026, Linh Truong), following Munkres, *Topology* (2nd ed.). Section numbers §1–§40 are the notes' own. Each section note's `munkres` property gives the matching Munkres section. LaTeX source: `tex/math590_topology_notes.tex`.

## How the chapters build on each other
Solid arrows: a chapter's proofs rely on the earlier chapter (arrows implied by others are omitted; exact counts are in each chapter note). Dashed arrows: results used *on credit* before they are proved in the course.

```mermaid
graph TD
  subgraph P1["Part I: General Topology"]
    C1["1 Topological Spaces and Constructions"]
    C2["2 Closedness, Continuity, and Hausdorff"]
    C3["3 Products, Metrics, and Quotients"]
    C4["4 Connectedness"]
    C5["5 Compactness"]
    C6["6 Countability and Separation"]
  end
  subgraph P2["Part II: Algebraic Topology"]
    C7["7 Algebraic Foundations"]
    C8["8 Homotopy and the Fundamental Group"]
    C9["9 Covering Spaces and Lifting"]
    C10["10 Applications of π₁"]
    C11["11 Computing π₁"]
  end
  C1 --> C2
  C2 --> C3
  C3 --> C4
  C4 --> C5
  C4 --> C8
  C5 --> C6
  C5 --> C9
  C7 --> C8
  C8 --> C9
  C9 --> C10
  C10 --> C11
  C5 -.->|on credit| C3
  C8 -.->|on credit| C2
  C9 -.->|on credit| C2
  C9 -.->|on credit| C8
  C11 -.->|on credit| C10
```

## Chapters
**Part I: General Topology**
- [[· 1 Topological Spaces and Constructions]]
- [[· 2 Closedness, Continuity, and Hausdorff]]
- [[· 3 Products, Metrics, and Quotients]]
- [[· 4 Connectedness]]
- [[· 5 Compactness]]
- [[· 6 Countability and Separation]]

**Part II: Algebraic Topology**
- [[· 7 Algebraic Foundations]]
- [[· 8 Homotopy and the Fundamental Group]]
- [[· 9 Covering Spaces and Lifting]]
- [[· 10 Applications of π₁]]
- [[· 11 Computing π₁]]

## Summary
- [[Algebraic Topology Toolkit]]: the four tools for computing π₁, a decision tree, and a table of computed fundamental groups.

## Prerequisites from other subjects
The results from other subjects that this course's proofs and definitions cite (with the number of citing items). Most connections to MATH 451 and Linear Algebra are conceptual and live in the Connections callouts rather than in proofs; each chapter note gives per-chapter counts.

**[[Single Variable Analysis]]**
- [[Extreme Value Theorem]] (1)
- [[§13 Some Topological Concepts in Metric Spaces#^def-13-new1|Definition §13.2: Cauchy Sequence in a Metric Space]] (1)
- [[§4 The Completeness Axiom#^thm-4-7|Theorem §4.7: Density of ℚ in ℝ]] (1)

**[[Linear Algebra]]**
- [[§5 Bases#^ladr-2-26|2.26 Basis]] (1)

**[[Group Theory]]**
- [[First Isomorphism Theorem for Groups]] (2)

## Workhorse examples
- [[Lower limit topology]]
- [[K-topology]]
- [[Box and product topologies on ℝ^ω]]
- [[Discrete and indiscrete topologies]]
- [[Punctured plane]]
- [[Figure eight]]
- [[Torus]]
- [[Double torus]]
- [[Projective plane]]
