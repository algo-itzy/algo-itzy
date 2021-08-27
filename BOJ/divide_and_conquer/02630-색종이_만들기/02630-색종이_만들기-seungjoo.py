import sys
input = sys.stdin.readline

def check(x,y,size):
    color = matrix[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if not color==matrix[i][j]:
                return False
    if color==1:
        answer[1] += 1
    else:
        answer[0] += 1
    return True


def divide_paper(start_x,start_y,length):
    if not check(start_x,start_y,length//2):
        divide_paper(start_x,start_y,length//2)
    if not check(start_x+length//2,start_y,length//2):
        divide_paper(start_x+length//2,start_y,length//2)
    if not check(start_x,start_y+length//2,length//2):
        divide_paper(start_x,start_y+length//2,length//2)
    if not check(start_x+length//2,start_y+length//2,length//2):
        divide_paper(start_x+length//2,start_y+length//2,length//2)
    

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [0,0]
if not check(0,0,N):
    divide_paper(0,0,N)
for color in answer:
    print(color)