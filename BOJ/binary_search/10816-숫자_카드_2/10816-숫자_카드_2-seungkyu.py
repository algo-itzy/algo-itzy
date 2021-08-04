"""
시간 매우 오래 걸림
메모리 사용 많음
"""
import sys


def solve():
    # 숫자가 몇 개 있는지 check하는 리스트(음수 부분은 10000000+1 더해서 계산)
    num_cnt = [0 for _ in range(10000000 * 2 + 1)]
    input = sys.stdin.readline
    n = int(input())
    having_numbers = list(map(int, input().split()))

    for num in having_numbers:  # 숫자 개수 업데이트
        num_cnt[num + 10000000] += 1

    m = int(input())
    check_numbers = list(map(int, input().split()))

    for num in check_numbers:  # 리스트에서 위치 찾아서 print
        print(num_cnt[num + 10000000], end=" ") if num_cnt[num + 10000000] else print(0, end=" ")


if __name__ == "__main__":
    solve()
