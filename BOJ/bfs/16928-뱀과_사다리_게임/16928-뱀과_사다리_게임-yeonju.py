from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())        # 사다리수 n, 뱀의 수 m

move = [0 for _ in range(101)]
visited = [False for _ in range(101)]
ladder = {}
snake = {}

for i in range(n):
    x,y = map(int, input().split())     # 사다리 - x 번 칸에 도착하면, y 번 칸으로 이동
    ladder[x] = y

for i in range(m):
    u, v = map(int, input().split())    # 뱀- u 번 칸에 도착하면, v 번 칸으로 이동
    snake[u] = v

def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        x = queue.popleft()              # 위치
        for i in range(1,7):
            next = x + i                 # 주사위 던져서 가게되는 위치
            if next <=100:
                if next in ladder:
                    next = ladder[next]  # ladder 의 next key 값의 value 만큼 이동하기
                if next in snake:
                    next = snake[next]
                if not visited[next]:
                    queue.append(next)
                    visited[next]= True
                    move[next] = move[x] + 1

bfs(1)                                   # 1 에서 시작
print(move[100])


# git commit -m "code: Solve boj 16928 뱀과 사다리 게임 (yeonju)"