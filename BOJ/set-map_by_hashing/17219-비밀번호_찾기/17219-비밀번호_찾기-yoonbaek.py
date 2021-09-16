from sys import stdin, stdout


rd = lambda : stdin.readline().split()
wr = stdout.write


if __name__ == "__main__":
    M, N = map(int, rd())
    hash = {}

    for _ in range(M):
        site, pw = rd()
        hash[site] = pw
    
    for _ in range(N):
        wr(f"{hash[rd()[0]]}\n")

# git commit -m "code: Solve boj 17219 비밀번호 찾기 (yoonbaek)"