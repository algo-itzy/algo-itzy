for test in range(1, int(input())+1):
    equation = input().split()
    flag = 0
    stack = []
    try:
        for el in equation:
            # 숫자면 stack에 밀어넣기.
            if el.isdigit():
                stack.append(int(el))
            # 연산자면 숫자 두개꺼내서 연산.
            elif el == '+':
                stack.append(stack.pop() + stack.pop())
            elif el == '-':
                tmp = stack.pop()
                stack.append(stack.pop() - tmp)
            elif el == '*':
                tmp = stack.pop()
                stack.append(stack.pop() * tmp)
            elif el == '/':
                tmp = stack.pop()
                stack.append(stack.pop() // tmp)
            else:
                answer = stack.pop()
                # 점 나왔는데 stack에 숫자 남아있으면 실패.
                if len(stack) != 0:
                    flag = 1
                break
    # 연산자 나왔는데 stack에 숫자 두개가 없을 떄.
    except:
        flag = 1
    if flag:
        print(f'#{test} error')
    else:
        print(f'#{test} {answer}')