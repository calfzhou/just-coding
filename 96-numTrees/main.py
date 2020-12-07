from typing import *
from math import *

"""
设 n 个节点可以组成 f(n) 种二叉搜索树。
任何一个数字都可以成为树根，当以 i 为根时，1...i-1 都在左子树，1+1...n 都在右子树。
左子树有 f(i-1) 种，右子树有 f(n-i) 种，两边相互独立，总数为二者乘积。
所以 f(n) = sum(1<=i<=n) { f(i - 1) * f(n - i) }。
初始条件 f(0) = 1，f(1) = 1。

用数学方法，f(n) 是 catalan 数，即 f(n + 1) = 2(2n + 1)C(n)/(n + 2)。
结果为 f(n) = C(n, 2n) / (n + 1)
"""

class Solution(object):
    def numTrees(self, n):
        f_n = factorial(n)
        f_2n = factorial(n << 1)
        return int(f_2n / f_n / f_n / (n + 1))

    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [None] * (n + 1)
        dp[0] = dp[1] = 1
        for k in range(2, n + 1):
            cnt = 0
            for i in range(1, k + 1):
                cnt += dp[i - 1] * dp[k - i]
            dp[k] = cnt

        print(dp)
        return dp[n]


sol = Solution()
data = 3 # 5
data = 10 # 16796
print(data)
res = sol.numTrees(data)
print(res)
