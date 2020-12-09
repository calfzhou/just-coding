from typing import *
from math import *


"""
用最大堆维护已知的数据中较小的一半（ceil(n / 2) 个），用最小堆维护较大的一半（floor(n / 2) 个）。
根据 n 的奇偶性和两个堆的堆顶数值可以计算出当前的中位数。
"""

import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = []
        self.bigger = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.smaller or num < -self.smaller[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.bigger, num)

        # Adjust two heaps' size.
        if len(self.smaller) < len(self.bigger):
            heapq.heappush(self.smaller, -heapq.heappop(self.bigger))
        elif len(self.smaller) - len(self.bigger) > 1:
            heapq.heappush(self.bigger, -heapq.heappop(self.smaller))

        print(self.smaller, self.bigger)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smaller) > len(self.bigger):
            return float(-self.smaller[0])
        else:
            return (-self.smaller[0] + self.bigger[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian()) # 1.5
obj.addNum(3)
print(obj.findMedian()) # 2
