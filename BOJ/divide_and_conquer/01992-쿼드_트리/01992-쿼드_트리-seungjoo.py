import sys
input = sys.stdin.readline


def check(n,s_x,s_y):
    pivot = matrix[s_x][s_y]
    for i in range(s_x,s_x+n):
        for j in range(s_y,s_y+n):
            if matrix[i][j] != pivot:
                return False
    return True


def compress_video(n,s_x,s_y):
    pivot = n//2
    if n==1:
        q_tree.append(str(matrix[s_x][s_y]))
        return
    if check(n,s_x,s_y):
        q_tree.append(str(matrix[s_x][s_y]))
        return
    q_tree.append('(')
    for i in range(2):
        for j in range(2):
            compress_video(pivot,s_x+(pivot*i),s_y+(pivot*j))
    q_tree.append(')')

N = int(input())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
q_tree = []

compress_video(N,0,0)
print(''.join(q_tree))