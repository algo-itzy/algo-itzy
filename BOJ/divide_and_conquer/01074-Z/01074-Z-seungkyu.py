import sys


def solve():
    input = sys.stdin.readline
    N, r, c = map(int, input().split())

    number = 0  #
    # 스터디 후 half를 이용하는 while문을 만들어야겠다는 것을 알게됨
    half = 2**(N-1)
    while half:  # half가 0이 될때까지 반복
        if r > half - 1: # 1 or 4분면일 때
            number += 2*(half*half)  # 규칙성을 통해 숫자를 더하는 것으로 진행
            r -= half # 작은 블록으로 나누면서 인덱스 값 수정

        if c > half - 1:  # 2 or 3분면일 때
            number += half*half
            c -= half
        half //= 2  # 작은 블록으로 나누기
    print(number)

if __name__ == "__main__":
    solve()
