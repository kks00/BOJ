from input_from_file import init_file, input
init_file("1967")

N = int(input())
tree = {}
dists = {}
for i in range(1, N + 1):
    tree[i] = {}
    dists[i] = {}

for _ in range(N - 1):
    start, dest, cost = list(map(int, input().split()))
    tree[start][dest] = cost

def mid_search(root, path):
    curr_childs = list(tree[root].keys())

    if len(curr_childs) >= 1:
        child_key = curr_childs[0]
        path.append((root, tree[root][child_key]))
        mid_search(child_key, path)
        path.pop()

    next_dist = 0
    for start, cost in path[::-1]:
        next_dist += cost
        dists[start][root] = next_dist

    if len(curr_childs) >= 2:
        child_key = curr_childs[1]
        path.append((root, tree[root][child_key]))
        mid_search(child_key, path)
        path.pop()


mid_search(1, [])


def get_route(root, find_key, route):
    result = False
    route.append(root)
    if root == find_key:
        return True
    for dest, _ in list(tree[root].items()):
        if get_route(dest, find_key, route):
            result = True
    if not result:
        route.pop()
    return result

def max_comm_parent(a, b):
    route_a = []
    get_route(1, a, route_a)

    route_b = []
    get_route(1, b, route_b)
    route_b = set(route_b)

    result = 1
    for i in route_a:
        if i in route_b:
            result = max(result, i)
    return result


# for start, dist in dists.items():
#     print(start, dist)

max_parent = {}
for a in range(1, N + 1):
    for b in range(a, N + 1):
        max_parent[(a, b)] = max_comm_parent(a, b)

result = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue

        if b in dists[a]: # 부모 - 자식 관계일 경우
            result = max(result, dists[a][b])
            continue
        if a in dists[b]:
            result = max(result, dists[b][a])
            continue

        curr_max_parent = max_parent[(min(a, b), max(a, b))]
        if a in dists[curr_max_parent] and b in dists[curr_max_parent]:
            result = max(result, dists[curr_max_parent][a] + dists[curr_max_parent][b])
print(result)