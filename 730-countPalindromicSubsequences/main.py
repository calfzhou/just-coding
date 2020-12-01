class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        base = 10 ** 9 + 7

        first = [None] * n
        last = [None] * n

        pos = [None] * 4
        for i in range(n):
            pos[ord(S[i]) - 97] = i
            last[i] = tuple(pos)

        pos = [None] * 4
        for i in range(n - 1, -1, -1):
            pos[ord(S[i]) - 97] = i
            first[i] = tuple(pos)

        cache = {}
        def calc(l, r):
            if (l, r) in cache:
                # print('cache', (l, r))
                return cache[(l, r)]

            cnt = 0
            for c in range(4):
                l0 = first[l][c]
                r0 = last[r][c]
                if l0 is None or r0 is None or l0 > r or r0 < l:
                    continue
                cnt += 1 # single char palindromic
                if l0 < r0:
                    cnt += calc(l0 + 1, r0 - 1) + 1 # the last 1 for empty subsequence

            cnt %= base
            cache[(l, r)] = cnt
            return cnt

        res = calc(0, n - 1)
        # print(cache)
        return res

sol = Solution()
s = 'bccb'
s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba' # 3104860382 -> 104860361
# s = 'a' # 1
r = sol.countPalindromicSubsequences(s)
print(s)
print(r)
