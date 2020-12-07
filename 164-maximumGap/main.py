from typing import *
from math import *

"""
最直接是基数排序。

若要再从系数上减少一些存储空间，可以将基数扩大为桶，但桶不能太大，避免所求的最大间距出现在桶内，未对问题作出实质的简化。
最大间距的上限是 ceil((max - min) / (n - 1))，此即为桶大小的上限（还要注意不能小于 1），记为 size。
此时桶内的最大间距是 size - 1，一定小于最大间距上限。
需要桶的个数为 (max - min) // size + 1。
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        smallest = min(nums)
        biggest = max(nums)
        size = max(1, floor((biggest - smallest) / (n - 1)))
        cnt = (biggest - smallest) // size + 1
        buckets = [[None, None] for _ in range(int(cnt))]
        # print(smallest, biggest, size, cnt)
        for x in nums:
            idx = (x - smallest) // size
            edge = buckets[int(idx)]
            edge[0] = x if edge[0] is None else min(edge[0], x)
            edge[1] = x if edge[1] is None else max(edge[1], x)

        # print(buckets)
        max_gap = 0
        max_num = None
        for small, big in buckets:
            if small is not None:
                if max_num is not None:
                    max_gap = max(max_gap, small - max_num)
                max_num = big

        return max_gap

sol = Solution()
data = [3,6,9,1] # 3
# data = [10] # 0
print(data)
res = sol.maximumGap(data)
print(res)
