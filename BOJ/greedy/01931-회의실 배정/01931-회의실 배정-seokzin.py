n = int(input())
times = []  # 회의 시간 리스트

for _ in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

times.sort(key=lambda x: (x[1], x[0]))

last = 0  # 마지막 회의 종료 시간
cnt = 0

for s, e in times:
    if s >= last:
        cnt += 1
        last = e

print(cnt)

# Greedy
# 정렬만으로 최적을 보장한다? 100% 와닿지는 않았다.