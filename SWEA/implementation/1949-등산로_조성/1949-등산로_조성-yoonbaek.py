from typing import AnyStr


moves = ((0, -1), (0, 1), (-1, 0), (1, 0))

def construct(r, c, cnt, construct_done):
    global ans
    if cnt > ans:
        ans = cnt

    visited[r][c] = 1

    for x, y in moves:
        next_r = r+x
        next_c = c+y

        if 0 <= next_r < N and 0 <= next_c < N:
            if not visited[next_r][next_c]:
                path = mat[next_r][next_c]
                if path < mat[r][c]:
                    construct(next_r, next_c, cnt+1, construct_done)
                elif path - K < mat[r][c] and construct_done:
                    mat[next_r][next_c] = mat[r][c] - 1
                    construct(next_r, next_c, cnt+1, 0)
                    mat[next_r][next_c] = path
    
    visited[r][c] = 0


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, K = map(int, input().split())
        visited = [[0 for _ in range(N)] for _ in range(N)]
        ans = 0

        mat = [list(map(int, input().split())) for _ in range(N)]
        top = 0
        tops = []

        for r in range(N):
            for c in range(N):
                if mat[r][c] > top:
                    tops = []
                    tops.append((c, r))
                    top = mat[r][c]
                elif mat[r][c] == top:
                    tops.append((c, r))
                
        for c, r in tops:
            construct(r, c, 1, 1)

        print(f"#{tc} {ans}")     

# git commit -m "code: Solve swea 1949 등산로 조성 (yoonbaek)"