def solution(n, t, m, p):
    answer = ''
    total = '0'
    num = 0
    alpha = {'10':'A', '11':'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    while len(total) < t * m: # t- 미리 구할 숫자의 갯수, m - 참가 인원
        rearranged = ''       # 해당 진수로 변환해서 값을 append 할 string 생성
        tmp_num = num
        while tmp_num != 0:
            changed = str(tmp_num % n)
            if changed in alpha:
                rearranged += alpha[changed]
            else:
                rearranged += changed
            tmp_num = tmp_num // n

        total += rearranged[::-1] # 18=12(16)인데 순서가 반대로 append 되었기에
        num += 1

    for i in range(len(total)):
        if len(answer) == t:
            break
        elif i % m == p-1:
            answer += total[i]

    return answer

print(solution(2,4,2,1))
# print(solution(16,16,2,1))

# git commit -m "code: Solve programmers n진수 게임 (yeonju)"