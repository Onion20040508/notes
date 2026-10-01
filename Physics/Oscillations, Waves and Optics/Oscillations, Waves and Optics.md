---
type: subject
discipline: physics
courses: ["PHY 287 (UMass, M. Kandula, Fall 2023)", "PHY 300 (Stony Brook, L. Mihaly, Fall 2024)"]
textbooks: ["OpenStax, University Physics Vol. 1 and 3", "French, Vibrations and Waves", "Fowles, Introduction to Modern Optics", "Schwartz, Physics 15c Waves lectures"]
conventions: "[[University Physics]]"
status: level A in progress
tags: [subject, oscillations-waves-and-optics]
---
# Oscillations, Waves and Optics

Oscillators, mechanical and sound waves, and light as a wave and as rays, in three levels: **A** introductory (University Physics Vol. 1 ch. 15–17 and Vol. 3 ch. 1–4; PHY 287), **B** upper-level (PHY 300; French; Fowles; Schwartz's Physics 15c lectures; the series Part I), **C** graduate. Statements are marked by layer: *principles* (assumed), *laws* (empirical, with their range), *theorems* (derived, with a derivation and a *Uses:* line) and *models* (idealisations). The mechanics it uses is in [[Classical Mechanics]]; electromagnetic waves themselves are in [[Electromagnetism]].

## Level A — introductory
- [[· A1 Oscillations]]
- [[· A2 Mechanical Waves]]
- [[· A3 Sound]]
- [[· A4 The Nature of Light]]
- [[· A5 Geometric Optics and Image Formation]]
- [[· A6 Interference]]
- [[· A7 Diffraction]]

## Level B — upper
- [[· B1 Damped and Driven Oscillators]]
- [[· B2 Coupled Oscillators and Normal Modes]]
- [[· B3 From the Bead Chain to the Wave Equation]]
- [[· B4 Fourier Analysis and Strings]]
- [[· B5 Travelling Waves, Energy and Impedance]]
- [[· B6 Wave Packets and Dispersion]]
- [[· B7 Waves in Two and Three Dimensions]]

### How the chapters build on each other
Arrows point from a chapter to the chapters that use it; labels count the citations from statements, derivations and *Uses:* lines. Dashed arrows are forward references.

```mermaid
graph TD
  A1["A1 Oscillations"]
  A2["A2 Mechanical Waves"]
  A3["A3 Sound"]
  A4["A4 The Nature of Light"]
  A5["A5 Geometric Optics and Image Formation"]
  A6["A6 Interference"]
  A7["A7 Diffraction"]
  B1["B1 Damped and Driven Oscillators"]
  B2["B2 Coupled Oscillators and Normal Modes"]
  B3["B3 From the Bead Chain to the Wave Equation"]
  B4["B4 Fourier Analysis and Strings"]
  B5["B5 Travelling Waves, Energy and Impedance"]
  B6["B6 Wave Packets and Dispersion"]
  B7["B7 Waves in Two and Three Dimensions"]
  A1 -->|2| A2
  A2 -->|18| A3
  A2 -->|2| A4
  A4 -->|9| A5
  A1 -->|5| A6
  A2 -->|6| A6
  A4 -->|5| A6
  A1 -->|2| A7
  A2 -->|1| A7
  A4 -->|5| A7
  A5 -->|1| A7
  A6 -->|20| A7
  A1 -->|26| B1
  A1 -->|11| B2
  A3 -->|2| B2
  B1 -->|6| B2
  A2 -->|15| B3
  B1 -->|2| B3
  B2 -->|11| B3
  A1 -->|7| B4
  A2 -->|7| B4
  A3 -->|8| B4
  B1 -->|2| B4
  B2 -->|1| B4
  B3 -->|7| B4
  A1 -->|3| B5
  A2 -->|6| B5
  A3 -->|4| B5
  B1 -->|7| B5
  B3 -->|8| B5
  B4 -->|1| B5
  A1 -->|1| B6
  A4 -->|1| B6
  B1 -->|3| B6
  B3 -->|8| B6
  B4 -->|10| B6
  B5 -->|2| B6
  A2 -->|5| B7
  A3 -->|3| B7
  B1 -->|1| B7
  B3 -->|4| B7
  B4 -->|9| B7
  A7 -.->|1| A6
  B4 -.->|1| B3
  B5 -.->|2| B4
  B6 -.->|1| B4
```

## Planned
Chapters without notes yet; sources in brackets (∅ = no typed source).

**Level B — upper (PHY 300; French; Fowles; Schwartz Physics 15c lectures; the series Part I)**
B1 Damped and driven oscillators, resonance [S-I §2–5; Schwartz 1–2] · B2 Coupled oscillators and normal modes [S-I §6–7; Schwartz 3] · B3 N-chain, continuum limit, wave equation [S-I §8–9; Schwartz 4] · B4 Fourier series and transforms, strings [Schwartz 5, 7–8] · B5 Travelling waves: energy, impedance, reflection [Schwartz 6, 9–10] · B6 Wavepackets and dispersion [Schwartz 11] · B7 Waves in 2D and 3D [S-I §10] · B8 Polarization and Jones calculus [Schwartz 14; Fowles 2] · B9 Fresnel equations, total internal reflection [Schwartz 15; Fowles 2] · B10 Interferometry and coherence [Fowles 3–4] · B11 Fraunhofer and Fresnel diffraction, resolution [Schwartz 19; Fowles 5] · B12 Matrix ray optics [Fowles 10] · B13 Optics of materials, colour [Schwartz 16–17; Fowles 6]
PHY 300's lectures are handwritten scans; level B is planned from the typed sources above.

**Level C — graduate**
C1 Fourier optics and scalar diffraction theory [∅] · C2 Lasers and Gaussian beams [Fowles 9] · C3 Statistical optics [∅] · C4 Waveguides and fibres [∅] · C5 Nonlinear optics [∅]
