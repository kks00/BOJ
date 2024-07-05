from input_from_file import init_file, input
init_file("11054")

N = int(input())
seq = list(map(int, input().split()))

max_seq = max(seq)

# index y까지의 최대값이 x인 증가 부분수열의 크기
inc_table = [[0 for _ in range(max_seq + 1)] for _ in range(N)]
for x in range(seq[0], max_seq + 1):
    inc_table[0][x] = 1
for y in range(1, N):
    for x in range(max_seq + 1):
        if seq[y] == x:
            inc_table[y][x] = inc_table[y][x - 1] + 1
        else:
            inc_table[y][x] = max(inc_table[y - 1][x], inc_table[y][x - 1])


# index y부터의 최대값이 x인 감소 부분수열의 크기
dec_table = [[0 for _ in range(max_seq + 1)] for _ in range(N)]
for x in range(seq[-1], max_seq + 1):
    dec_table[N - 1][x] = 1
for y in range(N - 2, -1, -1):
    for x in range(max_seq + 1):
        if seq[y] == x:
            dec_table[y][x] = dec_table[y][x - 1] + 1
        else:
            dec_table[y][x] = max(dec_table[y + 1][x], dec_table[y][x - 1])

result = 0
for k in range(-1, N):
    curr_result = 0

    left = seq[:k + 1]
    right = seq[k + 1:]

    print(k, left, right)
    max_val = max_seq
    if len(left) > 0:
        curr_result += inc_table[k][max_val]
        max_val = max(left) - 1
        print(inc_table[k][max_val])
    if len(right) > 0:
        curr_result += dec_table[k + 1][max_val]
        print(dec_table[k + 1][max_val])

    result = max(result, curr_result)

print(result)