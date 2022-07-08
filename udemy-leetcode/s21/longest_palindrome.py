class Solution:
    def longestPalindrome(self, s):
        n = len(s)

        if n < 2:
            return s

        palindrome = [[False for i in range(n)] for i in range(n)]

        for i in range(n):
            palindrome[i][i] = True

        left = 0
        right = 0

        for j in range(1, n):
            for i in range(0, j):
                inner = palindrome[i + 1][j - 1] or j - i <= 2
                if s[i] == s[j] and inner:
                    palindrome[i][j] = True
                    if j - i > right - left:
                        left = i
                        right = j

        return s[left:right + 1]

s = Solution()
print(s.longestPalindrome("babad"))
