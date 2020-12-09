from typing import *
from math import *


"""
根据正数的个数做分析：
正数 >= 3 个：三个最大的正数；两个最小负数和一个最大正数
正数 = 2 个：两个最小负数和一个最大正数；两个正数和最大非正数
正数 = 1 个：一个最大正数和两个最小负数
正数 = 0 个：三个最大非正数
因此总是比较三个最大数之积、两个最小数和一个最大数之积。
"""

import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap3 = [] # 用最小堆记录最大的三个数字
        heap2 = [] # 用最大堆记录最小的两个数字
        for i in range(3):
            heapq.heappush(heap3, nums[i])
            heapq.heappush(heap2, -nums[i])
        heapq.heappop(heap2)

        for i in range(3, len(nums)):
            if nums[i] > heap3[0]:
                heapq.heappushpop(heap3, nums[i])
            if -nums[i] > heap2[0]:
                heapq.heappushpop(heap2, -nums[i])

        return max(heap3[0] * heap3[1] * heap3[2], heap2[0] * heap2[1] * max(heap3))


sol = Solution()
data = [1,2,3] # 6
data = [1,2,3,4] # 24
print(data)
res = sol.maximumProduct(data)
print(res)
