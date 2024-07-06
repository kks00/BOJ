from input_from_file import init_file, input
init_file("2805")

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

left, right = (0, 1000000000)
last_success = 0
while (left <= right):
    mid = ((left + right) // 2)

    curr_tree = 0
    for tree in trees:
        if tree > mid:
            curr_tree += tree - mid
    # print(left, right, mid, curr_tree)

    if curr_tree >= M:
        last_success = max(last_success, mid)
        left = mid + 1
    else:
        right = mid - 1

print(last_success)