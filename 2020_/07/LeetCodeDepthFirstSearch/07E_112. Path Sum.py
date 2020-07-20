import collections
import numpy as np
from typing import List

#Runtime: 68 ms, faster than 17.25% of Python3 online submissions for Path Sum.
#Memory Usage: 15.7 MB, less than 31.29% of Python3 online submissions for Path Sum.
class Solution:
    def hasPathSum(self, root: TreeNode, sum2: int) -> bool:
        paths = []
        def traverse(root, path = []):
            if root:
                path.append(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                    return
                traverse(root.left, path.copy())
                traverse(root.right, path.copy())
        traverse(root)
        for path in paths:
            if sum(path) == sum2:
                return True
        return False