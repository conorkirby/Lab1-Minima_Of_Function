# Lab 1: Finding Minima of Functions

This repository contains the code and documentation for **Lab 1**, which focuses on finding **minima** and **roots** of functions using numerical methods. The lab explores the **bisection method** and the **Newton-Raphson method** for root-finding, as well as their application to finding equilibrium points in physical systems, such as ionic interaction potentials and charges on a ring.

## Key Concepts
- **Potential Energy and Equilibrium**: Understanding how minima of potential energy functions correspond to stable equilibrium points.
- **Root-Finding Methods**:
  - **Bisection Method**: A simple iterative method for finding roots of functions.
  - **Newton-Raphson Method**: A faster, derivative-based method for finding roots and minima.
- **Numerical Accuracy**: Exploring the trade-off between computational efficiency and accuracy in numerical solutions.

## Lab Structure

The lab is divided into three main exercises:

### 1. **Finding Roots of a Parabolic Function**
- Implement the **bisection method** to find the roots of a parabolic function.
- Plot the function and the roots, and analyze the number of steps required for convergence.
- Compare the efficiency of the bisection method with different tolerance levels.

### 2. **Newton-Raphson Method for Root-Finding**
- Implement the **Newton-Raphson method** to find the roots of a parabolic function.
- Compare the efficiency of the Newton-Raphson method with the bisection method.
- Experiment with different initial guesses and tolerance levels to understand the method's sensitivity.

### 3. **Finding Minima of a Potential Energy Function**
- Analyze the potential energy function for ionic interactions (e.g., Na⁺ and Cl⁻).
- Use the Newton-Raphson method to find the equilibrium separation (minimum of the potential energy function).
- Plot the potential energy and the corresponding force as a function of distance.

### **Supplementary Exercise: Equilibrium Positions of Charges on a Ring**
- Explore the equilibrium positions of three charges confined to a ring.
- Calculate the potential energy and forces between the charges.
- Use the Newton-Raphson method to find the equilibrium configuration.

## Repository Contents
- **Python scripts** for each exercise, including implementations of the bisection method, Newton-Raphson method, and potential energy analysis.
- **Documentation** explaining the physics and numerical methods used.
- **Plots** of functions, roots, and potential energy curves.
