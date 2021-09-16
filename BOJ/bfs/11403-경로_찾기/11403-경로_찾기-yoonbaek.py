from sys import stdin

rd = stdin.readline


def FW():
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if mat[start][mid] and mat[mid][end]:
                    mat[start][end] = 1


if __name__ == "__main__":
    N = int(rd())
    mat = [list(map(int, rd().split())) for _ in range(N)]

    FW()

    for row in mat:
        print(*row)
# git commit -m "code: Solve boj 11403 경로 찾기 (yoonbaek)"