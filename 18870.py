from input_from_file import init_file, input
init_file("18870")

N = int(input())
Xn = list(map(int, input().split()))

sorted_Xn = sorted(set(Xn))

def bin_search(lst, v):
    left, right = (0, len(lst))

    while (left <= right):
        mid = (left + right) // 2

        if lst[mid] >= v:
            right = mid - 1
        else:
            left = mid + 1
    return left

new_Xn = []
for i in Xn:
    new_Xn.append(bin_search(sorted_Xn, i))

print(" ".join(map(str, new_Xn)))