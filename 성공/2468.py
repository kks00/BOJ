from input_from_file import init_file, input
init_file("2468")

import sys
sys.setrecursionlimit(1000*1000)

N = int(input())
map_data = []
for _ in range(N):
    map_data.append(list(map(int, input().split())))

result = 0

def dfs(map, cy, cx, visited, max_val):
    for oy, ox in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ny, nx = cy + oy, cx + ox
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if (ny, nx) in visited:
            continue
        if map[ny][nx] <= max_val:
            continue

        visited.add((ny, nx))
        dfs(map, ny, nx, visited, max_val)

for curr_max in range(100, -1, -1):
    visited = set()
    curr_blocks = 0
    for y in range(N):
        for x in range(N):
            if ((y, x) not in visited) and map_data[y][x] > curr_max:
                visited.add((y, x))
                dfs(map_data, y, x, visited, curr_max)
                curr_blocks += 1
    result = max(result, curr_blocks)

print(result)