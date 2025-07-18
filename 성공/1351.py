N, P, Q = list(map(int, input().rstrip().split()))

import math

# A = [0 for _ in range(N + 1)]
# A[0] = 1
#
# for i in range(1, N+1):
#     a = int(math.floor(i/P))
#     b = int(math.floor(i/Q))
#
#     A[i] = A[a] + A[b]
#
# print(A[N])

table = {}
def solve(n):
    if n == 0:
        return 1
    if n in table:
        return table[n]

    a = int(math.floor(n/P))
    b = int(math.floor(n/Q))
    result = solve(a) + solve(b)
    table[n] = result
    return table[n]

print(solve(N))