from typing import *


class Solution:
    """
    与 198-rob 相比，唯一的限制是第一个房子和最后一个房子不能都被偷（可以都不偷）。
    那么就计算强制不偷第一个房子的最大收益，和强制不偷第二个房子的最大收益，二者取最大即可。
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        # 不偷第一个房子
        a1, a2 = nums[1], max(nums[1:3])
        for i in range(3, n):
            a1, a2 = a2, max(a1 + nums[i], a2)

        # 不偷最后一个房子
        b1, b2 = nums[0], max(nums[:2])
        for i in range(2, n - 1):
            b1, b2 = b2, max(b1 + nums[i], b2)

        return max(a2, b2)

    """
    先只管前 n - 1 个房子，计算逻辑跟 198-rob 是一致的。
    考察最后一个房子（第 n 个），可以偷或者不偷，看哪个收益大。
    1. 不偷：那么总收益等于刚才计算过的 f(n-1)
    2. 偷：总收益等于 $n + f(n - 2)，但如果 f(n - 2) 对应的方案是偷第一间房子，就会失败。
    所以前面计算的时候，要记录下来第一间房间是否要偷的选择，如果 f(n - 2) 的方案是偷第一间房子，
    则需要计算一次强制不偷第一间房子的情况下的 f'(n - 2)， 总收益为 $n + f'(n - 2)
    最后在偷与不偷第 n 间房子的两种收益之间取最大即可。
    """
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)

        a1 = nums[0], True
        a2 = max(nums[:2]), nums[0] >= nums[1]
        b1 = 0
        b2 = nums[1]
        for i in range(2, n - 1):
            b1, b2 = b2, max(b1 + nums[i], b2)
            if a1[0] + nums[i] >= a2[0]:
                a1, a2 = a2, (a1[0] + nums[i], a1[1])
            else:
                a1, a2 = a2, a2

        if a1[1]:
            rob_last = b1 + nums[-1]
        else:
            rob_last = a1[0] + nums[-1]

        return max(rob_last, a2[0])

sol = Solution()
data = [2,3,2] # 3, (2)
# data = [1, 2, 3, 1] # 4, (1, 3)
# data = [0] # 0
print(data)
res = sol.rob(data)
print(res)
