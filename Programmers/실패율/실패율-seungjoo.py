# git commit -m "code: Solve programmers 실패율 (seungjoo)"
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

def solution(N, stages):
    answer = []
    stages = sorted(stages)
    cnts = []
    for i in range(1, N + 1):
        left = bisect_left(stages, i)
        right = bisect_right(stages, i)
        total = len(stages) - left
        failure_rate = (right - left) / total if total else 0
        heappush(cnts, (-failure_rate, i))
    while cnts:
        answer.append(heappop(cnts)[1])
    return answer