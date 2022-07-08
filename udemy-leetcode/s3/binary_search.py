def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        p = (start + end) // 2
        if arr[p] == target:
            return p
        elif arr[p] > target:
            end = p - 1
        else:
            start = p + 1
    return None

arr = [1, 3, 5, 10, 15, 20, 23, 200, 250, 301, 350, 360, 361, 400]
result = binary_search(arr, 20)

if result:
    print(f"Index = {result}")
else:
    print("Not found")
