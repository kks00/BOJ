from input_from_file import init_file, input
init_file("17070")

N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

def check_pos(points):
    for point in points:
        y, x = point
        if not (0 <= y < N and 0 <= x < N):
            return False
        if m[y][x] == 1:
            return False
    return True

table = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

def solve(pos1, pos2, dir):
    y1, x1 = pos1
    y2, x2 = pos2
    if (y1 == N - 1 and x1 == N - 1) or (y2 == N - 1 and x2 == N - 1):
        return 1

    if table[y1][x1][dir] > 0:
        return table[y1][x1][dir]

    curr_result = 0
    if dir == 0: # 가로일 때
        next_pos1 = (y1, x1 + 1)
        next_pos2 = (y2, x2 + 1)
        if check_pos((next_pos1, next_pos2)):
            curr_result += solve(next_pos1, next_pos2, 0) # 가로 방향 이동

        next_pos1 = (y2, x2)
        next_pos2 = (y2, x2 + 1)
        next_pos3 = (y2 + 1, x2)
        next_pos4 = (y2 + 1, x2 + 1)
        if check_pos((next_pos2, next_pos3, next_pos4)):
            curr_result += solve(next_pos1, next_pos4, 2) # 대각선 방향 이동
    elif dir == 1: # 세로일 때
        next_pos1 = (y1 + 1, x1)
        next_pos2 = (y2 + 1, x2)
        if check_pos((next_pos1, next_pos2)):
            curr_result += solve(next_pos1, next_pos2, 1) # 세로 방향 이동

        next_pos1 = (y2, x2)
        next_pos2 = (y2, x2 + 1)
        next_pos3 = (y2 + 1, x2)
        next_pos4 = (y2 + 1, x2 + 1)
        if check_pos((next_pos2, next_pos3, next_pos4)):
            curr_result += solve(next_pos1, next_pos4, 2) # 대각선 방향 이동
    elif dir == 2: # 대각선 방향일 때
        next_pos1 = (y2, x2)
        next_pos2 = (y2, x2 + 1)
        if check_pos((next_pos1, next_pos2)):
            curr_result += solve(next_pos1, next_pos2, 0) # 가로 방향 이동

        next_pos1 = (y2, x2)
        next_pos2 = (y2 + 1, x2)
        if check_pos((next_pos1, next_pos2)):
            curr_result += solve(next_pos1, next_pos2, 1) # 세로 방향 이동

        next_pos1 = (y2, x2)
        next_pos2 = (y2, x2 + 1)
        next_pos3 = (y2 + 1, x2)
        next_pos4 = (y2 + 1, x2 + 1)
        if check_pos((next_pos2, next_pos3, next_pos4)):
            curr_result += solve(next_pos1, next_pos4, 2) # 대각선 방향 이동

    table[y1][x1][dir] = max(table[y1][x1][dir], curr_result)
    return table[y1][x1][dir]

if m[N - 1][N - 1] != 1:
    solve((0, 0), (0, 1), 0)

result = 0
for i in range(3):
    result = max(result, table[0][0][i])
print(result)