import sys
sys.stdin = open('input.txt')


def check(nr, nc):
    return 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and (not maze[nr][nc] or maze[nr][nc] == 3)


for t in range(1, int(input())+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[0] * n for _ in range(n)]
    result = 0

    # 시작 인덱스 찾기
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                visited[r][c] = 1
                stack = [(r, c)]

    while stack:
        r, c = stack.pop()
        if maze[r][c] == 3:
            result = 1
            break
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if check(nr, nc):
                stack.append((nr, nc))
                visited[nr][nc] = 1

    print(f'#{t} {result}')

"""
스택으로 풀었습니다.
조건부가 너무 길어서 따로 함수로 뺐습니다. (그래도 긴 건 함정..)
"""
