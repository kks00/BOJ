from input_from_file import init_file, input
init_file("30805")

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

seq_a = []
for i in range(N):
    seq_a.append((i, A[i]))
seq_a = sorted(seq_a, key=lambda x: (-x[1], x[0])) # 사전순으로 정렬된 결과 얻기 위해서 A를 값 기준으로 내림차순 정렬

seq = []
last_found_i = -1
last_found_j = -1
for i, k in seq_a:
    if i <= last_found_i: # 부분 수열은 순서대로 등장하여야 하므로 고를 수는 앞에서 골라진 수보다는 뒤에 위치하여야 함
        continue
    for j in range(last_found_j + 1, M): # 앞에서 선택된 수보다 뒷 수부터 탐색 시작
        if k == B[j] and last_found_j < j: # 수 일치할 시 마지막으로 선택된 수 인덱스 갱신하고 리스트에 추가 
            last_found_i = i
            last_found_j = j
            seq.append(k)
            break
print(len(seq))
print(" ".join(map(str,seq)))