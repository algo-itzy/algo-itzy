# git commit -m "code: Solve boj 01149 RGB거리 (jiwoong)"
import sys

input = sys.stdin.readline


def dist():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = arr[i][j] + min([v for idx, v in enumerate(arr[i - 1]) if idx != j])
    print(min(arr[-1]))


if __name__ == '__main__':
    dist()
