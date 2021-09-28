# git commit -m "code: Solve boj 15685 드래곤 커브 (seungjoo)"
import sys
input = sys.stdin.readline

delta = ((1, 0), (0, -1), (-1, 0), (0, 1))
N = int(input())
curves = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    # (x,y)시작, 처음 d방향으로 시작,(처음 선분하나로 시작) g 세대까지 진행.(1개추가, 2개추가, 4개 추가, 8개 추가.. 90도 회전시키며.)
    curves.add((x, y))
    cur_dragon = [d]
    next_dragon = [d]
    for _ in range(g+1):
        for d in cur_dragon:
            nx, ny = x + delta[d][0], y + delta[d][1]
            curves.add((nx, ny))
            x, y = nx, ny
        cur_dragon = [(d + 1) % 4 for d in next_dragon[::-1]]
        next_dragon = next_dragon + cur_dragon
        
cnt = 0
for i in range(100):
    for j in range(100):
        if (i, j) in curves and (i + 1, j) in curves and (i, j +  1) in curves and (i + 1, j + 1) in curves:
            cnt += 1 
print(cnt)