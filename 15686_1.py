from input_from_file import init_file, input
init_file("15686")

import itertools

N, M = list(map(int, input().split()))
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

homes = []
chickens = []
for y in range(N):
    for x in range(N):
        if m[y][x] == 1:
            homes.append((y, x))
        elif m[y][x] == 2:
            chickens.append((y, x))

def get_min_chicken_dist(curr_select):
    result = 0
    for curr_home in homes:
        curr_home_dist = int(1e9)
        for curr_chicken in curr_select:
            cy, cx = curr_chicken
            hy, hx = curr_home
            dist = abs(cy - hy) + abs(cx - hx)
            curr_home_dist = min(curr_home_dist, dist)
        result += curr_home_dist
    return result

result = int(1e9)
for count in range(1, M + 1):
    curr_selects = list(itertools.combinations(chickens, count))

    for curr_select in curr_selects:
        result = min(result, get_min_chicken_dist(curr_select))
print(result)