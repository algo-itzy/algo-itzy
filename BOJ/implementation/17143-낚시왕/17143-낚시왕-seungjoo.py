# git commit -m "code: Solve boj 17143 낚시왕 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush

def move_shark():
    new_sharks = defaultdict(list)
    for now_c in sharks:
        while sharks[now_c]:
            r, s, d, z = sharks[now_c].pop()
            total = s
            c = now_c
            if d == 0 or d == 1:
                s %= 2 * R - 2
                while s:
                    if (r == R - 1 and d == 1) or (r == 0 and d == 0):
                        d^= 1 
                    nr = r + delta[d][0]
                    s -= 1
                    r = nr
            else:
                s %= 2 * C - 2
                while s:
                    if (c == C - 1 and d == 2) or (c == 0 and d == 3):
                        d = (d - 2)^1 + 2
                    nc = c + delta[d][1]
                    s -= 1
                    c = nc
            heappush(new_sharks[c], (r, total, d, z))
    print(new_sharks)
    return new_sharks

R, C, M = map(int, input().split())
sharks = defaultdict(list)
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    heappush(sharks[c - 1], (r - 1, s, d - 1, z))

delta = ((-1, 0), (1, 0), (0, 1), (0, -1))
answer = 0
# 낚시왕은 1초당 1열씩 이동
for king_of_fishing in range(C):
    print(sharks)
    if sharks[king_of_fishing]:
        answer += heappop(sharks[king_of_fishing])[3]
    sharks = move_shark()
    print(sharks)
    print()
# 해당 열에서 가장 가까운 상어를 잡는다. 잡으면 상어는 사라진다.
# 상어들이 이동한다.
print(answer)