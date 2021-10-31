def solution(m, n, board):
    answer = 0

    b = [x[::-1] for x in zip(*board)]  # 돌려서 떨어지는 구현 편하게
    
    while True:
        k = [[0]*m for _ in range(n)]  # 없앨 블록 리스트

        for y in range(n-1): # 2*2 탐색이니까 1씩 뺀다
            for x in range(m-1):
                if b[y][x] and (b[y][x] == b[y+1][x] == b[y][x+1] == b[y+1][x+1]):
                    k[y][x] = k[y][x+1] = k[y+1][x] = k[y+1][x+1] = 1

        if sum(map(sum, k)) == 0:  # 지울게 없다면 탈출
            return answer

        for y in range(n):
            tmp = []

            for x in range(m):
                if k[y][x] == 0:
                    tmp.append(b[y][x])

            tmp += [''] * (m - len(tmp))
            b[y] = tmp

        answer += sum(map(sum, k))