import sys
input = sys.stdin.readline
from heapq import heappop,heappush

# 최솟값부터 출력 -> 최소힙 자료구조 이용 정렬된 상태로 삽입
N = int(input())
heap=[]
for _ in range(N):
    heappush(heap,int(input()))

# heappop을 통해 최솟값부터 출력.
for _ in range(N):
    print(heappop(heap))