from typing import List
#Runtime: 56 ms, faster than 95.23% of Python3 online submissions for Shuffle the Array.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        last_Half = nums[len(nums)//2:]
        newArr = []
        for i in range(len(nums)//2):
            newArr += nums[i],
            newArr += last_Half[i],
        return newArr

s = Solution()
print(s.shuffle([2,5,1,3,4,7], 3))