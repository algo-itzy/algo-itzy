import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
ans = 0

for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if cards[a] + cards[b] + cards[c] > m:
                continue
            else:
                ans = max(ans, cards[a] + cards[b] + cards[c])
print(ans)
