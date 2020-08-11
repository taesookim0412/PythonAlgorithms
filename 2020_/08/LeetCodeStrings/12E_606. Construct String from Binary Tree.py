import collections
import numpy as np
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Runtime: 48 ms, faster than 91.37% of Python3 online submissions for Construct String from Binary Tree.
#Memory Usage: 15.2 MB, less than 97.16% of Python3 online submissions for Construct String from Binary Tree.

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"

#TreeToStr via Preorder

#1, 2, 3
#1(2)(3)
class Solution2:
    def tree2str(self, t: TreeNode) -> str:
        self.res = str(t.val)
        def traverse(root):
            if root and root.val:
                self.res += "(" + str(root.val)
                traverse(root.left)
                if root.right and not root.left:
                    self.res += "()"
                traverse(root.right)
                self.res += ")"
        traverse(t.left)
        traverse(t.right)
        return self.res

class tp:
    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

#1(2
tree = TreeNode(1,
                TreeNode(2),
                TreeNode(3))
treeTwo = TreeNode(1,
                TreeNode(2, TreeNode(4)),
                TreeNode(3))
treeThree = TreeNode(1,
                TreeNode(2, None, TreeNode(4)),
                TreeNode(3))
s = Solution()
print(s.tree2str(tree))
print(s.tree2str(treeTwo))
print(s.tree2str(treeThree))
tp().preorder(treeThree)