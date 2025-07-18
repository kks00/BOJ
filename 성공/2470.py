from input_from_file import init_file, input
init_file("2470")

N = int(input())
L = list(map(int, input().rstrip().split()))

L = sorted(L)
# print(L)

'''
투포인터
- 왼쪽, 오른쪽 커서를 두고, 현재 커서가 가리키는 값 덧셈 연산
    - 연산 결과의 절댓값과 현재까지의 최소 절댓값 비교
        - 현재까지의 최소 절댓값보다 현재 절댓값이 작으면 가리킨 값 저장해둠
- 연산 결과가 음수이면 왼쪽 커서를 오른쪽으로 옮겨 절댓값 차이를 줄이고,
    연산 결과가 양수이면 오른쪽 커서를 왼쪽으로 옮겨 절댓값 차이를 줄여서 다시 비교
- 연산 결과가 0이면 절댓값이 최소인 경우이므로 종료
'''

min_val = (int(1e9) + 1) * 2
result = (None, None)

left, right = 0, N - 1
while left < right:
    curr_sum = L[left] + L[right]
    next_val = abs(curr_sum)
    if next_val < min_val:
        min_val = next_val
        result = L[left], L[right]
    if curr_sum == 0:
        break
    elif curr_sum < 0:
        left += 1
    else:
        right -= 1

# print(min_val)
print(result[0], result[1])