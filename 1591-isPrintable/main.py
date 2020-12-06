from typing import *

"""
对于任何一个颜色，可以找到包含该颜色的最小的包围矩形区域。检查这个区域内是否出现其他颜色，如果有，那么其他颜色只能在该颜色之后被打印。
整理完所有颜色的先后依赖关系，检查是否有循环依赖，如果有就不能成功打印。

颜色的先后关系可以构成一张有向图，判定图中是否有环。
在图中找一个入度为 0 的点，将其及其关联的边都删除。持续操作，如果最后剩下一组结点，入度均大于 0，说明有环。
"""

class Box:
    def __init__(self, r, c):
        self.top = self.bottom = r
        self.left = self.right = c

    def extend(self, r, c):
        self.top = min(self.top, r)
        self.bottom = max(self.bottom, r)
        self.left = min(self.left, c)
        self.right = max(self.right, c)

    def include(self, r, c):
        return self.top <= r <= self.bottom and self.left <= c <= self.right

    # def __repr__(self):
    #     return f'r{self.top}-{self.bottom} c{self.left}-{self.right}'

class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m = len(targetGrid)
        n = len(targetGrid[0])

        # 计算各颜色的最小包围矩形。
        boxes = {} # color -> [min_r, min_c, max_r, max_c]
        for r in range(m):
            for c in range(n):
                box = boxes.setdefault(targetGrid[r][c], Box(r, c))
                box.extend(r, c)
        # print(boxes)

        # 构造颜色打印顺序图
        graph = { c: set() for c in boxes } # color -> [descents]
        for r in range(m):
            for c in range(n):
                color = targetGrid[r][c]
                for another, box in boxes.items():
                    if another != color and box.include(r, c):
                        graph[another].add(color)
        # print(graph)

        # 检查图中是否有环
        in_degrees = { c: 0 for c in boxes } # node -> in_degree
        for u in graph:
            in_degrees.setdefault(u, 0)
            for v in graph[u]:
                in_degrees[v] += 1
        # print(in_degrees)

        while in_degrees:
            zero = None
            for u, degree in in_degrees.items():
                if degree == 0:
                    zero = u
                    break

            if zero is None:
                return False

            del in_degrees[zero]
            for v in graph[zero]:
                if v in in_degrees:
                    in_degrees[v] -= 1

        return True


sol = Solution()
data = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]] # True
data = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]] # True
# data = [[1,2,1],[2,1,2],[1,2,1]] # False
# data = [[1,1,1],[3,1,3]] # False
print(data)
res = sol.isPrintable(data)
print(res)
