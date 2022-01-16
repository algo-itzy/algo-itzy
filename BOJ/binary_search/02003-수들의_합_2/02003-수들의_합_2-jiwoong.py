# git commit -m "code: Solve boj 02003 수들의 합 2 (jiwoong)"
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
cnt, ans = 0, 0

while True:
    if cnt >= m:
        cnt -= a[s]
        s += 1
    elif e == n:
        break
    else:
        cnt += a[e]
        e += 1
    if cnt == m:
        ans += 1

print(ans)
