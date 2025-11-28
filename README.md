<!-- @format -->

# ChaosToCode - Computational Engineering Playground

Welcome to my personal laboratory for computational exploration! This repository serves as a digital sandbox where theoretical concepts from my engineering courses come to life through code. Each project represents a journey from mathematical equations on paper to working simulations and solvers.

## 🎯 Philosophy

Learning engineering isn't just about solving problems on paper—it's about understanding the phenomena deeply enough to model and simulate them. This repository documents my process of:

- Translating course concepts into computational models
- Bridging the gap between theory and implementation
- Building intuition through visualization and simulation
- Creating reusable tools for engineering analysis

## 📚 Projects Overview

### 01_Damped_Oscillation

**Course:** PH1010 (Physics)

A comprehensive exploration of harmonic oscillators, from simple to damped systems. This project implements numerical solutions to second-order differential equations governing oscillatory motion.

**Key Features:**

- Simple harmonic oscillator simulation
- Damped oscillation with variable damping coefficients (ζ)
- External forcing functions (including sinusoidal drives)
- Symbolic and numerical solving using SymPy and NumPy
- Visualization of different damping regimes (underdamped, critically damped, overdamped)

**Mathematical Foundation:** Solves the general equation: `ẍ + 2ζωₙẋ + ωₙ²x = F(t)`

---
### 02_Gravity

**Course:** PH1010 (Physics)

A simulation framework exploring gravitational interactions between celestial bodies. While currently focused on the classic Two-Body Problem, the architecture is designed to scale toward complex N-body simulations.

**Key Features:**

- **Center of Mass Reference Frame:** Simplifies calculations by analyzing motion relative to the system's barycenter.
- **Dynamic Initialization:** Calculates the state vectors (position and velocity) of the second body automatically based on the inputs of the first to ensure system stability.
- **High-Precision Integration:** Utilizes the Runge-Kutta 4th Order (RK4) method for accurate numerical integration of orbital mechanics.
- **Visualization Modes:**
    - *Decaying Trail:* Aesthetic visualization for presentation.
    - *Persistent Trail:* Full path tracking for scientific analysis.
    - *No Trail:* Performance-focused rendering.

**Ongoing Development:** Future plans include expanding the solver to handle the chaotic Three-Body Problem in collaboration with a team.

*> **Note:** The original Jupyter notebook for this project is currently unavailable; the implementation resides in the Python scripts.*

---

### 03_EE1100_ElectricCircuitSolver

**Course:** EE1100 (Basic Electrical Engineering)

A growing toolkit for analyzing electrical circuits using computational methods. Currently implements nodal analysis for resistive networks, with plans to expand as I progress through the course.

**Key Features:**

- Nodal analysis using conductance matrix formulation
- Kirchhoff's Current Law (KCL) and Voltage Law (KVL) implementation
- Matrix-based circuit solving: `[G]v = I`
- Interactive Jupyter notebooks for learning and documentation

**Ongoing Development:** This codebase evolves alongside my coursework, adding features like capacitor/inductor analysis, AC circuits, and more complex network theorems.

---

### 04_AM2530_Fluid_Sims

**Course:** AM2530 (Fluid Mechanics)

Numerical simulations exploring fluid dynamics principles, with a focus on fundamental theorems and their computational implementation.

**Projects:**

- **Reynolds Transport Theorem Simulator:** An interactive visualization tool (planned in Pygame) to understand the relationship between system and control volume formulations. Aims to demonstrate mass conservation through particle-based simulation.
- **Line Visualization:** Preliminary work on flow field representation and streamline plotting.

**Mathematical Foundation:** Implements the Reynolds Transport Theorem and its connection to differential forms (leading toward Navier-Stokes equations).

---

### 05_ME2201_Machines

**Course:** ME2201 (Mechanisms and Machines)

Computational tools for analyzing and synthesizing mechanical systems, focusing on kinematics and dynamics of machine elements.

**Sub-Projects:**

#### 01_Cam_Follower_Synthesis

Design and analysis tool for cam-follower mechanisms with different follower types.

**Features:**

- Polynomial motion profiles (3-4-5 polynomial, cycloidal, etc.)
- Flat-face follower design calculations
- Minimum base circle radius determination: `rb ≥ ρmin - [y(θ) + y''(θ)]min`
- Follower width optimization
- Displacement, velocity, and acceleration profile generation

#### 02_Analytical_Analysis

Tools for kinematic and dynamic analysis of linkages and mechanisms, including position, velocity, and acceleration analysis using both symbolic (SymPy) and numerical (SciPy) methods.

---

## 🛠️ Tech Stack

- **Python 3.x** - Primary language
- **NumPy** - Numerical computations
- **SymPy** - Symbolic mathematics and equation solving
- **SciPy** - Advanced numerical methods
- **Matplotlib** - Data visualization and plotting
- **Jupyter Notebooks** - Interactive development and documentation

## 📖 Documentation Style

Each project folder contains:

- **Notebooks (`.ipynb`)** - Interactive code with theory and visualizations
- **Python scripts (`.py`)** - Standalone implementations
- **Markdown files (`.md`)** - Theory notes, derivations, and logs

I believe in literate programming—code should tell a story, not just execute instructions.

## 🎓 Learning Approach

1. **Understand the Theory** - Derive equations and understand physical principles
2. **Model Mathematically** - Set up governing equations and boundary conditions
3. **Implement Computationally** - Translate math into code
4. **Visualize & Validate** - Plot results and verify against known solutions
5. **Iterate & Extend** - Add features and explore edge cases

## 📝 Note

This is a learning repository—code may be experimental, documentation might be in-progress, and implementations could be pedagogical rather than production-ready. The goal is understanding, not perfection.

---

**"From chaos of equations to clarity of code"** ✨
