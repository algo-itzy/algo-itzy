import sys
input = sys.stdin.readline


def check(n,s_x,s_y):
    pivot = matrix[s_x][s_y]
    for i in range(s_x,s_x+n):
        for j in range(s_y,s_y+n):
            if matrix[i][j] != pivot:
                return False
    return True


def divide_paper(n,s_x,s_y):
    global papers
    pivot = n//3
    if n==1:
        papers[matrix[s_x][s_y]] += 1
        return
    if check(n,s_x,s_y):
        papers[matrix[s_x][s_y]] += 1
        return
    for i in range(3):
        for j in range(3):
            divide_paper(pivot,s_x+(pivot*i),s_y+(pivot*j))


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
papers = {-1: 0, 0: 0, 1: 0}

divide_paper(N,0,0)
for paper in papers:
    print(papers[paper])