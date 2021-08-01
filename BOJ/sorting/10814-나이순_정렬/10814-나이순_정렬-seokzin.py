import sys
input = sys.stdin.readline

n = int(input())

members = []

for _ in range(n):
  age, name = map(str, input().split())
  members.append((int(age), name))

members.sort(key=lambda x: x[0]) 

for member in members:
  print(*member)

# write()는 readline()에 비해 극적인 성능차이가 없다고 생각합니다

"""
git commit -m "code: Solve boj 10814 나이순 정렬 (seokzin)"
"""