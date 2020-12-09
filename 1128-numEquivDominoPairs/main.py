from typing import *
from math import *


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        groups = {} # dominoe: cnt
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            groups[a, b] = groups.setdefault((a, b), 0) + 1

        total = 0
        for cnt in groups.values():
            if cnt > 1:
                total += int(cnt * (cnt - 1) / 2)

        return total


sol = Solution()
data = [[1,2],[2,1],[3,4],[5,6]] # 1
print(data)
res = sol.numEquivDominoPairs(data)
print(res)
