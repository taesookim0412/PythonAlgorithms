from typing import List

#TODO: Iterator and Map
#Basically this algorithms works by splitting the inorder list by the root.
#Recursively calls itself in order to assign root treenodes on the first preorder element.
#IT basically follows the layout of a preorder traversal but it indexes inorder elements based preorder[0]
#however slicing inorder allows for a correctly balanced tree.
#Example of when you just try to pop preorder: root.right = None
#Can't slice preorder.

#Runtime: 152 ms, faster than 60.21% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#Memory Usage: 52.1 MB, less than 53.84% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind:])
            return root


#Sample 60ms solution:
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idmax = {val: idx for idx, val in enumerate(inorder)}

        def helper(start, end):
            if start > end:
                return None

            root = TreeNode(preorder.pop(0))
            root.left = helper(start, idmax[root.val] - 1)
            root.right = helper(idmax[root.val] + 1, end)
            return root

        return helper(0, len(preorder) - 1)
