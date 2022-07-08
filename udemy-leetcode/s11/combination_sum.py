class Solution():
    def combinationSum(self, candidates, target):
        ans = []
        cur = []
        self.solution(candidates, ans, cur, target, 0, 0)
        return ans

    def solution(self, candidates, ans, cur, target, index, csum):
        if csum == target:
            ans.append(cur[:])
        elif csum < target:
            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, csum + candidates[i])
                cur.pop()
        return


candidates = [2, 3, 6, 7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))
