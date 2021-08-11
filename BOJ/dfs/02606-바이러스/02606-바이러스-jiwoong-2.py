"""
# 바이러스 - DFS
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스 감염

첫째 줄 : 컴퓨터의 수가 주어진다.
둘째 줄 : 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력
"""

infect = [1]


def dfs(con):
    global cnt, infect
    for i in range(1, n + 1):
        if i not in infect and nums[con][i] == 1:
            cnt += 1
            infect.append(i)
            dfs(i)


n = int(input())
cpt = int(input())
nums = [[0] * (n + 1) for i in range(n + 1)]
cnt = 0
for i in range(cpt):
    x, y = map(int, input().split())
    nums[x][y] = 1
    nums[y][x] = 1

dfs(1)
print(cnt)
