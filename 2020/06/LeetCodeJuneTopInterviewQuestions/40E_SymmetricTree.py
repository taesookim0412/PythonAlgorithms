# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#okay well apparantely they wanted to know if it was symmetric about the root
#not symmetric
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverseInorder(root):
            if not root: inorder.append(None)
            if root:
                traverseInorder(root.left)
                inorder.append(root.val)
                traverseInorder(root.right)

        inorder = []
        traverseInorder(root)
        idx = inorder.index(root.val)
        endx = inorder[idx + 1:]
        endx = endx[::-1]
        print(inorder[:idx], endx)
        if inorder[:idx] == endx: return True
        return False

