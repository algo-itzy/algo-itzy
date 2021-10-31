# git commit -m "code: Solve programmers 뉴스 클러스터링 (seungkyu)"
def solution(str1, str2):
    str1_lst = list(str1)
    str2_lst = list(str2)
    answer = 0
    tmp1, tmp2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            tmp1.append((str1[i]+str1[i+1]).lower())
        
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            tmp2.append((str2[j]+str2[j+1]).lower())
        
    kyo = 0
    
    for item in tmp1:
        if item in tmp2:
            kyo += 1
            tmp2.remove(item)
            
    if kyo == 0 and len(tmp1)+len(tmp2) == 0:
        answer = 1
    else:
        answer = kyo / (len(tmp1)+len(tmp2))
    answer = int(answer*65536)
    return answer