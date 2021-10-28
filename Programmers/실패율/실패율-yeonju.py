def solution(n, stages):

    answer = []
    dic = {}
    for i in range(1,n+1):
        dic[i] = 0
    participant = len(stages)
    stages = sorted(stages)
    cnt = 0
    for i in range(1, n+1):
        failure = 0
        if cnt == len(stages):
            break
        for j in range(cnt,len(stages)):
            if stages[j]==i:
                cnt+=1
                failure += 1
                
        dic[i] = failure/participant
        participant -= failure

    answer = [x[0] for x in sorted(dic.items(), key=lambda x:(x[1],-x[0]), reverse=True)]
    return answer


solution(5,[2, 1, 2, 6, 2, 4, 3, 3])


# git commit -m "code: Solve programmers 실패율 (yeonju)"