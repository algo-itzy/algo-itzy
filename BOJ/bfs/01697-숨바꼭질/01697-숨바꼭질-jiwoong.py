"""
# 숨바꼭질
수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K
"""

import sys
from collections import deque

input = sys.stdin.readline()

n, k = map(int, input.split())
max_value = 100001
visit = [0] * max_value


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return visit[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < max_value and not visit[next_pos]:
                visit[next_pos] = visit[now_pos] + 1
                q.append(next_pos)


print(bfs())
