from typing import *
from math import *


"""
先按 121-maxProfit 里面的方法计算出单次买卖的最大收益（和对应的买卖日子）。
在这笔交易前后的两个日期段落内，各找出最大收益的一笔买卖，二者取最大，与前一笔共同构成最终的两笔买卖。

但这不一定是最优方案，还有可能把最大收益的单笔买卖拆开，在中间某天卖掉，之后再次买入。
用类似的方法算出
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        def helper(first, last):
            if first >= last:
                return 0, None, None
            min_price = prices[first], first
            profit = 0, None, None
            for i in range(first, last + 1):
                price = prices[i]
                if price - min_price[0] > profit[0]:
                    profit = price - min_price[0], min_price[1], i
                if price < min_price[0]:
                    min_price = price, i
            # print(first, last, min_price, profit)
            return profit

        def helper2(first, last):
            if first >= last:
                return 0, None, None
            max_price = prices[first], first
            loss = 0, None, None
            for i in range(first, last + 1):
                price = prices[i]
                if price - max_price[0] < loss[0]:
                    loss = price - max_price[0], max_price[1], i
                if price > max_price[0]:
                    max_price = price, i
            # print(first, last, max_price, loss)
            return loss

        n = len(prices)
        profit1, buy, sell = helper(0, n - 1)
        if not sell:
            return 0

        profit2 = max(helper(0, buy - 1)[0], helper(sell + 1, n - 1)[0])

        loss, _, _ = helper2(buy + 1, sell - 1)
        return max(profit1 + profit2, profit1 - loss)


sol = Solution()
data = [3,3,5,0,0,3,1,4] # 6
# data = [1,2,3,4,5] # 4
# data = [7,6,4,3,1] # 0
# data = [2, 4, 1] # 2
data = [6,1,3,2,4,7] # 7
print(data)
res = sol.maxProfit(data)
print(res)
