from input_from_file import init_file, input
init_file("2343")

N, M = list(map(int, input().rstrip().split()))
vids = list(map(int, input().rstrip().split()))

curr_max = 0

def solve(mid):
    global curr_max
    curr_count, curr_len = 1, 0
    for i in range(N):
        next_len = curr_len + vids[i]
        if next_len > mid:
            curr_count += 1
            if curr_count > M:
                return False
            curr_max = max(curr_max, curr_len)
            curr_len = vids[i]
        else:
            curr_len = next_len
    curr_max = max(curr_max, curr_len)
    return True


result = 10001 * N
left, right = 0, 10001 * N
while (left <= right):
    # 블루레이 최대 크기
    mid = (left + right) // 2

    curr_max = 0
    r = solve(mid)
    if r:
        result = min(result, curr_max)
        right = mid - 1
    else:
        left = mid + 1
print(result)
