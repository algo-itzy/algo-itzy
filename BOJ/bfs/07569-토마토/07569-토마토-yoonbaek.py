# 3d 토마토 문제
# 허 시간 초과 ㅠㅠ 어케 해결하지
# 20번째 줄 때문에 시간초과가 났습니다.
# 범위 조건식도 함수로 로컬 함수로 주니까 시간이 1.33배 더 걸립니다. 16번째 줄

from sys import stdin
from collections import deque

rd = stdin.readline

MOVES = ((0, 0, -1), (0, 0, 1),
         (0, -1, 0), (0, 1, 0), 
         (-1, 0, 0), (1, 0, 0)) # 상하전후좌우

def search(now):
    # def is_in(x, idx):
    #     return 0 <= x < idx
    
    next = []
    for move in MOVES:
        # x, y, z = (sum(moved) for moved in zip(now, move))
        x, y, z = now[0]+move[0], now[1]+move[1], now[2]+move[2]
        if 0 <= x < M and 0 <= y < N and 0 <= z < Y:
            if box[z][y][x] == 0:
                next.append((x,y,z))

    return next


def BFS(starts: list):
    q = deque(starts)

    while q:
        now_x, now_y, now_z = q.popleft()

        for next_x, next_y, next_z in search((now_x, now_y, now_z)):
            box[next_z][next_y][next_x] = box[now_z][now_y][now_x]+1
            q.append((next_x, next_y, next_z))

    days = box[now_z][now_y][now_x]-1
    
    return days


def find(box, x):
    starts = []
    for d in range(H):
        for r in range(N):
            for c in range(M):
                if box[d][r][c] == x:
                    if x == 0:
                        return True
                    starts.append((c,r,d))
    return starts


def get_result(box):
    starts = find(box, 1)
    if not starts:
        return -1
    days = BFS(starts)
    if find(box, 0):
        return -1
    return days


if __name__ == "__main__":
    M, N, H = map(int, rd().split())
    box = [[list(map(int, rd().split())) for _ in range(N)] for _ in range(H)]

    ans = get_result(box)
    print(ans)

# git commit -m "code: Solve boj 07569 토마토 (yoonbaek)"