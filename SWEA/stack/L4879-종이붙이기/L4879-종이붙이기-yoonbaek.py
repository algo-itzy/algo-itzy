# solved by YoonBaek

if __name__ == "__main__":
    T = int(input())

    dp = [1, 1]

    # get dp first
    # test case가 많을 때 유리
    for i in range(2, 30+1):
        dp.append(dp[i-1] + 2*dp[i-2])

    for tc in range(1, T+1):
        N = int(input())
        N //= 10        

        print(f"#{tc} {dp[N]}")

