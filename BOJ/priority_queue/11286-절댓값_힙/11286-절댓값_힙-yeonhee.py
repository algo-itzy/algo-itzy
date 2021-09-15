import sys
import heapq

input = sys.stdin.readline
q = []

for _ in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(q, (abs(num), num))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
