from typing import List
#Runtime: 128 ms, faster than 5.32% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 14.1 MB, less than 46.59% of Python3 online submissions for Binary Tree Level Order Traversal.


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []
        self.traverseTree(root, 0)
        return root

    def traverseTree(self, root, level):
        if root:
            self.res.append(root.val)
            if len(self.res) < level +1:
                self.res.append([])
            self.res[level].append(root.val)
            self.traverseTree(root.left)
            self.traverseTree(root.right)

