# git commit -m "code: Solve boj 15683 감시 (seungjoo)"
import sys
input = sys.stdin.readline

def check_zero_area(cctvs):
    tmp = [[1]*M for _ in range(N)]
    q = []
    for cctv in cctvs:
        init_x, init_y, cctv_id, cctv_dir = cctv
        tmp[init_x][init_y] = 0
        dirs = cctv_setting[cctv_id][cctv_dir]
        for d in dirs:
            q.append((init_x, init_y))
            while q:
                x, y = q.pop()
                nx = x + delta[d][0]
                ny = y + delta[d][1]
                if 0<=nx<N and 0<=ny<M and not matrix[nx][ny]==6:
                    tmp[nx][ny] = 0
                    q.append((nx,ny))
    zero_cnt = 0
    for row in tmp:
        zero_cnt += sum(row)
    return zero_cnt
                    

def change_cctv_dir(idx):
    global min_cnt
    if idx == len(cctv_set):
        min_cnt = min(min_cnt, check_zero_area(cctv_set))
        return
    now_id = cctv_set[idx][2]
    if now_id == 2:
        for i in range(2):
            cctv_set[idx][3] = i
            change_cctv_dir(idx+1)
    elif now_id == 5:
        change_cctv_dir(idx+1)
    else:
        for i in range(4):
            cctv_set[idx][3] = i
            change_cctv_dir(idx+1)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cctv_setting = {1: [[0],[1],[2],[3]],2: [[0,2],[1,3]], 3: [[0,1],[1,2],[2,3],[3,0]], 4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]], 5: [[0,1,2,3]]}
delta = ((-1,0),(0,1),(1,0),(0,-1))
min_cnt = float('inf')

wall_cnt = 0
cctv_set = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 6:
            wall_cnt += 1
        elif matrix[i][j]:
            cctv_set.append([i,j,matrix[i][j],0])

# cctv_set 방향 바꾸기. / 하나씩 최대 8^4 가지 경우의 수.
change_cctv_dir(0)
# 방향 다 바꾸면 감시범위 조사하고 0이 가장 적은 맵으로 min숫자 갱신.
print(min_cnt-wall_cnt)