from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for num in course:
        array = []
        for order in orders:
            order = sorted(order)
            array.extend(list(combinations(order, num)))

        count = Counter(array)

        if count:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)
