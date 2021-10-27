from itertools import combinations


def solution(relation):
    x = len(relation[0])
    y = len(relation)
    cases = []

    for i in range(1, x+1):
        cases += combinations(range(x), i)

    UNI = []
    for case in cases:
        tmp = [tuple([data[x] for x in case]) for data in relation]
        
        if len(set(tmp)) == y:
            UNI.append(case)

    # 최소성 아닌 것
    DUP = []  
    for i in range(len(UNI)):
        for j in range(i+1, len(UNI)):
            if set(UNI[i]) & set(UNI[j]) == set(UNI[i]):
                DUP.append(UNI[j])

    # 최소성
    MIN = set(UNI) - set(DUP)

    answer = len(MIN)

    return answer