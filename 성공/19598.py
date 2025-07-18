from input_from_file import init_file, input
init_file("19598")

'''
(1, 2) 1 -> [2]
(1, 4) 2 -> [2, 4]
(2, 3) 1 -> [4, 4]
(5, 30) 2 -> [4]
'''

N = int(input().rstrip())
l = []
for _ in range(N):
    s, e = list(map(int, input().rstrip().split()))
    l.append((s, e))
l = sorted(l)

import heapq
h = []
result = 0
for s, e in l:
    if len(h) < 1 or h[0] > s:
        heapq.heappush(h, e)
        result += 1
    else:
        heapq.heappop(h)
        heapq.heappush(h, e)
print(result)