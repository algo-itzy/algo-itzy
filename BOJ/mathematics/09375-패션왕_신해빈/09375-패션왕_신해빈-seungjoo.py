# git commit -m "code: Solve boj 09375 패션왕 신해빈 (seungjoo)"
import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(int)
    ans = 1
    for _ in range(n):
        name, type_c = input().split()
        clothes[type_c] += 1
    for cloth in clothes:
        ans *= clothes[cloth]+1
    print(ans-1)