# solved by YoonBaek
from collections import deque


# 현재 노드의 다음 노드를 구성해주는 함수입니다.
def do_search(now: tuple) -> list:
    directions = [
        (0, -1), (0, 1), # 상하
        (-1, 0), (1, 0), # 좌우
    ]
    searched = []
    for h, v in directions:
        moved_x, moved_y = now[0]+h, now[1]+v

        is_in_maze = 0 <= moved_x < size and 0 <= moved_y < size
    
        if is_in_maze: 
            moved = maze[moved_y][moved_x]
            if not moved or moved == 3:
                searched.append((moved_x, moved_y))

    return searched


def BFS(now: tuple):
    q = deque()
    moves = deque()
    q.append(now); moves.append(-1)
    maze[now[1]][now[0]] = 1

    while q:
        now = q.popleft()
        move = moves.popleft()
        move += 1

        searches = do_search(now)

        for next in searches:
            if maze[next[1]][next[0]] == 3:
                return move
            if not maze[next[1]][next[0]]:
                # 다음 노드 정보 입력
                q.append(next)
                moves.append(move)
                # 방문처리
                maze[next[1]][next[0]] = 1

    return 0

if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        size = int(input())
        maze = []
        start_x = start_y = end_x = end_y = 0

        # input 받는 부분
        for row_num in range(size):
            row = list(map(int, list(input())))

            if 2 in row:
                start_x, start_y = row.index(2), row_num
            if 3 in row:
                end_x, end_y = row.index(3), row_num
            
            maze.append(row)

        cnt = BFS((start_x, start_y))

        # 방문 했는지 여부 체크
        print(f"#{tc} {cnt}")