import collections
import numpy as np
from typing import List
#Iterative
#78.11 %

#Append the tree nodes -> Iterate a stack with dynamic R->L append
#This contrasts the idea of looping and logging the current root node
#instead the only way the stack would work is to place side nodes beforehand
#else it would endlessly loop and log its lower left node
#(if created similar to a traditional recursive loop).
class Solution:
    def iterativeTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recursivePreorder(tree):
            if tree:
                res.append(tree.val)
                recursivePreorder(tree.left)
                recursivePreorder(tree.right)
        #recursivePreorder(root)
        recursivePreorder(root)
        return res
