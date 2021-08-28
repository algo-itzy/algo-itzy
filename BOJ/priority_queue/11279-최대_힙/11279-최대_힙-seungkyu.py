import heapq
import sys
input = sys.stdin.readline

n = int(input())

max_heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if max_heap:
            print((-1)*heapq.heappop(max_heap))  #  -1 곱해서 max heap만듬
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -x)
