from collections import deque

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(p, idx):
    q = deque([idx])
    visited = [[0]*5 for _ in range(5)]

    while q:
        r, c = q.popleft()
        visited[r][c] = max(visited[r][c], 1)

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                if p[nr][nc] == 'O' and visited[r][c] < 3:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

                elif p[nr][nc] == 'P' and visited[r][c] < 3:
                    return 0

    return 1


def solution(places):
    answer = []

    for place in places:
        tmp = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    tmp = tmp & bfs(place, (i, j))
        answer.append(tmp)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
