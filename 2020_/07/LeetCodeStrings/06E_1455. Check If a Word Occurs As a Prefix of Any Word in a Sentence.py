import collections
import numpy as np
from typing import List

#Runtime: 28 ms, faster than 79.01% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
#Memory Usage: 13.9 MB, less than 23.37% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        prefix = 1
        for s in sentence.split(' '):
            if s.startswith(searchWord):
                return prefix
            prefix+=1
        return -1

#Runtime: 28 ms, faster than 79.01% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
#Memory Usage: 13.9 MB, less than 32.47% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        prefix = 1
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                prefix += 1
            if sentence[i] == searchWord[0]:
                combinedLength = i + len(searchWord)
                if combinedLength < len(sentence) and i==0 or sentence[i-1] == ' ':
                    if sentence[i:combinedLength] == searchWord:
                        return prefix
        return -1