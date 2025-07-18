from input_from_file import init_file, input
init_file("2615")

m = []
for _ in range(19):
    m.append(list(map(int, input().rstrip().split())))

white, black = [], []
for y in range(19):
    for x in range(19):
        if m[y][x] == 1:
            black.append((y, x))
        elif m[y][x] == 2:
            white.append((y, x))

offsets = [
    ((-1, 0), (1, 0)), # 상하 연속 체크
    ((0, -1), (0, 1)), # 좌우 연속 체크
    ((1, 1), (-1, -1)), # 윈쪽상단 오른쪽하단 대각선 체크
    ((1, -1), (-1, 1)) # 오른쪽상단 왼쪽하단 대각선 체크
]

from collections import deque
def calc(col, offs, y, x):
    visited = set()
    visited.add((y, x))
    q = deque()
    q.append((y, x, 1))
    count = 1
    while len(q) > 0:
        cy, cx, cc = q.popleft()
        for oy, ox in offs:
            ny, nx = cy + oy, cx + ox
            if 0 <= ny < 19 and 0 <= nx < 19:
                if m[ny][nx] != col:
                    continue
                if (ny, nx) in visited:
                    continue
                visited.add((ny, nx))
                q.append((ny, nx, cc + 1))
                count += 1
    return count, visited

def solve(col, lst):
    for offset in offsets:
        for cy, cx in lst:
            r, v = calc(col, offset, cy, cx)
            # print(col, (cy, cx), offset, r, v)
            if r == 5: # 선 상에 5개만 놓여있으면 출력
                print(col)
                v = list(v)
                v = sorted(v, key=lambda x: (x[1], x[0]))
                print(v[0][0] + 1, v[0][1] + 1)
                return True
if not (solve(1, black) or solve(2, white)):
    print(0)