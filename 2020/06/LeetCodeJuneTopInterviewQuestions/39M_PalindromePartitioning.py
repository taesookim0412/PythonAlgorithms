from typing import List
#"aa", "b"
#"a", "ab"


#Runtime: 80 ms, faster than 75.51% of Python3 online submissions for Palindrome Partitioning.
#Memory Usage: 14.1 MB, less than 46.63% of Python3 online submissions for Palindrome Partitioning.

#TODO: Make an original solution. Recursion in order to receive substring permutations. Very interesting.
#Seems the pop solution is the standard solution here...
#

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()
        res = []
        dfs(s, [], res)
        return res

class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        for i in range(1, len(s)+1):
            #[['a', 'a', 'b'], ['a', 'ab'], ['aa', 'b'], ['aab']]
            if s[:i] == s[i-1::-1]:
                for data in self.partition(s[i:]):
                    res.append([s[:i]]+data)
                    print(s[:i], data)
        if not res:
            return [[]]
        return res


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        data = []
        for i in range(1, len(s)+1):
            if s[:i] == s[i-1::-1]:
                for x in self.partition(s[i:]):
                    print(x)
                    data.append([s[:i]] + x)
        if not data:
            return [[]]
        return data


s = Solution()
print(s.partition("aab"))