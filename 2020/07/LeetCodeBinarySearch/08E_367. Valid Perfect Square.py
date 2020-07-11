import collections
import numpy as np
from typing import List

#but C++ is 4ms xDD
# class Solution {
# public:
#     bool isPerfectSquare(int num){
#     int i=0;
#     int j=num;
#     long int mid=0;
#     while(i<=j){
#         mid=i+((j-i)/2);
#         if(mid*mid==num){
#             return true;
#         }
#           else if(mid*mid<num){
#             i=mid+1;
#         }
#         else if(mid*mid>num){
#             j=mid-1;
#         }
#     }
#     return false;
# }
# };

#Two Pointer TLE

#Binary Search
#Runtime: 56 ms, faster than 11.98% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 14.2 MB, less than 5.26% of Python3 online submissions for Valid Perfect Square.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l <= r:
            mid = l + (r-l)//2
            sqrd = mid*mid
            if sqrd==num:
                return True
            elif sqrd < num:
                l = mid +1
            else:
                 r = mid - 1
            print(mid,l,r)
        return False


#Runtime: 76 ms, faster than 5.24% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 15.9 MB, less than 5.26% of Python3 online submissions for Valid Perfect Square.
#Stack
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        squares = [1]
        while squares[-1] < num:
            squares.append((len(squares) +1)**2)
            if squares[-1] == num:
                return True
        return False

s = Solution()
print(s.isPerfectSquare(15))