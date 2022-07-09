import sys


# recursion
def solution(cur, row, col):
    global lines, k, m, ans

    if len(cur) == k:
        total = 0
        for i in range(len(cur)):
            total += pow(int(cur[i]), 2)
        ans = max(ans, total % m)
        print("ans", ans, total, total % m, file=sys.stderr)
        return

    for c in range(len(lines[row])):
        cur.append(lines[row][c])
        print(row, c, cur, file=sys.stderr)
        solution(cur, row+1, c)
        cur.pop()

n = 0
lines = []
for line in sys.stdin:
    arr = line.split()
    # remove first number that is the "number of elements in the row"
    if n > 0:
        arr.pop(0)
    lines.append(arr)
    n += 1

line = lines.pop(0)
k = int(line[0])
m = int(line[1])

ans = 0
solution([], 0, 0)
print(ans)

"""
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

First line: k-nr of lines, M-modulus
Next lines: n-nr of elements, elements
Formula: F(x) = xˆ2
Maximize: F(x1) + F(x2) + ... + F(xk) % M
"""
