class Solution:
    def binary(self, arr: list, t: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > t:
                r = mid - 1
            elif arr[mid] == t:
                return mid
            else:
                l = mid + 1
        return None

arr = [2, 3, 5, 6, 9, 11, 12, 14, 19, 20, 22, 25, 28, 30]
t = 11
s = Solution()
print(s.binary(arr, t))
