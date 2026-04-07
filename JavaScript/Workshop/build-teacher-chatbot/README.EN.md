# Build a Teacher Chatbot

Simple FreeCodeCamp workshop project to practice **JavaScript strings**.

## Overview
- Introduces the bot.
- Demonstrates string length and character access.
- Shows substring positions with `indexOf()`.

## Key Code Examples

```javascript
const botName = "teacherBot";
console.log(`My name is ${botName}.`);

const subject = "JavaScript";
const topic = "strings";
console.log(`Today, you will learn about ${topic} in ${subject}.`);

console.log(subject.length);
console.log(subject[0], subject[1], subject[subject.length - 1]);

const sentence = "Learning is fun.";
console.log(sentence.indexOf("Learning"));
console.log(sentence.indexOf("fun"));
console.log(sentence.indexOf("learning")); // -1, case-sensitive

console.log("I hope you enjoyed learning today.");

Concepts Learned
Template literals ${}
String .length
Accessing characters [index]
indexOf() and case-sensitivity