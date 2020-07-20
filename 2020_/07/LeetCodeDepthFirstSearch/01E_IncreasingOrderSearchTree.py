import collections
import numpy as np
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Runtime: 56 ms, faster than 8.82% of Python3 online submissions for Increasing Order Search Tree.
# Memory Usage: 13.9 MB, less than 38.53% of Python3 online submissions for Increasing Order Search Tree.

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        data = []
        def inorder(root):
            if root:
                inorder(root.left)
                data.append(root.val)
                inorder(root.right)
        inorder(root)
        #Unneccessary operation
        data = data[::-1]
        root = TreeNode(data.pop())
        curr = root
        while data:
            curr.right = TreeNode(data.pop())
            curr = curr.right
        return root