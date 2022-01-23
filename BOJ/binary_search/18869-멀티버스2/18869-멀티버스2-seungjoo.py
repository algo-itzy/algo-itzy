# git commit -m "code: Solve boj 18869 멀티버스2 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import defaultdict

m, n = map(int, input().split())
universe = defaultdict(int)
for _ in range(m):
    univ = list(map(int, input().split()))
    su = sorted(list(set(univ)))
    rnk = {su[i]: i for i in range(len(su))}
    add = tuple([rnk[x] for x in univ])
    universe[add] += 1

ans = 0
for cnt in universe.values():
    ans += cnt * (cnt - 1) // 2
print(ans)