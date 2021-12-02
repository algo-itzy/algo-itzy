# git commit -m "code: Solve boj 01167 트리의 지름 (jiwoong)"
import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    dp = [-1 for _ in range(V + 1)]
    dp[v] = 0
    q = deque()
    q.append(v)
    while q:
        tmp = q.popleft()
        for nc, nv in arr[tmp]:
            if dp[nv] == -1:  
                dp[nv] = dp[tmp] + nc
                q.append(nv)
    return dp


V = int(input())
arr = [[] for _ in range(V + 1)]
for _ in range(V):
    nums = list(map(int, input().split()))
    tmp = nums[0]
    for i in range(1, len(nums), 2):
        if nums[i] == -1:
            break
        arr[tmp].append((nums[i + 1], nums[i]))  
dist = bfs(1)  
v = dist.index(max(dist))  
print(max(bfs(v)))  
