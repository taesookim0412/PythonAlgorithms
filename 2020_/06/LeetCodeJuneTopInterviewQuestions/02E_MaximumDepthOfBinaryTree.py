
#06-01-2020_
#Runtime: 32 ms, faster than 97.82% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 15.4 MB, less than 68.75% of Python3 online submissions for Maximum Depth of Binary Tree.

class Solution:
    maxDepthVar = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.findDepth(root)
        print(root.val)
        self.maxDepthVar += 1
        return self.maxDepthVar

    def findDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        L = self.findDepth(root.left)
        R = self.findDepth(root.right)
        self.maxDepthVar = max(L, R, self.maxDepthVar)
        print(L, R, self.maxDepthVar)
        return max(L, R) + 1