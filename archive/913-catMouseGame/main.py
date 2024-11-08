from typing import *

"""
当前状态 [mouse, cat, moving] -> 老鼠位置，猫位置，当前该谁（MOUSE/CAT）移动。

正向思考
对于 [m, c, MOUSE]，老鼠移动后可以变成 [G(m), c, CAT]，这些后续状态
    如果有一个是老鼠赢，则当前老鼠必赢；
    如果所有都是猫赢，则当前猫必赢；
    否则为平局。
对于 [m, c, CAT]，猫移动后可以变成 [m, G(c)-{0}, MOUSE]，这些后续状态
    如果有一个是猫赢，则当前猫必赢；
    如果所有都是老鼠赢，则当前老鼠必赢；
    否则为平局。

反向推导
初始：
    [0, i, *] 是老鼠赢，[i, i, *] 是猫赢（i != 0）。
递推：
    取出一个未处理过的有确定结果的状态，遍历检查所有可以走到这一步前置状态：
        如果前置状态的移动者是本状态的赢家，则前置状态的赢家就是它；
        否则，检查前置状态还有没有未知结果的移动方案，若没有了，则前置状态的赢家是对手；否则前置状态的结果尚不能确定。
        将刚刚确认了结果的前置状态推入队列等待处理。
    最终会把所有有确定结果的状态都标记上，最终没有标记的都是和局状态。
"""

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        DRAW, MOUSE, CAT = range(3)
        N = len(graph)
        initial = (1, 2, MOUSE)

        # 记录每个状态未知结果的移动方案数
        degrees = {}
        for mouse in range(N):
            for cat in range(N):
                degrees[mouse, cat, MOUSE] = len(graph[mouse])
                degrees[mouse, cat, CAT] = len(graph[cat])
                if 0 in graph[cat]:
                    degrees[mouse, cat, CAT] -= 1

        results = {}
        tasks = []
        for i in range(1, N):
            for moving in (MOUSE, CAT):
                tasks.append((0, i, moving, MOUSE))
                results[0, i, moving] = MOUSE
                tasks.append((i, i, moving, CAT))
                results[i, i, moving] = CAT

        def parents(mouse, cat, moving):
            if moving == MOUSE:
                for c in graph[cat]:
                    if c > 0:
                        yield mouse, c, CAT
            elif moving == CAT:
                for m in graph[mouse]:
                    yield m, cat, MOUSE

        while tasks:
            mouse, cat, moving, winner = tasks.pop()
            for prev_mouse, prev_cat, prev_moving in parents(mouse, cat, moving):
                if (prev_mouse, prev_cat, prev_moving) in results:
                    continue
                elif prev_moving == winner:
                    if initial == (prev_mouse, prev_cat, prev_moving):
                        return winner
                    tasks.append((prev_mouse, prev_cat, prev_moving, winner))
                    results[prev_mouse, prev_cat, prev_moving] = winner
                else:
                    degrees[prev_mouse, prev_cat, prev_moving] -= 1
                    if degrees[prev_mouse, prev_cat, prev_moving] == 0:
                        if initial == (prev_mouse, prev_cat, prev_moving):
                            return moving
                        tasks.append((prev_mouse, prev_cat, prev_moving, moving))
                        results[prev_mouse, prev_cat, prev_moving] = moving

        return results.get(initial, DRAW)

sol = Solution()
data = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]] # 0
print(data)
res = sol.catMouseGame(data)
print(res)
