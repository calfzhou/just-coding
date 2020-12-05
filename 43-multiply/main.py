from typing import *

def safe_get(array, index):
    if index >= len(array):
        return 0
    else:
        return array[index]

def safe_set(array, index, value):
    while len(array) <= index:
        array.append(0)
    array[index] = value

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        elif num1 == '1':
            return num2
        elif num2 == '1':
            return num1

        n1 = [int(d) for d in num1][::-1]
        res = []
        for i, d2 in enumerate(num2[::-1]):
            d2 = int(d2)
            if d2 == 0:
                continue
            pos = i
            c = 0
            for d1 in n1:
                r = d1 * d2 + safe_get(res, pos) + c
                c, r = divmod(r, 10)
                safe_set(res, pos, r)
                pos += 1
            if c > 0:
                safe_set(res, pos, c)
            # print(num1, d2, i, res)

        return ''.join(str(d) for d in res[::-1]) or '0'


sol = Solution()
data = "2", "3" # "6"
data = "123", "456" # "56088"
# data = "9", "9" # "81"
data = "123456789", "987654321" # 121932631112635269
print(data)
res = sol.multiply(*data)
print(res)
