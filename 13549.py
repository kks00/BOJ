N, K = list(map(int, input().split()))

from collections import deque

q = deque()
q.append((0, N, 0))
visited = {}
while len(q) > 0:
    time, pos, last_op = q.popleft()
    if pos == K:
        print(time)
        break

    for next_pos, next_time, next_op in ((pos * 2, time, 1), (pos - 1, time + 1, 2), (pos + 1, time + 1, 3)):
        if pos > K and next_op == 1: # 현재 수가 K보다 큰 상태에서는 곱셈 수행하지않기
            continue
        if next_pos in visited:
            if next_time >= visited[next_pos]:
                continue
        visited[next_pos] = next_time
        q.append((next_time, next_pos, next_op))

