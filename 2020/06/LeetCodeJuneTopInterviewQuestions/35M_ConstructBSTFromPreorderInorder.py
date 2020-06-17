#HOLDUP this is the wrong thing

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.order = preorder[::-1]
        self.root = TreeNode(self.order.pop())
        root = self.root
        for i in range(len(preorder)):
            if not root:
                root = TreeNode(self.order.pop())


