#Runtime: 108 ms, faster than 63.26% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
#Memory Usage: 17.4 MB, less than 13.82% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum = 0
        def traverse(root, parent_even, gp_even):
            if root:
                if gp_even is True:
                    print(root.val, gp_even)
                    nonlocal sum
                    sum += root.val
                evenIndic = True if root.val % 2 == 0 else False
                traverse(root.left, evenIndic, parent_even)
                traverse(root.right, evenIndic, parent_even)
        traverse(root.left, root.val % 2 == 0, False)
        traverse(root.right, root.val % 2 == 0, False)
        return sum



