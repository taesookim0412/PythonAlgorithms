#Runtime: 124 ms, faster than 9.46% of Python3 online submissions for Search in a Binary Search Tree.
#Memory Usage: 15.8 MB, less than 24.85% of Python3 online submissions for Search in a Binary Search Tree.

#I swear these binary search tree problems end up becoming your favorite problems
#because they're so much easier
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            L = self.searchBST(root.left, val)
            if L: return L
            R = self.searchBST(root.right, val)
            if R: return R