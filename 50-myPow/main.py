from typing import *
from math import *

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        neg, n = n < 0, abs(n)

        res = 1.0
        x2 = x
        while n > 0:
            if n & 1 == 1:
                res *= x2
            x2 *= x2
            n >>= 1

        return 1.0 / res if neg else res

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        neg, n = n < 0, abs(n)

        def _pow(a, m):
            if m == 1:
                return a
            odd, m = m & 1, m >> 1
            ans = _pow(a, m)
            ans *= ans
            if odd:
                ans *= a
            return ans

        res = _pow(x, n)
        return 1.0 / res if neg else res

sol = Solution()
data = 2.00000, 10 # 1024.00000
# data = 2.10000, 3 # 9.26100
# data = 2.00000, -2 # 0.25000
print(data)
res = sol.myPow(*data)
print(res)
