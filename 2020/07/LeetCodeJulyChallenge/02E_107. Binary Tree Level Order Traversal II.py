#20
#10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def traverse(root, h):
            if root:
                if len(res) <= h:
                    res.append([])
                res[h] += root.val,
                traverse(root.left, h + 1)
                traverse(root.right, h + 1)

        traverse(root, 0)
        return res[::-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#doesnt work the recursion stops at the deepest child on one side and wrong maxh
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        maxh = 0
        def postOrder(root, h):
            if root:
                nonlocal maxh; maxh = max(maxh, h)
                postOrder(root.left, h+1)
                postOrder(root.right, h+1)
                while len(res) <= h:
                    res.append([])
                print(maxh)
                res[maxh-h] += root.val,
        postOrder(root, 0)
        return res




























