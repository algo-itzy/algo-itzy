import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap, max_heap = [], []
    visited = [0] * 1000001  # 각 id 별로 활성 상태를 기록하는  (최대힙과 최소힙 동기화)

    for i in range(int(input())):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = 1

        elif num == 1:
            while max_heap and not visited[max_heap[0][1]]:  # 상대 힙에서 이미 삭제된 노드들은 다 버림
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = 0
                heapq.heappop(max_heap)

        elif num == -1:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = 0
                heapq.heappop(min_heap)

    # 모든 연산이 끝난 후에도 쓰레기 노드가 남아 있을 수 있으므로 싹 다 버림
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 그리고 남은 첫 번째 원소가 최댓값, 최솟값
    print(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else 'EMPTY')

"""
아예 모르겠어서 구글링 참고했습니다.
의미를 이해하기 위해 생략 없이 구체적으로 풀어서 썼습니다.
"""
