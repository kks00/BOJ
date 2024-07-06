from input_from_file import init_file, input
init_file("17144")

import copy

R, C, T = list(map(int, input().split()))
m = []
for _ in range(R):
    m.append(list(map(int, input().split())))

cleaner_upper = -1
cleaner_lower = -1
for y in range(R):
    if m[y][0] == -1:
        if cleaner_upper == -1:
            cleaner_upper = y
        else:
            cleaner_lower = y

def spread():
    next_m = copy.deepcopy(m)

    for y in range(R):
        for x in range(C):
            if m[y][x] > 0:
                spread_count = 0
                spread_val = m[y][x] // 5
                for oy, ox in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + oy, x + ox
                    if 0 <= ny < R and 0 <= nx < C:
                        if m[ny][nx] >= 0:
                            spread_count += 1
                            next_m[ny][nx] += spread_val
                next_m[y][x] -= spread_val * spread_count

    return next_m

def rotate_upper():
    next_m = copy.deepcopy(m)

    cy, cx, ch = (cleaner_upper, 1, "right")
    while not (cy == cleaner_upper and cx == 0):
        py, px = (-1, -1)
        if ch == "right":
            py, px = (cy, cx - 1)
        elif ch == "up":
            py, px = (cy + 1, cx)
        elif ch == "left":
            py, px = (cy, cx + 1)
        elif ch == "down":
            py, px = (cy - 1, cx)

        pval = m[py][px]
        if py == cleaner_upper and px == 0:
            pval = 0
        next_m[cy][cx] = pval

        if ch == "right":
            cy, cx = (cy, cx + 1)
            if cx >= C:
                ch = "up"
                cy, cx = (cy - 1, cx - 1)
        elif ch == "up":
            cy, cx = (cy - 1, cx)
            if cy < 0:
                ch = "left"
                cy, cx = (cy + 1, cx - 1)
        elif ch == "left":
            cy, cx = (cy, cx - 1)
            if cx < 0:
                ch = "down"
                cy, cx = (cy + 1, cx + 1)
        elif ch == "down":
            cy, cx = (cy + 1, cx)
            if cy >= R:
                break

    return next_m

def rotate_lower():
    next_m = copy.deepcopy(m)

    cy, cx, ch = (cleaner_lower, 1, "right")
    while not (cy == cleaner_lower and cx == 0):
        py, px = (-1, -1)
        if ch == "right":
            py, px = (cy, cx - 1)
        elif ch == "up":
            py, px = (cy + 1, cx)
        elif ch == "left":
            py, px = (cy, cx + 1)
        elif ch == "down":
            py, px = (cy - 1, cx)

        pval = m[py][px]
        if py == cleaner_lower and px == 0:
            pval = 0
        next_m[cy][cx] = pval

        if ch == "right":
            cy, cx = (cy, cx + 1)
            if cx >= C:
                ch = "down"
                cy, cx = (cy + 1, cx - 1)
        elif ch == "down":
            cy, cx = (cy + 1, cx)
            if cy >= R:
                ch = "left"
                cy, cx = (cy - 1, cx - 1)
        elif ch == "left":
            cy, cx = (cy, cx - 1)
            if cx < 0:
                ch = "up"
                cy, cx = (cy - 1, cx + 1)
        elif ch == "up":
            cy, cx = (cy - 1, cx)

    return next_m

for t in range(T):
    m = spread()
    m = rotate_upper()
    m = rotate_lower()

result = 0
for y in range(R):
    for x in range(C):
        result += (0 if m[y][x] < 0 else m[y][x])
print(result)


