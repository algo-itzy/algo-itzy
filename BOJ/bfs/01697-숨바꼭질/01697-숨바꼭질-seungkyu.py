import sys

# 최적해를 찾아야 하므로 dfs아니고 bfs 이용
from collections import deque


def bfs(N, K):
    queue = deque()
    queue.append(N)  # 시작점 큐에 저장

    while queue:
        num = queue.popleft()  # 새로운 시작점 get
        if num == K:  # 목표점 도달 시 break
            print(cnt[num])
            break
        else:
            # 지금 지점에서 +1, -1, *2 한 지점으로 이동하고
            # 이동횟수가 1번 늘어난 것이므로 cnt를 업데이트 후 큐에 저장
            # 이동 각각 모두 시행해줘야하므로 if문 3번 사용
            if 0 <= num + 1 <= 100000 and not cnt[num + 1]:
                cnt[num + 1] = cnt[num] + 1
                queue.append(num + 1)

            if 0 <= num - 1 <= 100000 and not cnt[num - 1]:
                cnt[num - 1] = cnt[num] + 1
                queue.append(num - 1)

            if 0 <= num * 2 <= 100000 and not cnt[num * 2]:
                cnt[num * 2] = cnt[num] + 1
                queue.append(num * 2)


input = sys.stdin.readline
N, K = map(int, input().split())

cnt = [0] * 100001  # 횟수 저장 변수, 최대인 것으로 설정하려고 했으나 잘 안돼서 0으로 바꿈
bfs(N, K)
