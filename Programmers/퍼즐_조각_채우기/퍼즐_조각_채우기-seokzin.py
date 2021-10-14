D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(graph, x, y, pos, n, k):
    block = [pos]
    
    for dx, dy in D:
        nx, ny = x+dx, y+dy
        
        if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == k:
            graph[ny][nx] = 2
            block += dfs(graph, nx, ny, [pos[0]+dx, pos[1]+dy], n, k)

    return block


def solution(game_board, table):
    res = 0
    n = len(game_board)
    blocks = []
    
    for i in range(n):  # 블록 자리 추출
        for j in range(n):
            if game_board[j][i] == 0:
                game_board[j][i] = 2
                blocks.append(dfs(game_board, i, j, [0, 0], n, 0))
                
    for _ in range(4):
        table = list(map(list, zip(*table[::-1])))  # 한 줄 회전 코드인데 실전에선 함수 구현 추천
        table_tmp = [x[:] for x in table]

        for i in range(n):
            for j in range(n):
                if table_tmp[j][i] == 1:
                    table_tmp[j][i] = 2

                    block = dfs(table_tmp, i, j, [0, 0], n, 1)

                    if block in blocks:
                        blocks.pop(blocks.index(block))
                        res += len(block)
                        
                        table = [x[:] for x in table_tmp]
                    else:
                        table_tmp = [x[:] for x in table]

    return res

# 함수 풀이에서 파이썬의 LEGB 규칙이랑 JS 스코프 개념이랑 충돌했습니다..
# 파이썬 개념에서 부족함을 느껴 문법은 코드를 참조했습니다. 구현 로직 자체는 간단합니다.