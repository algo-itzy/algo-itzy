IDX = '0123456789ABCDEF'


def solution(n, t, m, p):

    def dec_to_n(n, x):
        a, b = divmod(n, x)

        if a == 0:
            return IDX[b]
        else:
            return dec_to_n(a, x) + IDX[b]

    answer = ''
    tmp = []

    for i in range(t*m):  # 총 정답 구하기
        for x in dec_to_n(i, n):
            tmp.append(x)

    for i in range(p-1, t*m, m):  # 튜브 정답 추출
        answer += tmp[i]

    return answer
