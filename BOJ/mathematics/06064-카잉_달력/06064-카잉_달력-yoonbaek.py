'''
Python3 676ms

느낀 점
gcd / lcm 리마인드할 수 있어서 좋았음

Point
log M*N -> M 으로 줄여야 하는 문제
'''

from sys import stdin

# first-class func
rd = stdin.readline

# user func
def get_gcd(n1, n2):
    while n1 % n2:
        tmp = n1
        n1 = n2
        n2 = tmp % n2
    
    return n2


def get_lcm(n1, n2):
    gcd = get_gcd(n1, n2)
    last_year = n1*n2//gcd

    return last_year


def get_inca_year(M, N, x, y):
    last_year = get_lcm(M,N)
    # 예외처리
    y = 0 if y == N else y
    
    # M을 만족하는 year를 기준으로 N % year == y가 성립하는지 탐색
    for year in range(x,last_year+1,M):
        if year % N == y:
            return year

    return -1


# main
if __name__ == "__main__":
    T = int(rd())

    for _ in range(T):
        M, N, x, y = map(int, rd().split())

        ans = get_inca_year(M, N, x, y)
        print(ans)
        


# git commit -m "code: Solve boj 06064 카잉 달력 (yoonbaek)"