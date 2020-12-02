from typing import *

import itertools

# 将算术表达式字符串拆分为 tokens
def tokenize(expr):
    i = 0
    begin = 0
    while i < len(expr):
        c = expr[i]
        if not ('a' <= c <= 'z' or '0' <= c <= '9'):
            if begin < i:
                yield expr[begin:i]
            if c != ' ':
                yield c
            begin = i + 1
        i += 1
    if begin < len(expr):
        yield expr[begin:]

# 构建逆波兰表达式
def build_reverse_polish(tokens, params):
    notes = []
    ops = []
    op_levels = { '+': 1, '-': 1, '*': 2 }
    for token in tokens:
        if 'a' <= token[0] <= 'z':
            if token in params:
                notes.append(polynominal(params[token]))
            else:
                notes.append(polynominal(token))
        elif '0' <= token[0] <= '9':
            notes.append(polynominal(int(token)))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                notes.append(ops.pop())
            ops.pop()
        else:
            level = op_levels[token]
            while ops and op_levels.get(ops[-1], 0) >= level:
                notes.append(ops.pop())
            ops.append(token)

        # print(notes, ops)

    while ops:
        notes.append(ops.pop())

    return notes

class Atom:
    def __init__(self, k, vars):
        self.k = k
        self.vars = tuple(sorted(vars))

    def order(self):
        return len(self.vars)

    def __repr__(self):
        return '*'.join((str(self.k), *self.vars))

# 将整数或自变量变为多项式
def polynominal(x):
    if isinstance(x, int) and x != 0:
        return [Atom(x, [])]
    elif isinstance(x, str):
        return [Atom(1, [x])]
    else:
        return []

# 简化多项式（合并同类项）
def simplify(atoms):
    res = []
    for b in sorted(atoms, key=lambda x: (-x.order(), tuple(x.vars))):
        if res and res[-1].vars == b.vars:
            a = res.pop()
            if a.k != -b.k:
                res.append(Atom(a.k + b.k, a.vars))
        else:
            res.append(b)
    return res

def add(a, b):
    return simplify(itertools.chain(a, b))

def sub(a, b):
    return simplify(itertools.chain(a, (Atom(-y.k, y.vars) for y in b)))

def mul(a, b):
    return simplify(Atom(x.k * y.k, itertools.chain(x.vars, y.vars)) for x, y in itertools.product(a, b))

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        params = {}
        for k, v in zip(evalvars, evalints):
            params[k] = v

        # print(list(tokenize(expression)))
        notes = build_reverse_polish(tokenize(expression), params)
        # print(notes)
        # print()

        stack = []
        ops = { '+': add, '-': sub, '*': mul }
        for note in notes:
            if note == '+' or note == '-' or note == '*':
                b, a = stack.pop(), stack.pop()
                res = ops[note](a, b)
                # print(a, b, note, res)
                stack.append(res)
            else:
                stack.append(note)

        res = stack.pop()
        return [str(atom) for atom in res]


sol = Solution()
data = "e + 8 - a + 5", ["e"], [1] # ["-1*a","14"]
data = '8 + 2 - 3 * 4', [], [] # ['-2']
data = "e - 8 + temperature - pressure", ["e", "temperature"], [1, 12] # ["-1*pressure","5"]
data = "(e + 8) * (e - 8)", [], [] # ["1*e*e","-64"]
data = "7 - 7", [], [] # []
data = "a * b * c + b * a * c * 4", [], [] # ["5*a*b*c"]
data = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [], [] # ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
# data = '0', [], [] # []
print(*data)
res = sol.basicCalculatorIV(*data)
print(res)
