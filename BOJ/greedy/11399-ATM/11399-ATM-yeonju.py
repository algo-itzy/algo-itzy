n = int(input())

time = list(map(int, input().split()))
time.sort()         # 오름차순 정렬해서, 앞에 있는 인덱스 값부터 더해나가기  

cnt = 0             # 한 사람이 기다리는 데 걸리는 시간
total = 0           # 모든 사람이 기다려야하는 시간의 총합

for i in time:
    cnt += i
    total += cnt 
print(total)




# git commit -m "Solve boj 11399 ATM (yeonju)"