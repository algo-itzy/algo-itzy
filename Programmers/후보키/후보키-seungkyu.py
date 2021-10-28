# git commit -m "code: Solve programmers 후보키 (seungkyu)"
from itertools import combinations

def solution(relation):
    answer = 0
    ans = []  # 후보키 인덱스 (세트로) 저장
    len_attrs = len(relation[0])  # 속성 개수
    indices = [i for i in range(len_attrs)]
    
    for k in range(1, len_attrs+1):
        candidates = []
        flag = False

        for comb in combinations(indices, k):  # 속성 인덱스값으로 조합
            comb = list(comb)
            tmp2 = []

            for rel in relation:
                tmp = []
                for idx in comb:
                    tmp.append(rel[idx])
                if tmp in tmp2:
                    flag = False
                    break
                tmp2.append(tmp)
                flag = True
            if flag:
                candidates.append(comb)

        # 후보키가 최소성 만족하는지 검사  
        for item in candidates:
            if ans:
                for k in ans:
                    # x.issubset(y) => x가 y의 부분집합인지
                    # 이거는 포함관계 알고 싶을 때 유용할 것 같습니다.
                    if set(k).issubset(set(item)):
                        break
                else:
                    ans.append(item)
            else:
                ans.append(item)
        
    answer = len(ans)

    return answer