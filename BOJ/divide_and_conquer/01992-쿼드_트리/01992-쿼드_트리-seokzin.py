def div(x, y, n):
    global res

    start = arr[y][x]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[j][i] != start: # 하나라도 틀리면 DnC

                print('(', end="")
                div(x, y, n//2)
                div(x+n//2, y, n//2)
                div(x, y+n//2, n//2)
                div(x+n//2, y+n//2, n//2)
                print(')', end="")

                return
    
    print(start, end="")


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

div(0, 0, n)

# str.extend를 도입했다가 18줄 return none 때문에 꼬였습니다.