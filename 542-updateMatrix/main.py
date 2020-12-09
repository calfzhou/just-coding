from typing import *
from math import *


"""
设结果为 dp。
对于 matrix 中的 0，对应的 dp 为 0。
否则 dp[cell] = min(上下左右) { dp[相邻] } + 1。
可以从 0 开始，逐渐往外推，直到覆盖所有的位置。
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        height = len(matrix)
        width = len(matrix[0])
        dp = [[None] * width for _ in range(height)]
        queue = []
        for r in range(height):
            for c in range(width):
                if matrix[r][c] == 0:
                    dp[r][c] = 0
                    queue.append((r, c))

        def neighbors():
            if r > 0:
                yield r - 1, c
            if r < height - 1:
                yield r + 1, c
            if c > 0:
                yield r, c - 1
            if c < width - 1:
                yield r, c + 1

        step = 1
        next_queue = []
        while queue:
            r, c = queue.pop()
            for r1, c1 in neighbors():
                if dp[r1][c1] is None:
                    dp[r1][c1] = step
                    next_queue.append((r1, c1))
            if not queue:
                step += 1
                queue, next_queue = next_queue, queue

        return dp


sol = Solution()
data = [[0,0,0],
 [0,1,0],
 [0,0,0]]
"""
[[0,0,0],
 [0,1,0],
 [0,0,0]]
"""
data = [[0,0,0],
 [0,1,0],
 [1,1,1]]
"""
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""
print(data)
res = sol.updateMatrix(data)
print(res)
