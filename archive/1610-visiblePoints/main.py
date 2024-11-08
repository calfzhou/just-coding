from typing import *

import math

def circleIter(angles, fieldOfView):
    for alpha in angles:
        yield alpha
    for alpha in angles:
        if alpha > fieldOfView:
            break
        yield alpha + 2 * math.pi

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        alwaysSeen = 0
        angles = []
        for x, y in points:
            x = x - location[0]
            y = y - location[1]
            if x == 0 and y == 0:
                alwaysSeen += 1
            else:
                angles.append(math.atan2(y, x)) # (-pi, pi)

        if not angles:
            return alwaysSeen

        fov = math.radians(angle)
        angles = sorted(angles)
        angles1 = circleIter(angles, fov - math.pi)
        angles2 = circleIter(angles, fov - math.pi)

        maxCnt = 0
        begin = 0
        beginAngle = next(angles1)
        for end, endAngle in enumerate(angles2):
            while endAngle - beginAngle > fov:
                begin += 1
                beginAngle = next(angles1)

            cnt = end - begin + 1
            maxCnt = max(maxCnt, cnt)

        return alwaysSeen + maxCnt

sol = Solution()
data = [[2,1],[2,2],[3,3]], 90, [1, 1] # 3
data = [[2,1],[2,2],[3,4],[1,1]], 90, [1,1] # 4
data = [[1,0],[2,1]], 13, [1,1] # 1
res = sol.visiblePoints(*data)
print(res)
