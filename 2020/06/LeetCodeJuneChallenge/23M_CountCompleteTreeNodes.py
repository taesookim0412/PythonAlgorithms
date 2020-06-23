# Definition for a binary tree node.
#Runtime: 96 ms, faster than 40.45% of Python3 online submissions for Count Complete Tree Nodes.
#Memory Usage: 21 MB, less than 97.86% of Python3 online submissions for Count Complete Tree Nodes.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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