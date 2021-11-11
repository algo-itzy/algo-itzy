from collections import deque

D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(arr):
    p_set = []
    
    for i in range(5):
        for j in range(5):
            if arr[j][i] == 'P':
                p_set.append([i, j])

    for p in p_set:
        sx, sy = p
        q = deque([(sx, sy, 0)])
        visit = [[0]*5 for _ in range(5)]

        while q:
            x, y, d = q.popleft()
            visit[y][x] = 1
            
            for dx, dy in D:
                nx, ny = x+dx, y+dy

                if 0 <= nx < 5 and 0 <= ny < 5 and not visit[ny][nx]:
                    visit[ny][nx] = 1
                    
                    if arr[ny][nx] == 'P':
                        if d <= 1:
                            return 0

                    elif arr[ny][nx] == 'O':
                        if d == 0:
                            q.append((nx, ny, d+1))

    return 1


def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
        
    return answer