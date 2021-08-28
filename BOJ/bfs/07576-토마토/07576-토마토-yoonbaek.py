# 1. 구현방식 : 주변터 차근차근 탐색... BFS
# 2. 다 익은 건지는 어떻게 판별할 건지... 끝점을 알 수 없음.
#    : 익음(visited) 처리할 때마다 cnt++, 전체(M*N) - 빈공간과의 차이가 1이상이면 False 다 안 익음?

# 3. unbound local error
# 익은 토마토가 하나도 없는 경우를 고려해야함
from collections import deque

ints = lambda : map(int, input().split())

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS(starts):
    q = deque(starts)
    moved_cnt = 0

    while q:
        now = q.popleft()
        for move in moves:
            next_x, next_y = now[0]+move[0], now[1]+move[1]
            if 0 <= next_x < M and 0 <= next_y < N:
                if not tomatoes[next_y][next_x]:
                    moved_cnt += 1
                    tomatoes[next_y][next_x] = tomatoes[now[1]][now[0]]+1
                    q.append((next_x, next_y))

    return tomatoes[now[1]][now[0]]-1, moved_cnt


if __name__ == "__main__":
    M, N = ints()

    tomatoes = [list(ints()) for _ in range(N)]
    empty_cnt, starts = 0, []

    for y in range(N):
        for x in range(M):
            if tomatoes[y][x] == 1:
                starts.append((x, y))
            elif tomatoes[y][x] == -1:
                empty_cnt += 1

    if starts:
        days, moved = BFS(starts)
        if M*N == moved+empty_cnt+len(starts):
            print(days)
        else:
            print(-1)
    else:
        print(-1)
# eof
