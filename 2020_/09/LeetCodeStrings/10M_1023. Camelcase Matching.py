import collections
import numpy as np
from typing import List
import re

#32/36
#and reported btw

def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    patterns = list(filter(None, re.split("([A-Z][^A-Z]*)", pattern)))
    longestLen = len(max(patterns, key=len))
    # queries_partitioned = [x[:longestLen]
    #                        for word in queries
    #                        for x in list(filter(None, re.split('([A-Z][a-z]*)', word)))]
    queries_partitioned = [list(filter(None, re.split('([A-Z][a-z]*)', word)))
                           for word in queries]
    res = []
    for query in queries_partitioned:
        # if query[0].islower() and not pattern[0].islower():
        #     query = query[1:]
        for word, pattern in zip(query, patterns):
            word_Ct = collections.Counter(word)
            pattern_Ct = collections.Counter(pattern)
            #print(word_Ct, pattern_Ct)
            word_Ct.subtract(pattern_Ct)
            #print(word_Ct)
            if any(num < 0 for num in word_Ct.values()):
                res.append(False)
                break
        else:
            res.append(len(query) == len(patterns))
    return res

print(camelMatch(None, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB"))
print(camelMatch(None, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))
print(camelMatch(None, ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))

#ControlPanel: True
print(camelMatch(None, ["CompetitiveProgramming","CounterPick","ControlPanel"], "CooP"))

#tttttttttttttt
print(camelMatch(None, ["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"],"ksvjLiknTzqn"))

#tttttttttt
print(camelMatch(None, ["uAxaqlzahfialcezsLfj","cAqlzyahaslccezssLfj","AqlezahjarflcezshLfj","AqlzofahaplcejuzsLfj","tAqlzahavslcezsLwzfj","AqlzahalcerrzsLpfonj","AqlzahalceaczdsosLfj","eAqlzbxahalcezelsLfj"], "AqlzahalcezsLfj"))
