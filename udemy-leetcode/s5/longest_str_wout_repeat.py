class Solution:
    def longest_substring_without_repetion(self, arr: list) -> int:
        m = {} # hashmap
        l = 0
        r = 0
        n = len(arr)
        longest = 0

        while l < n and r < n:
            elem = arr[r]
            print(f"elem={elem}")
            if elem in m:
                l = max(l, m[elem] + 1)
            m[elem] = r
            longest = max(longest, r - l + 1)
            print(f"l={l} r={r} long={longest}")
            r += 1

        return longest


# str = "abcdefabcbb"
str = "abba"
s = Solution()
longest = s.longest_substring_without_repetion(str)
print(f"Longest = {longest}")
