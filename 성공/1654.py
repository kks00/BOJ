from input_from_file import init_file, input
init_file("1654")

K, N = list(map(int, input().split()))
lans = []
for _ in range(K):
    lans.append(int(input()))

result = 0
left, right = (0, 2**31)
while (left <= right):
    mid = (left + right) // 2

    curr_count = 0
    for lan in lans:
        curr_count += lan // mid

    if curr_count >= N:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)