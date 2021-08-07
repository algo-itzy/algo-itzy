# 2^N × 2^N인 2차원 배열을 Z 모양으로 탐색
# r행 c열을 몇 번째로 방문하는지 출력

import sys
n, r, c = map(int, sys.stdin.readline().split())
ans = 0

while n >= 1:
    quad = (2 ** n) // 2
    if n > 1:
        if r < quad <= c:
            ans += quad ** 2
            c -= quad
        elif c < quad <= r:
            ans += (quad ** 2) * 2
            r -= quad
        elif r >= quad and c >= quad:
            ans += (quad ** 2) * 3
            r -= quad
            c -= quad

    elif n == 1:
        if r == 0 and c == 1:
            ans += 1
        elif r == 1 and c == 0:
            ans += 2
        elif r == 1 and c == 1:
            ans += 3
    n -= 1

print(ans)
