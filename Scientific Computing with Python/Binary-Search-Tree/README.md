# Binary Search Tree (BST) Implementation 🌳
This is my solution for the FreeCodeCamp Scientific Computing with Python project: Learn Tree Traversal by Building a Binary Search Tree.

## 🎯 Objective
Implement a Binary Search Tree (BST) in Python and practice tree traversal methods including insertion, search, deletion, and inorder traversal.

## ✅ Example Usage
```python
from bst import BinarySearchTree

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

print("Search for 80:", bst.search(80))
print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())

💡 Features
Insert nodes into the BST
Search for nodes
Delete nodes
Inorder traversal (sorted order)

🧠 FreeCodeCamp link
Learn Tree Traversal by Building a Binary Search Tree