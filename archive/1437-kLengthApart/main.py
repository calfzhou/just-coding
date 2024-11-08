from typing import *

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        lastOne = None
        for i, x in enumerate(nums):
            if x != 1:
                continue
            if lastOne is not None and i - lastOne - 1 < k:
                return False
            lastOne = i

        return True


sol = Solution()
data = [1,0,0,0,1,0,0,1], 2 # true
data = [1,0,0,1,0,1], 2 # false
data = [1,1,1,1,1], 0 # true
data = [0,1,0,1], 1 # true
res = sol.kLengthApart(*data)
print(res)
