import collections
import numpy as np
from typing import List

#18%
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
#18%
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        returnRes = []
        returnRes2 = []
        def preorder(root, res):
            if not root:
                res.append(None)
            if root:
                res.append(root.val)
                preorder(root.left, res)
                preorder(root.right, res)
        preorder(p, returnRes)
        preorder(q, returnRes2)
        return returnRes == returnRes2