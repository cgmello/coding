class Solution:
    def find_first(self, arr: list, t: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > t:
                r = mid - 1
            elif arr[mid] == t:
                if mid == 0 or arr[mid - 1] < t:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1

    def find_last(self, arr: list, t: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > t:
                r = mid - 1
            elif arr[mid] == t:
                if mid == len(arr) - 1 or arr[mid + 1] > t:
                    return mid
                else:
                    l = mid + 1
            else:
                l = mid + 1
        return -1

    def first_and_last(self, arr: list, t: int) -> list:
        first = self.find_first(arr, t)
        last = self.find_last(arr, t)

        return [first, last]


arr = [8, 8, 9, 10, 10, 11, 11, 11, 14, 15, 15, 16, 17]
target = 11
s = Solution()
result = s.first_and_last(arr, target)
print(result)
