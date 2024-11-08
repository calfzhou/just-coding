from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            m = max(dp[0] + nums[i], dp[1])
            dp[0], dp[1] = dp[1], m

        return dp[-1]

    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

sol = Solution()
data = [1,2,3,1] # 4, (1, 3)
data = [2, 7, 9, 3, 1] # 12, (1, 3, 5)
# data = [0] # 0
print(data)
res = sol.rob(data)
print(res)
