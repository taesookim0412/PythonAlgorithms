import collections
import numpy as np
from typing import List





#50 / 86
#"((()()))"
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        balance = 0
        ps = {'(': 1, ')': -1}
        score = 0
        subscore = 0
        for c in S:
            balance += ps[c]
            if not balance:
                score += 1 if not subscore else subscore * 2
                subscore = 0
            elif balance > 1 and c == '(':
                subscore += 1
        return score
