import sys
input = sys.stdin.readline

N = int(input())
meet_table = []
for _ in range(N):
    start,end = map(int,input().split())
    meet_table.append([start,end])
# end time이 빠르고 satrt time이 빠른 순서대로 정렬.
meet_table.sort(key=lambda x: (x[1],x[0]))
cnt=0
end=0
for i in range(N):
    # 끝나는 시간보다 시작시간이 느리면 갱신.
    if end <= meet_table[i][0]:
        end = meet_table[i][1]
        cnt+=1
print(cnt)