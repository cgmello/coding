class Solution(object):
    def missingNumber(self, nums):
        m = {}
        n = len(nums) + 1
        for i in range(n):
            m[i] = False
        for i in range(len(nums)):
            m[nums[i]] = True
        for i in range(n):
            if not m[i]:
                return i
        return -1

s = Solution()
print(s.missingNumber([3, 2, 4, 0]))
