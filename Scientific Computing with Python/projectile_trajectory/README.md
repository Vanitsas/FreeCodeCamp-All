# Projectile Trajectory Calculator

This project is a **Python-based projectile motion calculator** that demonstrates **encapsulation** and **object-oriented programming (OOP)** concepts.

---

## Features

- **Encapsulation:** Speed (`speed`), height (`height`), and angle (`angle`) are stored as private attributes.  
- **Getters and Setters:** Access and modify attributes safely.  
- **Physics Calculations:**  
  - Horizontal displacement  
  - Y-coordinate for each x  
  - Full list of coordinates  
- **ASCII Graph:** Visualizes the projectile trajectory with X and Y axes.  
- **Coordinate Table:** Displays all coordinates in a readable table.  
- **Helper Function:** Use `projectile_helper(speed, height, angle)` to generate all outputs easily.

---

## Usage

```python
from projectile import projectile_helper

# Example: speed=10 m/s, height=3 m, angle=45°
projectile_helper(10, 3, 45)

Output includes:

1. Projectile details (speed, height, angle, displacement)
2. Coordinate table
3. ASCII trajectory graph

Installation

1. Make sure Python 3.x is installed.
2. Download projectile.py.
3. Run the script from terminal or an IDE:

python projectile.py

Example Output
Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 12.6 m

  x      y
  0   3.00
  1   3.90
  2   4.61
  3   5.12
  4   5.43
  5   5.55
  6   5.47
  7   5.19
  8   4.72
  9   4.05
 10   3.19
 11   2.13
 12   0.87

⊣     ∙       
⊣  ∙∙∙ ∙∙∙    
⊣ ∙       ∙   
⊣∙         ∙  
⊣           ∙ 
⊣            ∙
⊣             
 TTTTTTTTTTTTT

License
MIT License


