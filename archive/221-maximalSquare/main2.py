from typing import *

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width = len(matrix[0])

        # topOnes[col] 表示 (上一行, col) 及其上边连续「1」的个数
        topOnes = [0] * width

        # squares[col] 表示以 (上一行, col) 为右下角全「1」正方形边长
        squares = [0] * width

        biggest = 0
        for row in range(len(matrix)):
            leftOnes = 0
            for col in range(width):
                if matrix[row][col] == '0':
                    leftOnes = 0
                    topOnes[col] = 0
                    currSquare = 0
                else:
                    currSquare = 1
                    if row > 0 and col > 0:
                        currSquare += min(leftOnes, topOnes[col], squares[col - 1])
                    topOnes[col] += 1
                    leftOnes += 1

                    biggest = max(biggest, currSquare)

                if col > 0:
                    squares[col - 1] = prevSquare
                prevSquare = currSquare

            squares[-1] = prevSquare

        print(leftOnes)
        print(topOnes)
        print(squares)
        return biggest ** 2

sol = Solution()
data = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] # 4
# data = [["0","1"],["1","0"]] # 1
# data = [["0"]] # 0
# data = [["1","1"],["1","1"]] # 4
res = sol.maximalSquare(data)
print(res)
