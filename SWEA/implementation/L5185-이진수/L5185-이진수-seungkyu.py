# git commit -m "code: Solve swea L5185 이진수 (seungkyu)"
T = int(input())

sixteen_d = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

def to_binary(num):
    ans = ''
    while num:
        ans = str(num%2) + ans
        num //= 2
    if len(ans) < 4:
        ans = '0'*(4-len(ans)) + ans
    return ans


for tc in range(1, T+1):
    answer = ''
    _ , num = input().split()
    for token in num:
        if token.isdigit():
            answer += to_binary(int(token))
        else:
            answer += to_binary(sixteen_d[token])

    print(f'#{tc} {answer}')