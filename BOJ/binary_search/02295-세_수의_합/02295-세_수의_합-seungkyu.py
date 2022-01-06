# git commit -m "code: Solve boj 02295 세 수의 합 (seungkyu)"
import sys
from itertools import combinations_with_replacement, combinations
input = sys.stdin.readline


def find(num, nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == num:
            return True
        elif nums[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    return False


nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

tot_lst = set()
for comb in combinations_with_replacement(nums, 2):
    tot = sum(comb)
    tot_lst.add(tot)

tot_lst = list(tot_lst)
tot_lst.sort()

ans = 0
for comb in combinations(nums, 2):
    diff = abs(comb[0] - comb[1])
    if find(diff, tot_lst):
        ans = max(ans, max(comb))

print(ans)