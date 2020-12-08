from typing import *
from math import *


"""
对 121-maxProfit 思路稍作扩展。
buy[i][j] 表示在第 i 天结束的时候，如果至多第 j 次持有股票，最大的剩余现金量。
sell[i][j] 表示在第 i 天结束的时候，如果完成了至多 j 次买卖，最大的剩余现金量。

buy[i][1] = max(buy[i - 1][1], -price[i])。
sell[i][1] = max(sell[i - 1][1], buy[i - 1][1] + price)。

buy[i][2] = max(buy[i - 1][2], sell[i - 1][1] - price[i])。
    即要么前一天已经是第二次持有，要么今天完成第二次买入。
sell[i][2] = max(sell[i - 1][2], buy[i - 1][2] + price[i])。
    即要么前一天已经第二次卖出，要么今天卖出。

对于两次买卖，都只需要记录前一天的数据。
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy1 = -prices[0]
        sell1 = 0
        buy2 = buy1
        sell2 = 0
        print(buy1, sell1, buy2, sell2)

        for price in prices[1:]:
            sell1_prev = sell1
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1_prev - price)
            print(buy1, sell1, buy2, sell2)

        return sell2


sol = Solution()
data = [3,3,5,0,0,3,1,4] # 6
# data = [1,2,3,4,5] # 4
# data = [7,6,4,3,1] # 0
# data = [2, 4, 1] # 2
# data = [6,1,3,2,4,7] # 7
data = [1,2,3,4,5] # 4
data = [3,2,6,5,0,3] # 7
print(data)
res = sol.maxProfit(data)
print(res)
