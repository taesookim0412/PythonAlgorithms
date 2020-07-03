#Runtime: 32 ms, faster than 48.16% of Python3 online submissions for Maximum 69 Number.
#Memory Usage: 13.8 MB, less than 47.70% of Python3 online submissions for Maximum 69 Number.

class Solution:
    def maximum69Number(self, num: int) -> int:
        nl = list(str(num))
        for i, a in enumerate(nl):
            if a == '6':
                nl[i] = '9'
                break
        return int(''.join(nl))