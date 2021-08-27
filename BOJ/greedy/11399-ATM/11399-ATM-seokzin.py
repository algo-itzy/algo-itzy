n = int(input())
p = sorted(list(map(int, input().split())))
res = 0

for i in range(1, n+1):
  res += sum(p[0 : i])

print(res)

# SJF 스케줄링과 비슷