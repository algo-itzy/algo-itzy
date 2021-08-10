"""
# 회의실 배정
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수

회의의 시작시간과 끝나는 시간
"""

import sys

input = sys.stdin.readline
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))
start = 0
ans = 0

for time in times:
    if time[0] >= start:
        start = time[1]
        ans += 1

print(ans)
