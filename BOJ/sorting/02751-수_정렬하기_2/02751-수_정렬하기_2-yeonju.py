"""
1<=N<=1,000,000
"""

import sys

N = int(input())
li = []

for i in range(N):
    li.append(sys.stdin.readline())

li.sort()

for i in li:
    print([i])
    

"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""