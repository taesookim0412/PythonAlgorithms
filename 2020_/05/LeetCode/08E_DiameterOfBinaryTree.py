# -*- coding: utf-8 -*-
# from DataStructures import TreeNode
from DataStructures.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    

#05-18-2020_
#Runtime: 64 ms, faster than 24.52% of Python3 online submissions for Diameter of Binary Tree.
#Memory Usage: 15.3 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
#just traverse the tree
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None: return 0
        if root.val is None: return 0
        if root.left is None and root.right is None: return 0
        self.traverseTree(root)
        return self.ans
    
    def traverseTree(self, root:TreeNode) -> int:
        if not root: return 0
        left = self.traverseTree(root.left)
        right = self.traverseTree(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) +1
        
        
    def __init__(self):
        tree = TreeNode(1)
        tree.insertList(tree, [2, 3, 4, 5])
        #tree.printInOrder(tree)
      #     1
      #    / \
      #   2   3
      #  / \     
      # 4   5    
        
        print(self.diameterOfBinaryTree(tree))
    
Solution()
