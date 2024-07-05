from input_from_file import init_file, input
init_file("15686")

import itertools
from collections import deque

N, M = list(map(int, input().split()))
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

homes = []
chickens = []
for y in range(N):
    for x in range(N):
        if m[y][x] == 1:
            homes.append((y, x))
        elif m[y][x] == 2:
            chickens.append((y, x))

def bfs(start):
    q = deque()
    visited = set()

    visited.add(start)
    start_y, start_x = start
    q.append((start_y, start_x, 0))
    while (len(q) > 0):
        cy, cx, cc = q.popleft()

        if m[cy][cx] == 2:
            return cc

        for oy, ox in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = cy + oy, cx + ox
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if (ny, nx) in visited:
                continue

            visited.add((ny, nx))
            q.append((ny, nx, cc + 1))
    return -1

result = int(1e9)
for count in range(len(chickens) - M, len(chickens)):
    curr_removes = list(itertools.combinations(chickens, count))

    for remove in curr_removes:
        for cy, cx in remove:
            m[cy][cx] = 0

        curr_result = 0
        for home in homes:
            curr_result += bfs(home)
        result = min(result, curr_result)

        for cy, cx in remove:
            m[cy][cx] = 2
print(result)