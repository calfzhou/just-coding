from typing import *
from math import *


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)

        return profit

sol = Solution()
data = [7,1,5,3,6,4] # 5
# data = [7,6,4,3,1] # 0
print(data)
res = sol.maxProfit(data)
print(res)
