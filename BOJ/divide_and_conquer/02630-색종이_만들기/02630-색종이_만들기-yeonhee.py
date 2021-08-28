def cut_paper(row, col, n):
    global white, blue

    paper_sum = 0
    for r in range(row, row+n):
        for c in range(col, col+n):
            paper_sum += paper[r][c]

    if paper_sum == n*n:
        blue += 1

    elif paper_sum == 0:
        white += 1

    else:
        cut_paper(row, col, n//2)
        cut_paper(row + n//2, col, n//2)
        cut_paper(row, col + n//2, n//2)
        cut_paper(row + n//2, col + n//2, n//2)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

cut_paper(0, 0, N)
print(white)
print(blue)
