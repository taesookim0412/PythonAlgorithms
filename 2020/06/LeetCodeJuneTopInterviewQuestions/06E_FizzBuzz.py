from typing import List

#Runtime: 40 ms, faster than 80.27% of Python3 online submissions for Fizz Buzz.
#Memory Usage: 14.8 MB, less than 6.38% of Python3 online submissions for Fizz Buzz.
#LOL

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resp = ["Fizz", "Buzz", "FizzBuzz", ""]
        return [self.switchData(i, resp) for i in range(1, n+1)]

    def switchData(self, i, resp) -> str:
        if i % 3 == 0 and i % 5 == 0:
            return resp[2]
        if i % 3 == 0:
            return resp[0]
        if i % 5 == 0:
            return resp[1]
        resp[3] = str(i)
        return resp[3]

print(Solution().fizzBuzz(15))