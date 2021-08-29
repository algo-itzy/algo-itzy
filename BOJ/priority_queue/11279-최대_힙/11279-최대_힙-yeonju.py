# x 가 자연수면 배열에 값 추가
# x 가 0 이면 가장 큰 값 출력 + 그 값 제거 

import heapq
import sys

input = sys.stdin.readline 

n = int(input())
heap = []

for i in range(n):
    x = int(input())

    if x > 0:                           # x 가 자연수인 경우
        heapq.heappush(heap, (-1)* x)

    else:                               # x= 0
        if len(heap) == 0:              # 배열이 비어있는 경우, 0 출력 
            print(0)
        else: 
            print((-1) * heapq.heappop(heap))
        

# 파이썬은 최소 힙만을 제공 -> 넣어주는 값을 음수 처리한 후, 최솟값을 꺼내게되면 곧 그게 최대가 됨

# git commit -m "Solve boj 11279 최대 힙 (yeonju)"