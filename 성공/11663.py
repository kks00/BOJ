from input_from_file import init_file, input
init_file("11663")

N, M = list(map(int, input().rstrip().split()))
dots = list(map(int, input().rstrip().split()))
dots = sorted(dots)
lines = []
for _ in range(M):
    start, end = list(map(int, input().rstrip().split()))
    lines.append((start, end))

from bisect import bisect_left, bisect_right

for line in lines:
    start, end = line
    left = bisect_left(dots, start)
    right = bisect_right(dots, end)

    # print(line, left, right)
    result = right - left
    print(result)


