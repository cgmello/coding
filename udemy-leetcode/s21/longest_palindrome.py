class Solution:
    def longestPalindrome(self, s):
        n = len(s)

        if n < 2:
            return s

        # create a matrix NxN all marked as false
        palindrome = [[False for i in range(n)] for i in range(n)]
        print(palindrome)

        # single characters are palindromes
        for i in range(n):
            palindrome[i][i] = True

        # answer is the limits of the substring
        left = 0
        right = 0

        for j in range(1, n):
            for i in range(0, j):
                # j-2<=2 has no inner substring (eg "ab")
                inner = palindrome[i + 1][j - 1] or j - i <= 2
                # first char = last char and inner is palindrome ?
                if s[i] == s[j] and inner:
                    palindrome[i][j] = True
                    # update biggest substring that is palindrome
                    if j - i > right - left:
                        left = i
                        right = j

        return s[left:right + 1]

s = Solution()
print(s.longestPalindrome("babad"))
