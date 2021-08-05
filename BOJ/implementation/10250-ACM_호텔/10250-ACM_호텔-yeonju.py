"""
1<=H, W<=99
"""

# T는 테스트 케이스의 개수
# H는 층수, W 는 호수, N은 마지막 번째 손님

T = int(input())

for i in range(T):
    H, W, N = map(int,input().split()) 
    
    a = N % H # N번째 손님이 머물게 될 층의 수
    b = N// H +1 # N번쨰 손님이 머물게 될 호수
    if a == 0:
        a = H
        b = N//H
    
    print(a*100+ b)


"""
git commit -m "code: Solve boj 00000 문제 이름 (yeonju)"
"""