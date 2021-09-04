import sys
input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

def div_and_conquer(x, y, n):
    global cnt_zero, cnt_one, cnt_minus
    color = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[i][j] != color:
                # solve 9개로 나눠서 진행
                for k in range(3):
                    for l in range(3):
                        div_and_conquer(x + k*n//3, y + l*n//3, n//3)
                return  # 새로 자르는 것이므로 뒤에 cnt 안셈
    # for 문 모두 통과 => 한가지 색으로 이루어짐            
    if color == 0:
        cnt_zero += 1
    elif color == 1:
        cnt_one += 1
    elif color == -1:
        cnt_minus += 1


cnt_zero = cnt_one = cnt_minus = 0
div_and_conquer(0, 0, N)
print(cnt_minus, cnt_zero, cnt_one, sep='\n')
