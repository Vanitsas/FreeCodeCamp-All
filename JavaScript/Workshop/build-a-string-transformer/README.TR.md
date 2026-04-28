# String Dönüştürücü Oluştur

[freeCodeCamp](https://www.freecodecamp.org/) müfredatı kapsamında tamamlanmış başlangıç seviyesi bir JavaScript atölyesidir.

## 📌 Hakkında

Bu atölyede string dönüştürme metodları incelenmiştir. Program cümlelerdeki kelimeleri değiştirir, bir kelimenin tüm tekrarlarını aynı anda değiştirir ve yeni bir cümle oluşturmak için bir string'i birden fazla kez tekrarlar.

## 🧠 Çalışılan Kavramlar

- Bir alt string'in ilk geçtiği yeri değiştirmek için `replace()` kullanımı
- Bir alt string'in tüm geçtiği yerleri değiştirmek için `replaceAll()` kullanımı
- Bir string'i birden fazla kez tekrarlamak için `repeat()` kullanımı
- Sondaki boşluğu temizlemek için `repeat()` ile `trimEnd()` kombinasyonu
- `${}` ile template literal kullanımı

## 💻 Nasıl Çalıştırılır

1. Kodu tarayıcının geliştirici konsoluna yapıştır, veya
2. Node.js ile çalıştır:

```bash
node index.js
```

## 📄 Beklenen Çıktı

```
Original string:
I love cats.
After using the replace() method:
I love dogs.
Original sentence:
I love cats and cats are so much fun!
Replacing all occurrences of cats with dogs:
I love dogs and dogs are so much fun!
Original learning sentence:
I love learning!
love love love
I love love love learning.
```

## 🔗 Atölye Linki

[freeCodeCamp - Build a String Transformer](https://www.freecodecamp.org/learn/javascript-v9/#workshop-string-transformer)
