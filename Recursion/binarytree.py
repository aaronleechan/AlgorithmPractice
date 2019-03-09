class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def maxDepth(self,node):

		if node is None:
			return 0
		left = self.maxDepth(node.left)
		right= self.maxDepth(node.right)
		# print({"Right height": right+1})
		# print({"Left height": left+1})
		return max(left,right)+1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left = Node(4)
root.left = Node(10)
root.right = Node(12)
root.left = Node(23)
root.left = Node(123)
root.left = Node(34)
root.left = Node(90)


maxD = root.maxDepth(root)
print({" Max Depth": maxD})