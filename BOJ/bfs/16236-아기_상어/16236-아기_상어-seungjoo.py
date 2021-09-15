# git commit -m "code: Solve boj 16236 아기 상어 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque


def eat_fish(fish, s, c):
    fish.sort()
    x, y = fish[0]
    aquarium[x][y] = 0
    c += 1
    if c==s:
        s += 1
        c = 0
    return (x, y, s, c)


def find_fish(start):
    global time
    x, y, size, cnt = start
    q = deque()
    q.append((x,y))
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    tmp = 0
    while q:
        feed = []
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if aquarium[nx][ny] and aquarium[nx][ny] < size:
                        feed.append((nx,ny))
                    elif not aquarium[nx][ny] or aquarium[nx][ny] == size:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        tmp += 1
        if feed:
            return tmp, eat_fish(feed, size, cnt)
    return 0, 0

def call_mother(baby_size):
    for i in range(N):
        for j in range(N):
            if aquarium[i][j] and aquarium[i][j] < baby_size:
                return True
    return False


N = int(input())
delta = ((-1,0),(0,-1),(0,1),(1,0))
baby_shark = 0
aquarium = []
for i in range(N):
    fish = list(map(int, input().split()))
    aquarium.append(fish)
    if not baby_shark:
        for j in range(N):
            if fish[j]==9:
                aquarium[i][j] = 0
                baby_shark = (i, j, 2, 0)
                break

time = 0
while call_mother(baby_shark[2]):
    t, baby_shark = find_fish(baby_shark)
    time += t
    if not baby_shark:
        break
print(time)

