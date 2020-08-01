import collections
import numpy as np
from typing import List

#Runtime: 32 ms, faster than 60.94% of Python3 online submissions for Goat Latin.
#Memory Usage: 14 MB, less than 5.68% of Python3 online submissions for Goat Latin.

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = [list(x) for x in S.split(' ')]
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i, word in enumerate(words):
            if word[0] in vowels:
                word += 'm','a',
            else:
                word += word.pop(0),'m','a',
            word += ['a' for _ in range(i+1)]
        return ' '.join([''.join(x) for x in words])

s = Solution()
#Imaa peaksmaaa oatGmaaaa atinLmaaaaa
print(s.toGoatLatin("I speak Goat Latin"))