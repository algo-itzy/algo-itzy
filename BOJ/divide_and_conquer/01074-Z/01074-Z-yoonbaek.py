# solved by YoonBaek

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