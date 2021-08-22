def forth():
    stack = []
    for i in range(len(code)):
        # 연산자
        if code[i] == "+" or code[i] == '-' or code[i] == '*' or code[i] == '/':
            if len(stack) >= 2:  # 연산 가능
                op2, op1 = int(stack.pop()), int(stack.pop())
                if code[i] == "+":
                    stack.append(op1 + op2)
                elif code[i] == "-":
                    stack.append(op1 - op2)
                elif code[i] == "*":
                    stack.append(op1 * op2)
                elif code[i] == "/":
                    stack.append(op1 // op2)
            else:  # 연산 불가능
                return "error"

        # 숫자면 stack 삽입
        elif code[i] != ' ' and code[i] != '.':
            stack.append(code[i])
        elif code[i] == ".":
            if len(stack) == 1:
                return stack.pop()
            else:  # 연산 불가능
                return "error"


T = int(input())
for tc in range(1, T + 1):
    code = list(input().split())
    # print(code)
    print("#{} {}".format(tc, forth()))
