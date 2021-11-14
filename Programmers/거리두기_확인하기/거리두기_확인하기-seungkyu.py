# git commit -m "code: Solve programmers 거리두기 확인하기 (seungkyu)"
delta = ((0, 1),(0, -1),(1, 0),(-1, 0))

def bfs(place, x, y):
    dist = [[0]*5 for _ in range(5)]
    q = []
    dist[x][y] = 1
    q.append([x, y])
    while q:
        x, y = q.pop(0)
        if dist[x][y] >= 3:
            break
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<5 and 0<=ny<5 and not dist[nx][ny]:
                if place[nx][ny] == 'P':
                    return False
                elif place[nx][ny] == 'O':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
    return True

def check_dist(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(place, i ,j):
                    return 0
                
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_dist(place))
    return answer