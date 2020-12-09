from typing import *
from math import *


import random

class Node(object):
    def __init__(self, val = None):
        self.val = val
        self.rights = []

    def __repr__(self):
        return repr(self.val) + ' ' + repr([right.val if right else None for right in self.rights])


class Skiplist(object):

    def __init__(self):
        self.head = Node()
        self.head.rights.append(None)

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        node = self.head
        while node:
            for right in reversed(node.rights):
                if right:
                    if right.val == target:
                        return True
                    elif right.val < target:
                        node = right
                        break
            else:
                return False

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        node = self.head
        parents = []
        while node:
            for right in reversed(node.rights):
                # 若已经有相同数字，加到最后（稳定排序）
                if right and right.val <= num:
                    node = right
                    break
                else:
                    parents.append(node)
            else:
                break

        new_node = Node(num)
        need_ins = 1
        level = 0
        while need_ins > 0:
            if level < len(parents):
                parent = parents[-level - 1]
            else:
                parent = self.head
                parent.rights.append(None)
            new_node.rights.append(parent.rights[level])
            parent.rights[level] = new_node
            level += 1
            need_ins = random.randrange(2) # 平均每往上一层，节点数少一半

        # print(self)

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        node = self.head
        parents = []
        while node:
            for right in reversed(node.rights):
                # 若有相同数字，删除最前面的
                if right and right.val < num:
                    node = right
                    break
                else:
                    parents.append(node)
            else:
                break

        node = parents[-1].rights[0]
        if not node or node.val != num:
            return False

        for level in range(len(node.rights)):
            parents[-level - 1].rights[level] = node.rights[level]

        # print(self)
        return True

    def __repr__(self):
        node = self.head
        parts = []
        while node:
            parts.append(repr(node))
            node = node.rights[0]
        parts.append('----------------------------------------------------------------')
        return '\n'.join(parts)


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


def test1():
    skiplist = Skiplist()
    # print(skiplist.erase(0)) # false
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    print(skiplist.search(0)) # false
    skiplist.add(4)
    print(skiplist.search(1)) # true
    print(skiplist.erase(0)) # false，0 不在跳表中
    print(skiplist.erase(1)) # true
    print(skiplist.search(1)) # 返回 false，1 已被擦除
    # print(skiplist.erase(1)) # true
    # print(skiplist.erase(10)) # false

def test2():
    skiplist = Skiplist()
    for i in range(32):
        skiplist.add(random.randrange(100))
    print(skiplist)

# test1()
test2()
