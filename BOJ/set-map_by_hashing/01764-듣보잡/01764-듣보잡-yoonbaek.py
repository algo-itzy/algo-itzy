# solved by YoonBaek 

# hash를 이용한 풀이
# 단어 정렬에만 주의하면 됐던 문제

import sys

rd = sys.stdin.readline
wr = sys.stdout.write

if __name__ == "__main__":
    N, M = map(int, rd().split())
    dbj = {}

    cnt, result = 0, []
    for _ in range(N+M):
        name = rd().rstrip()
        if dbj.get(name):
            cnt += 1
            result.append(name)
        else:
            dbj[name] = 1

    result.sort()

    wr(f"{cnt}\n")
    print(*result, sep = "\n")