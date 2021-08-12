import sys
import heapq

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, x)

"""
힙은 처음 접했네요.
아래 링크가 도움이 되었습니다.
https://www.daleseo.com/python-heapq/
"""
