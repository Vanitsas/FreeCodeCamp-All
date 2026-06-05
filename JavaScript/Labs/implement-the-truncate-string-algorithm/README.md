# Implement the Truncate String Algorithm

A beginner JavaScript lab completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this lab, a function is built that truncates a string to a given length. If the string exceeds the limit, it is cut and `...` is appended. If the string is already within the limit, it is returned unchanged.

## 🧠 Concepts Practiced

- Declaring functions with multiple parameters
- `str.length` to check string length
- `slice()` to cut a string to a specific length
- `if...else` conditional
- String concatenation to append `...`

## 💻 How to Run

1. Copy the code into your browser's developer console, or
2. Run it with Node.js:

```bash
node index.js
```

## 📄 Test Cases

| Input | Expected Output |
|-------|----------------|
| `truncateString("A-tisket a-tasket A green and yellow basket", 8)` | `A-tisket...` |
| `truncateString("Peter Piper picked a peck of pickled peppers", 11)` | `Peter Piper...` |
| `truncateString("A-", 1)` | `A...` |
| `truncateString("Absolutely Longer", 2)` | `Ab...` |
| `truncateString("A-tisket...", 43)` | `A-tisket a-tasket A green and yellow basket` |

## 🔗 Lab Link

[freeCodeCamp - Implement the Truncate String Algorithm](https://www.freecodecamp.org/learn/javascript-v9/#lab-truncate-string)
