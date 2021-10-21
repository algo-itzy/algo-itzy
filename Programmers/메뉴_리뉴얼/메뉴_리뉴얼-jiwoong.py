# git commit -m "code: Solve programmers 메뉴 리뉴얼 (jiwoong)"
import itertools


def solution(menus, course):
    ans = []
    for i in course:
        com = set()
        for j in menus:
            menu = list(set(j))
            menu.sort()
            tmp = set(itertools.combinations(menu, i))
            com = com | tmp
        res = []
        max_cnt = 2
        for j in com:  
            j = ''.join(j)
            cnt = 0
            for k in menus:  
                tmp = 0
                for x in j:  
                    if x in k:
                        tmp += 1
                if tmp == len(j):
                    cnt += 1
            if cnt > max_cnt:
                res = [j]
                max_cnt = cnt
            elif cnt == max_cnt:
                res.append(j)
        ans.extend(res)
    ans.sort()
    return ans
