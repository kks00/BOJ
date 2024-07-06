from input_from_file import init_file, input
init_file("2512")

N = int(input())
reqs = list(map(int, input().split()))
M = int(input())

left, right = (0, M)
mid = 0
while (left <= right):
    mid = (left + right) // 2

    curr_budget = 0
    for req in reqs:
        curr_budget += min(mid, req)

    if curr_budget > M:
        right = mid - 1
    else:
        left = mid + 1

print(min(right, max(reqs)))