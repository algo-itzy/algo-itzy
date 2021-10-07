import sys
sys.stdin = open('input.txt')


def dfs(idx, cnt):
    global result

    if cnt >= result:
        return

    if idx >= N-1:
        if cnt <= result:
            result = cnt
        return

    for i in range(data[idx]):
        dfs(idx+i+1, cnt+1)


for t in range(1, int(input())+1):
    data = list(map(int, input().split()))
    N = data.pop(0)  # 정류장 수
    result = float('inf')
    dfs(0, -1)

    print(f'#{t} {result}')
