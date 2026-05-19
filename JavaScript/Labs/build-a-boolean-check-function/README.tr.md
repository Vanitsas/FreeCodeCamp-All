# Boolean Kontrol Fonksiyonu Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript laboratuvar çalışmasıdır.

## 📌 Hakkında

Bu laboratuvarda verilen bir değerin boolean primitive olup olmadığını kontrol eden bir fonksiyon oluşturulmuştur. Fonksiyon yalnızca `true` ve `false` değerleri için `true` döndürür; `"true"` gibi string'ler, sayılar, diziler ve nesneler dahil diğer her şey için `false` döndürür.

## 🧠 Çalışılan Kavramlar

- Fonksiyon tanımlama ve çağırma
- Bir değerin tipini kontrol etmek için `typeof` operatörü kullanımı
- Boolean primitive'ler ile diğer tipler arasındaki farkı anlamak
- Bir karşılaştırmanın sonucunu doğrudan fonksiyondan döndürme

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Test Durumları

| Girdi | Beklenen Çıktı |
|-------|----------------|
| `booWho(true)` | `true` |
| `booWho(false)` | `true` |
| `booWho(1)` | `false` |
| `booWho("true")` | `false` |
| `booWho("false")` | `false` |
| `booWho("a")` | `false` |
| `booWho(NaN)` | `false` |
| `booWho([1, 2, 3])` | `false` |
| `booWho({ "a": 1 })` | `false` |
| `booWho([].slice)` | `false` |

## 🔗 Lab Linki

[freeCodeCamp - Build a Boolean Check Function](https://www.freecodecamp.org/learn/javascript-v9/#lab-boolean-check)
