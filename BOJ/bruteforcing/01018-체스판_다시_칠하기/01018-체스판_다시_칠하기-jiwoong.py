# MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수
# 브루트포스 : 모든 경우의 수

import sys

n, m = map(int, sys.stdin.readline().split())
chess = []  # 원래 판
for _ in range(n):
    chess.append(input())
ans = []  # 바뀐 체스판 갯수

for a in range(n - 7):  # 시작점, a : 행, b : 열
    for b in range(m - 7):
        white = 0  # W, B로 시작할 경우 바뀐 체스판 갯수
        black = 0
        for c in range(a, a + 8):  # 8칸씩 모두 체크하는데
            for d in range(b, b + 8):
                if (c + d) % 2 == 0:  # 현재 행열 번호 합이 짝수면 시작과 색깔 같아야함
                    if chess[c][d] != 'W':
                        white = white + 1
                    if chess[c][d] != 'B':
                        black = black + 1
                else:
                    if chess[c][d] != 'B':
                        white = white + 1
                    if chess[c][d] != 'W':
                        black = black + 1
        ans.append(white)
        ans.append(black)

print(min(ans))  # 바뀐 것 중 가장 작은 수
