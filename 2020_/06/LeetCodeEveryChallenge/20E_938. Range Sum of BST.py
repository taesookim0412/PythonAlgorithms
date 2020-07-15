#Runtime: 292 ms, faster than 40.46% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 22 MB, less than 18.01% of Python3 online submissions for Range Sum of BST.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        rSum = 0
        def traverse(root):
            if root:
                if L <= root.val <= R:
                    nonlocal rSum
                    rSum += root.val
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return rSum