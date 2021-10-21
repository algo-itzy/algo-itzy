# git commit -m "code: Solve programmers 메뉴 리뉴얼 (seungjoo)"
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    sets = defaultdict(int)
    for order in orders:
        order = sorted(list(order))
        for num in course:
            for new_comb in combinations(order, num):
                sets[''.join(list(new_comb))] += 1
    ans_set = {num: [] for num in course}
    for comb in sets:
        if sets[comb] < 2:
            continue
        n = len(comb)
        if n in ans_set:
            if not ans_set[n]:
                ans_set[n].append(comb)
            elif sets[ans_set[n][-1]] < sets[comb] :
                ans_set[n].clear()
                ans_set[n].append(comb)
            elif sets[ans_set[n][-1]] == sets[comb]:
                ans_set[n].append(comb)
    for num in ans_set:
        for comb in ans_set[num]:
            answer.append(comb)
    answer.sort()
    return answer