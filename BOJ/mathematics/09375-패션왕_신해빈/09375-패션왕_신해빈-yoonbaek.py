# 프로그래머스에서 많이 보던 문제

from sys import stdin

rd = stdin.readline

class Dict(dict):
    def push(self, key):
        if key in self:
            self[key] += 1
        else:
            self[key] = 1


if __name__ == "__main__":
    T = int(rd())
    for _ in range(T):
        n = int(rd())
        clothes = Dict()

        for _ in range(n):
            _, key = rd().split()
            clothes.push(key)

        cnt = 1
        for key in clothes:
            cnt *= (clothes[key]+1)

        print(cnt-1)

# git commit -m "code: Solve boj 09375 패션왕 신해빈 (yoonbaek)"