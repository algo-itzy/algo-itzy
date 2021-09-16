import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums_add =[0]                               # 누적 합 리스트

for i in range(n):
    nums_add.append(nums_add[-1] + nums[i])

for i in range(m):
    i, j = map(int, input().split())

    print(n

# git commit -m "code: Solve boj 11659 구간 합 구하기 4 (yeonju)"