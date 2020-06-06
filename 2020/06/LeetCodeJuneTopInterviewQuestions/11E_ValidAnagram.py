#Runtime: 40 ms, faster than 84.92% of Python3 online submissions for Valid Anagram.
#Memory Usage: 14.9 MB, less than 5.03% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s);t=list(t);s.sort();t.sort();return s==t



print(Solution().isAnagram("a", "b"))