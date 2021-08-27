def div(x, y, n):
    global blue, white

    start = arr[y][x]  # 첫 색깔
      
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[j][i] != start: # 하나라도 틀리면 DnC

                div(x, y, n//2)
                div(x+n//2, y, n//2)
                div(x, y+n//2, n//2)
                div(x+n//2, y+n//2, n//2)
                
                return
    
    if start == 0: # 모두 흰색
        white += 1
    else:
        blue += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

div(0, 0, n)

print(white, blue, sep='\n')

# 개선하려고 다시 풀어봤는데 크게 개선할 방법을 못 찾겠다.
# return 존재 의미가 크다. 색이 다르면 DnC 후 탐색 완전 종료!