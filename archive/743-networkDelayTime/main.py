from typing import *

"""
TODO: 用 Dijkstra's 算法更快，求出最小支撑树。
"""

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0

        weights = [{} for _ in range(N + 1)]
        for u, v, w in times:
            weights[u][v] = w

        queue = [K]
        dp = { K: 0 } # u: time(u)
        while queue:
            u = queue.pop()
            u_time = dp[u]
            for v, w in weights[u].items():
                # print(u, v, w)
                v_time = u_time + w
                if v not in dp or dp[v] > v_time:
                    dp[v] = v_time
                    queue.append(v)

        if len(dp) < N:
            return -1

        return max(dp.values())

sol = Solution()
data = [[2,1,1],[2,3,1],[3,4,1]], 4, 2 # 2
print(*data)
res = sol.networkDelayTime(*data)
print(res)
