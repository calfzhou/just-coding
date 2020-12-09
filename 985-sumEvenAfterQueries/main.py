from typing import *
from math import *


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = sum(x for x in A if x % 2 == 0)
        res = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                ans -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                ans += A[idx]
            res.append(ans)

        return res

sol = Solution()
data = [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]] # [8,6,2,4]
print(*data)
res = sol.sumEvenAfterQueries(*data)
print(res)
