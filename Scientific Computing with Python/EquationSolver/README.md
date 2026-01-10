# EquationSolver

This project allows you to solve and analyze **LinearEquation** and **QuadraticEquation** objects.

## Features

- Solve linear and quadratic equations.
- Display solutions and detailed analysis of the equation in a formatted output.
- Show the vertex, minimum/maximum, and concavity of parabolas.
- All outputs are aligned and easy to read.

## Usage

1. Navigate to the folder containing the code and run it from the terminal:

```bash
python solver.py
Or import and use the classes and solver function:

python
Kodu kopyala
from solver import LinearEquation, QuadraticEquation, solver

# Linear equation example
lin_eq = LinearEquation(2, 3)
print(solver(lin_eq))

# Quadratic equation example
quadr_eq = QuadraticEquation(1, 2, 1)
print(solver(quadr_eq))
Output Examples
Linear Equation

markdown
Kodu kopyala
----Linear Equation-----

       2x +3 = 0         

-------Solutions--------

       x = -1.500       

--------Details---------

slope =        2.000
y-intercept =  3.000
Quadratic Equation

markdown
Kodu kopyala
---Quadratic Equation---

    x**2 +2x +1 = 0     

-------Solutions--------

       x = -1.000       

--------Details---------

concavity =      upwards
min =    (-1.000, 0.000)
Requirements
Python 3.10 or higher (required for pattern matching)