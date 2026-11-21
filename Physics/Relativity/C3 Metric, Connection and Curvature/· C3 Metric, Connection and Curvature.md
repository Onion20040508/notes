---
type: chapter
subject: "[[Relativity]]"
level: C
chapter: C3
tags: [chapter, relativity]
---
# C3 Metric, Connection and Curvature
← [[· C2 Manifolds and Tensor Fields]] · ↑ [[Relativity]] · [[· C4 Matter in Curved Spacetime]] →

**Builds on:** [[· B1 Minkowski Spacetime and the Lorentz Group|B1 Minkowski Spacetime and the Lorentz Group]] (12), [[· B3 Relativistic Dynamics from an Action|B3 Relativistic Dynamics from an Action]] (4), [[· C1 From Special Relativity to Gravity|C1 From Special Relativity to Gravity]] (54), [[· C2 Manifolds and Tensor Fields|C2 Manifolds and Tensor Fields]] (176), [[· C4 Matter in Curved Spacetime|C4 Matter in Curved Spacetime]] (3), [[· C5 Einstein's Equations|C5 Einstein's Equations]] (3)
**Used by:** [[· B1 Minkowski Spacetime and the Lorentz Group|B1 Minkowski Spacetime and the Lorentz Group]] (1), [[· B3 Relativistic Dynamics from an Action|B3 Relativistic Dynamics from an Action]] (2), [[· B4 Fields in Special Relativity|B4 Fields in Special Relativity]] (2), [[· C1 From Special Relativity to Gravity|C1 From Special Relativity to Gravity]] (6), [[· C2 Manifolds and Tensor Fields|C2 Manifolds and Tensor Fields]] (7), [[· C4 Matter in Curved Spacetime|C4 Matter in Curved Spacetime]] (198), [[· C5 Einstein's Equations|C5 Einstein's Equations]] (207)

★ *Self-study: general relativity beyond any course taken (spine: Couzens' Oxford GR notes; textbooks d'Inverno & Vickers, Hartle, Schutz).*

**The question.** C1 showed that free fall extremizes proper time in a metric and that tidal acceleration is what remains of gravity in a freely falling frame; C2 supplied tensors on manifolds but no lengths and no derivative along a single direction. How does one measure, compare vectors at different points, and detect curvature from inside? In order: the metric (§C3.1) and its Lorentzian light cones and local inertial frames (§C3.2), the volume form and the Levi-Civita tensor (§C3.3) and the Hodge star (§C3.4), a derivative that needs extra structure — the connection (§C3.5) — and the one connection the metric singles out (§C3.6); transport along curves and geodesics, where C1's extremal proper time becomes the geodesic equation (§C3.7); normal coordinates, the equivalence principle made precise (§C3.8); curvature as the failure of transport around loops (§C3.9), its symmetries and the Bianchi identities (§C3.10), and its contractions, the Ricci and Einstein tensors (§C3.11); geodesic deviation, which identifies curvature with the tidal tensor of C1 (§C3.12); and symmetries, Killing vectors and their conserved quantities (§C3.13).

## Sections
- [[§C3.1 The Metric Tensor]] — GR1 §4.1–4.1.1; Hartle 7; Schutz 6.1
- [[§C3.2 Lorentzian Manifolds꞉ Light Cones, Proper Time, Local Inertial Frames]] — GR1 §4.1.2, §4.4.2; Schutz 6.2; Hartle 7.4
- [[§C3.3 The Volume Form and the Levi-Civita Tensor]] — GR1 §4.1.3; Hartle 7.6
- [[§C3.4 The Hodge Star and the Codifferential]] — GR1 §4.1.3, (4.31)–(4.37)
- [[§C3.5 The Covariant Derivative]] — GR1 §4.2; Schutz 5.6–5.7, 6.3
- [[§C3.6 Torsion and the Levi-Civita Connection]] — GR1 §4.3, §4.3.4; Hartle 8
- [[§C3.7 Parallel Transport and Geodesics]] — GR1 §4.4–4.4.1; Hartle 8; d'Inverno 7.6
- [[§C3.8 Normal Coordinates]] — GR1 §4.4.2; Hartle 8.8, 21
- [[§C3.9 The Riemann Tensor]] — GR1 §4.3.2–4.4.4; Schutz 6.4–6.5
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities]] — GR1 §4.5
- [[§C3.11 The Ricci and Einstein Tensors]] — GR1 §4.5.1; d'Inverno 6, 24
- [[§C3.12 Geodesic Deviation]] — GR1 §4.4.5; Hartle 21; d'Inverno 10
- [[§C3.13 Isometries and Killing Vectors]] — GR1 §6.1.1; GR2 §6.4; Hartle 8.2; d'Inverno 7.7

