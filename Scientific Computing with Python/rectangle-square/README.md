# Rectangle and Square Python Project

This project is a **FreeCodeCamp Python project** that focuses on creating **Rectangle and Square classes**. The goal is to practice **object-oriented programming (OOP)** by designing and testing these shape classes.

## Project Features

- `Rectangle` and `Square` classes are implemented.
- `Square` is a subclass of `Rectangle`.
- Both classes include the following methods:
  - `get_area()` → Calculates the area
  - `get_perimeter()` → Calculates the perimeter
  - `get_diagonal()` → Calculates the diagonal length
  - `get_picture()` → Returns a string representation of the shape using stars
  - `get_amount_inside(other_shape)` → Returns how many times one shape fits inside another
- The `Square` class includes a `set_side()` method to change its side length.
- `Square` also overrides `set_width()` and `set_height()` to maintain its square shape.

## Example Usage

```python
from rectangle_square import Rectangle, Square

# Rectangle
r = Rectangle(3, 6)
print(r)                    # Rectangle(width=3, height=6)
print(r.get_area())          # 18
print(r.get_perimeter())     # 18
print(r.get_diagonal())      # 6.708203932499369
print(r.get_picture())

# Square
s = Square(5)
print(s)                    # Square(side=5)
print(s.get_area())          # 25
print(s.get_perimeter())     # 20
print(s.get_diagonal())      # 7.0710678118654755
print(s.get_picture())

## Installation

Python 3 must be installed.  
To run the code, execute in the terminal or IDE:

```bash
python rectangle_square.py
```

## Contribution
Since this is a FreeCodeCamp Python project, contributions and improvements are welcome.