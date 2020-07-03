import collections
import numpy as np
from typing import List

#Runtime: 64 ms, faster than 5.70% of Python3 online submissions for Unique Morse Code Words.
#Memory Usage: 13.8 MB, less than 55.32% of Python3 online submissions for Unique Morse Code Words.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        conts = set()
        for x in words:
            bld = []
            for c in x:
                bld+= morseTable[ord(c) - 97],
            conts.add(''.join(bld))
        return len(conts)