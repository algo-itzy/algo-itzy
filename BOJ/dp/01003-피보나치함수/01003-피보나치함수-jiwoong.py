# 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    c1 = 0
    c0 = 1
    tmp = 0
    for _ in range(n):
        tmp = c1
        c1 = c1 + c0
        c0 = tmp
    print(c0, c1)
