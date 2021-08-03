import sys


def solve():
    n = int(input())
    numbers = []

    # 숫자를 모두 입력 받고 한 번만 정렬 => 시간 오래 걸림
    for _ in range(n):
        number = int(sys.stdin.readline().strip())
        numbers.append(number)
    print(*sorted(numbers))


if __name__ == "__main__":
    solve()
