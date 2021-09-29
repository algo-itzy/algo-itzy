from collections import deque

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
moves = (up, down, left, right)

def BFS(starts):
    q = deque(starts)
    total = 0

    while q:
        nowc, nowr = q.popleft()
        
        for movec, mover in moves:
            movec += nowc
            mover += nowr
            if 0 <= movec < M and 0 <= mover < N:
                if visited[mover][movec] == -1:
                    visited[mover][movec] = visited[nowr][nowc] + 1
                    q.append((movec, mover))
                    total += visited[mover][movec]

    return total
    

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        mat, starts = [], []
        visited = [[-1 for _ in range(M)] for _ in range(N)]

        for r in range(N):
            row = input()
            for c in range(M):
                if row[c] == "W":
                    visited[r][c] = 0
                    starts.append((c, r))
            mat.append(row)

        total = BFS(starts)

        print(f"#{tc} {total}")

# git commit -m "code: Solve swea 10966 물놀이를 가자 (yoonbaek)"