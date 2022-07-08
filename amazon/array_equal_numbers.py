class Solution:
    """
    Um jogo de convergir um array para todos do mesmo valor e a jogada pode ser só acrescentar 1 em todos
    do array menos um elemento
    """
    def array_equal(self, arr):
        def is_equal(arr):
            # all elements are equal if the mean is equal to that last element
            return sum(arr)/len(arr) == arr[len(arr)-1]

        print(arr)

        steps = 0
        arr.sort()
        while not is_equal(arr):
            # sum 1, unless the last one
            for i in range(len(arr)-1):
                arr[i] += 1
            steps +=1

            # sort, if needed
            n = len(arr)
            if arr[n-2] > arr[n-1]:
                arr.sort()

        print(arr)

        return steps

    def array_equal_optimized(self, arr):
        steps = 0
        arr.sort()
        for i in range(len(arr)):
            steps += arr[i] - arr[0]
        return steps

print(Solution().array_equal([5, 2, 12, 12, 20, 34]))
print(Solution().array_equal_optimized([5, 2, 12, 12, 20, 34]))
