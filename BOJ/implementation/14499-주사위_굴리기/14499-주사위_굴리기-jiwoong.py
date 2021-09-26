# git commit -m "code: Solve boj 14499 주사위 굴리기 (jiwoong)"
import sys
input = sys.stdin.readline

N, M, X, Y, K = map(int, input().split()) 
nums = [list(map(int, input().split())) for _ in range(N)]  
orders = list(map(int, input().split()))  
dice = [0] * 7 

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for _ in range(K):
    order = int(orders.pop(0))
    nx = X + dx[order - 1]
    ny = Y + dy[order - 1]

    if 0 <= nx < N and 0 <= ny < M: 
        if order == 1:  
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif order == 2:  
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif order == 3: 
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        else: 
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

        if nums[nx][ny] == 0: 
            nums[nx][ny] = dice[6] 
        else:  
            dice[6] = nums[nx][ny] 
            nums[nx][ny] = 0 

        X = nx
        Y = ny
        print(dice[1])
