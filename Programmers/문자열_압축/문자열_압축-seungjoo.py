# git commit -m "code: Solve programmers 문자열 압축 (seungjoo)"
def solution(s):
    n = len(s)
    answer = n
    for unit in range(1, n//2 + 1):
        cnt = 1
        now = s[:unit]
        tmp_answer = ''
        for i in range(unit, n + unit, unit):
            if s[i:i + unit] == now:
                cnt += 1
            else:
                if cnt > 1:
                    tmp_answer += str(cnt) + now
                else:
                    tmp_answer += now
                now = s[i:i + unit]
                cnt = 1
        answer = min(answer, len(tmp_answer))
    return answer