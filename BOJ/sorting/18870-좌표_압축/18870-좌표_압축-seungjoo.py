import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr2  = sorted(list(set(arr)))
for num in arr:
    print(bisect_left(arr2,num),end=' ')