# Build a Leap Year Calculator

A beginner JavaScript lab completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this lab, a function is built that determines whether a given year is a leap year. The function applies the standard leap year rules: divisible by 4, except for century years — unless also divisible by 400.

**Leap Year Rules:**
- Divisible by `4` → leap year
- Divisible by `100` → NOT a leap year
- Divisible by `400` → leap year (overrides the 100 rule)

## 🧠 Concepts Practiced

- Declaring and calling functions
- Modulo operator (`%`) to check divisibility
- Combining conditions with logical AND (`&&`) and OR (`||`)
- `if...else` conditional
- String concatenation for the return message

## 💻 How to Run

1. Copy the code into your browser's developer console, or
2. Run it with Node.js:

```bash
node index.js
```

## 📄 Test Cases

| Input | Expected Output |
|-------|----------------|
| `isLeapYear(2024)` | `2024 is a leap year.` |
| `isLeapYear(2000)` | `2000 is a leap year.` |
| `isLeapYear(1900)` | `1900 is not a leap year.` |

## 🔗 Lab Link

[freeCodeCamp - Build a Leap Year Calculator](https://www.freecodecamp.org/learn/javascript-v9/#lab-leap-year-calculator)
