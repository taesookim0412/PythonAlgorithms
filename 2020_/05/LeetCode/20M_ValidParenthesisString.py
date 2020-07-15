# For the last challenge you must become an alcoholic. Solve this problem.
# Oh yeah and it's the hardest problem in the set.
# Oh yeah and it'll be the easiest answer ever with an original solution.
#Runtime: 52 ms, faster than 5.39% of Python3 online submissions for Valid Parenthesis String.
#Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions for Valid Parenthesis String.
#05-30-2020_
#Thx LeetCode Looking Forward To June's Challenge (Integrate it into my schedule)

# 05-30-2020_
# fails:
# )  (*)
# (*))  )


#Input: ")()("
# LR DDP:
# )=-1
# (=+1
# *=Wildcard
# DP1: [0, -1, 0, 1, 0]
##if <0 and ) : if dp[i] + astsks < 0 return False
#Two forloops
# Reversal DP:
# DP2: [0, 1, 0, -1, 0]
##if >0 and (: if dp[i] + astsks < 0 return False
#
#
#
#
#
#
#
#
#
#
#
# scs:

# (())

# L:3 R:4 A:2
# (((*)*)))
#
#
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = [0] * (len(s) + 1)
        astsks = 0
        for i in range(len(s)):
            print(dp)
            if s[i] == '(':
                dp[i + 1] = dp[i] + 1
            elif s[i] == ')':
                dp[i + 1] = dp[i] - 1
            elif s[i] == '*':
                astsks += 1
                dp[i + 1] = dp[i]
            if dp[i + 1] + astsks < 0:
                return False
        #dbg purpsps
        dp = [0] * (len(s) + 1)
        bkwdI = 0
        astsks = 0
        for i in range(len(s) - 1, -1, -1):
            print(dp)
            if s[i] == '(':
                dp[bkwdI + 1] = dp[bkwdI] + 1
            elif s[i] == ')':
                dp[bkwdI + 1] = dp[bkwdI] - 1
            elif s[i] == '*':
                astsks += 1
                dp[bkwdI + 1] = dp[bkwdI]
            if dp[bkwdI + 1] - astsks > 0:
                print(dp[bkwdI + 1], astsks)
                return False
            bkwdI +=1
        return True

sol = Solution()
print(sol.checkValidString("()"))
print(sol.checkValidString(")()("))

#TC: T
print(sol.checkValidString("(*))"))

#TC: T
print(sol.checkValidString("(*()"))

#TC: T
print(sol.checkValidString("((*)"))
