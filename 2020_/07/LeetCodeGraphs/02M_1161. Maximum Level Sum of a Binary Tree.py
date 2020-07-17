import collections
import numpy as np
from typing import List

# Runtime: 440 ms, faster than 28.12% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 17.9 MB, less than 81.13% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res = collections.defaultdict(int)
        def preorder(root, h):
            if root:
                res[h] += root.val
                preorder(root.left, h+1)
                preorder(root.right, h+1)
        preorder(root, 1)
        return heapq.nlargest(1, res.keys(), res.get)[-1]