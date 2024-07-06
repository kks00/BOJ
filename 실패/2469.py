from input_from_file import init_file, input
init_file("2469")

k = int(input())
n = int(input())
seq = input()
m = {}

unknown_y = -1
for y in range(n):
    for x, v in enumerate(list(input())):
        if v == "?":
            unknown_y = y
            break
        if v == "-":
            dy, dx = (y, x)
            m[(dy, dx)] = 1
            dy, dx = (y, x + 1)
            m[(dy, dx)] = -1

result = [None for _ in range(k - 1)]
def test(key, cy, cx):
    if cy == n + 1:
        if seq[cx] == chr(ord('A') + key):
            return True
        return False

    if cy == unknown_y:
        if test(key, cy + 1, cx):
            return True
        else:
            if cx + 1 < k and test(key, cy + 1, cx + 1):
                if result[cx] == None:
                    result[cx] = 1
                else:
                    result[cx] += 1
            if cx - 1 >= 0 and test(key, cy + 1, cx - 1):
                if result[cx - 1] == None:
                    result[cx - 1] = -1
                else:
                    result[cx - 1] -= 1
        return False

    if (cy, cx) in m:
        offset = m[(cy, cx)]
        return test(key, cy + 1, cx + offset)
    else:
        return test(key, cy + 1, cx)

def solve():
    for i in range(k):
        test(i, -1, i)

    result_str = ["*" for _ in range(k - 1)]

    for i in range(k - 1):
        if result[i] == None:
            continue
        if result[i] == 0:
            result_str[i] = "-"
        else:
            return "x" * (k - 1)
    return "".join(result_str)

print(solve())