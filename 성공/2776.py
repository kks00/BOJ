from input_from_file import init_file, input
init_file("2776")

def exists(l, v):
    left, right = 0, len(l) - 1
    while (left <= right):
        mid = ((left + right) // 2)
        if l[mid] == v:
            return True
        if l[mid] < v:
            left = mid + 1
        else:
            right = mid - 1
    return False

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    dic1 = list(map(int, input().rstrip().split()))
    dic1 = sorted(dic1)
    M = int(input().rstrip())
    dic2 = list(map(int, input().rstrip().split()))
    for v in dic2:
        print(1 if exists(dic1, v) else 0)
