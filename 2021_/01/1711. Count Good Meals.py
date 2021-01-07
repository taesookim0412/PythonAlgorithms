#1584ms 20.7 MB
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        dels = collections.defaultdict(int)
        max_num = 0
        for dish in deliciousness:
            dels[dish] += 1
            max_num = max(max_num, dish)
        pows = [2**i for i in range(22)]
        for dish in deliciousness:
            for powNum in pows:
                diff = powNum - dish
                if diff > max_num:
                    break
                if diff in dels:
                    res += dels[diff]
                if diff==dish:
                    res -= 1
        return (res//2) % 1000000007

##2 Million 100 thousand elements with numpy array: 3512 ms	51.5 MB
import numpy as np
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        dels = np.zeros(2100000, dtype=int)
        max_num = 0
        for dish in deliciousness:
            dels[dish] += 1
            max_num = max(max_num, dish)
        pows = [2**i for i in range(22)]
        for dish in deliciousness:
            for powNum in pows:
                diff = powNum - dish
                if diff > max_num:
                    break
                if diff >= 0:
                    res += dels[diff]
                if diff==dish:
                    res -= 1
        return (res//2) % 1000000007

#2 Million 100 thousand elements W/O numpy: 6184ms, 35.9MB
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res = 0
        dels = [0 for _ in range(2100000)]
        max_num = 0
        for dish in deliciousness:
            dels[dish] += 1
            max_num = max(max_num, dish)
        pows = [2**i for i in range(22)]
        for dish in deliciousness:
            for powNum in pows:
                diff = powNum - dish
                if diff > max_num:
                    break
                if diff >= 0:
                    res += dels[diff]
                if diff==dish:
                    res -= 1
        return (res//2) % 1000000007
#	2152 ms	70.9 MB
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ct = 0
        ctr = collections.defaultdict(int)
        max_num = max(deliciousness)
        pows = [2**i for i in range(22)]
        for dish in deliciousness:
            for powNum in pows:
                diff = powNum - dish
                if diff > max_num:
                    break
                ct += ctr[diff]
            ctr[dish] += 1
        return ct % 1000000007;
#O(N*22) Runtime (No Break) 3628ms
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ct = 0
        ctr = collections.defaultdict(int)
        for dish in deliciousness:
            for i in range(22):
                ct += ctr[2**i - dish]
            ctr[dish] += 1
        return ct % 1000000007;

#Original O(N^2) Runtime (TLE)
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        moduloNum = pow(10, 9) + 7
        twos = set()
        for i in range(21):
            twos.add(pow(2, i) % moduloNum)
        ct = 0
        for i in range(len(deliciousness)):
            for j in range(i + 1, len(deliciousness)):
                total = (deliciousness[i] + deliciousness[j]) % moduloNum
                if total in twos:
                    ct = (ct + 1) % moduloNum
        return ct
