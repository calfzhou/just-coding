from typing import *
from math import *

"""
如果能跳到第 k 个位置，则所有 k 前面的位置都可以到达。
检查 k 及其前面的每个元素，计算从各个元素跳一次最远能跳到的位置，更新 k。
持续计算直到 k 够到最后一个位置，或者 k 不再变大。
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        longest = 0
        for i in range(n):
            longest = max(longest, i + nums[i])
            if longest >= n - 1:
                # print('reachable at', i)
                return True
            elif longest == i:
                # Cannot go further anymore.
                # print('stopped at', i)
                return False

        return False

    """
    dp[i] 记录从 i 能否到达最后一个位置。
    要计算 dp[i]，考虑从 i 往后跳 x 步（1 <= x <= nums[i]），
    dp[i] = has_true(x) { dp(i + x) }
    """
    def canJump_Slow(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            for x in range(1, nums[i] + 1):
                if dp[i + x]:
                    dp[i] = True
                    break

        print(dp)
        return dp[0]

sol = Solution()
data = [2,3,1,1,4] # True
# data = [3,2,1,0,4] # False
print(data)
res = sol.canJump(data)
print(res)
