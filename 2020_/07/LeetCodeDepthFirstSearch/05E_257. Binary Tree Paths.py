import collections
import numpy as np
from typing import List

# Runtime: 56 ms, faster than 11.94% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 13.8 MB, less than 75.03% of Python3 online submissions for Binary Tree Paths.

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def traverse(root, path = []):
            if root:
                path += root.val,
                if not root.left and not root.right:
                    res.append("->".join([str(x) for x in path]))
                    return
                traverse(root.left, path.copy())
                traverse(root.right, path.copy())
        traverse(root)
        return res