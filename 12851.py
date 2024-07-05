N, K = list(map(int, input().split()))

from collections import deque

q = deque()
q.append((N, 0))
result = [int(1e9), 0]
visited = {}
while (len(q) > 0):
    p, c = q.popleft()
    if p == K:
        result[0] = min(result[0], c)
        result[1] += 1
        continue
    else:
        if c + 1 > result[0]:
            continue
        for np in (p - 1, p + 1, p * 2):
            if not (0 <= np <= 100000):
                continue
            if np in visited:
                if visited[np] < c + 1:
                    continue
            visited[np] = c + 1
            q.append((np, c + 1))

for i in result:
    print(i)