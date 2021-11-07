# git commit -m "code: Solve programmers n진수 게임 (seungjoo)"
def solution(n, t, m, p):
    answer = ''
    parse_table = {i: hex(i)[2:].upper() for i in range(16)}
    p -= 1
    tmp = '0'
    num = 1
    while len(tmp) < p + t * m:
        k = 1
        while num >= k:
            k *= n
        k //= n
        now = num
        while k:
            a = now // k
            tmp += parse_table[a]
            now -= a * k
            k //= n
        num += 1
    for i in range(p, p + t * m, m):
        answer+= tmp[i]
    return answer