import sys
input = sys.stdin.readline

N = int(input())
times = []

for i in range(N):
    times.append(list(map(int, input().split())))

# 끝 시간으로 정렬 후 시작 시간으로 정렬
# 끝 시간이 빠른 회의 + 시작 시간 빠른 회의 골라야
times.sort(key=lambda x: (x[1], x[0]))

ptr = cnt = 0  # ptr: 끝 지점 check 변수, cnt: 회의 개수 카운트

for start, end in times:
    if start >= ptr:
        cnt += 1
        ptr = end  # 체크 지점 업데이트

print(cnt)