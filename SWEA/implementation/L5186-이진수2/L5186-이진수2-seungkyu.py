# git commit -m "code: Solve swea L5186 이진수2 (seungkyu)"
T = int(input())

for tc in range(1, T+1):
    num = float(input())
    ans = ''
    n = 1
    flag = True
    while num:
        ans += str(int(num//(2**(-n)))) 
        num = num % (2**(-n))
        n += 1
        if len(ans) > 13:
            flag = False
            break

    if flag:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')