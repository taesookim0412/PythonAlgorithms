import collections
from typing import List

#23
#ad, ae, af
#bd, be, bf
#cd, ce, cf
#3^n permutations
#234
#adg adh adi aeg
#

#Runtime: 40 ms, faster than 15.93% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 13.8 MB, less than 60.20% of Python3 online submissions for Letter Combinations of a Phone Number.

#Recursive Backtracking Practice
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {                    '2':['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        output = []
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
                return
            for letter in nums[next_digits[0]]:
                perm = combination + letter
                backtrack(perm, next_digits[1:])
        if digits == "": return []
        backtrack("", digits)
        return output

s = Solution()
print(s.letterCombinations("23"))