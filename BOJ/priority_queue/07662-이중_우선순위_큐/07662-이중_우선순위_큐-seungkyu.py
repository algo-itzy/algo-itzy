'''
못 풀었습니다.. 추후에 다시 풀어서 업로드하겠습니다
'''
import heapq
import sys
input = sys.stdin.readline

min_heap, max_heap = [], []
for _ in range(T):
    k = int(input())
    # 최소, 최대 힙 2개 사용
    min_heap, max_heap = [], []
    
    # 동시 삭제 위한 visited
    visited = [False] * 1000001
    # is_exist = {} 딕셔너리 이용해보려고 했으나 잘 안됨
    for i in range(k):
        cmd = input().split()

        if cmd[0] == 'I':
            heapq.heappush(min_heap, (int(cmd[1]), i))
            heapq.heappush(max_heap, (-int(cmd[1]), i))
            visited[i] = True

        elif cmd[0] == 'D':
            if cmd[1] == '1':
                
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                # max heap에서도 동시에 삭제
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif cmd[1] == '-1':
                
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # min heap에서도 동시에 삭제
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0], sep=' ')
