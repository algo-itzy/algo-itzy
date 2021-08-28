import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        print(-1 * heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, -x)

"""
시간초과 오랜만...
"""
