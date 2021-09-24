# # 0 빈칸, 6 벽, 1-5 CCTV 번호, 감시 영역 #

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # cctv 번호가 인덱스가 되도록
direction = [
            [],
            [[0], [1], [2], [3]],
            [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]],
            [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]
            ]


n, m = map(int, input().split())            # 세로 n, 가로 m
room = [list(map(int, input().split())) for _ in range(n)]
dic = dict()
zero_cnt = 0
camera = []
for i in range(n):
    for j in range(m):
        if 1 <= room[i][j] <= 5: # cctv이면 딕셔너리에 좌표 값 (i, j) 저장
            dic[(i,j)] = [] # (i,j) 를 key, []를 value 로
            idx = -1

            for ds in direction[room[i][j]]: # cctv가 볼 수 있는 방향 돌아보기
                idx += 1
                dic[(i,j)].append(set())
                for d in ds:                # ex) 1번 cctv 가 바라볼 수 있는 방향 중 하나씩 탐색
                    x, y = i, j
                    while 1:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if room[nx][ny] == 0:       # 0 인 경우, set 에 좌표를 추가
                                dic[(i,j)][idx].add((nx, ny))
                            elif room[nx][ny]==6:
                                break
                            x, y = nx, ny
                        else:
                            break
        elif room[i][j] == 0:
            zero_cnt += 1

key = list(dic.keys())              # 딕셔너리 순서가 없기에, list 로 순서 부여

l = len(key)
res = 0


def func(idx, watch):
    global res
    if idx == l:                    # 딕셔너리를 다 돌아보면 값을 비교해서 멈춤
        if res < len(watch):
            res = len(watch)
        return

    for value in dic[key[idx]]:    # dic[key[idx]]에는 idx 에 해당되는 딕셔너리의 값이 들어있음
        func(idx+1, value|watch) # value|watch 합집합해서 다음 함수에 넘긴다는 말


func(0, set())
print(zero_cnt - res)              # 0의 개수 - 볼 수 있는 공간의 수 = 사각지대의 수


# git commit -m "code: Solve boj 15683 감시 (yeonju)"
