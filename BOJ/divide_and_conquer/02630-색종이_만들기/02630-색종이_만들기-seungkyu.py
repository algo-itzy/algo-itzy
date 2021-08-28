# 분할 정복 문제, 인덱스를 기준으로 나누기
import sys


def divide_conquer(x, y, N):
    global zero_num, one_num  # 0 정사각형, 1 정사각형 수
    start = matrix[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
          if matrix[i][j] != start:
              divide_conquer(x, y, N//2)  # 2사분면
              divide_conquer(x, y + N//2, N//2)  # 3사분면
              divide_conquer(x + N//2, y, N//2)  # 1사분면
              divide_conquer(x + N//2, y + N//2, N//2)  # 4사분면
              return

    if start == 0:
        zero_num += 1
    else:
        one_num += 1

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

zero_num = one_num = 0

divide_conquer(0, 0, N)

print(zero_num, one_num, sep='\n')
