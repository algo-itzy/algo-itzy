import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    chars = [input() for _ in range(n)]

    # 행
    for i in range(n):
        for j in range(n-m+1):
            result = chars[i][j:j+m]
            if result == result[::-1]:
                print(f'#{t} {result}')

    # 열 : 일단 열 전체 뽑아서 m 길이로 검증
    for j in range(n):
        col = ''
        for i in range(n):
            col += chars[i][j]

        for k in range(n-m+1):
            result = col[k:k+m]
            if result == result[::-1]:
                print(f'#{t} {result}')
