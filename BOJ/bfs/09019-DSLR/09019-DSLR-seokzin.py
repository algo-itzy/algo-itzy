from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([a, ""])

    while q:
        n, cmd = q.popleft()

        if n == b:
            return cmd

        dn = n*2 % 10000

        if not visit[dn]:
            visit[dn] = 1
            q.append([dn, cmd + "D"])

        sn = n-1 if n != 0 else 9999
        
        if not visit[sn]:
            visit[sn] = 1
            q.append([sn, cmd + "S"])

        ln = n%1000 * 10 + n//1000
        
        if not visit[ln]:
            visit[ln] = 1
            q.append([ln, cmd + "L"])

        rn = n%10 * 1000 + n//10

        if not visit[rn]:
            visit[rn] = 1
            q.append([rn, cmd + "R"])


for _ in range(int(input())):
    a, b = map(int, input().split())
    visit = [0 for _ in range(10000)]
    print(bfs())

# 조금 지저분한 문제 (시간초과는 덤)