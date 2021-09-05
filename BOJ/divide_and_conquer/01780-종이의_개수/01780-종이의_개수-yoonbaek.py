from sys import stdin

# 일급함수
read = stdin.readline

# 쿼드트리로 압축할 만한 범위인지 판단
def is_color_same(start_x, start_y, end_x, end_y):
    start = paper[start_y][start_x]

    for row in range(start_y, end_y):
        for col in range(start_x, end_x):
            if paper[row][col] != start:
                return False

    # 파이썬에선 0이 False이므로 0이 안나오게 +1
    return start+2

# 쿼드트리 구성
def scissor(start_x, start_y, end_x, end_y):
    check = is_color_same(start_x, start_y, end_x, end_y)
    middle_x_1 = start_x+(end_x-start_x)//3
    middle_x_2 = start_x+(end_x-start_x)//3*2
    middle_y_1 = start_y+(end_y-start_y)//3
    middle_y_2 = start_y+(end_y-start_y)//3*2


    if not check:
        # 9분면 탐색
        scissor(start_x, start_y, middle_x_1, middle_y_1) # 1
        scissor(middle_x_1, start_y, middle_x_2, middle_y_1) # 2
        scissor(middle_x_2, start_y, end_x, middle_y_1) # 3
        scissor(start_x, middle_y_1, middle_x_1, middle_y_2) # 4
        scissor(middle_x_1, middle_y_1, middle_x_2, middle_y_2) # 5
        scissor(middle_x_2, middle_y_1, end_x, middle_y_2) # 6
        scissor(start_x, middle_y_2, middle_x_1, end_y) # 7
        scissor(middle_x_1, middle_y_2, middle_x_2, end_y) # 8
        scissor(middle_x_2, middle_y_2, end_x, end_y) # 9
    else:
        # check에서 반환된 2와 1을 다시 1과 0으로 만들어 출력
        RGB[check-1] += 1


if __name__ == "__main__":
    N = int(input())
    paper = [list(map(int, read().split())) for _ in range(N)]
    # 색깔 정보 저장
    RGB = [0,0,0]
    scissor(0,0,N,N)
    
    print(*RGB, sep="\n")

# git commit -m "code: Solve boj 01780 종이의 개수 (yoonbaek)"