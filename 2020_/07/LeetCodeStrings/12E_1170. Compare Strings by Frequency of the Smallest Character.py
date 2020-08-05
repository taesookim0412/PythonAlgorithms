import collections
import bisect

import numpy as np
from typing import List

#Runtime: 72 ms, faster than 91.49% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.4 MB, less than 14.81% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

#This is binary searching a sorted list of counts.
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        wordCts = sorted(x.count(min(x)) for x in words)
        for q in queries:
            idx = q.count(min(q))
            s = bisect.bisect(wordCts, idx)
            res += len(wordCts) - s,
        return res



#Runtime: 60 ms, faster than 99.59% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.2 MB, less than 66.67% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.














# ?
class Solution2:
    def numSmallerByFrequency(self, queries, words):
        W = sorted([w.count(min(w)) for w in words])
        res = []
        for q in queries:
            cnt = q.count(min(q))
            idx = bisect(W, cnt)
            res.append(len(W) - idx)
        return res

#Brute force
#Runtime: 560 ms, faster than 50.00% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
#Memory Usage: 14.3 MB, less than 62.96% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
class Solution3:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        wordFreqs = [self.getFrequency(word) for word in words]
        for query in queries:
            freqCt = 0
            freq = self.getFrequency(query)
            for wordFreq in wordFreqs:
                if freq < wordFreq:
                    freqCt += 1
            res += freqCt,
        return res

    def getFrequency(self, woord) -> int:
        smallestChr = min(woord)
        return woord.count(smallestChr)

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
