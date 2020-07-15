import collections
from typing import List

#Runtime: 100 ms, faster than 54.94% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
#Memory Usage: 13.8 MB, less than 80.42% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

#fun fact: if not spots[n2[i]] returns true if its value is 0 (fails test case)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n2 = sorted(nums)
        spots = collections.defaultdict(dict)
        for i in range(len(n2)):
            if n2[i] not in spots:
                spots[n2[i]] = i
        for i in range(len(nums)):
            nums[i] =spots[nums[i]]
        return nums

s = Solution()
print(s.smallerNumbersThanCurrent([7,7,7,7]))