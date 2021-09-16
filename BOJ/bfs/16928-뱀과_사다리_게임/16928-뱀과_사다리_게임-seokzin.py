from collections import deque


def bfs():
    q = deque()
    q.append(1)

    while q :
        x = q.popleft()

        for i in range(1, 7) :
            if x+i <= 100:
                nx = arr[x+i]  # 사다리, 뱀 체크

                if not visit[nx]:
                    visit[nx] = visit[x]+1
                    q.append(nx)


n, m = map(int, input().split())
arr = [*range(101)]  # 이런 방법도 가능
visit = [0] * 101

for _ in range(n+m) :
    x, y = map(int, input().split())
    arr[x] = y

bfs()

print(visit[-1])