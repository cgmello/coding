class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in m:
                return [m[goal], i]
            else:
                m[nums[i]] = i

s = Solution()
print(s.twoSum([1, 5, 7, 8, 10], 13))
