N, K = list(map(int, input().rstrip().split()))

'''
N=20 K=2

N=0 K=0 0
N=1 K=0 0

N=0 K=1 0 1
N=1 K=1 1 1
N=2 K=1 2 1
N=3 K=1 3 1

N=0 K=2 0+0 1
N=1 K=2 0+1 1+0 2
N=2 K=2 0+2 2+0 1+1 3
N=3 K=2 1+2 2+1 2

N=0 K=3 0+0+0 1
N=1 K=3 1+0+0 0+1+0 0+0+1 3
N=2 K=3 0+0+2 0+2+0 2+0+0 0+1+1 1+0+1 1+1+0 6
=> K=2로 0만들기+2: 1
=> K=2로 1만들기+1: 2
=> K=2로 2만들기+0: 3 
'''

table = [[0 for _ in range(N+1)] for _ in range(K+1)]
for x in range(N+1):
    table[1][x] = 1
for y in range(2, K+1):
    for x in range(0, N+1):
        for i in range(x+1):
            table[y][x] = (table[y][x] + table[y-1][x-i]) % 1000000000

# for i in table:
#     print(i)
print(table[K][N])