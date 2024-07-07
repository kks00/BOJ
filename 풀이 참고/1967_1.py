from input_from_file import init_file, input
init_file("1967")

N = int(input())
tree = {}
for i in range(1, N + 1):
    tree[i] = {}
for _ in range(N - 1):
    a, b, cost = list(map(int, input().split()))
    tree[a][b] = cost
    tree[b][a] = cost

max_dist_node, max_val = (-1, -1)
visited = None
def dfs(node, cost):
    global max_dist_node, max_val

    curr_visited = 0
    for dest, next_cost in tree[node].items():
        if dest not in visited:
            curr_visited += 1
            visited.add(dest)
            dfs(dest, cost + next_cost)

    if curr_visited < 1:
        if max_val < cost:
            max_dist_node = node
            max_val = cost
        return

visited = set()
visited.add(1)
dfs(1, 0)

next_start_node = max_dist_node
max_dist_node, max_val = (-1, -1)
visited = set()
visited.add(next_start_node)
dfs(next_start_node, 0)
print(max_val)