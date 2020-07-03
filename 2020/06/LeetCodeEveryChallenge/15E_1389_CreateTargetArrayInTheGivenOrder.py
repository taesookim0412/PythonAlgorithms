#Runtime: 36 ms, faster than 42.51% of Python3 online submissions for Create Target Array in the Given Order.
#Memory Usage: 14 MB, less than 10.19% of Python3 online submissions for Create Target Array in the Given Order.

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target