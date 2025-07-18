from input_from_file import init_file, input
init_file("11053")

'''
10 20 10 30 20 50
10 20 30 50

10 1 2 20 3 4 25 30
'''

N = int(input().rstrip())
l = list(map(int, input().rstrip().split()))

table = [0 for _ in range(1002)]

for i in range(N):
    for j in range(l[i] + 1, 1002):
        table[j] = max(table[j], table[l[i]] + 1)
print(table[1001])