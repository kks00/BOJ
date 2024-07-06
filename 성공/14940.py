from input_from_file import init_file, input
init_file("14940")

n, m = list(map(int, input().split()))
Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))

Dist = [[-1 for _ in range(m)] for _ in range(n)]
for y in range(n):
    for x in range(m):
        if Map[y][x] == 2:
            dest_y, dest_x = (y, x)
            Dist[dest_y][dest_x] = 0
        if Map[y][x] == 0:
            Dist[y][x] = 0

from collections import deque
q = deque()
q.append((dest_y, dest_x))
while len(q) > 0:
    cy, cx = q.popleft()

    for oy, ox in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ny, nx = cy + oy, cx + ox
        if not (0 <= ny < n and 0 <= nx < m):
            continue

        if Map[ny][nx] == 0:
            Dist[ny][nx] = 0
            continue

        if Map[ny][nx] == 1:
            if Dist[ny][nx] == -1:
                Dist[ny][nx] = Dist[cy][cx] + 1
                q.append((ny, nx))
            else:
                if Dist[ny][nx] > Dist[cy][cx] + 1:
                    Dist[ny][nx] = Dist[cy][cx] + 1
                    q.append((ny, nx))

for i in Dist:
    print(" ".join(map(str, i)))