from typing import *

import itertools

# 将算术表达式字符串拆分为 tokens
def tokenize(expr):
    i = 0
    begin = 0
    while i < len(expr):
        c = expr[i]
        if not ('0' <= c <= '9'):
            if begin < i:
                yield int(expr[begin:i])
            if c != ' ':
                yield c
            begin = i + 1
        i += 1
    if begin < len(expr):
        yield int(expr[begin:])

# 构建逆波兰表达式
def build_reverse_polish(tokens):
    notes = []
    ops = []
    op_levels = { '+': 1, '-': 1, '*': 2, '/': 2 }
    for token in tokens:
        if isinstance(token, int):
            notes.append(token)
        else:
            level = op_levels[token]
            while ops and op_levels.get(ops[-1], 0) >= level:
                notes.append(ops.pop())
            ops.append(token)
        # print(notes, ops)

    while ops:
        notes.append(ops.pop())

    return notes

class Solution:
    def calculate(self, s: str) -> int:
        # print(list(tokenize(s)))
        notes = build_reverse_polish(tokenize(s))
        # print(notes)
        # print()

        stack = []
        for note in notes:
            if isinstance(note, int):
                stack.append(note)
            else:
                b, a = stack.pop(), stack.pop()
                if note == '+':
                    res = a + b
                elif note == '-':
                    res = a - b
                elif note == '*':
                    res = a * b
                elif note == '/':
                    res = a // b
                # print(a, b, note, res)
                stack.append(res)

        return stack.pop()


sol = Solution()
data = "3+2*2" # 7
# data = " 3/2 " # 1
# data = " 3+5 / 2 " # 5
print(data)
res = sol.calculate(data)
print(res)
