import sys

def div_and_conquer(x, y, n):
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != matrix[i][j]:
                print('(', end='')
                # for문이 어떤 방향으로 돌아가는지만 조심하면 될 듯
                for k in range(2):
                    for l in range(2):
                        div_and_conquer(x + k*n//2, y + l*n//2, n//2)
                print(')', end='')
                return  # 새로 자르는 것이므로 뒤에 cnt 안셈
    if color == '0':
        print('0', end='')
    elif color == '1':
        print('1', end='')


input = sys.stdin.readline
N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
div_and_conquer(0, 0, N)
