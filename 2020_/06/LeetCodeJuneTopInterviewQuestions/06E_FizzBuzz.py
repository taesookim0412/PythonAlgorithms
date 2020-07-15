from typing import List

#Runtime: 36 ms, faster than 94.17% of Python3 online submissions for Fizz Buzz.
#Memory Usage: 14.9 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.
#LOL

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resp = ["Fizz", "Buzz", "FizzBuzz", ""]
        return [resp[self.switchData(i, resp)] for i in range(1, n+1)]

    def switchData(self, i, resp) -> str:
        if i % 3 == 0 and i % 5 == 0:
            return 2
        if i % 3 == 0:
            return 0
        if i % 5 == 0:
            return 1
        resp[3] = str(i)
        return 3

print(Solution().fizzBuzz(15))