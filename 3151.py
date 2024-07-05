from input_from_file import init_file, input
init_file("3151")

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

def lower_index(lst, left, k):
    left, right = left, len(lst) - 1
    while (left <= right):
        mid = (left + right) // 2

        if lst[mid] >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

def upper_index(lst, left, k):
    left, right = left, len(lst) - 1
    while (left <= right):
        mid = (left + right) // 2

        if lst[mid] <= k:
            left = mid + 1
        else:
            right = mid - 1
    return right

def get_list_count(lst, left, k):
    return upper_index(lst, left, k) - lower_index(lst, left, k) + 1

result = 0
for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        a, b = A[i], A[j]
        c = (a + b) * -1
        result += get_list_count(A, j + 1, c)
print(result)


