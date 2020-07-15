# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
#Runtime: 32 ms, faster than 70.79% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
#Memory Usage: 14 MB, less than 73.91% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
#straight shot it


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def pTraverse(root, level):
            if not root:
                return
            if len(data) <= level: data.append([])
            data[level].append(root.val)
            pTraverse(root.left, level+1)
            pTraverse(root.right, level+1)
        data = []
        pTraverse(root, 0)
        for i in range(1, len(data), 2):
            data[i] = data[i][::-1]
        return data

s = Solution()

tree = TreeNode(3)
#this doesnt work refer to 37H_Deserialize
# def treeify(data)->TreeNode:
#     if len(data)==0: return None
#     val = data.pop(0)
#     if val is None:
#         return None
#     root = TreeNode(val)
#     root.left = treeify(data)
#     root.right = treeify(data)
#     return root
def pOrder(root):
    if not root: return
    print(root.val)
    pOrder(root.left)
    pOrder(root.right)

data = [3,9,20,None,None,15,7]
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
pOrder(tree)


print(s.zigzagLevelOrder(tree))