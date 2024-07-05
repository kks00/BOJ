from input_from_file import init_file, input
init_file("30805")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

table = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for y in range(1, N + 1):
    for x in range(1, M + 1):
        if A[y - 1] == B[x - 1]:
            next_val = table[y - 1][x - 1] + 1
            table[y][x] = next_val
        else:
            next_val = max(table[y - 1][x], table[y][x - 1])
            table[y][x] = next_val

for i in table:
    print(i)

seq = []
cy, cx = N, M
max_val = max(N, M) + 1
while (cy >= 0 and cx >= 0):
    left = max_val
    upper = max_val
    me = table[cy][cx]
    if me == 0:
        break

    if cx - 1 >= 0:
        left = table[cy][cx - 1]
    if cy - 1 >= 0:
        upper = table[cy - 1][cx]

    if left == upper and upper == me:
        cy -= 1
        cx -= 1
        seq.append(max(B[cx], A[cy]))
    elif left == me:
        cx -= 1
    elif upper == me:
        cy -= 1
    else:
        cy -= 1
        cx -= 1
        seq.append(max(B[cx], A[cy]))
seq = seq[::-1]
print(seq)

seqs = []
import itertools
for i in range(1, len(seq) + 1):
    seqs.extend(list(itertools.combinations(seq, i)))
seqs= sorted(seqs, reverse=True)
print(seqs)

if len(seqs) > 0:
    print(len(seqs[0]))
    print(" ".join(map(str, seqs[0])))
else:
    print(0)
