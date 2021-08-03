import sys
import itertools


def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    ans = 0
    # 조합이용, 3개 순서없이 뽑은 경우의 수를 모두 생각
    numbers_combinations = itertools.combinations(numbers, 3)

    # 최대 수(m)을 넘지 않으면서 기존 ans보다 클 경우 업데이트
    for combination in numbers_combinations:
        sum_num = sum(combination)
        if sum_num <= m and ans < sum_num:
            ans = sum_num
    print(ans)


if __name__ == "__main__":
    solve()
