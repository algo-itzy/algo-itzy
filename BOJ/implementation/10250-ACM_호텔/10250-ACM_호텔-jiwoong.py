# 빈 방 배정
# 걷는 거리가 같을 때에는 아래층의 방을 더 선호
import sys

t = int(input())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split()) # 층 수, 각 층의 방 수, 몇 번째 손님
    floor = n % h
    room = n // h + 1
    if floor == 0:
        room -= 1
        floor = h
    print(floor * 100 + room)
