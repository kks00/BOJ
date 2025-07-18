'''
[0, 1, 1, 2, 3, 5, 8...]

0: 0 1 0
1: 1 0 1
2: 1 1 1 
3: 2 1 2
4: 3 2 3
5: 5
6: 8
'''

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    zero = [0 for _ in range(N + 1)]
    one = [0 for _ in range(N + 1)]

    zero[:2] = [1, 0]
    one[:2] = [0, 1]

    for i in range(2, N + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
    print(zero[N], one[N])
