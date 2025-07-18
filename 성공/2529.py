from input_from_file import init_file, input
init_file("2529")

N = int(input().rstrip())
tokens = input().rstrip().split()

results = []
def solve(stack, dic):
    if len(stack) == N + 1:
        results.append("".join(map(str, stack)))
    for i in range(0, 10):
        if i in dic:
            continue
        if len(stack) > 0:
            if len(stack) > N:
                break
            curr_token = tokens[len(stack) - 1]
            if curr_token == "<":
                if stack[-1] > i:
                    continue
            else:
                if stack[-1] < i:
                    continue
        dic.add(i)
        stack.append(i)
        solve(stack, dic)
        stack.pop()
        dic.remove(i)

solve([], set())

results = sorted(results, key=lambda x: int(x))
print(results[-1])
print(results[0])