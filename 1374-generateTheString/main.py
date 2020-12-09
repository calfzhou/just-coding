from typing import *
from math import *


import collections

def verify(n, s):
    if len(s) != n:
        print('string length is not', n)
        return False

    counter = collections.Counter(s)
    for k, c in counter.items():
        if c & 1 == 0:
            print('letter', k, 'occur', c, 'times')
            return False

    return True


################################################################


class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n & 1 == 0:
            return 'a' * (n - 1) + 'b'
        else:
            return 'a' * n


sol = Solution()
data = 4
# data = 2
# data = 7
print(data)
res = sol.generateTheString(data)
print(res)
print(verify(data, res))
