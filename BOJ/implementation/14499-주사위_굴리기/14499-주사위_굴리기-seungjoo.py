# git commit -m "code: Solve boj 14499 주사위 굴리기 (seungjoo)"
import sys
input = sys.stdin.readline

# 1은 동쪽
def turn_east():
    dice[1][2], dice[3][0] = dice[3][0], dice[1][2]
    dice[1] = [dice[1][2]]+dice[1][:2]
# 2는 서쪽
def turn_west():
    dice[1][0], dice[3][0] = dice[3][0], dice[1][0]
    dice[1] = dice[1][1:] + [dice[1][0]]
# 3은 북쪽
def turn_north():
    temp = dice[0][0]
    dice[0][0] = dice[1][1]
    dice[1][1] = dice[2][0]
    dice[2][0] = dice[3][0]
    dice[3][0] = temp
# 4는 남쪽
def turn_south():
    temp = dice[3][0]
    dice[3][0] = dice[2][0]
    dice[2][0] = dice[1][1]
    dice[1][1] = dice[0][0]
    dice[0][0] = temp

N,M,x,y,K = map(int,input().split())
dice = [[0],[0,0,0],[0],[0]]
maps = []
for _ in range(N):
    maps.append(list(map(int,input().split())))
    
orders = list(map(int,input().split()))
for i in range(K):
    if orders[i]==1:
        if not y+1<M:
            continue
        y=y+1
        turn_east()
    elif orders[i]==2:
        if not y-1>=0:
            continue
        y=y-1
        turn_west()
    elif orders[i]==3:
        if not x-1>=0:
            continue
        x=x-1
        turn_north()
    elif orders[i]==4:
        if not x+1<N:
            continue
        x=x+1
        turn_south()

    if maps[x][y]==0:
        maps[x][y]=dice[3][0]
    else:
        dice[3][0]=maps[x][y]
        maps[x][y]=0

    print(dice[1][1])
