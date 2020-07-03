import collections
#what a dumb question
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        for x in S:
            if x == "(":
#1. A valid parentheses string S is primitive if it is nonempty,
#2. and there does not exist a way to split it into S = A+B,
#3. with A and B nonempty valid parentheses strings.
#1. all paranthese strings are nonempty
#2. What does that even mean Split it into S = A +B
#ur trying to explain a problem NOT UR ANSWER
#like i can say For my algorithm I'm going to Run my functions F = A +B and that would make more sense
#that doesnt mean anything use english
#3. all paren strings are empty


#huh
# class Solution:
#     def removeOuterParentheses(self, S: str) -> str:
#         L = R = 0
#         closures = 0
#         adds = collections.defaultdict(dict)
#         if S[0] == "(": L += 1
#         elif S[0] == ")": R += 1
#         for i in range(1, len(S)):
#             if S[i] == "(":
#                 L += 1
#             elif S[i] == ")":
#                 R += 1
#             if S[i-1] == "(" and S[i] == ")":
#                 adds[closures] = min(L, R)
#                 closures += 1
#                 L = R = 0
#         ret = ""
#         print(adds)
#         for i in range(closures):
#             times = adds[i]
#             for j in range(times):
#                 ret += "("
#             for j in range(times):
#                 ret += ")"
#         return ret

s = Solution()
print(s.removeOuterParentheses("(()())(())"))