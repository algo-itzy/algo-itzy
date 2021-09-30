t = int(input())


def dfs(now, total):

    global min_usage

    if sum(visited) == n-1:             # 모든 구역 다 방문했으면
        if total + arr[now][0] < min_usage:
            min_usage = total + arr[now][0]
            return

    for next in range(1, n):            # 갈 수 있는 모든 경로 dfs 탐색
        if visited[next] == 0:
            visited[next] = 1
            dfs(next, total + arr[now][next])
            visited[next] = 0


for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n                   # 방문 체크할 리스트 선언
    min_usage = 100 * 10
    dfs(0, 0)                           # 지금 위치, 현재까지 배터리 사용량

    print(f'#{tc+1} {min_usage}')


# git commit -m "code: Solve swea L5201 컨테이너 운반 (yeonju)"