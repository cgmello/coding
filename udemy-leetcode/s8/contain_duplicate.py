class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = {}
        for num in nums:
            if num in m:
                return True
            else:
                m[num] = 1
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1]))
