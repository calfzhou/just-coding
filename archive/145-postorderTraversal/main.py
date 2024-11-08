from typing import *

# Definition for a binary tree node.
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

################################################################

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return res[::-1]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        vals = []
        stack = [(root, False)]
        while stack:
            node, ready = stack.pop()
            if ready:
                vals.append(node.val)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))

        return vals


sol = Solution()
data = [1,None,2,3] # [3,2,1]
data = [3,1,2] # [1, 2, 3]
print(data)
res = sol.postorderTraversal(build_tree(data))
print(res)
