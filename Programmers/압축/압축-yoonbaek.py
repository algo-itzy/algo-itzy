def solution(msg):
    alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {alphas[i-1]: i for i in range(1, 27)}
    
    answer, start, idx = [], 0, 26
    msg_len, max_len = len(msg), 1
    
    while 1:
        for end in range(start+max_len, start, -1):
            w = msg[start:end]
            if w in d:
                idx += 1
                answer.append(d[w])
                if end >= msg_len:
                    return answer
                start = end
                c = msg[end]
                if len(w)+1 > max_len:
                    max_len = len(w)+1
                d[w+c] = idx
                break
            
# git commit -m "code: Solve programmers 압축 (yoonbaek)"