import collections
import numpy as np
from typing import List

#Nim Game: 40/60
class Solution:
    #0: Player
    #1: Friend
    def canWinNim(self, n: int) -> bool:
        def playGame(n:int, turn:int):
            if n<=3:
                #if Enemy
                if turn&1:
                    return False
                #if Player's
                elif not turn&1:
                    return True
            return playGame(n-1, (turn+1)&1) or playGame(n-2, (turn+1)&1) or playGame(n-3, (turn+1)&1)
        diff = n - 3
        if 0<=n<=3: return True
        if 1 < diff%8 < 5: return True
        else: return False
        return playGame(n,0)