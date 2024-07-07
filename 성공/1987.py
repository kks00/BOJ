from input_from_file import init_file, input
init_file("1987")

R, C = list(map(int, input().split()))
m = []
for _ in range(R):
    m.append(list(input()))

max_depth = 0
def dfs(cy, cx, depth, visited):
    global max_depth

    max_depth = max(max_depth, depth)

    for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = cy + oy, cx + ox

        if 0 <= ny < R and 0 <= nx < C:
            if m[ny][nx] not in visited:
                visited.add(m[ny][nx])
                dfs(ny, nx, depth + 1, visited)
                visited.remove(m[ny][nx])

dfs(0, 0, 1, set(m[0][0]))

print(max_depth)