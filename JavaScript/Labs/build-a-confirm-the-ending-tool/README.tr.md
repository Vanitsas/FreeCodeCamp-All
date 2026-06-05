# String Sonu Doğrulama Aracı Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript laboratuvar çalışmasıdır.

## 📌 Hakkında

Bu laboratuvarda bir string'in belirli bir hedef string ile bitip bitmediğini kontrol eden bir fonksiyon oluşturulmuştur — yerleşik `.endsWith()` metodu kullanılmadan. Çözüm, string'in sonundan karakter almak için negatif indeksli `slice()` kullanır ve sonucu hedefle karşılaştırır.

## 🧠 Çalışılan Kavramlar

- Birden fazla parametreli fonksiyon tanımlama
- String'in sonundan karakter almak için negatif indeksli `slice()` kullanımı
- Kaç karakter kesileceğini dinamik olarak belirlemek için `target.length` kullanımı
- String karşılaştırması için katı eşitlik operatörü (`===`)
- Karşılaştırma sonucunu doğrudan fonksiyondan döndürme

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Test Durumları

| Girdi | Beklenen Çıktı |
|-------|----------------|
| `confirmEnding("Bastian", "n")` | `true` |
| `confirmEnding("Congratulation", "on")` | `true` |
| `confirmEnding("Abstraction", "action")` | `true` |
| `confirmEnding("Connor", "n")` | `false` |
| `confirmEnding("Open sesame", "sage")` | `false` |
| `confirmEnding("Open sesame", "game")` | `false` |

## 🔗 Lab Linki

[freeCodeCamp - Build a Confirm the Ending Tool](https://www.freecodecamp.org/learn/javascript-v9/#lab-string-ending-checker)
