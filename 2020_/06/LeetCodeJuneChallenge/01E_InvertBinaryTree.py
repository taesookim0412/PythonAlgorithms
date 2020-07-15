
#Great start
#75.61% Faster Runtime
#06-01-2020_
#This problem was inspired by this original tweet by Max Howell:
#Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
#https://leetcode.com/problems/invert-binary-tree


class Solution:
    contents = []
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.right
            root.right = root.left
            root.left = temp
        return root