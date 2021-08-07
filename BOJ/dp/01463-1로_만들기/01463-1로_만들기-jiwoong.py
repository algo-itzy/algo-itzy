# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys

input = sys.stdin.readline()
n = int(input)
lst = [0] * (n + 1)

for i in range(2, n + 1):
    lst[i] = lst[i - 1] + 1
    if i % 3 == 0:
        lst[i] = min(lst[i], lst[i // 3] + 1)
    if i % 2 == 0:
        lst[i] = min(lst[i], lst[i // 2] + 1)
print(lst[n])