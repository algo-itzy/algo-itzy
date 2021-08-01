n, k = map(int, input().split())

# 재귀함수로 factorial 구현
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print(int(factorial(n) / (factorial(n-k) * factorial(k))))
