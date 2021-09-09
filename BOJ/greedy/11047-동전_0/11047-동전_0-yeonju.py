import sys

input = sys.stdin.readline

n,k = map(int, input().split())     # k원 만들기

a =[0]*(n+1)
amount = k
cnt = 0
for i in range(1, n+1):
    a[i]=int(input())

for i in range(n,0,-1):             # 큰 단위부터 빼주기 
    if amount >= a[i]:
       cnt += amount//a[i]
       amount -= (a[i]* (amount//a[i]))
       
print(cnt)

# git commit -m "code: Solve boj 11047 동전 0 (yeonju)"