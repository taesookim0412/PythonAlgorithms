from typing import List


#Binary search a brain teaser and create results based on the variables
#except u manipulate the results to return the answer
#(just use if else).

#TODO: Binary Search

#Runtime: 152 ms, faster than 60.72% of Python3 online submissions for H-Index II.
#Memory Usage: 20.3 MB, less than 82.92% of Python3 online submissions for H-Index II.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        if n==0: return 0
        r = n - 1
        while l <= r:
            mid = (l+r)>>1
            elem = citations[mid]
            if elem >= n - mid:
                r= mid - 1
            else:
                l = mid+1
        return n-l


#[100] -> 1:
    #1 paper
#[1, 2] -> 1:
    #1 paper
#[0] -> 0:
s = Solution()
#print(s.hIndex([1,2, 3, 4, 5]))
#print(s.hIndex([100]))
#0
print(s.hIndex([0, 0]))
#1
print(s.hIndex([0,1]))
