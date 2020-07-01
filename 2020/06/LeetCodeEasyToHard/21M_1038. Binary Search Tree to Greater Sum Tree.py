# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#diagram doesnt make sense how can 1 and 0 both have the same sum of total nodes that are greater than it
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         nums = []
#         def inorder(root):
#             if root:
#                 inorder(root.left)
#                 nums.append(root.val)
#                 inorder(root.right)
#         def composeInOrder(root):
#             # root.left =
#
#         inorder(root)
#         newRoot = TreeNode(sum(nums)-root.val)
#         composeInOrder(newRoot)
