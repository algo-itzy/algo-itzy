def div(x, y, n):
    global minus, zero, plus

    start = arr[y][x]  # 첫 색깔

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[j][i] != start: # 하나라도 틀리면 DnC

                for a in range(3):
                    for b in range(3):
                        div(x + a*n//3, y + b*n//3, n//3)
                
                return
    
    if start == -1: # 모두 흰색
        minus += 1
    elif start == 0:
        zero += 1
    else:
        plus += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minus, zero, plus = 0, 0, 0

div(0, 0, n)

print(minus, zero, plus, sep='\n')

# 2630 문제를 재탕