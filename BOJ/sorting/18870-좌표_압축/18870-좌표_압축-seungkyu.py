import sys
input = sys.stdin.readline

n = int(input())

numbers = list(set(map(int, input().split())))
numbers.sort()

ans = []
num_dict = {}

# 1바퀴 돌면서 작은 순서대로 인덱스값 지정해주기
for idx, num in enumerate(numbers):
    num_dict[num] = idx

# dictionary에서 값 찾아서 출력
for num in numbers:
    ans.append(num_dict[num])

print(*ans)
