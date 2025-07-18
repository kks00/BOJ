from input_from_file import init_file, input
init_file("17503")

N, M, K = list(map(int, input().rstrip().split()))

l = []
for _ in range(K):
    v, c = list(map(int, input().rstrip().split()))
    l.append((v, c))
l = sorted(l, key=lambda x: (x[1], -x[0]))
# print(l)
l = l[::-1]

import heapq
def solve():
    selected = []
    curr_count, curr_sum, curr_max = 0, 0, 0
    while (len(l) > 0):
        cv, cc = l.pop()
        curr_count += 1
        curr_sum += cv
        heapq.heappush(selected, (cv, cc))
        curr_max = max(curr_max, cc)
        if curr_count >= N:
            if curr_sum < M:
                hv, hc = heapq.heappop(selected)
                curr_sum -= hv
                curr_count -= 1
            else:
                return curr_max
    return -1

print(solve())

'''
레벨 최댓값 안에서 임의로 N개를 선택했을 떄의 선호도 합이 M 이상
만족하지 않았을 시 가장 선호도가 낮은 것 한개를 버리기
'''