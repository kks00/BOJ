from input_from_file import init_file, input
init_file("30804")

combs = []
def get_comb(lst, length, last, curr):
    global combs
    if len(curr) == length:
        combs.append(tuple(curr))
        return
    for i in range(last + 1, len(lst)):
        curr.append(lst[i])
        get_comb(lst, length, i, curr)
        curr.pop()
get_comb([i for i in range(1, 10)], 2, -1, [])

N = int(input())
lst = list(map(int, input().split()))

result = 0
for curr_comb in combs:
    a, b = curr_comb

    table = [0 for _ in range(N + 1)]
    for i in range(N):
        if lst[i] == a or lst[i] == b:
            table[i + 1] = table[i] + 1
    result = max(result, max(table))

print(result)