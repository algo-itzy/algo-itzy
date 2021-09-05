import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result =[]

def solution(x,y,n):
    num = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                solution(x,y, n//3)
                solution(x, y+n//3, n//3)
                solution(x, y+ (n//3 *2), n//3)
                solution(x+ n//3, y, n//3)
                solution(x+ n//3, y+n//3, n//3)
                solution(x+ n//3, y+(n//3 *2), n//3)
                solution(x+ (n//3 *2), y, n//3)
                solution(x+ (n//3 *2), y+ n//3, n//3) 
                solution(x+ (n//3 *2), y+ (n//3 *2), n//3) 
                return

    if num == -1:
        result.append(-1)
    elif num == 0:
        result.append(0)
    elif num == 1:
        result.append(1)
    return

solution(0, 0, n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))

# git commit -m "code: Solve boj 01780 종이의 개수 (yeonju)"