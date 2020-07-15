from typing import List

#Runtime: 232 ms, faster than 20.44% of Python3 online submissions for Reverse String.
#Memory Usage: 18.2 MB, less than 5.81% of Python3 online submissions for Reverse String.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(len(s)//2):
            tmp = s[n - i]
            s[n-i] = s[i]
            s[i] = tmp

Solution().reverseString(['a', 'b', 'c'])