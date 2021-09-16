import sys
import heapq

input = sys.stdin.readline
n = int(input())

h = []

for i in range(n):
    x = int(input())

    if x !=0:
        heapq.heappush(h, (abs(x),x))
    else:                               # x 가 0 이면
        if h:                           # 큐가 비어있지 않으면
            print(heapq.heappop(h)[1])
        else:                           # 큐가 비어있으면
            print(0)


# git commit -m "code: Solve boj 11286 절댓값 힙 (yeonju)"