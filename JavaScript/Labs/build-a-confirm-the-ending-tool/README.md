# Build a Confirm the Ending Tool

A beginner JavaScript lab completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this lab, a function is built that checks whether a string ends with a given target string — without using the built-in `.endsWith()` method. The solution uses `slice()` with a negative index to extract the end of the string and compares it to the target.

## 🧠 Concepts Practiced

- Declaring functions with multiple parameters
- `slice()` with a negative index to extract characters from the end of a string
- `target.length` to dynamically determine how many characters to slice
- Strict equality (`===`) to compare strings
- Returning the result of a comparison directly from a function

## 💻 How to Run

1. Copy the code into your browser's developer console, or
2. Run it with Node.js:

```bash
node index.js
```

## 📄 Test Cases

| Input | Expected Output |
|-------|----------------|
| `confirmEnding("Bastian", "n")` | `true` |
| `confirmEnding("Congratulation", "on")` | `true` |
| `confirmEnding("Abstraction", "action")` | `true` |
| `confirmEnding("Connor", "n")` | `false` |
| `confirmEnding("Open sesame", "sage")` | `false` |
| `confirmEnding("Open sesame", "game")` | `false` |

## 🔗 Lab Link

[freeCodeCamp - Build a Confirm the Ending Tool](https://www.freecodecamp.org/learn/javascript-v9/#lab-string-ending-checker)
