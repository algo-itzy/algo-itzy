import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for i in range(n):
        cnt = 0

        for j in range(n):  # 행
            if puzzle[i][j]:
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1:  # 벽을 만나거나 0이 되었을 때
                if cnt == k:
                    result += 1
                cnt = 0

        for j in range(n):  # 행
            if puzzle[j][i]:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{t} {result}')
