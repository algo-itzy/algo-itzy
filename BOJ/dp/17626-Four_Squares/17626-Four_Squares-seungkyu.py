# git commit -m "code: Solve boj 17626 Four Squares (seungkyu)"
from itertools import combinations_with_replacement  # 중복 조합
import sys
input = sys.stdin.readline


def solve(n):
    answer = 4
    for i in range(1, 4):
        for nums in combinations_with_replacement(dp, i):
            if sum(nums) == n:
                answer = i
                return answer
    return answer


n = int(input())
n_sqrt = int(n**(1/2))
dp = [i**(2) for i in range(1, n_sqrt+1)]

print(solve(n))
