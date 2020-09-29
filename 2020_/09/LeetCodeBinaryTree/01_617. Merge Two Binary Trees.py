import collections
import numpy as np
from typing import List


#Runtime: 108 ms, faster than 34.10% of Python3 online submissions for Merge Two Binary Trees.
#Memory Usage: 15.6 MB, less than 5.10% of Python3 online submissions for Merge Two Binary Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        def preorder(t1, t2, t3):
            if not t1 and not t2:
                return
            total = 0
            t1left, t2left, t1right, t2right = None, None, None, None
            if t1:
                total += t1.val
                t1left = t1.left
                t1right = t1.right
            if t2:
                total += t2.val
                t2left = t2.left
                t2right = t2.right
            t3.val = total
            if t1left or t2left:
                t3.left = TreeNode(None)
                preorder(t1left, t2left, t3.left)
            if t1right or t2right:
                t3.right = TreeNode(None)
                preorder(t1right, t2right, t3.right)

        resTree = TreeNode(None)
        preorder(t1, t2, resTree)
        return resTree
