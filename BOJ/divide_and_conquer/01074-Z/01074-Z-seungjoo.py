import sys
input = sys.stdin.readline

# 핵심은 배열을 4등분하는 분할을 통해 
# 배열의 크기가 1인 사각형들의 모임으로 만드는 것. 
def Z(n,r,c):
    # 배열의 크기가 1이 되면 0을 정복하여 반환한다.
    if n==0: 
        return 0
    # 배열의 크기를 반을 기준으로 4영역으로 분할한다.
    harf = 2**(n-1)
    if r < harf and c<harf: 
        return Z(n-1,r,c)
    elif r < harf and c>=harf: 
        return harf**2 + Z(n-1,r,c-harf)
    elif r >=harf and c<harf: 
        return 2*harf**2 + Z(n-1,r-harf,c)
    else:
        return 3*harf**2 + Z(n-1,r-harf,c-harf)

N,r,c = map(int,input().split())
print(Z(N,r,c))