# Python Vektör Sınıfları (R2Vector & R3Vector) 📐
Bu proje, **FreeCodeCamp Scientific Computing with Python** sertifikası kapsamında yapılan Python vektör sınıfları çalışmasını içerir.

## 🎯 Amaç
Python’da vektörler kullanarak nesne yönelimli programlama (OOP) kavramlarını göstermek; özel metotlar, operatör yükleme, kalıtım ve dinamik özellik yönetimini uygulamak.

## ✅ Örnek Kullanım
```python
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

# Vektör işlemleri
v3 = v1 + v2          # toplama
v4 = v1 - v2          # çıkarma
dot = v1 * v2         # skaler çarpım (dot product)
cross = v1.cross(v2)  # vektörel çarpım (cross product)

# Sonuçları yazdır
print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v1 + v2 = {v3}')
print(f'v1 - v2 = {v4}')
print(f'v1 * v2 = {dot}')
print(f'v1 x v2 = {cross}')

Özellikler
Özel metotlar (__init__, __str__, __repr__, __add__, __sub__, __mul__, __eq__, __lt__, __gt__, __le__, __ge__)
Operatör yükleme: toplama, çıkarma, skaler çarpım, skaler çarpım (dot product), vektörel çarpım (cross product)
R2Vector’dan R3Vector’a kalıtım
vars() ve getattr() ile dinamik özellik yönetimi
Her boyutta vektör işlemlerinin esnek uygulanışı