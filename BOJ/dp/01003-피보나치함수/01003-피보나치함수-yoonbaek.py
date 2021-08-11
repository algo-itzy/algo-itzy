# solved by YoonBaek

#   0 1 2 3 4
# 0 1 0 0 0 0 ...
# 1 0 1 0 0 0 ...
# 2 1 1 1 0 0 ...
# 3 1 2 1 1 0 ...
# 4 2 3 2 1 1
# 5 3 5 3 2 1
# 6 5 8 5 3 2
# ... : 피보나치 규칙을 따르는 것을 발견
# 0은 fib(n-1) 1은 fib(n)

# 이 문제 풀이할 때 주의할 점은 loop마다 dp를 갱신하지 않고
# 초기에 dp 연산이 1 ~ 40 까지로 작기 때문에
# dp를 전체 케이스에서 만들어 놓고 접근하면
# 다수의 테스트 케이스를 O(1)으로 빠르게 풀 수 있습니다.
import sys

rd = sys.stdin.readline
wr = sys.stdout.write


def get_fibo_dp(x: int):
    if x == 0:
        dp[x] = 0
    if x == 1:
        dp[x] = 1
    else:
        dp[x] = dp[x-1] + dp[x-2] 

    return dp


if __name__ == "__main__":
    T = int(rd())

    # init DP first
    dp = [0] * 41
    for i in range(1, 41):
        get_fibo_dp(i)

    for _ in range(T):
        n = int(rd())

        if n == 0:
            wr(f"1 0\n")
        else:
            wr(f"{dp[n-1]} {dp[n]}\n")