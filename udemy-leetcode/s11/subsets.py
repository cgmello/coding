class Solution():
    def subsets(self, nums):
        ans = []
        cur = []
        print(nums)
        self.solution(nums, ans, cur, 0)
        return ans

    def solution(self, nums, ans, cur, index):
        if index > len(nums):
            return
        ans.append(cur[:])
        print(ans, cur, index)
        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                print(cur)
                self.solution(nums, ans, cur, i)
                cur.pop()
        return

s = Solution()
print(s.subsets([1, 2, 3]))
