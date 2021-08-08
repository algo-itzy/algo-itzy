# solved by YoonBaek

# 4사분면으로 구분 후 구만큼 더해주심(n=1까지)
# quad라는 변수를 이용 좀 더 정리된. 직관된 코드.
def z(n: int, r: int, c:int):
    num = 0; quad = 0

    while n:
        half = 2**(n-1)

        # choose quad place
        if c < half and r < half : quad = 0
        if c >= half and r < half : quad = 1
        if c < half and r >= half : quad = 2
        if c >= half and r >= half : quad = 3

        # jump quad
        num += half**2 * quad
        c %= half; r %= half

        # reduce scope
        n-=1

    return num


if __name__ == "__main__":
    n, r, c = map(int, input().split())

    print(z(n,r,c))