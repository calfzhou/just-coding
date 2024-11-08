"""
出现次数最多的字符个数不能超过一半（上取整）。
"""

import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) <= 1:
            return S

        maxCount = 0
        chars = {}
        for c in S:
            chars[c] = chars.get(c, 0) + 1
            maxCount = max(maxCount, chars[c])

        if maxCount > (len(S) + 1) // 2:
            return ''

        res = []

        h = [(-n, c) for c, n in chars.items()]
        heapq.heapify(h)

        while len(h) >= 2:
            n1, c1 = heapq.heappop(h)
            n2, c2 = heapq.heappop(h)
            res.append(c1)
            res.append(c2)
            n1 += 1
            n2 += 1
            if n1 < 0:
                heapq.heappush(h, (n1, c1))
            if n2 < 0:
                heapq.heappush(h, (n2, c2))

        if h:
            res.append(h[0][1])

        return ''.join(res)


sol = Solution()
s = 'aab'
r = sol.reorganizeString(s)
print(s, r)
