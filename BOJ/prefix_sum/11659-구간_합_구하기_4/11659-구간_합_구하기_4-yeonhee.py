import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
num_sums = [0]
for i in range(N):
    num_sums.append(num_sums[-1] + numbers[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(num_sums[j]-num_sums[i-1])
