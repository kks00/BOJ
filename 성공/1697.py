N, K = list(map(int, input().rstrip().split()))

from collections import deque

def solve():
    queue = deque()
    queue.append((N, 0))
    visited = set()
    visited.add(N)

    while len(queue) > 0:
        pos, time = queue.popleft()
        if pos == K:
            return time

        next_list = set()
        if pos > K:
            next_list.add(pos - 1)
        else:
            next_list.add(pos - 1)
            next_list.add(pos + 1)
            next_list.add(pos * 2)

        for next in next_list:
            if next == K:
                return time + 1
            if next in visited:
                continue
            visited.add(next)
            queue.append((next, time + 1))

print(solve())