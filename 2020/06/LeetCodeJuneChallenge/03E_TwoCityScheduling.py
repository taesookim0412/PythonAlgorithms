import heapq
from typing import List
#Runtime: 36 ms, faster than 90.00% of Python3 online submissions for Two City Scheduling.
#Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Two City Scheduling.

#Two pass (Actually one pass)
class Solution:
    #O(NLog(N)) Runtime
    #[[10,20],[30,200],[400,50],[30,20]]
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #There are no constraints between the people in costs[i]??
        diffsA = []
        diffsB = []
        sum1 = 0
        sum2 = 0
        print(len(costs))
        for i in range(len(costs)):
            diffsA.append([costs[i][0] - costs[i][1], i])
            diffsB.append([costs[i][1] - costs[i][0], i])
        diffsA.sort()
        diffsB.sort()
        print(diffsA)
        print(diffsB)

        passed = {}

        for i in range(len(costs)//2):
            sum1 += costs[diffsA[i][1]][0]
            passed[diffsA[i][1]] = True
            sum2 += costs[diffsB[i][1]][1]
        passScan = 0
        for i in range(len(costs)//2):
            sum1 += costs[diffsB[i][1]][1]
            if diffsB[i][1] in passed:
                passScan += 1
                sum1 -= costs[diffsB[i][1]][1]
            sum2 += costs[diffsA[i][1]][0]
        Li = len(costs)//2
        while passScan > 0:
            if diffsB[Li][1] in passed:
                passScan += 1
                sum1 -= costs[diffsB[Li][1]][1]
            else:
                sum1 += costs[diffsB[Li][1]][1]
                passScan -=1
        return(sum1)
        #print(sum2)

        #for i in range(len(costs)//2):












        # TODO: Make time for dynamic solution
        # dp = [0 for _ in range(len(costs)+1)]
        # for i in range(len(costs)):
        #     dp[i+1] = dp[i] + min(costs[i][0], costs[i][1])
        #
        # print(dp)


#110
#print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
#1859
#print(Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

#20269
print(Solution().twoCitySchedCost([[33,135],[849,791],[422,469],[310,92],[253,489],[995,760],[852,197],[658,216],[679,945],[197,341],[362,648],[22,324],[408,25],[505,734],[463,279],[885,512],[922,850],[784,500],[557,860],[528,367],[877,741],[554,545],[598,888],[558,104],[426,427],[449,189],[113,51],[201,221],[251,62],[981,897],[392,519],[115,70],[961,109],[512,678],[476,708],[28,902],[763,282],[787,774],[925,475],[253,532],[100,502],[110,857],[822,942],[231,186],[869,491],[651,344],[239,806],[651,193],[830,360],[427,69],[776,875],[466,81],[520,959],[798,775],[875,199],[110,396]]))