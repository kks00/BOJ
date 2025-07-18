s = input().rstrip()

stack = []
result = ""
for i in s:
    if ord("A") <= ord(i) <= ord("Z"): # 피연산자일 때 결과에 바로 추가
        result += i
    else:
        if len(stack) < 1:
            stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            elif i in ["/", "*"]: # 연산자가 *, / 일 때
                for _ in range(len(stack)):
                    popped = stack.pop()
                    if popped in ["*", "/"]: # *거나 /인 연산자가 스택 탑에 있으면 결과에 추가
                        result += popped
                    else:
                        stack.append(popped)
                        break
                stack.append(i)
            elif i in ["+", "-"]: # 연산자가 +, -일 때
                for _ in range(len(stack)): # 괄호 앞까지 스택에 들어있던 모든 연산자 결과에 추가
                    popped = stack.pop()
                    if popped == "(":
                        stack.append(popped)
                        break
                    result += popped
                stack.append(i)
            elif i == ")":
                for _ in range(len(stack)): # 괄호 앞까지 스택에 들어있던 모든 연산자 결과에 추가
                    popped = stack.pop()
                    if popped == "(":
                        break
                    result += popped
for i in range(len(stack)):
    result += stack.pop()
print(result)