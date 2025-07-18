from input_from_file import init_file, input
init_file("1051")

N, M = list(map(int, input().rstrip().split()))

m = []
for _ in range(N):
    m.append(list(map(int, input().rstrip())))

result = 1
for size in range(2, min(N, M) + 1):
    for sy in range(0, N - size + 1):
        for sx in range(0, M - size + 1):
            lt, lb, rt, rb = m[sy][sx], m[sy + size - 1][sx], m[sy][sx + size - 1], m[sy + size - 1][sx + size - 1]
            if lt == lb and lb == rt and rt == rb:
                result = max(result, size)

print(result * result)