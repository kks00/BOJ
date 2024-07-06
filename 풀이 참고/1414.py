from input_from_file import init_file, input
init_file("1414")

import heapq

N = int(input())
m = []
for _ in range(N):
    m.append(list(input()))

sum_val = 0
max_val = 53
def convert(v):
    if ord('A') <= ord(v) <= ord('Z'):
        return 27 + ord(v) - ord('A')
    elif ord('a') <= ord(v) <= ord('z'):
        return 1 + ord(v) - ord('a')
    return 0

h = []
for y in range(N):
    for x in range(N):
        m[y][x] = convert(m[y][x])
        if m[y][x] > 0:
            heapq.heappush(h, (m[y][x], (y, x)))
        sum_val += m[y][x]

parent = [-1 for _ in range(N)]

def get_parent(i):
    if parent[i] == -1:
        return i
    parent[i] = get_parent(parent[i])
    return parent[i]

def set_parent(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)
    parent[a_parent] = b_parent

def solve():
    selected = 0
    selected_cost = 0
    while (selected < N - 1) and (len(h) > 0):
        curr_cost, curr_pos = heapq.heappop(h)
        a, b = curr_pos

        a_parent, b_parent = get_parent(a), get_parent(b)
        if a_parent != b_parent:
            selected += 1
            selected_cost += curr_cost
            set_parent(a, b)

    if selected == N - 1:
        return sum_val - selected_cost
    return -1

print(solve())

# for y in range(N):
#     for x in range(N):
#         m[y][x] = convert(m[y][x])
#         sum_val += m[y][x]
#
# def solve():
#     result = 0
#     for start_node in range(N):
#         selected = 0
#         selected_cost = 0
#
#         min_dist = [max_val for _ in range(N)]
#         visited = set()
#         h = []
#
#         for i in range(N):
#             new_cost = m[start_node][i]
#             if new_cost > 0 and i != start_node:
#                 heapq.heappush(h, (new_cost, i))
#         while (len(h) > 0 and (selected < N - 1)):
#             curr_cost, curr_node = heapq.heappop(h)
#             if curr_node in visited:
#                 continue
#             visited.add(curr_node)
#
#             selected += 1
#             selected_cost += curr_cost
#
#             for i in range(N):
#                 new_cost = m[curr_node][i]
#                 if (curr_node != i) and (new_cost > 0) and (new_cost < min_dist[i]) and (i not in visited):
#                     min_dist[i] = new_cost
#                     heapq.heappush(h, (new_cost, i))
#
#         print(selected, sum_val - selected_cost)
#         result = max(result, sum_val - selected_cost)
#     return result
#
# print(solve())