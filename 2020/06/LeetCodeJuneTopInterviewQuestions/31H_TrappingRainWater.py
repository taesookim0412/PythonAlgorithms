from typing import List

#Runtime: 44 ms, faster than 96.43% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 14.7 MB, less than 25.53% of Python3 online submissions for Trapping Rain Water.
#Two-Pass then subtract the mins with the height index
#then subtract its height (which is the area of water)

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = list(height), list(height)
        for i in range (1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        print(f"HT: {height}")
        print(f"LM: {left_max}")
        print(f"RM: {right_max}")
        ans = 0
        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans


s = Solution()

print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))