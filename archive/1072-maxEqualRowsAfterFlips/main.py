from typing import *
from math import *


"""
当某一行经过若干列的翻转后变成全零（或全一）的时候，所有初始跟它完全相同或者刚好互补的行，也变成了全一（或全零）。
因此可以认为完全相同或更好互补的行是一组，只要找到最大的组即可。
"""

"""
用字典加速查找相同的组。考察互补的话，就先统一翻转为第一个数字为 0 的状态。
"""

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        groups = {} # row: group size
        for row in matrix:
            if row[0] == 0:
                key = tuple(row)
            else:
                key = tuple(1 - x for x in row)
            groups[key] = groups.setdefault(key, 0) + 1

        # print(groups)
        return max(groups.values())


################################

def norm(row):
    flip = row[0] == 1
    for x in row:
        yield 1 - x if flip else x

def same_group(row1, row2):
    for a, b in zip(norm(row1), norm(row2)):
        if a != b:
            return False
    return True

class SolutionTooSlow(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        groups = {} # 行号 -> 与该行同组的行数
        for i in range(len(matrix)):
            for j in groups:
                if same_group(matrix[i], matrix[j]):
                    groups[j] += 1
                    break
            else:
                groups[i] = 1

        return max(groups.values())


sol = Solution()
data = [[0,1],[1,1]] # 1
data = [[0,1],[1,0]] # 2
data = [[0,0,0],[0,0,1],[1,1,0]] # 2
print(data)
res = sol.maxEqualRowsAfterFlips(data)
print(res)
