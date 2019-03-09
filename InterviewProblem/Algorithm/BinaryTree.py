class Node:

	def __init__(self,val):
		self.val = val
		self.left= None
		self.right = None

	def maxPathNode(self,root):
		if root is None:
			return 0
		self.maxSum = 0
		self.helper(root)
		return self.maxSum

	def helper(self,root):
		leftSum = self.helper(root.left)
		rightSum = self.helper(root.right)
		self.maxSum = max(root.val + leftSum + rightSum + self.maxSum, 
						  leftSum + root.val, 
						  rightSum + root.val, 
						  root.val)
		return max(root.val + leftSum, root.val + rightSum)



root = Node(1)
root.left = Node(3)
root.right = Node(10)

result = root.maxPathNode(root)
print({"Result": result})