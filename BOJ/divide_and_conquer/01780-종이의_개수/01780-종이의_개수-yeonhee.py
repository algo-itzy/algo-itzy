import sys
input = sys.stdin.readline


def cut_out_paper(x, y, n):
    global minus, zero, plus

    tmp = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != tmp:
                for k in range(3):
                    for l in range(3):
                        cut_out_paper(x + k*n//3, y + l*n//3, n//3)
                return

    if tmp == -1:
        minus += 1
    elif tmp == 0:
        zero += 1
    else:
        plus += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus, zero, plus = 0, 0, 0

cut_out_paper(0, 0, N)

print(minus, zero, plus, sep='\n')
