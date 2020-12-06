from typing import *

class Master(object):
    def __init__(self, secret, words):
        self.secret = secret
        self.words = words
        self.chance = 10
        self.win = False

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        assert self.chance > 0, 'Run out of chances!'
        self.chance -= 1

        if word not in self.words:
            print('guess:', word, 'result:', -1)
            return -1

        right = 0
        for i in range(len(self.secret)):
            if self.secret[i] == word[i]:
                right += 1

        if right == len(self.secret):
            self.win = True

        print('guess:', word, 'result:', right)
        return right


################################################################

"""
对于一个可选单词 word，计算它与其他可选单词彼此的匹配度（m: [0, 5]）。
统计每个匹配度数值对应的可选单词数量（cnt_m, 0 <= m <= 5），最多的是猜测 word 之后剩余单词数量的上界。
检查所有的可选单词，选剩余单词数量上界最小的那个进行猜测。

```
min(word){ max(m){ cnt_m(word) } }
```
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import collections

def calc_match(word1, word2):
    match = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            match += 1
    return match

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = len(wordlist)
        word_matches = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                match = calc_match(wordlist[i], wordlist[j])
                word_matches[i][j] = word_matches[j][i] = match

        # for i in range(n):
        #     print(word_matches[i])

        candidates = tuple(range(n))

        for _ in range(10):
            min_worst = None, None
            for i in candidates:
                counter = collections.Counter(word_matches[i][j] for j in candidates)
                worst = max(counter.values())
                if min_worst[0] is None or min_worst[0] > worst:
                    min_worst = worst, i

            # print(candidates, min_worst)
            word = min_worst[1]
            res = master.guess(wordlist[word])
            if res == 6:
                break

            candidates = tuple(j for j in candidates if word_matches[word][j] == res)

sol = Solution()
data = "acckzz", ["acckzz","ccbazz","eiowzz","abcczz"]
data = "acckzz", ["ccbazz","eiowzz","abcczz","acckzz"]
data = "eiowzz", ["ccbazz","eiowzz","abcczz","acckzz"]
print(data)
master = Master(*data)
res = sol.findSecretWord(data[1], master)
# print(res)
print(master.win)
