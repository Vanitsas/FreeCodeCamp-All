# Teacher Chatbot Oluşturma

FreeCodeCamp workshop projesi, **JavaScript stringlerini** pratik etmek için.

## Genel Bakış
- Botu tanıtır.
- String uzunluğu ve karakter erişimini gösterir.
- `indexOf()` ile alt string konumlarını bulur.

## Örnek Kod

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
console.log(sentence.indexOf("learning")); // -1, büyük/küçük harf duyarlı

console.log("I hope you enjoyed learning today.");

Öğrenilen Konular
Template literals ${}
String .length
Karakterlere erişim [index]
indexOf() ve büyük/küçük harf duyarlılığı