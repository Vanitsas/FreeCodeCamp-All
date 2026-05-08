# Mathbot Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript atölyesidir.

## 📌 Hakkında

Bu atölyede en sık kullanılan JavaScript `Math` nesnesi metodlarını tanıtan bir matematik öğretim botu oluşturulmuştur. Bot; rastgele sayı üretme, yuvarlama ve maksimum/minimum değer bulma konularını adım adım anlatır.

## 🧠 Çalışılan Kavramlar

- `Math.random()` — 0 ile 1 arasında sahte rastgele sayı üretir
- `Math.random()` kullanarak özel bir aralıkta rastgele sayı üretme
- `Math.floor()` — sayıyı en yakın tam sayıya aşağı yuvarlar
- `Math.floor()` + `Math.random()` kombinasyonu ile aralıkta rastgele tam sayı üretme
- `Math.ceil()` — sayıyı en yakın tam sayıya yukarı yuvarlar
- `Math.round()` — sayıyı en yakın tam sayıya yuvarlar
- `Math.max()` — bir kümedeki en büyük değeri döndürür
- `Math.min()` — bir kümedeki en küçük değeri döndürür
- `${}` ile template literal kullanımı

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Beklenen Çıktı

```
Hi there! My name is MathBot and I am here to teach you about the Math object!
The Math.random() method returns a pseudo random number greater than or equal to 0 and less than 1.
[0 ile 1 arasında rastgele sayı]
Now, generate a random number between two values.
[1 ile 100 arasında rastgele sayı]
The Math.floor() method rounds the value down to the nearest whole integer.
6
Now, generate a random integer between two values.
[1 ile 100 arasında rastgele tam sayı]
The Math.ceil() method rounds the value up to the nearest whole integer.
4
The Math.round() method rounds the value to the nearest whole integer.
3
11
The Math.max() and Math.min() methods are used to get the maximum and minimum number from a range.
125
2
It was fun learning about the different Math methods with you!
```

## 🗂️ Kaynak

[freeCodeCamp - JavaScript Algoritmaları ve Veri Yapıları](https://www.freecodecamp.org/learn)
