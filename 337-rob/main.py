from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    front = 0
    i = 1
    while i < len(vals):
        node = queue[front]
        front += 1

        v = vals[i]
        i += 1
        if v is not None:
            node.left = TreeNode(v)
            queue.append(node.left)

        if i >= len(vals):
            break

        v = vals[i]
        i += 1
        if v is not None:
            node.right = TreeNode(v)
            queue.append(node.right)

    return root

################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0, 0

            rob_left, not_rob_left = helper(node.left)
            rob_right, not_rob_right = helper(node.right)
            rob_this = node.val + not_rob_left + not_rob_right
            not_rob_this = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
            return rob_this, not_rob_this

        return max(helper(root))

class Solution1:
    def rob(self, root: TreeNode) -> int:
        dp = {}
        def helper(node):
            if node is None:
                return 0
            elif id(node) in dp:
                return dp[id(node)]

            total = node.val
            if node.left is not None:
                total += helper(node.left.left) + helper(node.left.right)
            if node.right is not None:
                total += helper(node.right.left) + helper(node.right.right)

            total = max(total, helper(node.left) + helper(node.right))
            dp[id(node)] = total
            return total

        return helper(root)

class SolutionTooSlow:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0

        total = root.val
        if root.left is not None:
            total += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right is not None:
            total += self.rob(root.right.left) + self.rob(root.right.right)

        return max(total, self.rob(root.left) + self.rob(root.right))

sol = Solution()
data = [3,2,3,None,3,None,1] # 7, (3 + 3 + 1)
# data = [3,4,5,1,3,None,1] # 9, (4 + 5)
print(data)
res = sol.rob(build_tree(data))
print(res)
