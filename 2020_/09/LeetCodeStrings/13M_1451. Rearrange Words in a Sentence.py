import collections
import numpy as np
from typing import List
#Runtime: 36 ms, faster than 92.30% of Python3 online submissions for Rearrange Words in a Sentence.
#Memory Usage: 16.3 MB, less than 24.62% of Python3 online submissions for Rearrange Words in a Sentence.

class Solution:
    def arrangeWords(self, text: str) -> str:
        # return list(map(lambda T: T[0][0].lower(), list(list(map(lambda t: t.lower(), sorted(text.split(' '), key=len))))))
        #res = hello(res)
        #hello = lambda fc:  [fc[0][0].upper() + fc[0][1:]] + fc[1:][:]
        return ' '.join(list(map(lambda fc: [fc[0][0].upper() + fc[0][1:]] + fc[1:][:],[list(map(lambda t: t.lower(), sorted(text.split(' '), key=len)))]))[-1])

#['Up', 'elon', 'give', 'musk:', 'never']
print(Solution().arrangeWords("Elon Musk: Never Give Up"))
print(Solution().arrangeWords("To be or not to be"))
print(Solution().arrangeWords("You and i"))