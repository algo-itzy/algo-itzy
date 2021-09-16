import sys
import heapq

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
