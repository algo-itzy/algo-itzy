import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
# x좌표, y좌표 순으로 정렬했습니다(배열의 0인자, 1인자순서.)
arr.sort(key=lambda x: (x[0],x[1]))

for i in arr:
    print(*i)