# git commit -m "code: Solve programmers 후보키 (seungjoo)"
from itertools import combinations

def solution(relation): 
    n = len(relation[0])
    cnt = 0
    checked = set()
    for i in range(1, n + 1):
        for comb in combinations([k for k in range(n)], i):
            dicts = set()
            tmp = []
            for row in relation:
                tmp.append(''.join(row[each] for each in comb))
            flag = 0
            for c in tmp:
                if flag: break
                if c not in dicts:
                    dicts.add(c)
                else:
                    flag = 1
                    break
            if not flag:
                flag = 0
                for i in range(1, len(comb)):
                    if flag: break
                    for com in combinations(list(comb), i):
                        if com in checked:
                            flag = 1
                            break
                if not flag:
                    checked.add(comb)
                    cnt += 1
    return cnt