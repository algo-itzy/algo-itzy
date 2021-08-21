# solved by YoonBaek
class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, x):
        self.items.append(x)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            return self.items.pop()
        return -1

    def top(self):
        if self.size:
            return self.items[-1]
        return -1


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
            if not moved:
                searched.append((moved_x, moved_y))

    return searched


def dfs_stack(now: tuple):
    stack = Stack()
    stack.push(now)

    while stack.items:

        searches = do_search(now)

        if searches:
            for now in searches:
                # 다음 노드 정보 입력
                stack.push(now)
                # 방문처리
                maze[now[1]][now[0]] = 1
                # 다음 노드로 이동
                now = stack.top()
        else: 
            # 이전 노드로 이동
            now = stack.pop()


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        size = int(input())
        maze = []
        start_x = start_y = end_x = end_y = 0

        for row_num in range(size):
            row = list(map(int, list(input())))

            if 2 in row:
                start_x, start_y = row.index(2), row_num
            if 3 in row:
                end_x, end_y = row.index(3), row_num
            
            maze.append(row)

        # 종료지점 방문 안 함 처리
        maze[end_y][end_x] = 0

        dfs_stack((start_x, start_y))

        # 방문 했는지 여부 체크
        print(f"#{tc} {maze[end_y][end_x]}")