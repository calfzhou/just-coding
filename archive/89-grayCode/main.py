from typing import *


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        cap = 1
        for _ in range(n):
            res.extend(x | cap for x in res[::-1])
            cap <<= 1
        return res


class Solution1(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        half = self.grayCode(n - 1)
        cap = 1 << (n - 1)
        res = []
        res[:] = half
        res.extend(x | cap for x in half[::-1])
        return res

sol = Solution()
data = 2 # [0,1,3,2]
# data = 0 # [0]
print(data)
res = sol.grayCode(data)
print(res)
for x in res:
    print(bin(x))
