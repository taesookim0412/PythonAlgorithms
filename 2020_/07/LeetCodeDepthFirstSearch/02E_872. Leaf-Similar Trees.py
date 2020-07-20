import collections
import numpy as np
from typing import List

# Runtime: 56 ms, faster than 11.40% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 13.8 MB, less than 74.09% of Python3 online submissions for Leaf-Similar Trees.

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = []
        leaves2 = []
        def traverse(root, arr):
            if root:
                if not root.left and not root.right:
                    arr.append(root.val)
                    return
                traverse(root.left, arr)
                traverse(root.right, arr)
        traverse(root1, leaves1)
        traverse(root2, leaves2)
        return leaves1 == leaves2