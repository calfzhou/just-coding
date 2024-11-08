from typing import *

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total = 0
        locked_boxes = set()
        got_keys = set()
        queue = []
        for b in initialBoxes:
            if status[b] == 1:
                queue.append(b)
            else:
                locked_boxes.add(b)

        while queue:
            box = queue.pop()
            total += candies[box]

            for k in keys[box]:
                if k in locked_boxes:
                    queue.append(k)
                    locked_boxes.remove(k)
                else:
                    got_keys.add(k)

            for b in containedBoxes[box]:
                if status[b] == 1:
                    queue.append(b)
                elif b in got_keys:
                    queue.append(b)
                    got_keys.remove(b)
                else:
                    locked_boxes.add(b)

        return total

sol = Solution()
data = [1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0] # 16
data = [1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0] # 6
data = [1,1,1], [100,1,100], [[],[0,2],[]], [[],[],[]], [1] # 1
data = [1], [100], [[]], [[]], [] # 0
data = [1,1,1], [2,3,2], [[],[],[]], [[],[],[]], [2,1,0] # 7
print(data)
res = sol.maxCandies(*data)
print(res)
