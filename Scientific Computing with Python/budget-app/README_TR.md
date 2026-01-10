# Bütçe Uygulaması

Bu Python uygulaması, farklı bütçe kategorilerini yönetmek ve harcamaları görselleştirmek için tasarlanmıştır. Bu proje **FreeCodeCamp Python Sertifikası** kapsamında tamamlanmıştır.

## Özellikler

- Food, Clothing, Auto gibi bütçe kategorileri oluşturma.
- Her kategoriye para yatırma ve çekme işlemleri.
- Kategoriler arasında para transferi.
- Her kategorinin mevcut bakiyesini görüntüleme.
- Harcama yüzdesini gösteren metin tabanlı çubuk grafik oluşturma.

## Kullanım

```python
from budget import Category, create_spend_chart

# Kategoriler oluştur
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

# Para yatırma ve çekme işlemleri
food.deposit(1000, "ilk bakiye")
food.withdraw(10.15, "market alışverişi")
food.withdraw(15.89, "restoran ve tatlı")
clothing.deposit(500, "ilk bakiye")
clothing.withdraw(50, "gömlek")
auto.deposit(1000, "ilk bakiye")
auto.withdraw(100, "araba tamiri")

# Kategoriler arası transfer
food.transfer(50, clothing)

# Ledger’ları yazdır
print(food)
print(clothing)
print(auto)

# Harcama grafiği oluştur
print(create_spend_chart([food, clothing, auto]))

Örnek Çıktı
*************Food*************
ilk bakiye             1000.00
market alışverişi       -10.15
restoran ve daha fazl -15.89
Transfer to Clothing    -50.00
Total: 923.96

Harcamaların Yüzdesi
100|          
 90|          
 80|          
 70|          
 60|          
 50|       o  
 40|       o  
 30| o     o  
 20| o  o  o  
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

Proje Notları
Kod basit ve okunabilir olacak şekilde tasarlanmıştır.
Liste işlemleri, döngüler, string formatlama ve temel matematik işlemlerine odaklanılmıştır.
create_spend_chart fonksiyonu FreeCodeCamp testleri için doğru spacing ile metin tabanlı grafik üretir.

Yazar
Aygün Çerin
FreeCodeCamp Python Sertifikası kapsamında tamamlanmıştır.