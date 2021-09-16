# git commit -m "code: Solve boj 11403 경로 찾기 (seungkyu)"
import sys
input = sys.stdin.readline


def floyd_washal():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if not ans[i][j] and ans[i][k]+ans[k][j] == 2:
                    ans[i][j] = 1

N = int(input())
ans = [list(map(int, input().split())) for _ in range(N)]

floyd_washal()

for row in ans:
    print(*row)
