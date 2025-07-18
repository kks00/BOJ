from input_from_file import init_file, input
init_file("11725")

N = int(input().rstrip())

graph = {}
for i in range(1, N+1):
    graph[i] = []
for _ in range(N-1):
    a, b = list(map(int, input().rstrip().split()))
    graph[a].append(b)
    graph[b].append(a)

parent = {}
def visit(graph, visited, curr):
    for i in graph[curr]:
        if i in visited:
            continue
        visited.add(i)
        parent[i] = curr
        visit(graph, visited, i)
visit(graph, set(), 1)

# parent = {}
# root = {1: {}}
# def insert(visited, root, key, val):
#     for ck in root.keys():
#         if ck in visited:
#             continue
#         visited.add(ck)
#         if ck == key:
#             parent[val] = key
#             root[key][val] = {}
#             return True
#         if insert(visited, root[ck], key, val):
#             return True
#     return False
#
# def search(visited, root, key):
#     is_found=False
#     for ck in root.keys():
#         if ck in visited:
#             continue
#         visited.add(ck)
#         if ck == key:
#             is_found=True
#             break
#         if search(visited, root[ck], key):
#             is_found=True
#             break
#     return is_found
#
# for _ in range(N-1):
#     a, b = list(map(int, input().rstrip().split()))
#     # print(a, b, search(root, a), search(root, b))
#     if search(set(), root, a):
#         insert(set(), root, a, b)
#     else:
#         insert(set(), root, b, a)
#
# # print(root)

result = [(a, b) for a, b in parent.items()]
result = sorted(result)
for a, b in result[1:]:
    print(b)