# git commit -m "code: Solve boj 15650 N과 M (2) (jiwoong)"
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
num = [i for i in range(1, N + 1)]
comb = combinations(num, M)
for i in comb:
    print(' '.join(map(str, i)))
