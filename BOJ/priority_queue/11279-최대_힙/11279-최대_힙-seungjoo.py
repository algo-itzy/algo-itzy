import sys
input = sys.stdin.readline
from heapq import heappush,heappop

queue = []
for _ in range(int(input())):
    x = int(input())
    if not x:
        print(heappop(queue)[1] if queue else 0)
    else:
        heappush(queue,(-x,x))