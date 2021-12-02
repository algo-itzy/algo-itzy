# git commit -m "code: Solve boj 15650 N과 M (2) (seungkyu)"
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]
for comb in combinations(numbers, M):
    print(*list(comb))