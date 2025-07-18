from input_from_file import init_file, input
init_file("1654")

K, N = list(map(int, input().rstrip().split()))
L = []
for _ in range(K):
    L.append(int(input()))

# 한 랜선의 길이를 이분탐색
result = 0
left, right = 0, (2 ** 31)
while (left <= right):
    mid = (left + right) // 2

    count = 0
    for i in range(K):
        count += (L[i] // mid)
    if count >= N:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid - 1

print(result)

