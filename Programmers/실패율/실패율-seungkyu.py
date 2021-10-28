# git commit -m "code: Solve programmers 실패율 (seungkyu)"
def solution(N, stages):
    answer = []
    dic = {}
    people = 0
    
    for i in stages:
        people += 1
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    fail_dic = {}
    
    for j in range(1, N+1):
        if j in dic:
            fail_dic[j] = dic[j] / (people)
            people = people - dic[j]
        else:
            fail_dic[j] = 0
            
    answer = sorted(fail_dic, key= lambda x : fail_dic[x], reverse=True)
    
    return answer