# Build a Card Counting Assistant

A beginner JavaScript lab completed as part of the [freeCodeCamp](https://www.freecodecamp.org/) curriculum.

## 📌 About

In this lab, a card counting assistant for the casino game Blackjack is built. The function tracks a global count based on the cards played and advises the player to either **Bet** (count is positive) or **Hold** (count is zero or negative).

**Counting Rules:**
| Cards | Effect on Count |
|-------|----------------|
| 2, 3, 4, 5, 6 | `+1` |
| 7, 8, 9 | No change |
| 10, J, Q, K, A | `-1` |

## 🧠 Concepts Practiced

- Declaring a global variable with `let`
- Modifying a global variable inside a function
- `if...else if` conditional chains
- Comparison operators and logical OR (`||`)
- Returning a formatted string based on a condition

## 💻 How to Run

1. Copy the code into your browser's developer console, or
2. Run it with Node.js:

```bash
node index.js
```

## 📄 Test Cases

| Cards Played | Last Call | Expected Output |
|--------------|-----------|----------------|
| 2, 3, 4, 5, 6 | `cardCounter(6)` | `5 Bet` |
| 7, 8, 9 | `cardCounter(9)` | `0 Hold` |
| 10, J, Q, K, A | `cardCounter("A")` | `-5 Hold` |
| 3, 7, Q, 8, A | `cardCounter("A")` | `-1 Hold` |
| 2, J, 9, 2, 7 | `cardCounter(7)` | `1 Bet` |
| 2, 2, 10 | `cardCounter(10)` | `1 Bet` |
| 3, 2, A, 10, K | `cardCounter("K")` | `-1 Hold` |

## 🔗 Lab Link

[freeCodeCamp - Build a Card Counting Assistant](https://www.freecodecamp.org/learn/javascript-v9/#lab-counting-cards)
