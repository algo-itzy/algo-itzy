"""
# 듣보잡
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로

듣보잡의 수와 그 명단을 사전순으로 출력
"""

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

listen = set() # 듣
see = set() # 보

for _ in range(n):
    listen.add(input().strip())

for _ in range(m):
    see.add(input().strip())

ans = sorted(list(listen & see))

print(len(ans))

for i in ans:
    print(i)
