# git commit -m "code: Solve programmers 거리두기 확인하기 (seungjoo)"
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

def is_check(place):
    q = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                q.append((i, j, 0, set()))
    while q:
        x, y, dist, visited = q.pop()
        visited.add((x, y))
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                if place[nx][ny] == 'X':
                    continue
                elif place[nx][ny] == 'O':
                    if dist < 2:
                        q.append((nx, ny, dist + 1, visited))
                else:
                    if dist < 2:
                        return False
    return True
    

def solution(places):
    answer = []
    for place in places:
        ret = 1 if is_check(place) else 0
        answer.append(ret)
    return answer