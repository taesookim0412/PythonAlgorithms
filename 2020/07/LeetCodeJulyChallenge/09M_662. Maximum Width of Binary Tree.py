import collections
import numpy as np
from typing import List


# Definition for a binary tree node.
#wow packed I think it needs level traversal
#In fact why do these challenges XD I can pace myself in a healthy manner
#width of a binary tree wow
#utter dog shit
#just goes to prove that the world is shit
#and only all the shit produced from this world
#is from shit and will be shit
#Adios LC Challenge u little shit

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = []
        hts = collections.defaultdict(list)
        def traverse(root, h):
            if not root:
                hts[h] += None,
            if root:
                hts[h] += root.val,
                L = traverse(root.left,h+1)
                R = traverse(root.right,h+1)
        traverse(root,0)
        print(hts)

tree = TreeNode(1, left=TreeNode(3,
                                 left=TreeNode(5,
                                               left= TreeNode(6))))
tree.right = TreeNode(2,
                    right=TreeNode(9,
                                   right=TreeNode(7)))
s = Solution()
print(s.widthOfBinaryTree(tree))