## Principles
- [[§C3.7 Parallel Transport and Geodesics#^pr-c3-7-5|§C3.7.5]] Free Test Bodies Follow Timelike Geodesics, Light Follows Null Geodesics

## Theorems
- [[§C3.1 The Metric Tensor#^thm-c3-1-1|§C3.1.1]] Components g_μν = g(∂_μ, ∂_ν) and Their Transformation
- [[§C3.1 The Metric Tensor#^thm-c3-1-2|§C3.1.2]] Index Gymnastics on a Manifold
- [[§C3.2 Lorentzian Manifolds꞉ Light Cones, Proper Time, Local Inertial Frames#^thm-c3-2-1|§C3.2.1]] Orthonormal Basis at a Point: g_μν(p) = η_μν
- [[§C3.2 Lorentzian Manifolds꞉ Light Cones, Proper Time, Local Inertial Frames#^thm-c3-2-2|§C3.2.2]] Local Flatness: g(p) = η and ∂g(p) = 0 Can Be Achieved, ∂∂g(p) Cannot
- [[§C3.2 Lorentzian Manifolds꞉ Light Cones, Proper Time, Local Inertial Frames#^thm-c3-2-3|§C3.2.3]] The Einstein Equivalence Principle in Geometric Form
- [[§C3.3 The Volume Form and the Levi-Civita Tensor#^thm-c3-3-1|§C3.3.1]] det g Is a Density of Weight 2; Its Sign Is Fixed by the Signature
- [[§C3.3 The Volume Form and the Levi-Civita Tensor#^thm-c3-3-2|§C3.3.2]] The Volume Form Is Chart-Independent
- [[§C3.3 The Volume Form and the Levi-Civita Tensor#^thm-c3-3-3|§C3.3.3]] Raised Levi-Civita Tensor and Contraction Identities
- [[§C3.4 The Hodge Star and the Codifferential#^thm-c3-4-1|§C3.4.1]] ⋆1 = vol, ⋆vol = s, and ⋆⋆ = s(−1)^{p(n−p)}
- [[§C3.4 The Hodge Star and the Codifferential#^thm-c3-4-2|§C3.4.2]] η ∧ ⋆ω = ⟨η, ω⟩ vol
- [[§C3.4 The Hodge Star and the Codifferential#^thm-c3-4-3|§C3.4.3]] The Codifferential: Components, Adjointness, d† = ±⋆d⋆
- [[§C3.4 The Hodge Star and the Codifferential#^thm-c3-4-4|§C3.4.4]] The Laplace–de Rham Operator on Functions
- [[§C3.5 The Covariant Derivative#^thm-c3-5-1|§C3.5.1]] Covariant Derivative of a Vector Field in Components
- [[§C3.5 The Covariant Derivative#^thm-c3-5-2|§C3.5.2]] Transformation Law of Γ: Inhomogeneous, so Γ Is Not a Tensor
- [[§C3.5 The Covariant Derivative#^thm-c3-5-3|§C3.5.3]] Difference of Two Connections Is a Tensor
- [[§C3.5 The Covariant Derivative#^thm-c3-5-4|§C3.5.4]] Extension to One-Forms and (r, s) Tensors
- [[§C3.5 The Covariant Derivative#^thm-c3-5-5|§C3.5.5]] The Covariant Derivative along a Curve Is Well Defined
- [[§C3.6 Torsion and the Levi-Civita Connection#^thm-c3-6-1|§C3.6.1]] Fundamental Theorem of Riemannian Geometry
- [[§C3.6 Torsion and the Levi-Civita Connection#^thm-c3-6-2|§C3.6.2]] Christoffel Symbols
- [[§C3.6 Torsion and the Levi-Civita Connection#^thm-c3-6-3|§C3.6.3]] The Contracted Christoffel Symbol
- [[§C3.6 Torsion and the Levi-Civita Connection#^thm-c3-6-4|§C3.6.4]] Divergence Formula and the Divergence Theorem
- [[§C3.6 Torsion and the Levi-Civita Connection#^thm-c3-6-5|§C3.6.5]] Raising and Lowering Commute with ∇
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-1|§C3.7.1]] Parallel Transport Is Linear and Preserves Inner Products
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-2|§C3.7.2]] Geodesic Equation
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-3|§C3.7.3]] Reparametrization of Geodesics
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-4|§C3.7.4]] Geodesics Are the Stationary Curves of Proper Time
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-6|§C3.7.6]] The Geodesic Lagrangian
- [[§C3.7 Parallel Transport and Geodesics#^thm-c3-7-7|§C3.7.7]] g(ẋ, ẋ) Is Conserved; Causal Character Is Preserved
- [[§C3.8 Normal Coordinates#^thm-c3-8-1|§C3.8.1]] Normal Coordinates Exist; at p They Give g = η, Γ = 0, ∂g = 0
- [[§C3.8 Normal Coordinates#^thm-c3-8-2|§C3.8.2]] The Metric to Second Order Is Fixed by the Curvature
- [[§C3.8 Normal Coordinates#^thm-c3-8-3|§C3.8.3]] Normal Coordinates Belong to a Freely Falling Observer and Are Unique up to a Lorentz Transformation
- [[§C3.9 The Riemann Tensor#^thm-c3-9-1|§C3.9.1]] The Curvature Operator Is a Tensor
- [[§C3.9 The Riemann Tensor#^thm-c3-9-2|§C3.9.2]] The Riemann Tensor in Components
- [[§C3.9 The Riemann Tensor#^thm-c3-9-3|§C3.9.3]] Ricci Identity
- [[§C3.9 The Riemann Tensor#^thm-c3-9-4|§C3.9.4]] Transport around an Infinitesimal Loop
- [[§C3.9 The Riemann Tensor#^thm-c3-9-5|§C3.9.5]] Flat if and only if the Riemann Tensor Vanishes
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities#^thm-c3-10-1|§C3.10.1]] Antisymmetries of the Riemann Tensor
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities#^thm-c3-10-2|§C3.10.2]] First Bianchi Identity
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities#^thm-c3-10-3|§C3.10.3]] Pair Symmetry
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities#^thm-c3-10-4|§C3.10.4]] Number of Independent Components
- [[§C3.10 Symmetries of the Riemann Tensor and the Bianchi Identities#^thm-c3-10-5|§C3.10.5]] Second Bianchi Identity
- [[§C3.11 The Ricci and Einstein Tensors#^thm-c3-11-1|§C3.11.1]] Ricci Is Symmetric and Is the Only Contraction
- [[§C3.11 The Ricci and Einstein Tensors#^thm-c3-11-2|§C3.11.2]] Contracted Bianchi Identity
- [[§C3.12 Geodesic Deviation#^thm-c3-12-1|§C3.12.1]] The Geodesic Deviation Equation
- [[§C3.12 Geodesic Deviation#^thm-c3-12-2|§C3.12.2]] The Newtonian Limit: the Tidal Tensor Is a Curvature Component
- [[§C3.12 Geodesic Deviation#^thm-c3-12-3|§C3.12.3]] Zero Relative Acceleration for Every Family Is Equivalent to Zero Curvature
- [[§C3.12 Geodesic Deviation#^thm-c3-12-4|§C3.12.4]] The Tide Measured by a Freely Falling Observer
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-1|§C3.13.1]] Killing's Equation
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-2|§C3.13.2]] A Killing Vector Gives a Conserved Quantity along Every Geodesic
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-3|§C3.13.3]] Killing Vectors Form a Lie Algebra
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-4|§C3.13.4]] The Second Derivatives of a Killing Vector Are Fixed by the Curvature
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-5|§C3.13.5]] At Most n(n + 1)/2 Independent Killing Vectors
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-6|§C3.13.6]] Adapted Coordinates for Stationary and Static Metrics
- [[§C3.13 Isometries and Killing Vectors#^thm-c3-13-7|§C3.13.7]] A Killing Vector Turns Local Conservation into a Conserved Total
