##Runtime: 72 ms, faster than 10.24% of Python3 online submissions for Roman to Integer.
#Memory Usage: 13.9 MB, less than 45.70% of Python3 online submissions for Roman to Integer.
#https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        nums = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = list(s)
        sum = 0
        prev = s[0]
        for i in range(len(s)):
            if nums[prev] < nums[s[i]]:
                sum -= nums[prev] * 2
            sum += nums[s[i]]
            prev = s[i]
        return sum

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("IV"))