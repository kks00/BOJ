from input_from_file import init_file, input
init_file("11286")

import heapq

plus_h, minus_h = ([], [])

N = int(input())
for _ in range(N):
    i = int(input())
    if i > 0:
        heapq.heappush(plus_h, i)
    elif i < 0:
        heapq.heappush(minus_h, abs(i))
    else:
        plus_min, minus_min = (None, None)
        if len(plus_h) > 0:
            plus_min = heapq.heappop(plus_h)
        if len(minus_h) > 0:
            minus_min = heapq.heappop(minus_h)

        if (plus_min is None) and (minus_min is None):
            print(0)
        elif (plus_min is None):
            print(-1 * minus_min)
        elif (minus_min is None):
            print(plus_min)
        else:
            if plus_min >= minus_min:
                print(-1 * minus_min)
                heapq.heappush(plus_h, plus_min)
            else:
                print(plus_min)
                heapq.heappush(minus_h, minus_min)