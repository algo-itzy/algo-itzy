# git commit -m "code: Solve programmers 카드 짝 맞추기 (seungjoo)"
from collections import defaultdict, deque
from itertools import permutations


def solution(board, r, c):

    def ctrl_move(x, y, dx, dy, visited):
        for i in range(1, 4):
            nx, ny = x + dx * i, y + dy * i
            if (nx, ny) in visited and not visited[(nx, ny)]:
                return (nx, ny)
            if dx == 1 and nx >= 3:
                return (3, ny)
            elif dx == -1 and nx <= 0:
                return (0, ny)
            elif dy == 1 and ny >= 3:
                return (nx, 3)
            elif dy == -1 and ny <= 0:
                return (nx, 0)
            

    def make_count(target, x, y, visited):
        q = deque()
        q.append((x, y, 0))
        check = [[float('inf')] * 4 for _ in range(4)]
        check[x][y] = True
        while q:
            x, y, dist = q.popleft()
            if (x, y) == target:
                return dist + 1
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if check[nx][ny] > dist + 1:
                        check[nx][ny] = dist + 1
                        q.append((nx, ny, dist + 1))
                ctrl_x, ctrl_y = ctrl_move(x, y, dx, dy, visited)
                if check[ctrl_x][ctrl_y] > dist + 1:
                    check[ctrl_x][ctrl_y] = dist + 1
                    q.append((ctrl_x, ctrl_y, dist + 1))



    def dfs(sequence, x, y, depth, key, cnt, visited):
        global min_cnt
        if cnt > min_cnt:
            return
        if depth == len(sequence):
            min_cnt = min(min_cnt, cnt)
            return
        if key:
            for target in num_set[sequence[depth]]:
                if visited[target]:
                    continue
                dist = make_count(target, x, y, visited)
                visited[target] = True
                dfs(sequence, target[0], target[1], depth + 1, 0, cnt + dist, visited)
                visited[target] = False
        else:
            for target in num_set[sequence[depth]]:
                dist = make_count(target, x, y, visited)
                visited[target] = True
                dfs(sequence, target[0], target[1], depth, 1, cnt + dist, visited)
                visited[target] = False


    global min_cnt
    num_set = defaultdict(list)
    delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
    visited = {}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                num_set[board[i][j]].append((i, j))
                visited[(i, j)] = False

    min_cnt = float('inf')
    for each_set in permutations([num for num in num_set], len(num_set)):
        dfs(each_set, r, c, 0, 0, 0, visited)

    return min_cnt