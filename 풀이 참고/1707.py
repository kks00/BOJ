from input_from_file import init_file, input
init_file("1707")

import sys
sys.setrecursionlimit(20000)

flag = True
visited = set()
def solve(graph, col, node):
    global flag

    if col[node] == -1: col[node] = 0
    if node not in graph:
        return flag

    for next in graph[node]:
        if col[next] == col[node]:
            flag = False
            return flag

        if next in visited:
            continue
        visited.add(next)

        col[next] = 0 if col[node] == 1 else 1
        if not solve(graph, col, next):
            return flag
    return flag

def solve_problem(graph, col, V):
    global flag, visited
    visited = set()
    for i in range(1, V + 1):
        flag = True
        visited.add(i)
        if not solve(graph, col, i):
            return False
    return True

K = int(input().rstrip())
for _ in range(K):
    V, E = list(map(int, input().rstrip().split()))

    col = {}
    for i in range(1, V + 1):
        col[i] = -1

    graph = {}
    for _ in range(E):
        u, v = list(map(int, input().rstrip().split()))
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    print("YES" if solve_problem(graph, col, V) else "NO")