
from DataStructures.TreeNode import TreeNode

from typing import List

#05-30-2020_
#Runtime: 96 ms, faster than 49.64% of Python3 online submissions for Binary Tree Maximum Path Sum.
#Memory Usage: 20.4 MB, less than 100.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
#https://leetcode.com/problems/binary-tree-maximum-path-sum
#Runtime is O(n) since it goes through every node
#O(n) space (No extra)
class Solution:
    maxSum = -9999999999
    #It's not "Maximum Number of Paths Sum" it's
    #Maximum One Path Sum
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -9999999999
        self.traverseMaxPath(root)
        return self.maxSum

    def traverseMaxPath(self, root)->int:
        if not root: return 0
        leftGain = max(self.traverseMaxPath(root.left), 0)
        rightGain = max(self.traverseMaxPath(root.right), 0)
        sum = root.val + leftGain + rightGain
        self.maxSum = max(sum, self.maxSum)
        return root.val + max(leftGain, rightGain)


#05-29-2020_
#i duno i think we have different kinds of binary search trees

# 54 / 93 test cases passed.
# Status: Wrong Answer
# Submitted: 0 minutes ago
# Input:
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# Output:
# 55
# Expected:
# 48
#nulls in bst
#
# class Solution:
#     #Find the maximum sum. The path must be the maximum path.
#     maxPath = 0
#     maxSum = -99999999
#
#     def maxPathSum(self, root: TreeNode) -> int:
#         self.maxPath = 0
#         self.maxSum = -99999999
#         self.initial = True
#         list = self.maxPathSumTraverse(root, [0, 0])
#
#         return self.maxSum
#
#     initial = True
#
#     def maxPathSumTraverse(self, root: TreeNode, data:List[int]) -> List[int]:
#         if not root:
#             return data
#         L = self.maxPathSumTraverse(root.left, data)
#         R = self.maxPathSumTraverse(root.right, data)
#         if L[0] + R[0] + 1 > self.maxPath: self.maxPath = L[0] + R[0] + 1
#         print(f"L {L[1]}")
#         print(f"R {R[1]}")
#         sum = root.val
#         sum += L[1]
#         sum += R[1]
#
#         self.maxSum = max(root.val, root.val + L[1], root.val + R[1], sum, self.maxSum)
#
#         addsum = root.val
#         #lols
#         # if self.initial is True:
#         #     addSum = 0
#         #     self.initial = False
#         return [max(L[0], R[0]) + 1, sum]





tree = TreeNode(2)
tree.insertList(tree, [1, 3])
sol = Solution()
print(sol.maxPathSum(tree))
