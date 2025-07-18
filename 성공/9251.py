from input_from_file import init_file, input
init_file("9251")

a = input().rstrip()
b = input().rstrip()

row = len(a) + 1
col = len(b) + 1

table = [[0 for _ in range(col)] for _ in range(row)]

for y in range(1, row):
    for x in range(1, col):
        if a[y-1] == b[x-1]:
            table[y][x] = table[y-1][x-1] + 1
        else:
            table[y][x] = max(table[y-1][x], table[y][x-1])

# for i in table[1:]:
#     print(i[1:])
print(table[row-1][col-1])