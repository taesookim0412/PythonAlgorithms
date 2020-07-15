
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Runtime: 76 ms, faster than 90.18% of Python3 online submissions for Count Complete Tree Nodes.
#Memory Usage: 21.4 MB, less than 5.33% of Python3 online submissions for Count Complete Tree Nodes.
#
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None: return 0
        left, right = root, root
        height = 0
        while right != None:
            left = left.left
            right = right.right
            height+=1
        if left == None:
            return 2**height -1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#Runtime: 96 ms, faster than 40.45% of Python3 online submissions for Count Complete Tree Nodes.
#Memory Usage: 21 MB, less than 97.86% of Python3 online submissions for Count Complete Tree Nodes.
#Original:
class SolutionOrig:
    def countNodes(self, root: TreeNode) -> int:
        ct = 0
        def traverseNode(root):
            if root:
                nonlocal ct; ct+= 1
                traverseNode(root.left)
                traverseNode(root.right)
        traverseNode(root)
        return ct



node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
s = Solution()
print(s.countNodes(node))