from typing import *

"""
从两个数组分别取 i、j 个数（i + j = k），且取出的数是原数组中最大的子序列。归并两个子序列。
"""

def max_sub(nums, k):
    remain_drop = len(nums) - k
    stack = []
    for x in nums:
        while remain_drop > 0 and stack and stack[-1] < x:
            stack.pop()
            remain_drop -= 1

        if len(stack) < k:
            stack.append(x)
        else:
            remain_drop -= 1

    return stack


def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    res = []
    i, j = 0, 0
    while i < m or j < n:
        if nums1[i:] >= nums2[j:]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    return res

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        max_res = []
        for i in range(max(0, k - n), min(m, k) + 1):
            j = k - i
            sub1 = max_sub(nums1, i)
            sub2 = max_sub(nums2, j)
            res = merge(sub1, sub2)
            print(i, j, sub1, sub2, res)
            if res > max_res:
                max_res = res

        return max_res

sol = Solution()
data = [3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5 # [9, 8, 6, 5, 3]
data = [6,7,5], [4,8,1], 3 # [8,7,5]
data = [6, 7], [6, 0, 4], 5 # [6, 7, 6, 0, 4]
data = [3, 9], [8, 9], 3 # [9, 8, 9]
data = [8, 9], [3, 9], 3 # [9, 8, 9]
data = [7,6,1,9,3,2,3,1,1], [4,0,9,9,0,5,5,4,7], 9 # [9,9,9,7,3,2,3,1,1]
print(data)
res = sol.maxNumber(*data)
print(res)
