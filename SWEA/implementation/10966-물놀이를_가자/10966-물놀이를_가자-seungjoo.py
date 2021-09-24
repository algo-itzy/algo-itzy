# git commit -m "code: Solve swea 10966 물놀이를 가자 (seungjoo)"
import sys
sys.stdin = open('input.txt')

for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pool = [list(input()) for _ in range(N)]
    dp_up_left = [[float('inf')] * M for _ in range(N)]
    dp_down_right = [[float('inf')] * M for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                dp_down_right[i][j] = 0
                continue
            if j:
                dp_down_right[i][j] = min(dp_down_right[i][j-1] + 1, dp_down_right[i][j])
            if i:
                dp_down_right[i][j] = min(dp_down_right[i-1][j] + 1, dp_down_right[i][j])

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if pool[i][j] == 'W':
                dp_down_right[i][j] = 0
                continue
            if not j == M - 1:
                dp_down_right[i][j] = min(dp_down_right[i][j+1] + 1, dp_down_right[i][j])
            if not i == N - 1:
                dp_down_right[i][j] = min(dp_down_right[i+1][j] + 1, dp_down_right[i][j])
            if dp_up_left[i][j] == float('inf') and dp_down_right[i][j] == float('inf'):
                continue
            answer += min(dp_up_left[i][j], dp_down_right[i][j])

    print(f'#{test} {answer}')
