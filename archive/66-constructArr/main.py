from typing import *
from math import *


"""
B[i] = PI(j != i) { A[j] }
     = PI(j < i) { A[j] } * PI(j > i) { A[j] }

dp1[i] = PI(j < i) { A[j] } = dp[i - 1] * A[i - 1]
dp2[i] = PI(j > i) { A[j] } = A[i + 1] * dp[i + 1]
"""

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        if not a:
            return []

        dp1 = [1] * n
        dp2 = [1] * n
        for i in range(n - 1):
            dp1[i + 1] = dp1[i] * a[i]
            dp2[-i - 2] = dp2[-i - 1] * a[-i - 1]

        for i in range(n):
            dp1[i] *= dp2[i]
        return dp1


sol = Solution()
data = [1,2,3,4,5] # [120,60,40,30,24]
print(data)
res = sol.constructArr(data)
print(res)
