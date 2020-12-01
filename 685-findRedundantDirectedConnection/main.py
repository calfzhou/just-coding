from typing import *

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {} # node -> parent(node)
        badEdge = None
        loopEdge = None
        for u, v in edges:
            print((u, v), badEdge, loopEdge, parents)
            if v in parents:
                badEdge = [u, v]
                if loopEdge is not None:
                    break
                else:
                    # Skip loop check
                    continue
            else:
                parents[v] = u

            # Check loop.
            p = u
            while p is not None and p != v:
                p = parents.get(p)
                if p == u:
                    break

            if p == v:
                loopEdge = [u, v]
                if badEdge is not None:
                    break


        print(badEdge, loopEdge, parents)
        if badEdge is None:
            return loopEdge
        elif loopEdge is None:
            return badEdge
        else:
            return [parents[badEdge[1]], badEdge[1]]

sol = Solution()
data = [[1,2], [1,3], [2,3]] # [2,3]
# data = [[1,2], [2,3], [3,4], [4,1], [1,5]] # [4, 1]
# data = [[2,1],[3,1],[4,2],[1,4]] # [2, 1]
# data = [[4,1],[1,5],[4,2],[5,1],[4,3]] # [5, 1]
# data = [[3,4],[4,1],[1,2],[2,3],[5,1]] # [4, 1]
res = sol.findRedundantDirectedConnection(data)
print(res)
