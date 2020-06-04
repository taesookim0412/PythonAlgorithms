from typing import List

#28.48% faster runtime
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(len(s)//2):
            s[i], s[n-i] = s[n-i], s[i]
        print(s)

print(Solution().reverseString(["h","e","l","l","o"]))
