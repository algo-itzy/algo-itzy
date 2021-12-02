# git commit -m "code: Solve boj 13549 숨바꼭질 3 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import deque

def BFS(N,K):
    q = deque()
    q.append(N)
    dp = [-1] * 100001
    dp[N] = 0
    while q:
        N = q.popleft()
        if N == K:
            print(dp[K])
            exit()
        for next_node in (2 * N, N + 1, N - 1):
            if 0 <= next_node<100001 and dp[next_node] == -1:
                if next_node == 2 * N:
                    q.appendleft(next_node)
                    dp[next_node] = dp[N]
                else:
                    q.append(next_node)
                    dp[next_node] = dp[N] + 1 

N, K = map(int, input().split())

print(BFS(N,K) if N < K else N - K)