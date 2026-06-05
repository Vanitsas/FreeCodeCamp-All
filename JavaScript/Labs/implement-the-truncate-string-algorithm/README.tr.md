# String Kesme Algoritmasını Uygula

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript laboratuvar çalışmasıdır.

## 📌 Hakkında

Bu laboratuvarda bir string'i belirli bir uzunlukta kesen bir fonksiyon oluşturulmuştur. String belirlenen sınırı aşıyorsa kesilir ve sonuna `...` eklenir. String zaten sınır dahilindeyse değiştirilmeden döndürülür.

## 🧠 Çalışılan Kavramlar

- Birden fazla parametreli fonksiyon tanımlama
- String uzunluğunu kontrol etmek için `str.length` kullanımı
- String'i belirli bir uzunlukta kesmek için `slice()` kullanımı
- `if...else` koşulu
- `...` eklemek için string birleştirme

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Test Durumları

| Girdi | Beklenen Çıktı |
|-------|----------------|
| `truncateString("A-tisket a-tasket A green and yellow basket", 8)` | `A-tisket...` |
| `truncateString("Peter Piper picked a peck of pickled peppers", 11)` | `Peter Piper...` |
| `truncateString("A-", 1)` | `A...` |
| `truncateString("Absolutely Longer", 2)` | `Ab...` |
| `truncateString("A-tisket...", 43)` | `A-tisket a-tasket A green and yellow basket` |

## 🔗 Lab Linki

[freeCodeCamp - Implement the Truncate String Algorithm](https://www.freecodecamp.org/learn/javascript-v9/#lab-truncate-string)
