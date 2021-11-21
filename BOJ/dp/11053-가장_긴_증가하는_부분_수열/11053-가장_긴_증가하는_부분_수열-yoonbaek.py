# git commit -m "code: Solve boj 11053 가장 긴 증가하는 부분 수열 (yoonbaek)"

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split()))
    dp = [1] * N

    for i in range(0, N):
        for j in range(i):
            if As[i] > As[j]:
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1

    print(max(dp))