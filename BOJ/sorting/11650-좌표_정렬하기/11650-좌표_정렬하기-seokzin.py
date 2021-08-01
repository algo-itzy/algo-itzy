import sys
input = sys.stdin.readline

n = int(input())

dots = []

for _ in range(n):
  dot = list(map(int, input().split()))
  dots.append(dot)

dots.sort(key=lambda x: (x[0], x[1]))  # x정렬 후 y정렬
# dots.sort()

for dot in dots:
  print(*dot)

# 사실 sort()로 해도 x정렬 -> y정렬 해준답니다

"""
git commit -m "code: Solve boj 11650 좌표 정렬하기 (seokzin)"
"""