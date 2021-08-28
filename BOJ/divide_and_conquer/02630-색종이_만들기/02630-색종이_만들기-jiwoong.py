import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0  # 0
blue = 0  # 1


def div_conq(row, col, n):
    global white, blue
    total = paper[row][col]
    tmp = True

    for i in range(row, row + n):
        if not tmp:
            break
        for j in range(col, col + n):
            if total != paper[i][j]:
                tmp = False
                div_conq(row, col, n // 2)
                div_conq(row, col + n // 2, n // 2)
                div_conq(row + n // 2, col, n // 2)
                div_conq(row + n // 2, col + n // 2, n // 2)
                break

    if tmp:
        if total == 1:
            blue += 1
        else:
            white += 1


div_conq(0, 0, n)
print(white)
print(blue)