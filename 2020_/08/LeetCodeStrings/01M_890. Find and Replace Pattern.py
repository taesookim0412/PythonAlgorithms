import collections
import numpy as np
from typing import List


#Runtime: 24 ms, faster than 99.71% of Python3 online submissions for Find and Replace Pattern.
#Memory Usage: 13.8 MB, less than 51.85% of Python3 online submissions for Find and Replace Pattern.

#A->B
#Pattern -> Word
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            mapAtoB = collections.defaultdict(str)
            mapBtoA = collections.defaultdict(str)
            truthy = True
            for i, ch in enumerate(word):
                if not mapBtoA[ch] and not mapAtoB[pattern[i]]:
                    mapBtoA[ch] = pattern[i]
                    mapAtoB[pattern[i]] = ch
                elif mapBtoA[ch] != pattern[i] or mapAtoB[pattern[i]] != ch:
                    truthy = False
                    break
            if truthy:
                res += word,
        return res



# ["ktittgzawn","dgphvfjniv","gceqobzmis","alrztxdlah","jijuevoioe","mawiizpkub","onwpmnujos","zszkptjgzj","zwfvzhrucv","isyaphcszn"]
# "zdqmjnczma"
# Output:
# ["alrztxdlah","onwpmnujos","zwfvzhrucv"]
# Expected:
# []
class Solution1:
    def getPatternCt(self,pattern):
        patternCt = []
        lastCt = 1
        for i in range(1, len(pattern)):
            if pattern[i] != pattern[i - 1]:
                patternCt += lastCt,
                lastCt = 0
            lastCt += 1
        if lastCt != 0: patternCt += lastCt,
        return patternCt
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        patternCt = self.getPatternCt(pattern)
        print(patternCt)
        unique_patternChars = len(collections.Counter(pattern))
        for word in words:
            wPatternCt = self.getPatternCt(word)
            wUnique_patternChars = len(collections.Counter(word))
            print(wPatternCt, word)
            if wUnique_patternChars == unique_patternChars and wPatternCt == patternCt:
                res += word,
        return res

#["yyxx"] <- shouldn't be output
#["badc","abab","dddd","dede","yyxx"]
#"baba"
class Solution2:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        pattern = collections.Counter(pattern)
        patternCt = [x for x in pattern.values()]
        unique_patternChars = len(pattern)
        for word in words:
            wPattern = collections.Counter(word)
            wPatternCt = [x for x in wPattern.values()]
            wUnique_patternChars = len(wPattern)
            if wUnique_patternChars == unique_patternChars and wPatternCt == patternCt:
                res += word,
        return res



s = Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],
"abb"))
print(s.findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba"))
print(s.findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba"))