import heapq
import sys

input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())

    if x == 0:
        print(-1 * heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, -x)