from input_from_file import init_file, input
init_file("11399")

N = int(input())
P = list(map(int, input().rstrip().split()))

P = sorted(P)
for i in range(1, N):
    P[i] = P[i] + P[i - 1]
print(sum(P))