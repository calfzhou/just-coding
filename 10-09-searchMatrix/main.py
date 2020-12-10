from typing import *
from math import *


"""
用 target 跟当前 [r, c] 格子的值比较，如果相等就找到了。
如果 target 较小，就继续看 [r, c-1]。
如果 target 较大，就继续看 [r+1, c]。
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, n - 1
        while r < m and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False


sol = Solution()
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
data = m, 5 # true
# data = m, 20 # false
print(*data)
res = sol.searchMatrix(*data)
print(res)
