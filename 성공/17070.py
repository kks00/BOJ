from input_from_file import init_file, input
init_file("17070")

N = int(input())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

from collections import deque

def check_pos(points):
    for point in points:
        y, x = point
        if not (0 <= y < N and 0 <= x < N):
            return False
        if m[y][x] == 1:
            return False
    return True

def bfs():
    result = 0

    q = deque()

    init_pos1, init_pos2 = ((0, 0), (0, 1))
    init_dir = 0 # 0: 가로, 1: 세로, 2: 대각선
    q.append((init_pos1, init_pos2, init_dir))
    while (len(q) > 0):
        pos1, pos2, dir = q.popleft()
        y1, x1 = pos1
        y2, x2 = pos2

        if (y1 == N - 1 and x1 == N - 1) or (y2 == N - 1 and x2 == N - 1):
            result += 1

        if dir == 0: # 가로일 때
            next_pos1 = (y1, x1 + 1)
            next_pos2 = (y2, x2 + 1)
            if check_pos((next_pos1, next_pos2)):
                q.append((next_pos1, next_pos2, 0)) # 가로 방향 이동

            next_pos1 = (y2, x2)
            next_pos2 = (y2, x2 + 1)
            next_pos3 = (y2 + 1, x2)
            next_pos4 = (y2 + 1, x2 + 1)
            if check_pos((next_pos2, next_pos3, next_pos4)):
                q.append((next_pos1, next_pos4, 2)) # 대각선 방향 이동
        elif dir == 1: # 세로일 때
            next_pos1 = (y1 + 1, x1)
            next_pos2 = (y2 + 1, x2)
            if check_pos((next_pos1, next_pos2)):
                q.append((next_pos1, next_pos2, 1)) # 세로 방향 이동

            next_pos1 = (y2, x2)
            next_pos2 = (y2, x2 + 1)
            next_pos3 = (y2 + 1, x2)
            next_pos4 = (y2 + 1, x2 + 1)
            if check_pos((next_pos2, next_pos3, next_pos4)):
                q.append((next_pos1, next_pos4, 2)) # 대각선 방향 이동
        elif dir == 2: # 대각선 방향일 때
            next_pos1 = (y2, x2)
            next_pos2 = (y2, x2 + 1)
            if check_pos((next_pos1, next_pos2)):
                q.append((next_pos1, next_pos2, 0)) # 가로 방향 이동

            next_pos1 = (y2, x2)
            next_pos2 = (y2 + 1, x2)
            if check_pos((next_pos1, next_pos2)):
                q.append((next_pos1, next_pos2, 1)) # 세로 방향 이동

            next_pos1 = (y2, x2)
            next_pos2 = (y2, x2 + 1)
            next_pos3 = (y2 + 1, x2)
            next_pos4 = (y2 + 1, x2 + 1)
            if check_pos((next_pos2, next_pos3, next_pos4)):
                q.append((next_pos1, next_pos4, 2)) # 대각선 방향 이동

    return result

print(bfs())