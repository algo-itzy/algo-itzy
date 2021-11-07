parse_hash = {i: chr(i+55) for i in range(10, 16)}
for i in range(0, 10):
    parse_hash[i] = str(i)

def solution(n, t, m, p):

    def dec_to_n(q, n):
        n_jinsoo = ''
        while 1:
            q, r = divmod(q, n)
            n_jinsoo = parse_hash[r] + n_jinsoo
            if q == 0:
                break
        return n_jinsoo

    answer, queue, i, L = '', '', 0, m*(t-1)+p

    while len(queue) < L:
        queue += dec_to_n(i, n)
        i+=1

    for i in range(t):
        answer += queue[m*i+p-1]

    return answer

# git commit -m "code: Solve programmers n진수 게임 (yoonbaek)"