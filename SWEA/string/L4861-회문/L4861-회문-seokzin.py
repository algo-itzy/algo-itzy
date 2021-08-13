T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = []

    for _ in range(N):
        table.append(input())

    # 가로 탐색
    for y in range(N):
        for x in range(N-M+1):
            row = table[y][x:M+x]  
            
            if row == row[::-1]:  
                print(f"#{tc}", row)


    # 세로 탐색
    for y in range(N-M+1):
        for x in range(N):
            col = []
            for i in range(M):
                col.append(table[y+i][x])

            if col == col[::-1]:  
                print(f"#{tc} ", *col, sep='')

# 무식하게 검증 했습니다.