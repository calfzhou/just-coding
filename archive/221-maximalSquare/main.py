from typing import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        # leftOnes[row][col] 表示 (row, col) 及其左边连续「1」的个数
        leftOnes = [[0] * width for _ in range(height)]
        topOnes = [[0] * width for _ in range(height)]

        # cache[row][col] 表示以 (row, col) 为右下角全「1」正方形边长
        cache = [[0] * width for _ in range(height)]

        biggest = 0
        for row in range(height):
            for col in range(width):
                if matrix[row][col] == '0':
                    continue

                leftOnes[row][col] = topOnes[row][col] = cache[row][col] = 1
                if row > 0:
                    topOnes[row][col] += topOnes[row - 1][col]
                if col > 0:
                    leftOnes[row][col] += leftOnes[row][col - 1]
                if row > 0 and col > 0:
                    cache[row][col] += min(topOnes[row - 1][col], leftOnes[row][col - 1], cache[row - 1][col - 1])
                biggest = max(biggest, cache[row][col])

        printMatrix(leftOnes)
        printMatrix(topOnes)
        printMatrix(cache)
        return biggest ** 2

def printMatrix(m):
    for row in m:
        print(row)
    print()

sol = Solution()
data = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] # 4
# data = [["0","1"],["1","0"]] # 1
# data = [["0"]] # 0
res = sol.maximalSquare(data)
print(res)
