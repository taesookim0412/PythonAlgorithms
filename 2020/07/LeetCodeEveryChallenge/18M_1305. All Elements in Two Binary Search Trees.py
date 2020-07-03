import collections
import numpy as np
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Runtime: 452 ms, faster than 35.71% of Python3 online submissions for All Elements in Two Binary Search Trees.
#Memory Usage: 21.8 MB, less than 14.17% of Python3 online submissions for All Elements in Two Binary Search Trees.

#TODO: Double Trouble
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        porder = []
        def traverse(root):
            if root:
                porder.append(root.val)
                traverse(root.left)
                traverse(root.right)
        traverse(root1)
        traverse(root2)
        porder.sort()
        return porder