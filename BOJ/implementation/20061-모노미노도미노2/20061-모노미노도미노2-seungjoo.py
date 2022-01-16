# git commit -m "code: Solve boj 20061 모노미노도미노2 (seungjoo)"
import sys
input = sys.stdin.readline

def move_block(points):
    min_x, min_y = 5, 5
    for x, y in points:
        # 초록은 y좌표에 대한 x를 5행부터 0행까지 검사
        for row in range(4, -1, -1):
            if not green_area[row][y] and green_area[row + 1][y]:
                min_x = min(min_x, row)
        # 파랑은 x좌표에 대한 y를 5부터 0까지 검사
        for col in range(4, -1, -1):
            if not blue_area[x][col] and blue_area[x][col + 1]:
                min_y = min(min_y, col)

    for x, y in points:
        green_area[min_x][y] = 1
        blue_area[x][min_y] = 1
    if len(points) > 1:
        x, y = points[0]
        if points[0][1] < points[1][1]:
            blue_area[x][min_y - 1] = 1
        elif points[0][0] < points[1][0]:
            green_area[min_x - 1][y] = 1


def check_areas():
    global answer
    # 녹색영역 검사
    remove_line = []
    for i in range(5, -1, -1):
        if sum(green_area[i]) == 4:
            answer += 1
            for j in range(4):
                green_area[i][j] = 0
            remove_line.append(i)
    for line in remove_line:
        for i in range(line, -1, -1):
            for j in range(4):
                green_area[i][j] = green_area[i - 1][j]
    for i in range(4):
        green_area[0][i] = 0
    # 파란영역 검사
    remove_line = []
    for i in range(5, -1, -1):
        tmp = 0
        for j in range(4):
            if blue_area[j][i]:
                tmp += 1
        if tmp == 4:
            answer += 1
            for j in range(4):
                blue_area[j][i] = 0
            remove_line.append(i)    
    for line in remove_line:
        for i in range(line, -1, -1):
            for j in range(4):
                blue_area[j][i] = blue_area[j][i - 1]
    for i in range(4):
        blue_area[i][0] = 0


def check_zeroarea():
    global green_area
    green_zeros = 0
    blue_zeros = 0
    for i in range(2):
        for j in range(4):
            if green_area[i][j] == 1:
                green_zeros += 1
                break
        for j in range(4):
            if blue_area[j][i] == 1:
                blue_zeros += 1
                break
    for _ in range(green_zeros):
        green_area.pop()
        green_area = [[0, 0, 0, 0]] + green_area
    for _ in range(blue_zeros):
        for i in range(4):
            blue_area[i].pop()
            blue_area[i] = [0] + blue_area[i]


N = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(N)]
# 1, 2 - 가로, 3 - 세로

blue_area = [[0] * 6 for _ in range(4)]
green_area = [[0] * 4 for _ in range(6)]

answer = 0
# 블록 놓기
for t, x, y in blocks:
    sites = []
    sites.append((x, y))
    if t == 2:
        sites.append((x, y + 1))
    elif t == 3:
        sites.append((x + 1, y))
    move_block(sites)
    check_areas()
    check_zeroarea()
cnt = 0
for i in range(4):
    for j in range(6):
        if blue_area[i][j]:
            cnt += 1
for i in range(6):
    for j in range(4):
        if green_area[i][j]:
            cnt += 1
print(answer)
print(cnt)
