from typing import *

import itertools

def nums(s):
    if s == '0' or s[0] != '0':
        yield s

    if s[-1] == '0':
        return

    for i in range(1, len(s)):
        a, b = s[:i], s[i:]
        if a[0] == '0' and a != '0':
            break
        yield '.'.join((a, b))

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        N = len(S)
        res = []
        for i in range(1, N):
            x, y = S[:i], S[i:]
            # print(x, y, ':')
            # print(list(nums(x)))
            # print(list(nums(y)))
            res.extend(''.join(('(', a, ', ', b, ')')) for a, b in itertools.product(nums(x), nums(y)))

        return res


sol = Solution()
data = "(123)" # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
data = "(00011)" # ["(0.001, 1)", "(0, 0.011)"]
data = "(0123)" # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
data = "(100)" # [(10, 0)]
print(data)
res = sol.ambiguousCoordinates(data)
print(res)
