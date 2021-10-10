def sol(idx, cnt): # 현재 위치, 교환 횟수
    global res

    if idx >= n-1: # 마지막에 도착한 경우
        res = min(res, cnt)
        return

    if cnt > res: # 중간에 이미 교환 횟수가 최소 교환 횟수를 넘으면 무시
        return

    for i in range(idx + stop[idx], idx, -1):
    # for i in range(idx + 1, idx + stop[idx] + 1): # 뒤에서부터 앞으로 와야 시간 초과 안 됨
        sol(i, cnt + 1)


for tc in range(int(input())):
    li = list(map(int, input().split()))
    n = li[0]
    stop = li[1:]
    res = 100000000
    cnt = 0
    sol(0, -1)
    print(f'#{tc+1} {res}')

# git commit -m "code: Solve swea L5208 전기버스2 (yeonju)"