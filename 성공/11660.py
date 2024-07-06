from input_from_file import init_file, input
init_file("11660")

N, M = list(map(int, input().split()))
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))
req = []
for _ in range(M):
    req.append(list(map(int, input().split())))

table = [[0 for _ in range(N + 1)] for _ in range(N)]
for y in range(N):
    for x in range(1, N + 1):
        table[y][x] = table[y][x - 1] + m[y][x - 1]

for cr in req:
    y1, x1, y2, x2 = cr
    y1, y2 = y1 - 1, y2 - 1

    result = 0
    for y in range(y1, y2+1):
        result += table[y][x2] - table[y][x1 - 1]
    print(result)