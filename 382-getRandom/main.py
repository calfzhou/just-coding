from typing import *
from math import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

################################################################

import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        n = 0
        choose = None
        node = self.head
        while node:
            n += 1
            if random.randrange(n) == 0:
                choose = node.val
            node = node.next
        return choose


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
solution = Solution(head)
import collections
counter = collections.Counter(solution.getRandom() for _ in range(10000))
print(counter)
