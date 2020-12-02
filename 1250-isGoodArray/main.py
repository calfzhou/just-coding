from typing import *
from math import *

# 裴蜀定理

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        d = nums[0]
        for b in nums[1:]:
            d = gcd(d, b)
            if d == 1:
                return True

        return d == 1

sol = Solution()
data = [12,5,7,23] # true
data = [29,6,10] # true
data = [3, 6] # false
print(data)
res = sol.isGoodArray(data)
print(res)
