from typing import *
from math import *


"""
跟 122-maxProfit 一样，只是再卖出的时候，把手续费用减去即可。
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        EMPTY, HOLD = range(2)
        dp = [[None, None] for _ in range(n)] # [空仓, 持仓]
        dp[0][EMPTY] = 0
        dp[0][HOLD] = -prices[0]
        for i in range(1, n):
            dp[i][EMPTY] = max(dp[i - 1][EMPTY], dp[i - 1][HOLD] + prices[i] - fee)
            dp[i][HOLD] = max(dp[i - 1][HOLD], dp[i - 1][EMPTY] - prices[i])

        # print(dp)
        return dp[-1][EMPTY]


sol = Solution()
data = [1, 3, 2, 8, 4, 9], 2 # 8
print(*data)
res = sol.maxProfit(*data)
print(res)
