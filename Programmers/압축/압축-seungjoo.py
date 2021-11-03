# git commit -m "code: Solve programmers 압축 (seungjoo)"
def solution(msg):
    msg += '.'
    answer = []
    dic = {chr(i + ord('A')): i + 1 for i in range(26)}
    idx, last_idx = 0, len(msg) - 1
    new_hash = 27
    while idx < last_idx:
        start = msg[idx]
        while idx < last_idx and start in dic:
            idx += 1
            start += msg[idx]
        answer.append(dic[start[:-1]])
        dic[start] = new_hash
        new_hash += 1
                
    return answer