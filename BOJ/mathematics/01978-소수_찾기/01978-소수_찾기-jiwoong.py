# 소수의 개수

import sys
n = int(input())
num = sys.stdin.readline().split()
prime = 0

for i in num:
    nums = 0
    for j in range(1, int(i)+1):
        if int(i) % j == 0:
            nums += 1
    if nums == 2:
        prime += 1
print(prime)