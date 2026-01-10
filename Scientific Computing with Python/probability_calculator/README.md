# Probability Calculator

This is a **Probability Calculator** project created as the final project for the **Scientific Computing with Python** certification on [freeCodeCamp](https://www.freecodecamp.org/).

## Description

The Probability Calculator allows users to calculate the probability of certain outcomes based on given events.  
It demonstrates basic Python concepts such as classes, functions, and random sampling.

## Project Features

- `Hat` class to simulate a hat containing colored balls
- `draw` method to randomly draw balls from the hat
- `experiment` function to run probability experiments and estimate outcomes
- Handles cases where the number of draws exceeds the number of items in the hat

## Technologies Used

- Python 3.x
- Standard Python libraries: `random`, `copy`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Vanitsas/probability-calculator.git
Navigate into the project directory:

bash
Kodu kopyala
cd probability-calculator
Run the main Python file:

bash
Kodu kopyala
python probability_calculator.py
Example Usage
python
Kodu kopyala
from probability_calculator import Hat, experiment

hat = Hat(blue=4, red=2, green=6)
result = experiment(hat, {"blue": 2, "red": 1}, 5, 1000)
print(result)
Project Structure
Kodu kopyala
probability-calculator/
│── probability_calculator.py
│── README.md
Author
Aygun Cerin
https://www.freecodecamp.org/ayguncerin

License
This project is for educational purposes as part of the freeCodeCamp curriculum.