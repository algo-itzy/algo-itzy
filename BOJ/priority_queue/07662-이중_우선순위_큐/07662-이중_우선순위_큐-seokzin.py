import heapq
import sys


def sync(q):
    while q and visit[q[0][1]] == 0:
        heapq.heappop(q)


for _ in range(int(input())): # T
    visit = [0] * 1000000
    h_min, h_max = [], []

    for i in range(int(input())): # K
        cmd, num = sys.stdin.readline().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(h_min, (num, i))
            heapq.heappush(h_max, (-num, i))
            visit[i] = 1

        elif num == 1:
            sync(h_max)
            
            if h_max:
                visit[h_max[0][1]] = 0
                heapq.heappop(h_max)

        elif num == -1:
            sync(h_min)

            if h_min:
                visit[h_min[0][1]] = 0
                heapq.heappop(h_min)

    sync(h_max)
    sync(h_min)

    if h_min and h_max:
        print(-h_max[0][0], h_min[0][0])
    else:
        print("EMPTY")

# sync를 최적화 할 수 있을 것 같아서.. 개선해보고 새로 올리겠습니다.