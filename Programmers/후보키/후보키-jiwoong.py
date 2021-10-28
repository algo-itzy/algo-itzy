# git commit -m "code: Solve programmers 후보키 (jiwoong)"
from itertools import combinations


def solution(relation):
    ans = 0
    arr = [i for i in range(len(relation[0]))]
    can = []
    for i in range(1, len(relation[0]) + 1):
        tmp = combinations(arr, i)
        can += tmp
    while can:
        key = can.pop(0)
        overlap = []  # 중복
        check = True
        for r in relation:
            tmp = []
            for k in key:
                tmp.append(r[k])
            # 중복 검사
            if tmp in overlap:
                check = False
            else:
                overlap.append(tmp)
        # 후보키
        if check:
            ans += 1
            length = len(can)
            repeat = 0
            idx = 0
            while repeat < length:
                i = can[idx]
                cnt = 0
                for j in i:
                    for k in key:
                        if k == j:
                            cnt += 1
                if cnt == len(key):
                    del can[idx]
                else:
                    idx += 1
                repeat += 1
    return ans
