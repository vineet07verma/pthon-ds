from binary_tree import BinaryTree
from node import Node

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))
tree.inorder()
print(tree)

print(f"              {tree.head.value}               ")
print(f"|-------------|---------------|")
print(f"{tree.head.left.value}                            {tree.head.right.value}")
