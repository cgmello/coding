class Solution:
    def container_most_water(self, arr: list) -> int:
        l = 0
        r = len(arr) - 1
        maxarea = 0
        while (l < r):
            area = min(arr[l], arr[r]) * (r - l)
            maxarea = max(maxarea, area)
            if (arr[l] < arr[r]):
                l += 1
            else:
                r -= 1
        return maxarea


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7, 2]
s = Solution()
max_container = s.container_most_water(heights)
print(f"Max = {max_container}")
