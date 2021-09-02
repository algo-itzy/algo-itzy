import sys
input = sys.stdin.readline

calculates = input().strip()
equations = []

# 한 바퀴 돌면서 숫자는 숫자로, 연산기호는 str 그대로 
num = ''
for token in calculates:
    if token.isdigit():
        num += token
    else:
        equations.extend([num, token])
        num = ''
equations.append(num)

ans = 0
flag = 0  # - 기호 앞에 나왔는지 나타내는 변수
# 한 바퀴 돌면서 -기호 뒤 나오는 숫자들은 모두 뺄셈 해줘야함
for token in equations:
    if token.isdigit():
        num = int(token)
        if flag:
            ans -= num
        else:
            ans += num
    elif token == '-':
        flag = 1

print(ans)
