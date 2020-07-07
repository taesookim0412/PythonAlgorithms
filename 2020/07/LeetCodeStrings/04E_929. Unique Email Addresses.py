import collections
import numpy as np
from typing import List


#Runtime: 104 ms, faster than 8.33% of Python3 online submissions for Unique Email Addresses.
#Memory Usage: 13.9 MB, less than 48.64% of Python3 online submissions for Unique Email Addresses.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i, a in enumerate(emails):
            idx = a.index('@')
            critical_String = a[:idx]
            domain = a[idx:]
            val = critical_String.find('+')
            valid_portion = critical_String[:val]
            if val == -1:
                valid_portion += critical_String[-1]
            valid_portion = valid_portion.replace('.', '')
            valid_portion += domain
            res.add(valid_portion)
        return len(res)


s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))