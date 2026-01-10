# Python Vector Classes (R2Vector & R3Vector) 📐
This is my solution for the FreeCodeCamp Scientific Computing with Python project: Python Vector Classes.

## 🎯 Objective
Demonstrate object-oriented programming (OOP) concepts in Python using vectors, including special methods, operator overloading, inheritance, and dynamic attribute handling.

## ✅ Example Usage
```python
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

# Vector operations
v3 = v1 + v2          # addition
v4 = v1 - v2          # subtraction
dot = v1 * v2         # dot product
cross = v1.cross(v2)  # cross product

# Print results
print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v1 + v2 = {v3}')
print(f'v1 - v2 = {v4}')
print(f'v1 * v2 = {dot}')
print(f'v1 x v2 = {cross}')

Features
Special methods (__init__, __str__, __repr__, __add__, __sub__, __mul__, __eq__, __lt__, __gt__, __le__, __ge__)
Operator overloading for addition, subtraction, scalar multiplication, dot product, and cross product
Inheritance from R2Vector to R3Vector
Dynamic attribute access using vars() and getattr()
Implementation of vector operations for any number of dimensions

FreeCodeCamp link
Learn Special Methods by Building a Vector Space