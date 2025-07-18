from input_from_file import init_file, input
init_file("1946")

'''
서류심사 성적, 면접시험 성적 둘 다
다른 모든 지원자와 비교했을 때 낮은 경우가 있는 사람 탈락

(3, 6) - (1, 4)때문에 탈락
(7, 3) - (4, 2)때문에 탈락
(4, 2) - 합격
(1, 4) - 합격
(5, 7) - (3, 6)때문에 탈락
(2, 5) - (1, 4)때문에 탈락
(6, 1) - 합격
'''

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    l = []
    for _ in range(N):
        a, b = list(map(int, input().rstrip().split()))
        l.append((a, b))
    l = sorted(l, key=lambda x: x[0])

    curr_min_a, curr_min_b = N + 1, N + 1
    result = 0
    for ca, cb in l:
        if curr_min_a < ca and curr_min_b < cb:
            continue
        curr_min_a = min(curr_min_a, ca)
        curr_min_b = min(curr_min_b, cb)
        result += 1
    print(result)