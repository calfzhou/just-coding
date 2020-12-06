from typing import *

"""
贪心算法。
先假设所有人都去 A，然后挑选 N 个人改成去 B。第 i 个人由 A 改 B，改变的费用是：
`cost[i][1] - cost[i][0]`。每次都取这个值最小的人去 B。
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        return sum(c[0] for c in costs) + sum(sorted(c[1] - c[0] for c in costs)[:len(costs) // 2])

sol = Solution()
data = [[10,20],[30,200],[400,50],[30,20]] # 110, (A, A, B, B)
print(data)
res = sol.twoCitySchedCost(data)
print(res)
