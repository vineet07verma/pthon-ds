from node import Node


class BinaryTree:
	def __init__(self, head: Node):
		self.head = head

	def add(self, new_node: Node):
		current_node = self.head

		while current_node:
			# Check for equal node values
			if current_node.value == new_node.value:
				raise ValueError("Same Value Node is already exist")
				break
			elif new_node.value < current_node.value:
				if current_node.left:
					current_node = current_node.left
				else:
					current_node.left = new_node
					break
			elif new_node.value > current_node.value:
				if current_node.right:
					current_node = current_node.right
				else:
					current_node.right = new_node
					break

	def ind(self, value):
		current_node: Node = self.head
		while current_node:
			if current_node.value == value:
				return current_node
			elif value > current_node.value:
				current_node = current_node.right
			else:
				current_node = current_node.left

	def inorder(self):
		self._inorder_recursive_call(self.head)

	def _inorder_recursive_call(self, current_node):
		if not current_node:
			return
		print(current_node.value)
		self._inorder_recursive_call(current_node.left)
		self._inorder_recursive_call(current_node.right)
