# git commit -m "code: Solve programmers 퍼즐 조각 채우기 (seungjoo)"
from collections import defaultdict, deque

def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    def bfs(graph, start_x, start_y, num):
        ret = [(0, 0)]
        q = deque()
        q.append((start_x, start_y, 0, 0))
        graph[start_x][start_y] = -1
        while q:
            x, y, pre_x, pre_y = q.popleft()
            for dx, dy in delta:
                nx, ny, n_pre_x, n_pre_y = x + dx, y + dy, pre_x + dx, pre_y + dy
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
                    graph[nx][ny] = -1
                    q.append((nx, ny, n_pre_x, n_pre_y))
                    ret.append((n_pre_x, n_pre_y))
        return ret
    # 빈칸 모양 찾기
    blanks = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if not game_board[i][j]:
                game_board[i][j] = -1
                blanks[tuple(bfs(game_board, i, j, 0))] += 1
                
    # 회전시켜 blanks 맞추기
    for _ in range(4):
        table = [list(row)[::-1] for row in zip(*table)]
        rotated_table = [row[:] for row in table]

        for i in range(n):
            for j in range(n):
                if rotated_table[i][j] == 1:
                    rotated_table[i][j] = -1
                    block = tuple(bfs(rotated_table, i, j, 1))
                    if block in blanks:
                        answer += len(block)
                        blanks[block] -= 1
                        if not blanks[block]:
                            del blanks[block]
                        table = [row[:] for row in rotated_table]
                    else:
                        rotated_table = [row[:] for row in table]
    return answer