from input_from_file import init_file, input
init_file("12919")

S = input()
T = input()

from collections import deque

def solve():
    q = deque()
    q.append(T)
    while (len(q) > 0):
        curr_t = q.popleft()
        if len(curr_t) <= len(S):
            if curr_t == S:
                return True
            continue

        if curr_t[0] == "B":
            q.append(curr_t[1:][::-1])
        if curr_t[-1] == "A":
            q.append(curr_t[:-1])
    return False

if solve():
    print(1)
else:
    print(0)