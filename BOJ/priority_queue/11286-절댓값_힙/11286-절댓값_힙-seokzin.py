import sys
import heapq

input = sys.stdin.readline

hq = []

for _ in range(int(input())):
    x = int(input())
    
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
