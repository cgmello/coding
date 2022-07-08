class Solution:
    def phoneCombinations(self, digits):
        ans = []
        if len(digits) == 0:
            return ans

        m = {}
        m["2"] = "abc"
        m["3"] = "def"
        m["4"] = "ghi"
        m["5"] = "jkl"
        m["6"] = "mno"
        m["7"] = "pqrs"
        m["8"] = "tuv"
        m["9"] = "wxyz"

        self.solution(ans, digits, "", m, 0)

        return ans

    def solution(self, ans, digits, cur, m, index):
        if index > len(digits):
            return

        if len(cur) == len(digits):
            ans.append(cur[:])
            return

        d = digits[index]
        curString = m[d]

        for i in range(len(curString)):
            self.solution(ans, digits, cur + curString[i], m, index + 1)

        return


s = Solution()
print(s.phoneCombinations("23"))
