def min_sum(curr, total):  # curr: 현재 행, total: 총합
    global minV
    if curr == N:
        # 최소값인지
        if total < minV:
            minV = total
        return
    elif minV <= total:  # 최소가 아니면
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                min_sum(curr + 1, total + arr[curr][i])
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]
    minV = 10000
    min_sum(0, 0)  # 0행에서 시작, 총합: 0
    print("#{} {}".format(tc, minV))
