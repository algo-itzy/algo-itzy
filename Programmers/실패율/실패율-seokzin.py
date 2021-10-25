from collections import Counter

def solution(N, stages):
    counter = Counter(stages)
    fail = []
    answer = []
    tot = len(stages)  # 총인원
    

    for i in range(1, N+1):
        if tot:
            fail.append([i, counter[i]/tot])
            tot -= counter[i]
        else:
            fail.append([i, 0])

    fail.sort(key = lambda x: -x[1])

    for x in fail:
        answer.append(x[0])
    
    return answer