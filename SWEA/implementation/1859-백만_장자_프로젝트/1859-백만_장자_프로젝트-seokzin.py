T = int(input())

for tc in range(1, T+1):
    N = int(input())
    costs = list(map(int, input().split()))
    top = costs[-1]
    res = 0

    for i in range(len(costs)-1, -1, -1):
        if top > costs[i]:
            res += top-costs[i]
        else:
            top = costs[i]

    print(f"#{tc} {res}")

# 처음엔 매번 최대값을 갱신해 앞에서 풀었으나 시간초과입니다...
# 그냥 시중에 있는 역탐색으로 풀었습니다. 아쉽