#Runtime: 32 ms, faster than 44.99% of Python3 online submissions for Defanging an IP Address.
#Memory Usage: 13.7 MB, less than 89.32% of Python3 online submissions for Defanging an IP Address.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        addy = list(address)
        for i,a in enumerate(addy):
            if a==".":
                addy[i] = "[.]"
        return ''.join(addy)
