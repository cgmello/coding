def max_sliding_window(arr: list, k: int):
    win_size = len(arr)
    if win_size < k:
        print("Sliding window is greater than array size")
        return None

    sum0 = sum(arr[i] for i in range(k))
    print(f"sum0={sum0}")
    max_sum = sum0

    for i in range(k - 1, win_size - 1):
        curr_sum = max_sum - arr[i] + arr[i + 1]
        max_sum = max(curr_sum, max_sum)
        print(f"sum={curr_sum} first={i} last={i + 1} remove={arr[i]} add={arr[i + 1]}")

    return max_sum


arr = [1, 3, 5, 10, 15, 20, 23, 200, 250, -500, 350, 360, 23, 11]
k = 4
max_sum = max_sliding_window(arr, k)

print(f"Max sum ({k}) = {max_sum}")
