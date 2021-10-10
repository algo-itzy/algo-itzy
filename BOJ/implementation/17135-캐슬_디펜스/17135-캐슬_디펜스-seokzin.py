from itertools import combinations
from collections import deque


def find(x, y, arr):  # 약식 bfs로 적 탐색
    D = ((-1, 0), (0, -1), (1, 0))
    visit = [[0] * m for _ in range(n+1)]
    q = deque([(x, y-1, 1)])  # 궁수 앞 칸부터 탐색

    while q:
        x, y, k = q.popleft()
        visit[y][x] = 1

        if k > d:
            return

        if arr[y][x] == 1:
            return x, y

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < m and 0 <= ny < n and not visit[ny][nx]:
                q.append((nx, ny, k+1))


def move(arr):  # 적 이동
    return [[0] * m] + arr[:-1]


def solve(pos, arr):
    arr = [x[:] for x in arr]  # Deepcopy
    cnt = 0

    while sum(map(sum, arr)):  # 적이 있다면
        targets = set()  # 같은 적을 쏠 수 있으니까

        for x in pos:
            targets.add(find(x, n, arr))

        for target in targets:
            if target:
                tx, ty = target
                arr[ty][tx] = 0
                cnt += 1

        arr = move(arr)

    return cnt


n, m, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cases = combinations(list(range(m)), 3)  # 궁수 위치
res = 0

for case in cases:
    res = max(res, solve(case, arr))

print(res)


"""
1. 노트로 충분한 손코딩 필요 (enemy list 설계 했어야 함)
2. 버전 관리 (기능 추가하다가 백업할 일이 생김)
3. 외부 참조 안하려고 인자로 리스트 전달 했는데도 값이 변했다. 이 것도 참조로 취급하나보다. (그래서 Deepcopy 씀) 
"""