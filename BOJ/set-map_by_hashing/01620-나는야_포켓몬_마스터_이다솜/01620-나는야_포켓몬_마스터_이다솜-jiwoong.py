"""
도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M
첫 글자만 대문자이고, 나머지 문자는 소문자로만
문제가 알파벳으로만 들어오면 포켓몬 번호,, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
d1, d2 = {}, {}

for i in range(1, n + 1):
    s = input().rstrip()
    d1[s] = i
    d2[i] = s

for _ in range(m):
    s = input().rstrip()
    if s.isdigit():
        print(d2[int(s)])
    else:
        print(d1[s])
