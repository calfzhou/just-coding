from typing import *
from math import *

"""
用 f(k) 表示只有前 k 天的子问题对应的最大收益。
考察最后一次买入是第 i 天（1 <= i < k），卖出应该在第 i 天之后价格最高的那天，对应的收益为 profit(i)。
f(k) = max(i) { profit(i) + f(i - 2) }
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        dp = [0] * n
        for k in range(1, n):
            # 记录每一天过去之后，能见到的最高价格。
            max_prices = [-1] * k
            max_prices[-1] = prices[k]
            for i in range(k - 2, -1, -1):
                max_prices[i] = max(prices[i + 1], max_prices[i + 1])

            best = 0
            for i in range(k):
                profit = max_prices[i] - prices[i]
                if i > 2:
                    profit += dp[i - 2]
                best = max(best, profit)

            dp[k] = best

        # print(dp)
        return dp[-1]

sol = Solution()
data = [1,2,3,0,2] # 3, [买入, 卖出, 冷冻期, 买入, 卖出]
print(data)
res = sol.maxProfit(data)
print(res)
