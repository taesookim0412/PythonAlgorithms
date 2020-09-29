import collections
import numpy as np
from typing import List
#Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        # def preorderTraversal(self, root: TreeNode) -> List[int]:
        #     stack = [root]
        #     res = []
        #     while stack:
        #         curr = stack.pop()
        #         if curr:
        #             res.append(curr.val)
        #             stack.append(curr.left)
        def recursivePreorder(tree):
            if tree:
                res.append(tree.val)
                recursivePreorder(tree.left)
                recursivePreorder(tree.right)
        recursivePreorder(root)
        return res