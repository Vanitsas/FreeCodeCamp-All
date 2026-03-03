# Bir piyano tasarlayın

Bu proje, FreeCodeCamp Responsive Web Design Certification kapsamında hazırlanmıştır.

## 📌 Proje Özeti

Bu çalışmada HTML ve CSS kullanılarak görsel bir piyano tasarımı oluşturulmuştur. Amaç; konumlandırma, pseudo-element kullanımı ve responsive tasarım tekniklerini pekiştirmektir.

Piyano beyaz ve siyah tuşlardan oluşur. Siyah tuşlar ekstra HTML elemanı eklemek yerine .black--key::after pseudo-elementi ile oluşturulmuştur.

## 🧱 Kullanılan Teknolojiler

- HTML5
- CSS3
- CSS Pseudo-element
- Box-sizing
- Float ve Position
- Media Query

## 🎯 Pekiştirilen Konular

Box Sizing Reset: box-sizing: border-box; ile tutarlı ölçülendirme sağlanmıştır.

Yapı:
- Ana kapsayıcı (#piano)
- Tuş alanı (.keys)
- Beyaz tuşlar (.key)
- Siyah tuşlar (.black--key::after)

Pseudo-element Kullanımı: .key.black--key::after seçicisi ile siyah tuşlar görsel olarak üretilmiştir. Bu yöntem HTML yapısını sade tutar.

Responsive Tasarım: Media query kullanılarak üç farklı ekran boyutuna uyum sağlanmıştır:
- 768px altı → Küçük ekran
- 769px - 1199px → Orta ekran
- 1200px ve üzeri → Geniş ekran

## 📱 Responsive Davranış

Ekran boyutuna göre piyano genişliği, tuş alanı ve logo boyutu otomatik olarak ayarlanır. Böylece farklı cihazlarda uyumlu bir görünüm elde edilir.

## 🚀 Kazanımlar

- CSS ile görsel bileşen tasarlama
- Pseudo-element mantığını kavrama
- Media query ile responsive yapı kurma
- Position ve float kullanımı

## 📂 Proje Konumu

Responsive Web Design Certification/Labs/design-a-piano

## 🔗 Repo

https://github.com/Vanitsas/FreeCodeCamp-All