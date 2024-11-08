class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        la = len(first)
        lb = len(second)
        if abs(la - lb) > 1:
            return False

        i = j = 0
        hasDiff = False
        while i < la and j < lb:
            if first[i] != second[j]:
                if hasDiff:
                    return False
                hasDiff = True
                if la > lb:
                    j -= 1
                elif la < lb:
                    i -= 1
            i += 1
            j += 1

        return True

sol = Solution()
data = 'pale', 'ple' # true
# data = 'palee', 'pal' # false
res = sol.oneEditAway(*data)
print(res)
