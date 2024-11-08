from typing import *
from math import *

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        nodes = []
        nodes.append(str(self.val))
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.left or node.right:
                nodes.append(str(node.left.val) if node.left else 'null')
                nodes.append(str(node.right.val) if node.right else 'null')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        while nodes and nodes[-1] == 'null':
            nodes.pop()
        return '[' + ','.join(nodes) + ']'

################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import itertools

"""
取 k 作为根节点（1 <= k <= n），生成所有 1...k-1 组成的子树 和 所有 k+1...n 的子树。
笛卡尔积所有可能。
"""
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        # dp[i][j] -> all trees for i...j
        dp = [[[None] for _ in range(n + 2)] for _ in range(n + 2)]

        for m in range(1, n + 1):
            for i in range(1, n - m + 2):
                j = i + m - 1
                trees = []
                for k in range(i, j + 1):
                    for l, r in itertools.product(dp[i][k - 1], dp[k + 1][j]):
                        trees.append(TreeNode(k, l, r))
                dp[i][j] = trees

        return dp[1][n]

    def generateTrees1(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        # 生成 i...j 所有的搜索树。
        def helper(i, j):
            if i == j:
                return [TreeNode(i)]
            elif i > j:
                return [None]

            trees = []
            for k in range(i, j + 1):
                left_trees = helper(i, k - 1)
                right_trees = helper(k + 1, j)
                for l, r in itertools.product(left_trees, right_trees):
                    root = TreeNode(k, l, r)
                    trees.append(root)

            return trees

        return helper(1, n)


sol = Solution()
data = 3
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]

# data = 0 # []
# data = 1 # [[1]]
print(data)
res = sol.generateTrees(data)
print(res)
