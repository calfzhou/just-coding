from typing import *

"""
对于任意一个段落 [i, j]，考察其最少的打印次数。
第 i 个字母被有效打印（不被后续覆盖）的时候，可以只打印 i，也可以从 i 连续打印到 k（i < k <= j）。
如果 s[k] != s[i]，可以忽略此方案，它与打印到 k 前面最后一个与 s[i] 相同的字母的方案没区别。
如果 s[k] = s[i] = s[k + 1]，可以忽略此方案，直接打印到 k + 1 更好。
对于特定的 k，先打印 [i, k] 段落，然后打印 [k + 1, j] 段落，两段次数之和为 cnt[k]。对所有可行的 k，取最小即可。

注意计算 [i, k] 段落最少打印次数的方法。因为 s[i] = s[k]，如果 k = i，次数为 1，否则与 [i, k - 1] 的打印次数是一致的。

整体计算的时候，可以自底向上，从任何 [i, i] 段落的最少打印次数为 1 往上算。
也可以从上往下计算，好处是并不是所有的 [i, j] 段落都需要计算（有连续重复的字母）。
"""

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        def iter_k(i, j):
            k1 = i
            while k1 <= j:
                if s[k1] == s[i]:
                    k2 = k1 + 1
                    while k2 <= j and s[k2] == s[i]:
                        k2 += 1
                    # [k1, k2) 是连续与 s[i] 相同的一段
                    yield k1, k2
                    k1 = k2 + 1
                else:
                    k1 += 1

        dp = {} # (i, j) -> min_cnt
        def helper(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if (i, j) in dp:
                return dp[i, j]
            min_cnt = None
            for k1, k2 in iter_k(i, j):
                cnt = max(1, helper(i, k1 - 1)) + helper(k2, j)
                if min_cnt is None or min_cnt > cnt:
                    min_cnt = cnt
            # print(i, j, s[i:j + 1], min_cnt)
            dp[i, j] = min_cnt
            return min_cnt

        return helper(0, len(s) - 1)


sol = Solution()
data = "aaabbb" # 2
# data = 'ab' # 2
# data = "aba" # 2
# data = "" # 0
# data = "a" # 1
print(data)
res = sol.strangePrinter(data)
print(res)
