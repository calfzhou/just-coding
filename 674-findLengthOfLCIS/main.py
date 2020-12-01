from typing import *

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxCnt = 1
        begin = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                maxCnt = max(maxCnt, i - begin)
                begin = i

        return max(maxCnt, len(nums) - begin)

sol = Solution()
data = [1,3,5,4,7] # 3
data =  [2,2,2,2,2] # 1
data = [1,3,5,7] # 4
res = sol.findLengthOfLCIS(data)
print(res)
