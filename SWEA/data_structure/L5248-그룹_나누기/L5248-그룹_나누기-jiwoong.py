# git commit -m "code: Solve swea L5248 그룹 나누기 (jiwoong)"
def divide(x):
    if x == par[x]:
        return x
    else:
        return divide(par[x])


def group(x, y):
    par[divide(y)] = divide(x)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))  # M쌍의 숫자들

    par = [i for i in range(N + 1)]  # 부모노드번호 기억할 리스트
    for i in range(M):
        x, y = nums[2 * i], nums[2 * i + 1]
        group(x, y)

    ans = set()
    for i in range(1, N + 1):
        ans.add(divide(i))
    print("#{} {}".format(tc, len(ans)))
