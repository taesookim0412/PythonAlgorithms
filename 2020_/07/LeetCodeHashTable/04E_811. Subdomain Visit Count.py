import collections
import numpy as np
from typing import List

#Runtime: 48 ms, faster than 94.85% of Python3 online submissions for Subdomain Visit Count.
#Memory Usage: 13.7 MB, less than 95.66% of Python3 online submissions for Subdomain Visit Count.
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subDomains = collections.defaultdict(int)
        for domain in cpdomains:
            numCt = domain.find(' ')
            domainCt = int(domain[:numCt])
            domain = domain[numCt+1:]
            dIdx = domain.find('.')
            while dIdx != -1:
                subDomains[domain] += domainCt
                domain = domain[dIdx+1:]
                dIdx = domain.find('.')
            subDomains[domain] += domainCt
        return [' '.join([str(val), key]) for key, val in subDomains.items()]

#Runtime: 96 ms, faster than 9.83% of Python3 online submissions for Subdomain Visit Count.
#Memory Usage: 13.9 MB, less than 58.06% of Python3 online submissions for Subdomain Visit Count.

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subDomains = collections.defaultdict(int)
        for domain in cpdomains:
            numCt = domain.find(' ')
            domainCt = int(domain[:numCt])
            domain = domain[numCt+1:]
            while domain != "":
                subDomains[domain] += domainCt
                dIdx = domain.find('.')
                if dIdx == -1:
                    break
                domain = domain[dIdx+1:]
        return [' '.join([str(val), key]) for key, val in subDomains.items()]

s = Solution()
print(s.subdomainVisits(["9001 discuss.leetcode.com"]))
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))


