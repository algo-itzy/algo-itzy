import sys
# 파이썬 리스트는 링크드리스트라 인덱스 접근이 느림(시간 초과뜸)
import heapq  

input = sys.stdin.readline
N = int(input())

min_heaps = []

for _ in range(N):
    num = int(input())

    if num:
        heapq.heappush(min_heaps, num)  # heapq.heappush(리스트, 넣을 숫자)
    else:
        
        if min_heaps:
            print(heapq.heappop(min_heaps))  # heapq.heappop(리스트)
        else:
            print(0)
        