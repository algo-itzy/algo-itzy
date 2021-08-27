import sys
input = sys.stdin.readline
from heapq import heappush,heappop
from collections import defaultdict


for test in range(int(input())):
    k = int(input())
    check = defaultdict(int)
    max_heap=[]
    min_heap=[]
    for i in range(k):
        command,n = input().split()
        n=int(n)
        if command=='D':
            if n==1:
                while max_heap and not check[-max_heap[0]]:
                    heappop(max_heap)
                if max_heap:
                    check[-max_heap[0]] -= 1
                    heappop(max_heap)
            else:
                while min_heap and not check[min_heap[0]]:
                    heappop(min_heap)
                if min_heap:
                    check[min_heap[0]] -= 1
                    heappop(min_heap)
        else:
            heappush(max_heap,-n)
            heappush(min_heap,n)
            check[n] += 1
    
    while max_heap and not check[-max_heap[0]]:
        heappop(max_heap)
    while min_heap and not check[min_heap[0]]:
        heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0],min_heap[0])
    else:
        print("EMPTY")