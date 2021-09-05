# 무지성 점화식 풀이
# N == 0 에만 주의하면 됩니다.

def solve(N):
    if N == 0:
        return 0

    dp = [0] * (N+1)
    
    for i in range(1, N+1):
        if i == 1:
            dp[i] = 1
        else: 
            dp[i] = i * dp[i-1]

    target = dp[N]

    cnt = 0
    while target % 10 == 0:
        cnt += 1
        target //= 10

    return cnt


if __name__ == "__main__":
    N = int(input())
    
    cnt = solve(N)

    print(cnt)
# git commit -m "code: Solve boj 01676 팩토리얼 0의 개수 (yoonbaek)"