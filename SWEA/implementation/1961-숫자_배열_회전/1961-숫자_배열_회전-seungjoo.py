import sys
input = sys.stdin.readline

def rotate_clock(n, matrix):
    rot90 = [k[::-1] for k in zip(*matrix)]
    rot180 = [k[::-1] for k in zip(*rot90)]
    rot270 = [k[::-1] for k in zip(*rot180)]
    merge_matrix = [[] for _ in range(n)]
    for matrix in rot90,rot180,rot270:
        for i in range(n):
            merge_matrix[i].append(''.join(map(str,matrix[i])))
    return merge_matrix

for test in range(1,int(input())+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test}')
    answer = rotate_clock(N, matrix)
    for row in answer:
        print(*row)