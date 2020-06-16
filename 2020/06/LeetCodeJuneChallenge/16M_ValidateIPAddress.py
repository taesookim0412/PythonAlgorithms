import re
#TODO: Regular Expression

#Runtime: 28 ms, faster than 69.38% of Python3 online submissions for Validate IP Address.
#Memory Usage: 13.6 MB, less than 97.68% of Python3 online submissions for Validate IP Address.

class Solution:
    #regex
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    pattern_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')
    def validIPAddress(self, IP: str) -> str:
        if self.pattern_IPv4.match(IP):
            return "IPv4"
        elif self.pattern_IPv6.match(IP):
            return "IPv6"
        return "Neither"

s = Solution()
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))



#Invalid
# from ipaddress import ip_address, IPv6Address
#
# class Solution:
#     def validIPAddress(self, IP: str) -> str:
#         try:
#             return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
#         except ValueError:
#             return "Neither"