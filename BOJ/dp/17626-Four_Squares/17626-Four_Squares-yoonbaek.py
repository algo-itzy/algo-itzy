sqrt = lambda x: int(x**0.5)

if __name__ == "__main__":
    N = int(input())

    cnt = 0
    dp = [4] * (N+1)
    end = sqrt(N)+1
    sqrs = [i**2 for i in range(1, end)]
    dp[0], dp[1] = 0, 1

    for i in range(2, N+1):
        for sqr in sqrs:
            if sqr <= i:
                mod = i - sqr
                dp[i] = min(dp[i], 1 + dp[mod])

    
    print(dp[N])

# 1 = 1 1**2
# 2 = 2 1**2 1**2         
# 3 = 3 1**2 1**2 1**2    
# 4 = 1 2**2
# 5 = 2 2**2 1**2 
# 6 = 3 2**2 1**2 1**2
# 7 = 4 2**2 1**2 1**2 1**2
# 8 = 2 2**2 2**2
# 9 = 1 3**2
# 10 = 2 3**2 1**2
# 11 = 3**2 1**2 1**2
# 12 = 3**2 1**2 1**2 1**2
# 13 = 3**2 2**2
# 14 = 3**2 2**2 1**2
# 15 = 3**2 2**2 1**2 1**2
# 16 = 4**2
    
# git commit -m "code: Solve boj 17626 Four Squares (yoonbaek)"