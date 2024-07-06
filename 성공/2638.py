from input_from_file import init_file, input
init_file("2638")

import sys
sys.setrecursionlimit(10001)

N, M = list(map(int, input().split()))
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

remain_cheese = set()
for y in range(N):
    for x in range(M):
        if m[y][x] == 1:
            remain_cheese.add((y, x))

def dfs(cy, cx, visited):
    for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = cy + oy, cx + ox
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if (ny, nx) not in visited and m[ny][nx] == 0:
            visited.add((ny, nx))
            m[ny][nx] = 2
            dfs(ny, nx, visited)

def get_curr_insides():
    result = set()
    dfs(0, 0, set())
    for y in range(N):
        for x in range(M):
            if m[y][x] == 0:
                result.add((y, x))
    for y in range(N):
        for x in range(M):
            if m[y][x] == 2:
                m[y][x] = 0
    return result

def get_remove_cheese(curr_insides):
    global remain_cheese
    result = set()

    for curr_cheese in remain_cheese:
        cy, cx = curr_cheese
        count = 0
        for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = cy + oy, cx + ox
            if (ny, nx) in curr_insides:
                continue
            if m[ny][nx] != 0:
                continue
            count += 1
        if count >= 2:
            result.add(curr_cheese)
    return result


result = 0
while True:
    curr_insides = get_curr_insides()
    removes = get_remove_cheese(curr_insides)
    if len(removes) > 0:
        result += 1
        for remove in removes:
            remain_cheese.remove(remove)
            cy, cx = remove
            m[cy][cx] = 0
    else:
        break
print(result)