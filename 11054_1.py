from input_from_file import init_file, input
init_file("11054")

N = int(input())
seq = list(map(int, input().split()))

inc_table = [1 for _ in range(N)]
dec_table = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j]:
            inc_table[i] = max(inc_table[i], inc_table[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if seq[i] > seq[j]:
            dec_table[i] = max(dec_table[i], dec_table[j] + 1)

result = 0
for k in range(N):
    result = max(result, inc_table[k] + dec_table[k] - 1)
print(result)