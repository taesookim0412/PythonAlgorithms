#Runtime: 252 ms, faster than 5.71% of Python3 online submissions for Insert into a Binary Search Tree.
#Memory Usage: 16 MB, less than 30.73% of Python3 online submissions for Insert into a Binary Search Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insertion(root, val):
            if not root:
                return
            if root:
                if root.left == None and val <= root.val:
                    root.left = TreeNode(val)
                    return
                elif root.right == None and val >= root.val:
                    root.right = TreeNode(val)
                    return
                if val <= root.val:
                    insertion(root.left, val)
                elif val >= root.val:
                    insertion(root.right, val)
        if not root: return TreeNode(val)
        insertion(root, val)
        return root