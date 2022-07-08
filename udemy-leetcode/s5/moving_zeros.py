class Solution:
    def moving_zeros(self, nums: list):
        mylen = len(nums)
        i = 0
        while i < mylen:
            if nums[i] == 0:
                pos = i
                j = i
                while nums[j] == 0 and j < mylen - 1:
                     j += 1
                nums[pos] = nums[j]
                nums[j] = 0
            i += 1
        return nums


arr = [0, 1, 0, 0, 3, 0, 5, 7, 9, 0, 11, 13, 0]
s = Solution()
result = s.moving_zeros(arr)
print(result)
