#Binary Tree Inorder
class InOrderClass:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val]\
            + self.inorderTraversal(root.right)


#Binary Tree PostOrder
class PostOrderClass:

    def postOrderTraversal(self,root):
        if root is None:
            return []
        return self.postOrderTraversal(root.left) + self.postOrderTraversal(root.right) + [root.val]




#Binary Tree  PreOrder
class PreOrderClass:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


