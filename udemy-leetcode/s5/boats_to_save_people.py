class Solution:
    def boats(self, arr: list, limit: int) -> int:
        arr.sort()

        print(arr)
        left = 0
        right = len(arr) - 1
        boats = 0

        while left <= right:

            if (left == right):
                print(f"Boat = {arr[left]}")
                boats += 1
                break

            if (arr[left] + arr[right] <= limit):
                print(f"Boat = {arr[left]}-{arr[right]}")
                left += 1
                right -= 1
                boats += 1

            else:
                print(f"Boat = {arr[right]}")
                right -= 1
                boats += 1

        return boats


weights = [3, 1, 2, 3, 2, 1, 2, 1, 1, 3, 1, 2]
s = Solution()
total = s.boats(weights, 3)
print(f"Total boats = {total}")
