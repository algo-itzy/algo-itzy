T = int(input())

for tc in range(1, T+1):
    datas = input().split()
    s = []  # stack
    res = 'error'

    for data in datas:
        if data.isdigit():
            s.append(int(data))
        elif data == '.' and len(s) == 1:  # 숫자만 있는 경우도 예외라니... 뭔가 별로다.
            res = s.pop()
        elif len(s) >= 2:
            b, a = s.pop(), s.pop()  # pop() 2번 할 때 순서 조심
            
            if data == '+' :
                s.append(a+b)
            elif data == '-' :
                s.append(a-b)
            elif data == '*' :
                s.append(a*b)
            elif data == '/' :
                s.append(a//b)
        else:
            break

    print(f'#{tc} {res}')

# 예외처리가 많이 필요한 문제다. 지저분하다.