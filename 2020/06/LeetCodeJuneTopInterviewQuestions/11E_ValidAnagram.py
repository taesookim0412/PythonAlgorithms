#Runtime: 40 ms, faster than 84.92% of Python3 online submissions for Valid Anagram.
#Memory Usage: 14.6 MB, less than 22.13% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s)==sorted(t)



print(Solution().isAnagram("a", "b"))