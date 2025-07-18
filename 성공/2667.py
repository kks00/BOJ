from input_from_file import init_file, input
init_file("2667")

N = int(input().rstrip())
m = []
for _ in range(N):
    m.append(list(map(int, input().rstrip())))

visited = set()
regions = []

from collections import deque
def visit(y, x):
    global visited

    queue = deque()
    queue.append((y, x))
    visited.add((y, x))
    curr_region = 1

    while len(queue) > 0:
        cy, cx = queue.popleft()
        for oy, ox in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = cy + oy, cx + ox
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if m[ny][nx] == 0:
                continue
            if (ny, nx) in visited:
                continue
            visited.add((ny, nx))
            queue.append((ny, nx))
            curr_region += 1
    return curr_region

for cy in range(N):
    for cx in range(N):
        if m[cy][cx] == 1 and (not (cy, cx) in visited):
            regions.append(visit(cy, cx))

regions = sorted(regions)
print(len(regions))
for i in regions:
    print(i)