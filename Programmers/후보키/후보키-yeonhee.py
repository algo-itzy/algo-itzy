from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    candidates = []

    for i in range(1, col+1):
        for comb in combinations(range(col), i):
            tmp = set([tuple([r[idx] for idx in comb]) for r in relation])

            if len(tmp) == row:
                candidates.append(comb)

    answer = set(candidates[:])

    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            if set(candidates[i]).issubset(set(candidates[j])):
                answer.discard(candidates[j])

    return len(answer)
