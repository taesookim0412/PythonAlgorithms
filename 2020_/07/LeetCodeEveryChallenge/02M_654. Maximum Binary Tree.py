# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
######Uhhhhhhhh construct a tree and create the tree from it?
#or how about a good description?
#The left subtree is the maximum tree constructed from left part subarray divided by the maximum number
#is this even english i thought we were supposed to solve the problem
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
