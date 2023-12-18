# Complex Ginzburg-Landau Equation (CGLE) Simulation

This repository contains a Jupyter Notebook (`cgle.ipynb`) that demonstrates a numerical simulation of the Complex Ginzburg-Landau Equation (CGLE), a nonlinear partial differential equation that describes a wide array of phenomena from fluid dynamics to quantum physics.

## Overview

The CGLE is an equation of great interest in the study of pattern formation and turbulence in nonlinear, nonequilibrium systems. The equation takes the form of a partial differential equation with both linear and nonlinear terms that include complex coefficients.

```math
\partial_t A = A + (1 + i\alpha) \nabla^2 A - (1 + i\beta)|A|^2 A
```

In this notebook, we present a numerical approach to solve this equation using a pseudo-spectral method and visualize the evolution of the complex field over time.

## Dependencies

To run the notebook, you will need the following:

- Python 3.x
- Matplotlib (for plotting and animation)
- NumPy (for numerical operations)

You can install these dependencies via `pip`:

`pip install matplotlib numpy`  


## Running the Simulation

To view and run the simulation:

1. Clone this repository or download `cgle.py` and `cgle.ipynb`.
2. Ensure you have Jupyter installed, or use an online platform such as Google Colab.
3. Open the notebook and execute the cells in sequence.

## Visualization

The notebook uses `matplotlib` to create snapshot plots that visualizes the dynamics of the complex field as they evolve in time according to the CGLE.