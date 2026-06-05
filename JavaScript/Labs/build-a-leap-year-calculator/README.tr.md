# Artık Yıl Hesaplayıcısı Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript laboratuvar çalışmasıdır.

## 📌 Hakkında

Bu laboratuvarda verilen bir yılın artık yıl olup olmadığını belirleyen bir fonksiyon oluşturulmuştur. Fonksiyon standart artık yıl kurallarını uygular: 4'e bölünebilir olmalı, ancak yüzyıl yılları hariç — 400'e de bölünebiliyorsa artık yıldır.

**Artık Yıl Kuralları:**
- `4`'e bölünebiliyorsa → artık yıl
- `100`'e bölünebiliyorsa → artık yıl DEĞİL
- `400`'e bölünebiliyorsa → artık yıl (100 kuralını geçersiz kılar)

## 🧠 Çalışılan Kavramlar

- Fonksiyon tanımlama ve çağırma
- Bölünebilirliği kontrol etmek için modulo operatörü (`%`)
- Mantıksal VE (`&&`) ve VEYA (`||`) ile koşulları birleştirme
- `if...else` koşulu
- Dönüş mesajı için string birleştirme

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Test Durumları

| Girdi | Beklenen Çıktı |
|-------|----------------|
| `isLeapYear(2024)` | `2024 is a leap year.` |
| `isLeapYear(2000)` | `2000 is a leap year.` |
| `isLeapYear(1900)` | `1900 is not a leap year.` |

## 🔗 Lab Linki

[freeCodeCamp - Build a Leap Year Calculator](https://www.freecodecamp.org/learn/javascript-v9/#lab-leap-year-calculator)
