from input_from_file import init_file, input
init_file("15654")

N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst = sorted(lst)

combs = []
def get_comb(lst, length, curr, visited):
    global combs

    if len(curr) == length:
        combs.append(tuple(curr))
        return
    for i in range(len(lst)):
        if i in visited:
            continue

        visited.add(i)
        curr.append(lst[i])
        get_comb(lst, length, curr, visited)
        curr.pop()
        visited.remove(i)
get_comb(lst, M, [], set())

results = []
for comb in combs:
    result = ""
    for i in comb:
        result += str(i) + " "
    result = result[:-1]
    results.append(result)
for i in results:
    print(i)