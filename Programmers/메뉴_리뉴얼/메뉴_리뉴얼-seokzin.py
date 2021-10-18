from itertools import combinations
from collections import Counter


def solution(orders, course):
    res = []

    for c in course:
        cases = []

        for order in orders:
            cases += combinations(sorted(order), c)  # 정렬 필수

        counter = Counter(cases)

        if counter and max(counter.values()) > 1:
            for key, val in counter.items():
                if val == max(counter.values()):
                    res += [''.join(key)]

    return sorted(res)

# dict.values()는 view 타입을 리턴하여 max 연산을 못 씀.
# counter가 value 순으로 정렬되어 있는데 for문으로 다루니까 섞임. 리팩토링 실패