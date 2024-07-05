from input_from_file import init_file, input
init_file("14938")

n, m, r = list(map(int, input().split()))
items = list(map(int, input().split()))

MAX_DIST = 15 * r + 1
map_data = [[MAX_DIST for _ in range(n)] for _ in range(n)]
for _ in range(r):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    map_data[a][b] = c
    map_data[b][a] = c
for i in range(n):
    map_data[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if map_data[i][k] < MAX_DIST and map_data[k][j] < MAX_DIST:
                map_data[i][j] = min(map_data[i][j], map_data[i][k] + map_data[k][j])

result = []
for i in range(n):
    curr_result = 0
    for j in range(n):
        if map_data[i][j] <= m:
            curr_result += items[j]
    result.append((curr_result, i))
result = sorted(result, reverse=True)
print(result[0][0])