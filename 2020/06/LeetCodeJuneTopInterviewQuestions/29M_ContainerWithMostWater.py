from typing import List

class Solution:
    #Two Pointer
    #Runtime: 200 ms, faster than 11.67% of Python3 online submissions for Container With Most Water.
    #Memory Usage: 15.2 MB, less than 89.53% of Python3 online submissions for Container With Most Water.
    def maxArea(self, height: List[int]) -> int:
        maxArea, l, r = 0, 0, len(height)-1
        while l < r:
            maxArea = max(min(height[l], height[r]) * (r-l), maxArea )
            if height[l] < height[r]:
                l+=1
            else:
                r -=1
        return maxArea

#n^2 Time limit exceeded
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i in range(len(height)):
            for j in range(len(height)):
                dist = abs(j - i)
                area = min(height[i], height[j]) * dist
                maxArea = max(maxArea, area)
        return maxArea

s = Solution()
#49
print(s.maxArea([1,8,6,2,5,4,8,3,7]))