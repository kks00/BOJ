N = int(input().rstrip())

import math

if N == 0:
    print(0)
elif N <= 2:
    print(N)
else:
    a = math.floor(math.log(N, 2))
    # print(a, 2**a)
    if 2 ** a == N:
        print(1 + a)
    else:
        print(2 + a)