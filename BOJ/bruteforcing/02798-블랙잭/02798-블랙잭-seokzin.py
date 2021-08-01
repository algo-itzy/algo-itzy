n, m = map(int, input().split())

cards = list(map(int, input().split()))

res = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      picks = cards[i] + cards[j] + cards[k]

      if picks <= m:
        res = max(picks, res)

print(res)

# 3중 for문 보자마자 순열이 생각났지만 모듈을 지양했음

"""
git commit -m "code: Solve boj 02798 블랙잭 (seokzin)"
"""