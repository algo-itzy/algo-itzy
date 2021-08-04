from math import factorial

n, k = map(int, input().split())
ans = factorial(n) // (factorial(k) * factorial(n - k))  # 이항계수 factorial 공식 적용
print(ans)
