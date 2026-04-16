# String İnceleyici Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript atölyesidir.

## 📌 Hakkında

Bu atölyede iki temel JavaScript string metodu incelenmiştir: `includes()` ve `slice()`. Program, belirli kelimelerin bir cümlede bulunup bulunmadığını kontrol eder ve bir string'in belirli bölümlerini ayıklar.

## 🧠 Çalışılan Kavramlar

- Bir string'in alt string içerip içermediğini kontrol etmek için `includes()` kullanımı
- `includes()` metodunun büyük/küçük harf duyarlı olduğunu anlamak
- İndeks ile string'in belirli bölümlerini ayıklamak için `slice()` kullanımı
- String'in sonundan karakter almak için negatif indeks ile `slice()` kullanımı
- `const` ile değişken tanımlama
- `${}` ile template literal kullanımı

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Beklenen Çıktı

```
Here are some examples of the includes() method:
fccSentence.includes("freeCodeCamp") returns true because the word "freeCodeCamp" is in the sentence.
fccSentence.includes("JavaScript") returns false because the word "JavaScript" is not in the sentence.
fccSentence.includes("freecodecamp") returns false because includes is case-sensitive.
Here are some examples of the slice() method:
The word "freeCodeCamp" was sliced from the message.
The first word is "Welcome".
The ending punctuation mark is a "!"
Workshop complete! You now know how to use includes() and slice().
```

## 🗂️ Kaynak

[freeCodeCamp - JavaScript Algoritmaları ve Veri Yapıları](https://www.freecodecamp.org/learn)
