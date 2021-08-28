# n이 11까지라 중복 테스트케이스를 물어보지는 않을꺼 같아서
# 가능한 테스트케이스는 최대 11개 일거라 가정하면,
# dp를 미리 만들s어 놓을 필요가 없는거 같습니다.
# 미리 만들어 놓을 경우: 연산 11회
# 미리 만들지 않을 경우: 11보다는 작은 T회

from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    dp = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

    for _ in range(T):
        n = int(input())
        if n > 3:
            for i in range(4,n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        print(dp[n])