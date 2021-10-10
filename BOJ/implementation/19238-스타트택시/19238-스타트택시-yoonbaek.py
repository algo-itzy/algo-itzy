from collections import deque

ints = lambda: map(int, input().split())
moves = ((-1, 0), (0, -1), (0, 1), (1, 0))

def rollback(history):
    for past_r, past_c in history:
        map_[past_r][past_c] = 0


def get_passenger(start):
    q = deque([start])
    history = [start]
    if start in dispatch:
        return start

    while q:
        row, col = q.popleft()

        for y, x in moves:
            y += row
            x += col
            if 0 <= x < N and 0 <= y < N:
                if not map_[y][x]: 
                    map_[y][x] = map_[row][col] - 1             
                    if (y, x) in dispatch:
                        if map_[y][x] < 0:
                            return
                        rollback(history) 
                        return (y, x)
                    history.append((y, x))
                    q.append((y, x))


def transit(dep):
    dest = dispatch[dep]
    q = deque([dep])
    history = [dep]

    while q:
        row, col = q.popleft()

        for y, x in moves:
            y += row
            x += col
            if 0 <= x < N and 0 <= y < N:
                if not map_[y][x]:
                    map_[y][x] = map_[row][col] - 1
                    if (y, x) == dest:
                        if map_[y][x] < 0:
                            return
                        map_[y][x] += 2*(map_[dep[0]][dep[1]] - map_[y][x])
                        rollback(history)
                        dispatch.pop(dep)
                        return (y, x)
                    history.append((y, x))
                    q.append((y, x))  


if __name__ == "__main__":
    N, M, fuel = ints()

    map_ = [list(ints()) for _ in range(N)]
    row, col = ints()
    start = (row-1, col-1)
    map_[start[0]][start[1]] = fuel

    dispatch = {}

    for i in range(1, M+1):
        dept_r, dept_c, dest_r, dest_c = ints()
        dept_r-=1; dept_c-=1; dest_r-=1; dest_c-=1;
        dispatch[(dept_r, dept_c)] = (dest_r, dest_c)

    destination = start
    while dispatch:
        departure = get_passenger(destination)
        if not departure:
            print(-1)
            break
        destination = transit(departure)
        if not destination:
            print(-1)
            break
    else:
        print(map_[destination[0]][destination[1]])

# git commit -m "code: Solve boj 19238 스타트택시 (yoonbaek)"