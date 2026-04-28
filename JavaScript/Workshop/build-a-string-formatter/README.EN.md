# Build a String Formatter

A beginner JavaScript workshop completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this workshop, common JavaScript string formatting methods are explored. The program trims whitespace, converts case, and manually constructs a camelCase version of a word using `slice()` and `toUpperCase()`.

## 🧠 Concepts Practiced

- Using `trim()` to remove whitespace from both ends of a string
- Using `trimStart()` to remove leading whitespace
- Using `trimEnd()` to remove trailing whitespace
- Using `toUpperCase()` and `toLowerCase()` for case conversion
- Combining `slice()` and `toUpperCase()` to manually camelCase a word
- Accessing a character by index with bracket notation (`string[index]`)

## 💻 How to Run

1. Copy the code into your browser's developer console, or
2. Run it with Node.js:

```bash
node index.js
```

## 📄 Expected Output

```
Original input:
   Hello World!   
Result of trimming whitespace from both ends:
Hello World!
After using the trimStart() method, leading spaces removed:
Hello World!   
After using the trimEnd() method, trailing spaces removed:
   Hello World!
Result of using the toUpperCase() method:
HELLO WORLD!
Result of using the toLowerCase() method:
hello world!
Camel cased version:
camelCase
```

## 🗂️ Source

[freeCodeCamp - JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn)
