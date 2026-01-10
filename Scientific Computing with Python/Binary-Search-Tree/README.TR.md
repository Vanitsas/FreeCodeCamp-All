# İkili Arama Ağacı (BST) Uygulaması 🌳
Bu proje, **FreeCodeCamp Scientific Computing with Python** sertifikası kapsamında yapılan "Learn Tree Traversal by Building a Binary Search Tree" çalışmasını içerir.

## 🎯 Amaç
Python’da bir İkili Arama Ağacı (Binary Search Tree - BST) uygulamak ve ekleme, arama, silme ve inorder (sıralı) dolaşım yöntemlerini pratik yapmak.

## ✅ Örnek Kullanım
```python
from bst import BinarySearchTree

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

print("80 için arama:", bst.search(80))
print("Inorder dolaşım:", bst.inorder_traversal())

bst.delete(40)
print("40 silindikten sonra inorder dolaşım:", bst.inorder_traversal())

💡 Özellikler
BST’ye düğüm ekleme
Düğümleri arama
Düğümleri silme
Inorder dolaşım (sıralı sıra)

🧠 FreeCodeCamp bağlantısı
Learn Tree Traversal by Building a Binary Search Tree
