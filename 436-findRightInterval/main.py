from typing import *
from math import *


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        if not intervals:
            return []

        n = len(intervals)
        by_left = sorted(range(n), key=lambda i: intervals[i][0])
        by_right = sorted(range(n), key=lambda i: intervals[i][1])
        # print(by_left)
        # print(by_right)

        res = [-1] * n
        i = 0
        for idx in by_right:
            right = intervals[idx][1]
            while i < n:
                if intervals[by_left[i]][0] >= right:
                    res[idx] = by_left[i]
                    break
                i += 1
            else:
                return res


sol = Solution()
data = [ [1,2] ] # [-1]
data = [ [3,4], [2,3], [1,2] ] # [-1, 0, 1]
# data = [ [1,4], [2,3], [3,4] ] # [-1, 2, -1]
print(data)
res = sol.findRightInterval(data)
print(res)
