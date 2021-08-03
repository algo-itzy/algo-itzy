# 오름차순 정렬 : 중복 X

import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums = sorted(nums)

for i in range(len(nums)):
    print(nums[i])