# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Runtime: 64 ms, faster than 7.16% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 14.1 MB, less than 15.32% of Python3 online submissions for Symmetric Tree.

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(root1, root2):
            if root1 is None and root2 is None: return True
            if root1 is None or root2 is None: return False
            return root1.val == root2.val and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
        if not root: return True
        return isMirror(root.left, root.right)




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

