class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        cnt = len(nums)

        for l in range(cnt - 1):
            if nums[l] > nums[l + 1]:
                break
        else:
            return 0

        for r in range(cnt - 1, 0, -1):
            if nums[r] < nums[r - 1]:
                break

        print(l, r)
        if l == 0 and r == cnt - 1:
            return r - l + 1

        for i in range(l, r + 1):
            while l > 0 and nums[i] < nums[l - 1]:
                l -= 1
            while r < cnt - 1 and nums[i] > nums[r + 1]:
                r += 1

        print(l, r)
        print(nums[:l], sorted(nums[l:r+1]), nums[r+1:])
        return r - l + 1

sol = Solution()
data = [2, 6, 4, 8, 10, 9, 15] # 5
data = [2, 6, 4, 18, 1, 9, 15] # 7
# data = [1, 2] # 0
# data = [1,3,2,2,2] # 4
data = [1,3,2,3,3] # 2
res = sol.findUnsortedSubarray(data)
print(res)
