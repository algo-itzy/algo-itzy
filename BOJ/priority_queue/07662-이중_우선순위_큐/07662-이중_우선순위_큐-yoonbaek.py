# git commit -m "Solve boj 07662 이중 우선순위 큐 (yoonbaek)"
# 처음에는 deque을 이용해서 구현해보려고 했으나,
# 힙 구조가 루트노드가 최소인건 보장해도 
# 최후 노드가 최댜안걸 보장하지는 않아서 포기하고

# https://kau-algorithm.tistory.com/135에 나온 로직을 생각해서 구현했습니다.
# 막상 구현은 그렇게 어려운 내용은 아닌데 개념을 생각해내기 어려운 것 같습니다.

from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict

input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        k = int(input())
        min_heap, max_heap = [], []
        count = defaultdict(int)

        for _ in range(k):
            op, val = input().split()
            val = int(val)

            if op == "I":
                heappush(min_heap, val)
                heappush(max_heap, -val)
                count[val] += 1
            else: # case D
                if val == 1: # case max heap pop
                    # sync with min heap
                    while max_heap and not count[-max_heap[0]]:
                        heappop(max_heap)
                    if max_heap:
                        count[-max_heap[0]] -= 1
                        heappop(max_heap)
                else: # case min heap pop
                    # sync with max heap
                    while max_heap and not count[min_heap[0]]:
                        heappop(min_heap)
                    if max_heap:
                        count[min_heap[0]] -= 1
                        heappop(min_heap)

        # deal with leftover
        while max_heap and not count[-max_heap[0]]:
            heappop(max_heap)
        while max_heap and not count[min_heap[0]]:
            heappop(min_heap)

        if max_heap:
            print(-max_heap[0], min_heap[0]) # top, bottom
        else:
            print("EMPTY")