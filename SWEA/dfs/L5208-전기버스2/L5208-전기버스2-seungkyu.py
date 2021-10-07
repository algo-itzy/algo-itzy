# git commit -m "code: Solve swea L5208 전기버스2 (seungkyu)"
import sys
sys.stdin = open('input.txt')


def dfs(x, cnt):
    global ans
    
    if cnt > ans:
        return
    
    if x >= m[0]:
        ans = cnt
        return

    for i in range(x+m[x], x, -1):
        cnt += 1
        dfs(i, cnt)
        cnt -= 1

T = int(input())
for tc in range(1, T+1):

    m = list(map(int, input().split()))
    
    ans = 100
    dfs(1, 0)

    print(f'#{tc} {ans-1}')
