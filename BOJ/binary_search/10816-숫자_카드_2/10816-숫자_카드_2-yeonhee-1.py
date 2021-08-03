# collections.Counter를 이용한 간단한 풀이

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
key_nums = list(map(int, input().split()))

num_cnt = Counter(numbers)

for key_num in key_nums:
    print(num_cnt[key_num], end = ' ')