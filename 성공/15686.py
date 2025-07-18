from input_from_file import init_file, input
init_file("15686")

N, M = list(map(int, input().rstrip().split()))

m = []
for y in range(N):
    m.append(list(map(int, input().rstrip().split())))

home = set()
chicken = set()
for y in range(N):
    for x in range(N):
        if m[y][x] == 2:
            chicken.add((y, x))
        elif m[y][x] == 1:
            home.add((y, x))

def get_curr_dist(homes, chickens):
    result = 0
    for hy, hx in homes:
        dists = [abs(hy - cy) + abs(hx - cx) for cy, cx in chickens]
        result += min(dists)
    return result

import itertools
result = int(1e9)
for i in range(1, M + 1):
    selects = list(itertools.combinations(list(chicken), i))
    for select in selects:
        # print(select, get_curr_dist(list(home), select))
        result = min(result, get_curr_dist(list(home), select))
print(result)