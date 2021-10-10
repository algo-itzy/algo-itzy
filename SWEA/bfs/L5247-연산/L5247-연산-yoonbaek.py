from collections import deque

ops = (
    lambda x : x+1,
    lambda x : x-1,
    lambda x : x*2,
    lambda x : x-10
)

def bfs(start):
    q = deque([start])

    while q:
        now_val, cnt  = q.popleft()

        for i in range(4):
            next_val = ops[i](now_val)
            if 0 < next_val <= 1000000:
                if not next_val in visited:
                    visited[next_val] = 1
                    if next_val == M:
                        return cnt+1
                    q.append((next_val, cnt+1))
                    

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        visited = {}

        cnt = bfs((N, 0))

        print(f"#{tc} {cnt}")

# git commit -m "code: Solve swea L5247 연산 (yoonbaek)"