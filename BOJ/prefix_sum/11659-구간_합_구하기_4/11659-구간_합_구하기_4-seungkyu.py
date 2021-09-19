# git commit -m "code: Solve boj 11659 구간 합 구하기 4 (seungkyu)"
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
accumulated_num = []

tot = 0
for num in nums:
    tot += num
    accumulated_num.append(tot)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(accumulated_num[j-1])
    else:
        print(accumulated_num[j-1]-accumulated_num[i-2])
