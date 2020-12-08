from typing import *
from math import *


"""
看手上持有的现金，买入相当于现金减少，卖出相当于现金增加。
买入时要花尽量少的钱，卖出时要拿到尽量多的钱。所以不管买入还是卖出，都是要在操作后，持有的现金最多。

buy[i] 表示在第 i 天结束的时候，如果持有股票，最大的剩余现金量，初始值为第一天股价的负数。
sell[i] 表示在第 i 天结束的时候，如果不持有股票（可能曾经持有过，也可能没有），最大的剩余现金量，初始值为 0。
buy[i] = max(buy[i - 1], -price[i])。
    即要么前一天就已经持有，要么今天购买。
sell[i] = max(sell[i - 1], buy[i - 1] + price[i]) = max(sell[i - 1], buy[i] + price[i])。
    即要么前一天就不持有，要么今天卖出。
递推过程，只需要保留前一天的 buy 和 sell 值即可。
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = -prices[0]
        sell = 0
        # print(buy, sell)
        for price in prices[1:]:
            sell = max(sell, buy + price)
            buy = max(buy, -price)
            # print(buy, sell)

        return sell

sol = Solution()
data = [7,1,5,3,6,4] # 5
# data = [7,6,4,3,1] # 0
print(data)
res = sol.maxProfit(data)
print(res)
