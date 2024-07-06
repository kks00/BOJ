from input_from_file import init_file, input
init_file("1043")

N, M = list(map(int, input().split()))
map_data = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

knows = list(map(int, input().split()))[1:]
for i in range(1, M + 1):
    visitors = list(map(int, input().split()))[1:]
    for v in visitors:
        map_data[v][i] = 1

visited = set()
result = [1 for _ in range(M + 1)]
def visit(cp):
    global visited, result
    visited.add(cp)

    for party in range(1, M + 1):
        if map_data[cp][party] == 1:
            result[party] = 0
            for np in range(1, N + 1):
                if map_data[np][party] == 1 and (np not in visited):
                    visit(np)

for know in knows:
    visit(know)

print(sum(result[1:]))