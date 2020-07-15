#Runtime: 72 ms, faster than 80.87% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
#Memory Usage: 15.9 MB, less than 95.72% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
#what

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root = TreeNode(nums[len(nums)//2])
        root.left = self.sortedArrayToBST(nums[:len(nums//2)])
        root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])

        return root