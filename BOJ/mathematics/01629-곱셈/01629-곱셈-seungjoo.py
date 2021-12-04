# git commit -m "code: Solve boj 01629 곱셈 (seungjoo)"
import sys
input = sys.stdin.readline

def pow(n):
    if n == 1:
        return a % c
    left = pow(n // 2)
    if not n & 1:
        return left * left % c
    return left * left * a % c

a, b, c = map(int, input().split())
print(pow(b))