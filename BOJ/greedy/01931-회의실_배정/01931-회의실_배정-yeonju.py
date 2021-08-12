N = int(input()) # 회의의 수 

time =[]
for i in range(N):
    start, end = map(int, input().split())
    time.append([start, end]) 

time = sorted(time, key = lambda x : x[0]) # 시작 시간을 기준으로 오름차순 정렬
time = sorted(time, key = lambda x : x[1])  # 끝나는 시간 기준으로 내림차순 정렬

last = 0
cnt = 0                                     # 회의의 개수를 저장

# print(time)

for i, j in time:
    if i >= last:   # 시작 시간이 회의의 마지막 시간보다 크거나 같으면 카운트
        cnt +=1
        last = j

print(cnt)


