# Build a Boolean Check Function

A beginner JavaScript lab completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this lab, a function is built that checks whether a given value is a boolean primitive. The function returns `true` only for the values `true` and `false`, and returns `false` for everything else — including strings like `"true"`, numbers, arrays, and objects.

## 🧠 Concepts Practiced

- Declaring and calling functions
- Using the `typeof` operator to check a value's type
- Understanding the difference between boolean primitives and other types
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
| `booWho(true)` | `true` |
| `booWho(false)` | `true` |
| `booWho(1)` | `false` |
| `booWho("true")` | `false` |
| `booWho("false")` | `false` |
| `booWho("a")` | `false` |
| `booWho(NaN)` | `false` |
| `booWho([1, 2, 3])` | `false` |
| `booWho({ "a": 1 })` | `false` |
| `booWho([].slice)` | `false` |

## 🔗 Lab Link

[freeCodeCamp - Build a Boolean Check Function](https://www.freecodecamp.org/learn/javascript-v9/#lab-boolean-check)
