from input_from_file import init_file, input
init_file("1325")

N, M = list(map(int, input().rstrip().split()))

m = {}
for _ in range(M):
    A, B = list(map(int, input().rstrip().split()))
    if B not in m:
        m[B] = []
    m[B].append(A)

from collections import deque

def visit(n):
    result = 1
    visited = set()
    visited.add(n)

    q = deque()
    q.append(n)
    while len(q) > 0:
        curr = q.popleft()
        if curr not in m:
            continue
        for next in m[curr]:
            if next in visited:
                continue
            visited.add(next)
            q.append(next)
            result += 1
    return result

results = []
for i in range(1, N + 1):
    results.append((i, visit(i)))
results = sorted(results, key=lambda x: -1 * x[1])

max_val = results[0][1]
for a, b in results:
    if b < max_val:
        break
    print(a, end=" ")
print()