def solution(s):
    answer = float('inf')
    for i in range(1, len(s)//2+2):
        result = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s)+i, i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1

        answer = min(answer, len(result))
    return answer
