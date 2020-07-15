from typing import List

#05/16/2020_
#Runtime: 3792 ms, faster than 5.00% of Python3 online submissions for Group Anagrams.
#Memory Usage: 16.4 MB, less than 47.17% of Python3 online submissions for Group Anagrams.
#https://leetcode.com/problems/group-anagrams/submissions/
#I dunno seems kinda slow


class Solution():
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        sol = []
        for i, a in enumerate(strs):
            sol.append(list(a))
            sol[i].sort()
            sol[i] = ''.join(sol[i])
            
        ans = []
        grpd = [0] * len(strs)
        for i, a in enumerate(sol):
            if grpd[i] == 0:
                ans.append([strs[i]])
                grpd[i] = 1
            for j in range(i, len(strs)):
                if j != i and sol[j] == a and grpd[j] == 0:
                    ans[len(ans)-1].append(strs[j])
                    grpd[j] = 1
                
        return ans
        
    def __init__(self):
        print(self.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    
Solution()