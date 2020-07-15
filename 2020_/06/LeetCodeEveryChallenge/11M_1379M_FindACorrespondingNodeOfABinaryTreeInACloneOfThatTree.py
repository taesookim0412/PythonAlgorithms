#Runtime: 972 ms, faster than 10.65% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.
#Memory Usage: 23.5 MB, less than 44.40% of Python3 online submissions for Find a Corresponding Node of a Binary Tree in a Clone of That Tree.

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        data = []
        found = False
        def traverseOrig(root):
            if not root: return
            nonlocal found
            if not found:data.append(root.val)
            if root == target:
                found = True
                return
            traverseOrig(root.left)
            traverseOrig(root.right)
        data2 = []
        retRoot = None
        def traverseClone(root):
            if not root:return
            data2.append(root.val)
            if data2 == data:
                nonlocal retRoot;retRoot = root
                return
            traverseClone(root.left)
            traverseClone(root.right)
        traverseOrig(original)
        traverseClone(cloned)
        return retRoot