T = int(input())

for tc in range(T):
    code = str(input())

    stack =[]
    res = 1                        # 괄호 짝 맞추기 성공할 때 결과값을 result에 넣어둠 -> 괄호 짝 맞추기 실패를 거르기  

    for i in range(len(code)):
        if code[i] == '(' or code[i] == '{':
            stack.append(code[i])

        elif code[i] == ')':
            if len(stack) == 0:     # 스택이 비었는데 닫는 소괄호가 나오는 경우, 괄호 짝 맞추기 실패라는 것도 고려해줘야 함
                res = 0
                break

            if stack.pop() != '(':  # 스택의 마지막 원소가 '(' 인 경우에만 새롭게 들어온 ')' 와 완전한 짝이 됨         
                res = 0             # 그 외의 경우는 괄호 짝 맞추기 실패 
                break

        elif code[i] == '}':
            if len(stack) == 0:
                res = 0
                break
            if stack.pop() != '{':
                res = 0
                break

    if len(stack) > 0 :         # for 문을 다 돌았는데에도 스택에 여는 괄호가 남아있다면, 완전한 괄호 만들기 실패
        res = 0
    
    print(f'#{tc+1} {res}')

# for i in code:
#   if i =='(':
# 이게 더 편했을 듯!
    
    

  