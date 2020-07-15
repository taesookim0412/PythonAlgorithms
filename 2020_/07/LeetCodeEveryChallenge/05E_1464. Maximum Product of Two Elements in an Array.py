from typing import List

#Runtime: 64 ms, faster than 41.17% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 14.2 MB, less than 5.11% of Python3 online submissions for Maximum Product of Two Elements in an Array.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = secondLargest = -999999
        for x in nums:
            if x > largest:
                secondLargest = largest
                largest = x
            elif x > secondLargest:
                secondLargest = x
            print(x,largest, secondLargest)
        return (largest-1) * (secondLargest-1)

s = Solution()
print(s.maxProduct([1,5,4,5]))