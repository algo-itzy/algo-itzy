# git commit -m "code: Solve boj 11286 절댓값 힙 (seungkyu)"
import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    
    num = int(input())
    if num:
        if num < 0:
            flag = -1
        else:
            flag = 1
        heapq.heappush(heap, (abs(num), flag))

    else:
        if heap:
            num, flag = heapq.heappop(heap)
            print(num * flag)
        else:
            print(0)