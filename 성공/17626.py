N = int(input())

table = [4 for _ in range(50001)]
table[0] = 0
for i in range(50001):
    curr_val = table[i]
    for j in range(251):
        next_index = j ** 2 + i
        if next_index > 50000:
            break
        table[next_index] = min(table[next_index], curr_val + 1)

#print(table)
print(table[N])