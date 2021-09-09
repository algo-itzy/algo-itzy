# 테스트 케이스만 통과가 되네요 ㅠㅠ 좀 더 보겠습니다 
import sys

input = sys.stdin.readline
t = int(input())

for tc in range(t):
    m,n,x,y = map(int, input().split())
    
    while x <= n*m:
        if x%n == y:
            print(x)
            break
        x = x+ m 
    else: 
        print(-1)
                

# git commit -m "code: Solve boj 06064 카잉 달력 (yeonju)"