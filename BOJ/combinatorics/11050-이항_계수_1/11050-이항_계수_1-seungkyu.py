"""
팩토리얼
"""
# import math, math.factorial 이용 => 시간 비슷


def solve():
    n, k = map(int, input().split())
    print(factorial(n) // (factorial(k) * factorial(n-k)))


def factorial(n):

    if n <= 1:
        return 1

    return factorial(n-1) * n


if __name__ == "__main__":
    solve()
