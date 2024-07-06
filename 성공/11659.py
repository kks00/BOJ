from input_from_file import init_file, input
init_file("11659")

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))

table = [0 for _ in range(N + 1)]
table[0] = 0
for i in range(N):
    table[i + 1] = table[i] + lst[i]

for _ in range(M):
    i, j = list(map(int, input().split()))
    i -= 1
    print(table[j] - table[i])