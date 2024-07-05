from input_from_file import init_file, input
init_file("2110")

N, C = list(map(int, input().split()))
homes = []
for _ in range(N):
    homes.append(int(input()))

homes = sorted(homes)

max_dist = 1000000000
result = 0
left, right = (0, max_dist)
while (left <= right):
    mid = (left + right) // 2 # 공유기 간 최소 거리

    curr_count = 1
    last_home = homes[0]
    curr_min_dist = max_dist
    for home in homes[1:]:
        dist = home - last_home
        if dist >= mid: # 공유기 사이 최소 거리보다 크면 설치
            curr_count += 1
            last_home = home
            curr_min_dist = min(curr_min_dist, dist) # 가장 인접한 두 공유기 사이 거리

    if curr_count >= C:
        left = mid + 1 # 공유기 간 최소 거리를 늘리기
        result = max(result, curr_min_dist) # 정답에 반영
    else:
        right = mid - 1

print(result)