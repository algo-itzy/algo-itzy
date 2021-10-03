# git commit -m "code: Solve boj 19238 스타트택시 (jiwoong)"
import sys
from collections import deque

input = sys.stdin.readline


def run():
    N, M, fuel = map(int, input().split())
    area = [[0] * (N + 1)]

    for _ in range(N):
        area.append([0] + list(map(int, input().split())))

    row, col = map(int, input().split())
    dict = {}

    for _ in range(M):
        sr, sc, dr, dc = map(int, input().split())
        area[sr][sc] = 2

        dict[(sr, sc)] = (dr, dc)

    while M:
        visited = [[0] * (N + 1) for _ in range(N + 1)]
        visited[row][col] = 1

        q = deque([(row, col)])
        mv = 0

        taxi = []

        if area[row][col] == 2:
            taxi.append((row, col))

        while q and not taxi:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tr = row + dx
                    tc = col + dy

                    if 0 < tr <= N and 0 < tc <= N:
                        if not visited[tr][tc]:
                            visited[tr][tc] = 1

                            if area[tr][tc] == 2:
                                taxi.append((tr, tc))

                            elif area[tr][tc] == 0:
                                q.append((tr, tc))

            mv += 1

        taxi.sort()
        fuel -= mv

        if fuel < 0 or not taxi:
            print(-1)
            break

        sr, sc = taxi[0]
        area[sr][sc] = 0

        row, col = sr, sc

        q = deque([(row, col)])
        visited = [[0] * (N + 1) for _ in range(N + 1)]
        visited[row][col] = 1

        mv = 0
        dest = dict[(sr, sc)]
        tmp = 1

        while q and tmp:
            for _ in range(len(q)):
                row, col = q.popleft()

                if (row, col) == dest:
                    tmp = 0
                    break

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    tr = row + dx
                    tc = col + dy

                    if 0 < tr <= N and 0 < tc <= N:
                        if not visited[tr][tc]:
                            visited[tr][tc] = 1

                            if area[tr][tc] != 1:
                                q.append((tr, tc))

            if tmp:
                mv += 1

        fuel -= mv

        if fuel < 0 or tmp:
            print(-1)
            break

        fuel += mv * 2
        row, col = dest

        M -= 1

    if not M:
        print(fuel)


if __name__ == "__main__":
    run()
