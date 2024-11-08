from typing import *
from math import *


class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        size = m * n
        res = [[None] * n for _ in range(m)]

        pos = k % size
        for r in range(m):
            for c in range(n):
                r1, c1 = divmod(pos, n)
                res[r1][c1] = grid[r][c]
                pos = (pos + 1) % size

        return res


sol = Solution()
data = [[1,2,3],[4,5,6],[7,8,9]], 1 # [[9,1,2],[3,4,5],[6,7,8]]
data = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4 # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
print(*data)
res = sol.shiftGrid(*data)
print(res)
