# 모듈
from math import gcd

a, b = map(int, input().split())


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
