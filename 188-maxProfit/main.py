from typing import *
from math import *


"""
把 123-maxProfit 扩展到更一般的情况即可。
buy[i][j] 表示在第 i 天结束的时候，如果至多第 j 次持有股票，最大的剩余现金量。
sell[i][j] 表示在第 i 天结束的时候，如果完成了至多 j 次买卖，最大的剩余现金量。

buy[i][1] = max(buy[i - 1][1], -price[i])。
sell[i][1] = max(sell[i - 1][1], buy[i - 1][1] + price)。

buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - price[i])。
sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + price[i])。

另外最多可以买卖 floor(n / 2) 次。
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        k = min(k, len(prices) >> 1)
        if k == 0:
            return 0

        buys = [-prices[0]] * k
        sells = [0] * k
        # print(*zip(buys, sells))

        for price in prices[1:]:
            sell_prev = 0
            for j in range(k):
                sell = sells[j]
                sells[j] = max(sells[j], buys[j] + price)
                buys[j] = max(buys[j], sell_prev - price)
                sell_prev = sell
            # print(*zip(buys, sells))

        return sells[-1]


sol = Solution()
data = 2, [2,4,1] # 2
data = 2, [3,2,6,5,0,3] # 7
print(*data)
res = sol.maxProfit(*data)
print(res)
