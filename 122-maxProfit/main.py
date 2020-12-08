from typing import *
from math import *


"""
虽然最后一天手上的股票都要卖光，但中间的日子，是可以持有股票的，所以空仓和持仓状态都要考虑。
f(k, status) 表示第 k 天的状态是 status，到这天为止的最大收益。
因为收益就是计算差价，可以买入的时候减去当前价格，卖出时加上当前价格。

- f(k, 空仓)
  可以前一天是空仓，今天保持：f(k - 1, 空仓)。
  或者前一天是持仓，今天卖掉：f(k - 1, 持仓) + prices[i]。
  二者取最大。
- f(k, 持仓)
  可以前一天是持仓，今天保持：f(k - 1, 持仓)。
  或者前一天是空仓，今天买入：f(k - 1, 空仓) - prices[i]。
  二者取最大。
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
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
            dp[i][EMPTY] = max(dp[i - 1][EMPTY], dp[i - 1][HOLD] + prices[i])
            dp[i][HOLD] = max(dp[i - 1][HOLD], dp[i - 1][EMPTY] - prices[i])

        print(dp)
        return dp[-1][EMPTY]


sol = Solution()
data = [7,1,5,3,6,4] # 7
# data = [1,2,3,4,5] # 4
# data = [7,6,4,3,1] # 0
print(data)
res = sol.maxProfit(data)
print(res)
