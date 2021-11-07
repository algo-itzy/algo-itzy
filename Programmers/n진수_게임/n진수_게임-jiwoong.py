# git commit -m "code: Solve programmers n진수 게임 (jiwoong)"
import string
tmp = string.digits + string.ascii_uppercase[:6]


def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer, nums = '', ''
    cnt, check = 0, 0
    while cnt < t * m:
        i = convert(check, n)
        nums += i
        cnt += len(i)
        check += 1

    for i in range(p - 1, cnt, m):
        answer += nums[i]
    return answer[:t]
