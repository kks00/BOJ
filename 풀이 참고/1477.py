from input_from_file import init_file, input
init_file("1477")

N, M, L = list(map(int, input().split()))
stops = list(map(int, input().split()))
stops = sorted(stops)
stops.insert(0, 0)
stops.append(L)

results = []
left, right = (0, 1000)
while (left <= right):
    mid = (left + right) // 2 # 휴게소 간 최대 거리를 MID로 설정

    curr_need = 0 # 휴게소 간 최대 거리를 넘지 않기 위해 설치해야 할 휴게소의 수
    for i in range(len(stops) - 1):
        a, b = stops[i], stops[i + 1]
        curr_dist = b - a
        if curr_dist > mid:
            if mid < 1:
                curr_need += curr_dist
            else:
                curr_need += curr_dist // mid
                if (curr_dist % mid == 0):
                    curr_need -= 1

    if curr_need <= M: # 설치해야 할 휴게소의 수가 M개 이하일 시 거리 줄이기
        results.append(mid) # 정답에 추가
        right = mid - 1
    else: # M개 이상일 시 거리 늘리기
        left = mid + 1

print(min(results))


# import heapq
#
# h = []
# stops = sorted(stops)
# stops.insert(0, 0)
# stops.append(L)
# for i in range(len(stops) - 1):
#     a, b = stops[i], stops[i + 1]
#     curr_dist = b - a
#     heapq.heappush(h, (-1 * curr_dist, a, b))
#
# for _ in range(M):
#     if len(h) > 0:
#         dist, a, b = heapq.heappop(h)
#         dist = dist * -1
#
#         install_pos = (a + b) // 2
#
#         heapq.heappush(h, (-1 * (install_pos - a), a, install_pos))
#         heapq.heappush(h, (-1 * (b - install_pos), install_pos, b))
#
# list = []
# while (len(h) > 0):
#     dist, a, b = heapq.heappop(h)
#     dist *= -1
#     list.append((a, b, dist))
# list = sorted(list)
# print(list)