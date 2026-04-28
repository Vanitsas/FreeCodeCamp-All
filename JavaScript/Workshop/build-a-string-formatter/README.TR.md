# String Biçimlendirici Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript atölyesidir.

## 📌 Hakkında

Bu atölyede yaygın JavaScript string biçimlendirme metodları incelenmiştir. Program boşlukları temizler, büyük/küçük harf dönüşümü yapar ve `slice()` ile `toUpperCase()` kullanarak bir kelimenin camelCase versiyonunu manuel olarak oluşturur.

## 🧠 Çalışılan Kavramlar

- String'in her iki ucundaki boşlukları kaldırmak için `trim()` kullanımı
- Baştaki boşlukları kaldırmak için `trimStart()` kullanımı
- Sondaki boşlukları kaldırmak için `trimEnd()` kullanımı
- Büyük/küçük harf dönüşümü için `toUpperCase()` ve `toLowerCase()` kullanımı
- Bir kelimeyi manuel olarak camelCase yapmak için `slice()` ve `toUpperCase()` kombinasyonu
- Köşeli parantez notasyonu ile karaktere indeksle erişim (`string[index]`)

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Beklenen Çıktı

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

## 🗂️ Kaynak

[freeCodeCamp - JavaScript Algoritmaları ve Veri Yapıları](https://www.freecodecamp.org/learn)
