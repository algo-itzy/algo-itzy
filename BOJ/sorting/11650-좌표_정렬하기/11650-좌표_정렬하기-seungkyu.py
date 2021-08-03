import sys


def solve():
    input = sys.stdin.readline
    n = int(input())
    dots = []
    
    for _ in range(n):
        x_y = list(map(int, input().split()))
        # [x, y] 형태 그대로 새로운 리스트에 append
        dots.append(x_y)

    # 1. x[0] -> x , 2. x[1] -> y 순서로 정렬함 (-붙이면 반대로 정렬)
    sorted_dots = sorted(dots, key=lambda x: (x[0], x[1]))
    for dots in sorted_dots:
        print(*dots)


if __name__ == "__main__":
    solve()
