from input_from_file import init_file, input
init_file("1260")

from collections import deque

'''
- stack으로 그래프 DFS탐색
    - 스택에 역순으로 현재 노드로부터 갈 수 있는 정점 저장
    - 스택에서 하나씩 꺼내서 방문처리
        - 스택에서 하나씩 꺼내었을 때 방문한 정점 출력
'''

table = {}

N, M, V = list(map(int, input().rstrip().split()))
for _ in range(M):
    a, b = list(map(int, input().rstrip().split()))
    if a in table:
        table[a].append(b)
    else:
        table[a] = [b]
    if b in table:
        table[b].append(a)
    else:
        table[b] = [a]
for key in table.keys():
    table[key].sort()

# visited = set()
# visited.add(V)
# def dfs(v):
#     global visited
#
#     print(v, end=" ")
#     if v not in table:
#         return
#     for next in table[v]:
#         if next in visited:
#             continue
#         visited.add(next)
#         dfs(next)

def dfs(start):
    visited = set()
    stack = []
    stack.append(start)
    while len(stack) > 0:
        top = stack.pop()
        if top in visited:
            continue
        visited.add(top)
        print(top, end=" ")
        if top not in table:
            continue
        for next in table[top][::-1]:
            if next in visited:
                continue
            stack.append(next)

def bfs(start):
    visited = set()
    visited.add(start)
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        top = queue.popleft()
        print(top, end=" ")
        if top not in table:
            continue
        for next in table[top]:
            if next in visited:
                continue
            visited.add(next)
            queue.append(next)
    print()

dfs(V)
print()
bfs(V)