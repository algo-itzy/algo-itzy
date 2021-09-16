from sys import stdin, stdout

rd = lambda: map(int, stdin.readline().split())
wr = stdout.write

if __name__ == "__main__":
    N, M = rd()
    numbers = list(rd())

    for i in range(1, N):
        numbers[i] += numbers[i-1]

    for _ in range(M):
        i, j = tuple(rd())
        if i == 1:
            wr(f"{numbers[j-1]}\n")
        else:
            wr(f"{numbers[j-1] - numbers[i-2]}\n")
    

# git commit -m "code: Solve boj 11659 구간 합 구하기 4 (yoonbaek)"