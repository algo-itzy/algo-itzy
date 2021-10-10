# git commit -m "code: Solve boj 19238 스타트택시 (seungkyu)"
import sys
from collections import deque
input = sys.stdin.readline

DIRS = ((1, 0),(-1, 0),(0, 1),(0, -1))


def bfs(x, y):
    visited = [[-1]*N for _ in range(N)]  # 거리 쉽게 구하기 위해 -1로 설정
    q = deque([(x, y)])
    visited[x][y] += 1

    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N and not mat[nx][ny] and visited[nx][ny] < 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited


N, M, fuel = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(M)]
flag = True

for _ in range(M):
    visited = bfs(x-1, y-1)  # 현재 지점에서 거리 구하기
    
    for idx, customer in enumerate(customers):
        c_x, c_y, end_x, end_y = customer
        customers[idx].append(visited[c_x-1][c_y-1])
    customers.sort(key=lambda x: (-x[4], -x[0], -x[1]))  # 거리 가까운 승객 찾기
    c_x, c_y, end_x, end_y, dist = customers.pop()  # pop해서 사용

    for customer in customers:
        customer.pop()  # dist 변수 pop

    visited = bfs(c_x-1, c_y-1)  # 승객 태우고 목적지로 이동
    end_dist = visited[end_x-1][end_y-1]  # 목적지까지의 거리
    x, y = end_x, end_y  # 시작점 갱신

    check1 = fuel-dist
    check2 = fuel-dist-end_dist
    if dist == -1 or end_dist == -1 or check1 < 0 or check2 < 0:  # 못 가는 경우
        flag = False
        break

    # dist: 승객 태우러 가는 거리 / end_dist: 승객 목적지 가는 거리
    fuel = fuel - dist + end_dist  # 연료 채우기

print(fuel) if flag else print(-1)
