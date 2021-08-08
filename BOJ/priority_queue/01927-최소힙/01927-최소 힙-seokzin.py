import heapq
import sys

input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())

    if x == 0:
        print(heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, x)

# 내용보단 우선순위 큐 개념이 중요했던 문제