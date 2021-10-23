from collections import defaultdict
from itertools import combinations


def solution(infos, queries):
    answer = []
    dic = defaultdict(list)

    for info in infos:
        info = info.split(' ')
        score = int(info[-1])
        info = info[:-1]

        for n in range(5):
            for c in combinations(info, n):  # 모든 조합 구하기
                key = ''.join(c)
                dic[key].append(score)

    for v in dic.values():
        v.sort()

    for query in queries:
        query = query.split(' ')
        required = int(query[-1])
        query = query[:-1]

        query = ''.join(query)
        query = query.replace('-', '')
        query = query.replace('and', '')

        if query in dic:
            scores = dic[query]
            if len(scores) > 0:
                left, right = 0, len(scores)  # 이분탐색
                while left < right:
                    mid = (left + right) // 2
                    if scores[mid] >= required:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scores) - left)
        else:
            answer.append(0)

    return answer
