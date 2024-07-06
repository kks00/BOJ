from input_from_file import init_file, input
init_file("4485")

# from collections import deque
# def solve(map_data, cost_data, n):
#     queue = deque()
#     queue.append((0, 0))
#     cost_data[0][0] = map_data[0][0]
#     while len(queue) > 0:
#         cy, cx = queue.popleft()
#         for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             ny, nx = cy + oy, cx + ox
#             if not (0 <= ny < n and 0 <= nx < n):
#                 continue
#
#             if cost_data[ny][nx] < cost_data[cy][cx] + map_data[ny][nx]:
#                 continue
#             cost_data[ny][nx] = min(cost_data[ny][nx], cost_data[cy][cx] + map_data[ny][nx])
#             queue.append((ny, nx))

import heapq
def solve(map_data, cost_data, n):
    cost_data[0][0] = map_data[0][0]

    queue = []
    heapq.heappush(queue, (cost_data[0][0], 0, 0))
    while len(queue) > 0:
        cw, cy, cx = heapq.heappop(queue)
        if cy == n - 1 and cx == n - 1:
            return

        for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + oy, cx + ox
            if not (0 <= ny < n and 0 <= nx < n):
                continue

            if cost_data[ny][nx] <= cost_data[cy][cx] + map_data[ny][nx]:
                continue
            cost_data[ny][nx] = cost_data[cy][cx] + map_data[ny][nx]
            heapq.heappush(queue, (cost_data[ny][nx], ny, nx))

count = 0
while True:
    N = int(input())
    if N < 1:
        break
    count += 1

    cost_data = [[10 * N * N for _ in range(N)] for _ in range(N)]
    map_data = []
    for _ in range(N):
        map_data.append(list(map(int, input().split())))

    solve(map_data, cost_data, N)

    # for i in cost_data:
    #     print(i)

    print("Problem {0}: {1}".format(count, cost_data[N - 1][N - 1]))