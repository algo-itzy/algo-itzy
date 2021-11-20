# git commit -m "code: Solve boj 11053 가장 긴 증가하는 부분 수열 (seungjoo)"
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

q=[]
for x in a:
    if not q or x > q[-1]:
        q.append(x)
    else:
        q[bisect_left(q,x)] = x

print(len(q))
