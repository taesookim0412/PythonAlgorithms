#TODO: Don't input garbage

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return TreeNode()
        root = TreeNode()
        n = len(nums)
        root.val = nums[n//2]
        del nums[n//2]
        curr = root
        for i in range(n//2 - 1, -1, -1):
            curr.left = TreeNode(nums[i])
            curr = curr.left
        curr = root
        for i in range(n//2, len(nums)):
            curr.right = TreeNode(nums[i])
            curr = curr.right
        return root