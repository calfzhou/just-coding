class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        parts = []
        while n > 0:
            n, idx = divmod(n - 1, 26)
            parts.append(letters[idx])

        return ''.join(reversed(parts))
