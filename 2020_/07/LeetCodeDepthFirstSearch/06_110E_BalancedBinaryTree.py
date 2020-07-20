import collections
import numpy as np
from typing import List


#balance deez nuts
#test case: [1, null, 2, null, 3]
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        leafHeights = []
        def traverse(root, h):
            if root:
                if not root.left or not root.right:
                    leafHeights.append(h)
                    return
                traverse(root.left, h+1)
                traverse(root.right, h+1)
        traverse(root, 0)
        return 0 <= max(leafHeights) - min(leafHeights) <= 1
