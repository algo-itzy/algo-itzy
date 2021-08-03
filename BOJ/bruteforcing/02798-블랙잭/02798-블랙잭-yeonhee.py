from typing import Mapping


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_of_nums = numbers[i] + numbers[j] + numbers[k]
            if sum_of_nums <= M:
                result = max(result, sum_of_nums)

print(result)

