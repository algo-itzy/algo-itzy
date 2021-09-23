# git commit -m "code: Solve boj 15683 감시 (seungkyu)"
import sys
import copy
input = sys.stdin.readline
'''
못 풀어서 풀이는 검색해서 참고했습니다.
'''
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동변수
DIRECTIONS = [[], 
            [[0], [1], [2], [3]], # 1
            [[0, 1], [2, 3]],  # 2
            [[0, 2], [2, 1], [1, 3], [3, 0]], # 3
            [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], # 4
            [[0, 1, 2, 3]]] # 5


def move(x, y, direction, tmp):

    for d in direction:  # 방향 따라서 갈 수 있는 곳 모두 방문
        new_x = x
        new_y = y
        while True:
            new_x += DIRS[d][0]
            new_y += DIRS[d][1]
            if 0<=new_x<N and 0<=new_y<M and tmp[new_x][new_y] != 6:
                if tmp[new_x][new_y] == 0:
                    tmp[new_x][new_y] = '#'
            else:  # 범위 벗어나거나 벽 만나면 종료
                break


def dfs(matrix, cnt):
    global ans
    tmp = copy.deepcopy(matrix)
    if cnt == cctv_cnt:
        zero_cnt = 0
        for row in tmp:  # 열 별로 0 세기
            zero_cnt += row.count(0)
        ans = min(ans, zero_cnt)  # 최솟값만 저장
        return
    x, y, cctv = q[cnt]
    for i in DIRECTIONS[cctv]:  # cctv번호에 따라서 갈 수 있는 방향들 지정
        move(x, y, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(matrix)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

q = []
cctv_cnt = 0  # cctv 개수 카운팅
ans = float('inf')
for i in range(N):
    for j in range(M):
        if 1<=matrix[i][j]<=5:
            cctv_cnt += 1
            q.append([i, j, matrix[i][j]])

dfs(matrix, 0)
print(ans)