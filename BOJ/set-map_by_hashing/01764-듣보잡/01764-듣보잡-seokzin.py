import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = []  # 듣
b = []  # 보

for _ in range(n):
    d.append(input().rstrip())

for _ in range(m):
    b.append(input().rstrip())

db = sorted(list(set(d) & set(b)))  # 듣보

print(len(db))

print(*db, sep='\n')