from typing import *
from math import *

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

    def canWinNim2(self, n: int) -> bool:
        # n <= 3, first player win
        if n <= 3:
            return True
        dp = [True] * 3
        for k in range(4, n + 1):
            win = False in dp
            # print(k, win)
            dp[:] = dp[1], dp[2], win

        return dp[-1]

sol = Solution()
data = 4 # false
data = 100
data = 1348820612
print(data)
res = sol.canWinNim(data)
print(res)
