import collections
from bisect import bisect

import numpy as np
from typing import List
#Runtime: 60 ms, faster than 99.59% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.2 MB, less than 66.67% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

# ?
class Solution:
    def numSmallerByFrequency(self, queries, words):
        W = sorted([w.count(min(w)) for w in words])
        res = []
        for q in queries:
            cnt = q.count(min(q))
            idx = bisect(W, cnt)
            res.append(len(W) - idx)
        return res

#Runtime: 5844 ms, faster than 7.30% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.3 MB, less than 66.67% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
class Solution2:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        for query in queries:
            freqCt = 0
            freq = self.getFrequency(query)
            for word in words:
                wordFreq = self.getFrequency(word)
                if freq < wordFreq:
                    freqCt += 1
            res += freqCt,
        return res

    def getFrequency(self, word) -> int:
        smallestChr = min(word)
        return word.count(smallestChr)


#Runtime: 7408 ms, faster than 5.27% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.4 MB, less than 22.22% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
class Solution2:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        for query in queries:
            freqCt = 0
            freq = self.getFrequency(list(query))
            for word in words:
                wordFreq = self.getFrequency(list(word))
                if freq < wordFreq:
                    freqCt += 1
            res += freqCt,
        return res

    def getFrequency(self, word) -> int:
        word.sort()
        return word.count(word[0])

s = Solution()
print(s.numSmallerByFrequency(["cbd"],
["zaaaz"]))
