class Solution(object):
    def palindromePartitioning(self, s: str) -> list:
        self.ans = []
        self.cur = []
        self.solution(s)
        return self.ans

    def solution(self, s) -> list:
        if len(s) == 0 and len(self.cur) > 0:
            self.ans.append(self.cur[:])
            return

        index = len(s) + 1

        for i in range(1, index):
            segment = s[0:i]
            if self.isPalindrome(segment):
                self.cur.append(segment)
                self.solution(s[i:])
                self.cur.pop()

    def isPalindrome(self, substr) -> bool:
        i = 0
        j = len(substr) - 1
        while i < j:
            if substr[i] != substr[j]:
                return False
            i += 1
            j += -1
        return True


s = Solution()
print(s.palindromePartitioning("aab"))
