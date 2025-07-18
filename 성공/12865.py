from input_from_file import init_file, input
init_file("12865")

'''
배낭 문제
table[y][x] = y개 까지 물건을 무게 x까지 담았을 때의 최대 가치
'''

N, K = list(map(int, input().rstrip().split()))
items = []
for _ in range(N):
    w, v = list(map(int, input().rstrip().split()))
    items.append((w, v))

width = K+1
height = N+1

table = [[0 for _ in range(width)] for _ in range(height)]

for i, k in enumerate(items):
    w, v = k
    for x in range(width):
        table[i+1][x] = table[i][x]
        dy, dx = i, x-w
        if 0 <= dx < width:
            table[i+1][x] = max(table[i+1][x], table[dy][dx] + v)

# for i in table:
#     print(i)
print(table[height-1][width-1])