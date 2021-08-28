import sys
input = sys.stdin.readline

N = int(input())
Pi = list(map(int, input().split()))

Pi.sort()  # 정렬해서 풀면 쉬운 문제
total = 0

for idx, num in enumerate(Pi):
    total += (len(Pi)-idx)*num
print(total)