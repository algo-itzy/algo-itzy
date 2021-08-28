import heapq
import sys
input = sys.stdin.readline

min_heap, max_heap = [], []
T = int(input())
for _ in range(T):
    k = int(input())

    # 최소, 최대 힙 2개 사용
    cnt = len_heap = 0
    is_exist = {}
    for _ in range(k):
        cmd = input().split()

        if cmd[0] == 'I':
            heapq.heappush(min_heap, int(cmd[1]))
            if int(cmd[1]) not in is_exist:
                is_exist[int(cmd[1])] = 1
            else:
                is_exist[int(cmd[1])] += 1
            heapq.heappush(max_heap, -int(cmd[1]))
            cnt += 1
        elif cmd[0] == 'D' and cnt:
            if cmd[1] == '1':
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if is_exist[num] == 1:
                        cnt -= 1
                        is_exist[num] -= 1
                        break
            elif cmd[1] == '-1':
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if is_exist[num] == 1:
                        cnt -= 1
                        is_exist[num] -= 1
                        break
    print(min_heap, max_heap)
    print(is_exist)
    if cnt == 1:
        while min_heap:
            ans = heapq.heappop(min_heap)
            if ans in is_exist:
                print(ans, ans)
                break
    elif cnt > 1:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
    else:
        print('EMPTY')
