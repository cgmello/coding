class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


s = Solution()
print(s.singleNumber([2, 2, 1, 1, 4]))
