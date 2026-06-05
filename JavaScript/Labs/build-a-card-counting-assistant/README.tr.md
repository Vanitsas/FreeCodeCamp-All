# Kart Sayma Asistanı Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript laboratuvar çalışmasıdır.

## 📌 Hakkında

Bu laboratuvarda Blackjack casino oyunu için bir kart sayma asistanı oluşturulmuştur. Fonksiyon, oynanan kartlara göre global bir sayacı takip eder ve oyuncuya **Bet** (bahis yap — sayaç pozitifse) ya da **Hold** (bekle — sayaç sıfır veya negatifse) tavsiyesi verir.

**Sayma Kuralları:**
| Kartlar | Sayaca Etkisi |
|---------|--------------|
| 2, 3, 4, 5, 6 | `+1` |
| 7, 8, 9 | Değişmez |
| 10, J, Q, K, A | `-1` |

## 🧠 Çalışılan Kavramlar

- `let` ile global değişken tanımlama
- Fonksiyon içinde global değişkeni güncelleme
- `if...else if` koşul zinciri
- Karşılaştırma operatörleri ve mantıksal VEYA (`||`)
- Koşula göre biçimlendirilmiş string döndürme

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Test Durumları

| Oynanan Kartlar | Son Çağrı | Beklenen Çıktı |
|-----------------|-----------|----------------|
| 2, 3, 4, 5, 6 | `cardCounter(6)` | `5 Bet` |
| 7, 8, 9 | `cardCounter(9)` | `0 Hold` |
| 10, J, Q, K, A | `cardCounter("A")` | `-5 Hold` |
| 3, 7, Q, 8, A | `cardCounter("A")` | `-1 Hold` |
| 2, J, 9, 2, 7 | `cardCounter(7)` | `1 Bet` |
| 2, 2, 10 | `cardCounter(10)` | `1 Bet` |
| 3, 2, A, 10, K | `cardCounter("K")` | `-1 Hold` |

## 🔗 Lab Linki

[freeCodeCamp - Build a Card Counting Assistant](https://www.freecodecamp.org/learn/javascript-v9/#lab-counting-cards)
