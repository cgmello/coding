class Solution:
    def valid_mountain(self, arr: list) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 1
        while i < n and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == n:
            return False

        print(f"Pivot #{i} = {arr[i]}")

        while i < n:
            if arr[i] >= arr[i - 1]:
                return False
            i += 1

        return True

arr = [1, 3, 5, 7, 9, 8, 7, 6, 4, 3]
# arr = [3,5,5]
# arr = [1,3,2]
s = Solution()
result = s.valid_mountain(arr)
print(f"Valid = {result}")
