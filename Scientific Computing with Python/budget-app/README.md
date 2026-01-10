# Budget App

A simple Python application to manage budgets by category and visualize spending. This project was completed as part of the **FreeCodeCamp Python Certification**.

## Features

- Create budget categories such as Food, Clothing, and Entertainment.
- Deposit and withdraw funds in each category.
- Transfer funds between categories.
- Display the current balance of each category.
- Generate a text-based bar chart showing percentage of spending per category.

## Usage

```python
from budget import Category, create_spend_chart

# Create categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Add deposits and withdrawals
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and dessert")
clothing.deposit(500, "initial deposit")
clothing.withdraw(50, "shirts")
auto.deposit(1000, "initial deposit")
auto.withdraw(100, "car repair")

# Transfer between categories
food.transfer(50, clothing)

# Print category ledger
print(food)
print(clothing)
print(auto)

# Create spending chart
print(create_spend_chart([food, clothing, auto]))

Example Output

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

Project Notes

Designed to be simple and readable.

Focused on string formatting, list handling, loops, and basic math operations.

The create_spend_chart function produces a text-based bar chart with exact spacing for FreeCodeCamp tests.

Author

Aygün Çerin
Completed as part of FreeCodeCamp Python Certification projects.