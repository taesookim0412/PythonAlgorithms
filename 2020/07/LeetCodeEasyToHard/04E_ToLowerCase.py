#Runtime: 48 ms, faster than 6.45% of Python3 online submissions for To Lower Case.
#Memory Usage: 13.9 MB, less than 21.14% of Python3 online submissions for To Lower Case.

class Solution:
    def toLowerCase(self, str: str) -> str:
        stri = []
        for x in str:
            char = ord(x)
            if 65 <= char <= 90:
                stri += chr(char+32),
            else:
                stri += x
        return ''.join(stri)