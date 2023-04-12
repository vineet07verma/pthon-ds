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

	def find_parent(self, value: int):
		if self.head and self.head.value == value:
			return self.head

		current_node = self.head
		while current_node:
			if current_node.left and current_node.left.value == value or \
					current_node.right and current_node.right.value == value:
				return current_node
			elif value > current_node.value:
				current_node = current_node.right
			else:
				current_node = current_node.left

	def find(self, value):
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
		# print(current_node.value)
		self._inorder_recursive_call(current_node.left)
		self._inorder_recursive_call(current_node.right)

	@staticmethod
	def find_right_most(node: Node) -> Node:
		current_node = node
		while current_node.right:
			current_node = current_node.right
		return current_node

	def delete(self, value):
		to_delete = self.find(value)
		to_delete_parent = self.find_parent(value)

		# delete node has bot children
		if to_delete.left and to_delete.right:
			pass
		# only one child
		elif to_delete.right or to_delete.left:
			if to_delete == to_delete_parent.left:
				to_delete_parent.left = to_delete.left or to_delete.right
			elif to_delete == to_delete_parent.right:
				to_delete_parent.right = to_delete.left or to_delete.right
			else:
				self.head = to_delete.left or to_delete.right
		# No Children
		else:
				# Now check deleted node has in left of his parent
				if to_delete == to_delete_parent.left:
					to_delete_parent.left = None
				# Now check deleted node has in right of his parent
				elif to_delete == to_delete_parent.right:
					to_delete_parent.right = None
				else:
					# Deleted node is at root now
					self.head = None
