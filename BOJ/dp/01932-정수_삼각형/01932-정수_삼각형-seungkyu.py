# git commit -m "code: Solve boj 01932 정수 삼각형 (seungkyu)"
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append([0] + list(map(int, input().split())) + [0])

for i in range(1, n):
    for j in range(1, i+2):
        numbers[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])

print(max(numbers[n-1]))